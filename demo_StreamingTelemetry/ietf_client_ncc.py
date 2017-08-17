from ncclient import manager
from ncclient.xml_ import new_ele, sub_ele
import logging
import time
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import threading

from kafka import KafkaProducer
from kafka.errors import KafkaError
from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import os.path
import json

log = logging.getLogger(__name__)
logging.basicConfig(
    level = logging.INFO,
    format = '%(levelname)-8s | %(threadName)-10s | %(asctime)s | %(message)s',
)


#----------------------
# REST API Settings
#----------------------
app = Flask(__name__)
required_fields = ['xpath', 'incident_id']
mutually_exclusive_fields = ['period', 'dampening_period']
publish_lock = False
db_file = './subs_inc_db.json'

@app.route("/editconfig", methods=['GET', 'POST'])
def editconfig():

    if request.method == 'GET':
        return "Hello Edit Config!"

    try:
        data = request.get_json()
    except:
        return 'Unable to extract JSON data from message.  Please check JSON format', 400


    rpc = '''   
    <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" xmlns:ios-acl="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
        <ip>
          <access-list>
            <ios-acl:extended>
              <ios-acl:name>test_acl</ios-acl:name>
              <ios-acl:access-list-seq-rule>
                <ios-acl:sequence>10</ios-acl:sequence>
                <ios-acl:ace-rule>
                  <ios-acl:action>deny</ios-acl:action>
                  <ios-acl:protocol>ip</ios-acl:protocol>
                  <ios-acl:any/>
                  <ios-acl:dst-any/>
                </ios-acl:ace-rule>
              </ios-acl:access-list-seq-rule>
              <ios-acl:access-list-seq-rule>
                <ios-acl:sequence>20</ios-acl:sequence>
                <ios-acl:ace-rule>
                  <ios-acl:action>permit</ios-acl:action>
                  <ios-acl:protocol>ip</ios-acl:protocol>
                  <ios-acl:any/>
                  <ios-acl:dst-any/>
                </ios-acl:ace-rule>
              </ios-acl:access-list-seq-rule>
            </ios-acl:extended>
          </access-list>
'''

    edit_config = manager.edit_config(target='running', config=rpc)
    log.info(edit_config.xml)
    return edit_config.xml


@app.route("/delsub", methods=['GET', 'POST'])
def delsub():
    global publish_lock
    global db_file

    if request.method == 'GET':
        return 'Hello delsub'
    
    try:
        data = request.get_json()
    except:
        return 'Unable to extract JSON data from message.  Please check JSON format', 400

    # Send delete RPC
    try:
        manager.delete_subscription(data['subs_id'])
    except:
        return 'Unable to send delete rpc', 400

    try:
        # Remove subscription from database incident table
        if os.path.isfile(db_file):
            log.info('Reading contents of %s', db_file)
            with open(db_file, 'r') as fp:
                try:
                    db_data = json.load(fp)
                except:
                    log.error('Error reading %s, init db_data to empty', db_file)
                    db_data = {}
        else:
            log.info('initialize db_data to empty')
            db_data = {}

        new_db_data = {key: db_data[key] for key in db_data.keys() if key != data['subs_id']}
        with open(db_file, 'w') as fp:
            json.dump(new_db_data, fp)
    except:
        return 'Unable to write database file', 400

    return 'OK'
    
def callback_kafka_publish(notif):
    ''' Publishes message to Kafka messaging bus '''
    producer.send(TOPIC, json.dumps(notif.xml).encode('utf-8'))

def errback(notif):
    pass


@app.route("/sendrpc", methods=['GET', 'POST'])
def sendrpc():
    global publish_lock
    global db_file

    if request.method == 'GET':
        if os.path.isfile(db_file):
            log.info('Reading contents of %s', db_file)
            with open(db_file, 'r') as fp:
                try:
                    db_data = json.load(fp)
                except:
                    return 'Error reading %s, init db_data to empty', 400
        else:
            db_data = {}
        return json.dumps(db_data)

    try:
        data = request.get_json()
    except:
        return 'Unable to extract JSON data from message.  Please check JSON format', 400

    # Validate all required fields are present
    missing_fields = set(required_fields) - set(data.keys())
    if len(missing_fields) != 0:
        return 'Missing fields: %s' % missing_fields, 400

    period_fields = set(mutually_exclusive_fields) - set(data.keys())
    if len(period_fields) != 1:
        return 'Must specify period or dampening_period but not both', 400

    period = None
    dampening_period = None
    try:
        period = data['period']
    except KeyError:
        dampening_period = data['dampening-period']

    s = manager.establish_subscription(callback_kafka_publish,
                                       errback,
                                       xpath=data['xpath'],
                                       period=period,
                                       dampening_period=dampening_period)
    subscriptions.append(s)

    #--------------------
    # Write subscription_id to incident id to database
    #--------------------
    # Only write data with a real incident id
    if data['incident_id'] == '1234' or data['incident_id'] == 1234:
        log.info('Not a real incident, skip writing to DB')
        return str(s.subscription_id)

    if os.path.isfile(db_file):
        log.info('Reading contents of %s', db_file)
        with open(db_file, 'r') as fp:
            try:
                db_data = json.load(fp)
            except:
                log.error('Error reading %s, init db_data to empty', db_file)
                db_data = {}
    else:
        log.info('initialize db_data to empty')
        db_data = {}
    log.info('Adding subs_id %s, incident_id %s to database', s.subscription_id, data['incident_id'])
    db_data[s.subscription_id] = data['incident_id']
    with open(db_file, 'w') as fp:
        json.dump(db_data, fp)

    return str(s.subscription_id)

if __name__ == '__main__':
    # USAGE: python ietf_client.py --uut_ip <device_ip>
    import argparse

    # Set root logging level to be used for all imported modules
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    
    parser = argparse.ArgumentParser(description="standalone parser")
    parser.add_argument('--uut_ip', dest='uut_ip', default='')
    parser.add_argument('--port', dest='port', default=8320)
    parser.add_argument('--topic', dest='topic', default='Telemetry')
    parser.add_argument('--compute_rate', dest='compute_rate', default=False)
    parser.add_argument('--window', dest='window', default=15)
    parser.add_argument('--kafka', dest='kafka', default='ott-kafka-1')
    parser.add_argument('--user', dest='user', default='admin')
    parser.add_argument('--password', dest='password', default='admin')

    # parse args
    args, unknown = parser.parse_known_args()

    uut_ip = str(args.uut_ip)
    port = int(args.port)
    TOPIC = str(args.topic)
    compute_rate = True if 'True' in str(args.compute_rate) else False
    window = int(args.window)
    kafka = str(args.kafka)
    user = str(args.user)
    password = str(args.password)

    # Delete subscription database on startup
    if os.path.isfile(db_file):
        log.info('Removing %s', db_file)
        os.remove(db_file)

    # Setup Kafka Producer
    producer = KafkaProducer(bootstrap_servers=['%s:9092'%kafka])


    # Start NETCONF session
    def unknown_host_cb(host, fingerprint):
        return True

    manager = manager.connect(host=uut_ip,
                              port=830,
                              username=user,
                              password=password,
                              allow_agent=False,
                              look_for_keys=False,
                              hostkey_verify=False,
                              unknown_host_cb=unknown_host_cb,
                              timeout=10)
    subscriptions = []
    app.run(host='0.0.0.0', port=port)
