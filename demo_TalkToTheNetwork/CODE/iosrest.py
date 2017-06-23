#!/usr/bin/python

# This is our Alexa app. I won't get into all the libs improted below. Let's
# assume the coder knows why we're importing them, or knows Python better than I
# do anyway.
from flask import Flask, jsonify
from flask import send_from_directory
from flask import send_file
from flask import url_for
from flask import request
import json
import os
import sys
import time
import requests
# OK this one is noteworthy, as it powers our application.
from flask_ask import Ask, statement
# OK this one is too. It's a common-funcs file being imported that makes the
# code way more readable here.
from common_funcs import *


#common with Flask
app = Flask(__name__)

######################################  Alexa items ############################

# common with Flask-Ask
ask = Ask(app, "/")


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked by specific utterances. It defines a function called "hello"
# and returns "Hello jafrazie". Use keep this around to make sure the skill and
# app are up and operatinal. Otherhwise, this doesn't do a thing to a network
# device.
@ask.intent("HelloIntent")
def hello():
    return statement("Hello jafrazie")


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked by specific utterances. It defines a function called
# "disable_restconf" and returns "I don't want to do that, because we wouldn't
# have as much fun". Easter egg just for fun. Otherhwise, this doesn't do a
# thing to a network device.
@ask.intent("DisableRestconf")
def disable_restconf():
    return statement("I don't want to do that, because we wouldn't have as much fun")


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked by specific utterances. It defines a function called
# "intent_save_config". 'output' is then defined as a function called
# 'cmn_save_config()'. This function technically lives in the common_funcs file.
# The function is what does the actual work of talking to the CSR. This allows
# the coder to see the easy nature of flask-ask. Pass in an intent with no
# paramters, and a return statement is the output we'd like to read.
@ask.intent('SaveConfig')
def intent_save_config():
    output = cmn_save_config()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked by specific utterances. It defines a function called
# "intent_rollback_config". 'output' is then defined as a function called
# 'cmn_rollback_config()'. This function technically lives in the common_funcs
# file. The function is what does the actual work of talking to the CSR. This
# allows the coder to see the easy nature of flask-ask. Pass in an intent with
# no paramters, and a return statement is the output we'd like to read.
@ask.intent('RollbackConfig')
def intent_rollback_config():
    output = cmn_rollback_config()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked by specific utterances. It defines a function called
# "intent_get_cpu". 'output' is then defined as a function called
# 'cmn_get_cpu()'. This function technically lives in the common_funcs
# file. The function is what does the actual work of talking to the CSR. This
# allows the coder to see the easy nature of flask-ask. Pass in an intent with
# no paramters, and a return statement is the output we'd like to read.
@ask.intent('GetCPU')
def intent_get_cpu():
    output = cmn_get_cpu()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked be specific utterances. It defines a function called
# "intent_get_interface_state_gigabit_ethernet_one". 'output' is then defined as
# a function called 'cmn_get_interface_state_gigabit_ethernet_one()'. This
# function technically lives in the common_funcs file. The function is what does
# the actual work of talking to the CSR. This allows the coder to see the easy
# nature of flask-ask. Pass in an intent with no paramters, and a return
# statement is the output we'd like to read.
@ask.intent('GetInterfaceStateGigabitEthernetOne')
def intent_get_interface_state_gigabit_ethernet_one():
    output = cmn_get_interface_state_gigabit_ethernet_one()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked be specific utterances. It defines a function called
# "intent_get_interface_state_loopback_one". 'output' is then defined as
# a function called 'cmn_get_interface_state_loopback_one()'. This
# function technically lives in the common_funcs file. The function is what does
# the actual work of talking to the CSR. This allows the coder to see the easy
# nature of flask-ask. Pass in an intent with no paramters, and a return
# statement is the output we'd like to read.
@ask.intent('GetInterfaceStateLoopbackOne')
def intent_get_interface_state_loopback_one():
    output = cmn_get_interface_state_loopback_one()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked be specific utterances. It defines a function called
# "intent_set_interface_state_loopback_two". 'output' is then defined as
# a function called 'cmn_set_interface_state_loopback_two()'. This
# function technically lives in the common_funcs file. The function is what does
# the actual work of talking to the CSR. This allows the coder to see the easy
# nature of flask-ask. Pass in an intent with no paramters, and a return
# statement is the output we'd like to read.
@ask.intent('SetInterfaceStateLoopbackTwo')
def intent_set_interface_state_loopback_two():
    output = cmn_set_interface_state_loopback_two()
    return statement(output)


# This is an ask intent. There is a corresponding intent in our Alexa skill with
# this name, invoked be specific utterances. It defines a function called
# "intent_destroy_interface_state_loopback_two". 'output' is then defined as
# a function called 'cmn_destroy_interface_state_loopback_two()'. This
# function technically lives in the common_funcs file. The function is what does
# the actual work of talking to the CSR. This allows the coder to see the easy
# nature of flask-ask. Pass in an intent with no paramters, and a return
# statement is the output we'd like to read.
@ask.intent('DestroyInterfaceStateLoopbackTwo')
def intent_destroy_interface_state_loopback_two():
    output = cmn_destroy_interface_state_loopback_two()
    return statement(output)


######################################  NON Alexa items ########################################

# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route("/HelloIntent")
def route_hello():
    return ("Hello jafrazie\n")


# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/SaveConfig', methods = ['POST'])
def route_save_config():
    output = cmn_save_config()
    return (output)


# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/GetCPU', methods = ['GET'])
def route_get_cpu():
    output = cmn_get_cpu()
    return (output)


# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/GetInterfaceStateGigabitEthernetOne', methods = ['GET'])
def route_get_interface_state_gigabit_ethernet_one():
    output = cmn_get_interface_state_gigabit_ethernet_one()
    return (output)


# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/GetInterfaceStateLoopbackOne', methods = ['GET'])
def route_get_interface_state_loopback_one():
    output = cmn_get_interface_state_loopback_one()
    return (output)


# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/SetInterfaceStateLoopbackTwo', methods = ['POST'])
def route_set_interface_state_loopback_two():
    output = cmn_set_interface_state_loopback_two()
    return (output)

# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route('/DestroyInterfaceStateLoopbackTwo', methods = ['POST'])
def route_destroy_interface_state_loopback_two():
    output = cmn_destroy_interface_state_loopback_two()
    return (output)

# This is an app intent in flask. This should demonstrate how flask-ask is an
# extension to flask itself. Web calls can be made for this, when added onto the
# web interface for the app itself.
@app.route("/", methods = ['GET'])
def hello():
    return "Return information about available calls here"

# This tells our app to run. It pulls in a self-signed-cert and private-key, and
# runs on port 443 on the localhost.
if __name__ == "__main__":
    context = ('certificate.pem', 'private-key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context, threaded=True, debug=True)
