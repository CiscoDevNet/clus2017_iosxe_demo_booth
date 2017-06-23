# This is the file that does the heavy-lifting for our Alexa app.
# I won't get into all the libs improted below. Let's assume the coder knows why
# we're importing them, or knows Python better than I do anyway. But, as we're
# just doing JSON and HTTP calls here, should be pretty straightforward.
import requests
import json


# Define 'base_url' and set it to the CSRs root tree for RESTCONF. This just
# saves us from typing it over and over again.
base_url = "http://ec2-52-91-174-10.compute-1.amazonaws.com:80/restconf/api/"

# Define a function called 'cmn_save_config'. Bring in the base_url, and apply
# the REST verb. This does a POST, with headers. This is an RPC that tells the
# device to save its config. The 2nd to last 'return' statement is key. We know
# what we should get back, so we are reading those values specifically. The last
# except/return is essentially for erroring out gracefully.
def cmn_save_config():
    global base_url
    try:
        response = requests.post(
            url= base_url + \
                "operations/cisco-ia:save-config",
            headers={
                "Content-Type": "application/vnd.yang.operation+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.operation+json",
            },
            data=json.dumps({

            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return (response.json()['output']['result'])
    except requests.exceptions.RequestException:
        return ("Failed to save config")


# Define a function called 'cmn_rollback_config'. Bring in the base_url, and
# apply the REST verb. This does a POST, with headers. This is an RPC that tells
# the devices to replace its config with the file contained in the 'data'
# parameter that is also passed in. The 2nd to last 'return' statement is key.
# We know what we should get back, so we are reading those values specifically.
# The last except/return is essentially for erroring out gracefully.
def cmn_rollback_config():
    global base_url
    try:
        response = requests.post(
            url= base_url + \
                "operations/cisco-ia:rollback",
            headers={
                "Content-Type": "application/vnd.yang.operation+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.operation+json",
            },
            data="{\"cisco-ia:input\": {\"target-url\":\"bootflash:demo-start.cfg\"}}"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return (response.json()['output']['result'])
    except requests.exceptions.RequestException:
        return ("Failed to save config")


# Define a function called 'cmn_get_cpu'. Bring in the base_url, and
# apply the REST verb. This does a GET, with headers. This asks the router
# for the same data a human would see in 'sho proc cpu'. The 2nd to last 'return'
# statement is key. We know what we should get back, so we are reading those
# values specifically. Yes, it's sorta long. We are technically just reading 2
# of the fields from the returned data. The last except/return is essentially
# for erroring out gracefully.
def cmn_get_cpu():
    global base_url
    try:
        response = requests.get(
            url= base_url + \
                "operational/cpu-usage/cpu-utilization",
            headers={
                "Content-Type": "application/vnd.yang.data+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.data+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return ("The five second CPU is " + str(response.json()['Cisco-IOS-XE-process-cpu-oper:cpu-utilization']['five-seconds']) + ".  The one minute CPU is " + str(response.json()['Cisco-IOS-XE-process-cpu-oper:cpu-utilization']['one-minute']))
    except requests.exceptions.RequestException:
        return ("Failed to get CPU")


# Define a function called 'cmn_get_interface_state_gigabit_ethernet_one'.
# Bring in the base_url, and apply the REST verb. This does a GET, with headers.
# This asks the router for the same data a human would see in 'sho int g1'. This
# is where the code needs to be better. Interfaces can be brought in from 'slots'
# in an Alexa skill, and they can be normalized. Hey, it's a demo. Cheating here.
# The 2nd to last 'return' statement is key. We know what we should get back, so
# we are reading those values specifically. We are technically just reading the
# 'oper-status' of the interface directly from JSON. The last except/return is
# essentially for erroring out gracefully.
def cmn_get_interface_state_gigabit_ethernet_one():
    global base_url
    try:
        response = requests.get(
            url= base_url + \
                "operational/interfaces-state/interface/GigabitEthernet1",
            headers={
                "Content-Type": "application/vnd.yang.data+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.data+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return "The status of Interface Gigabit Ethernet One is " + \
               str(response.json()['ietf-interfaces:interface']['oper-status'])
    except requests.exceptions.RequestException:
        return "Failed to get interface status"


# Define a function called 'cmn_get_interface_state_loopback_one'. Bring in the
# base_url, and apply the REST verb. This does a GET, with headers. This asks
# the router for the same data a human would see in 'sho int lo1'. This
# is where the code needs to be better. Interfaces can be brought in from 'slots'
# in an Alexa skill, and they can be normalized. Hey, it's a demo. Cheating here.
# The 2nd to last 'return' statement is key. We know what we should get back, so
# we are reading those values specifically. We are technically just reading the
# 'oper-status' of the interface directly from JSON again. The last except/return
# is essentially for erroring out gracefully.
def cmn_get_interface_state_loopback_one():
    global base_url
    try:
        response = requests.get(
            url= base_url + \
                "operational/interfaces-state/interface/Loopback1",
            headers={
                "Content-Type": "application/vnd.yang.data+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.data+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return ("The status of Interface Loop Back One is " + str(response.json()['ietf-interfaces:interface']['oper-status']))
    except requests.exceptions.RequestException:
        return ("Failed to get interface status")


# Define a function called 'cmn_set_interface_state_loopback_two'. Bring in the
# base_url, and apply the REST verb. This does a PUT, with headers. This asks
# the router to essentially 'conf t, int lo 2'. The 2nd to last 'return'
# statement is hard-coded, letting us know the operation was successful, as we
# get no JSON data returned from this operation. The last except/return
# is essentially for erroring out gracefully.
def cmn_set_interface_state_loopback_two():
    global base_url
    try:
        response = requests.put(
            url=base_url + \
                "config/native/interface/Loopback/2",
            headers={
                "Content-Type": "application/vnd.yang.data+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.data+json",
            },
            data="{\"Cisco-IOS-XE-native:Loopback\": {\"name\": \"2\"}}"
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return ("Interface Created")
    except requests.exceptions.RequestException:
        return ("Failed to get interface status")

# Define a function called 'cmn_destroy_interface_state_loopback_two'. Bring in
# the base_url, and apply the REST verb. This does a DELETE, with headers. This
# asks the router to essentially 'conf t, no int lo 2'. The 2nd to last 'return'
# statement is hard-coded, letting us know the operation was successful, as we
# get no JSON data returned from this operation. The last except/return
# is essentially for erroring out gracefully.
def cmn_destroy_interface_state_loopback_two():
    global base_url
    try:
        response = requests.delete(
            url=base_url + \
                "config/native/interface/Loopback/2",
            headers={
                "Content-Type": "application/vnd.yang.data+json",
                "Authorization": "Basic Y2lzY286QzFzZGV2b3Bz",
                "Accept": "application/vnd.yang.data+json",
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        return ("Interface Destroyed")
    except requests.exceptions.RequestException:
        return ("Failed to get interface status")

1;
