#!/usr/bin/env python

from flask import Flask, render_template
import markdown

app = Flask(__name__)

demos = [
    {
        "name": "ChatOps",
        "short_desc": "Programmability provides push notification of changes made to a device",
        "long_desc": "A user is able to go and make a change to the CAT9300 (adding a new route, etc.), once they have done this EEM uses an on-box python script to determine configuration diff and post to Spark room showing what has changed.",
        "owners": ["Jeff M"],
        "features": ["eem", "python", "guest shell"],
        "image": "chatops.png",
        "code": "chatops"
        "demo_steps": markdown.markdown(open("static/demo_chatops_steps.md").read())
    },
    {
        "name": "Streaming Telemetry",
        "short_desc": "Telemetry delivers insights at scale & performance not available before",
        "long_desc": "Using ELK Stack and the IETF client setup a periodic subscription on the CAT9300 and then visualize the telemetry output using Kibana. ",
        "owners": ["Jeff M", "Fabrizio"],
        "features": ["netconf", "telemetry", "yang", "pub/sub", "operational"],
        "image": "telemetry.png",
        "code": "telemetry"
    },
    {
        "name": "DevOps Golden Config",
        "short_desc": "Programmability enables DevOps workflow to programmatically manage golden images ",
        "long_desc": "Use the ia.yang data model perform a config replace on the device ",
        "owners": ["Krishna"],
        "features": ["netconf", "continuous delivery", "python", "config-replace", "devops"],
        "image": "devops.png",
        "code": "devops"
    },
    {
        "name": '"Git-ing" Code',
        "short_desc": "Use 'git' within IOS XE to deploy code and scripts.",
        "long_desc": "Manage on-box automation and code with source control for an excellent developer experience.",
        "owners": ["Hank P"],
        "features": ["guestshell", "git", "devops"],
        "image": "git.png",
        "code": "git",
        "demo_steps": markdown.markdown(open("static/demo_git_steps.md").read())
    },
    {
        "name": "Talk to the Network",
        "short_desc": "Programmability enables interaction between network devices & other systems or apps",
        "long_desc": "Talk with Alexa to see how the interfaces are doing on the CAT9300 (ietf-interfaces.yang), ask Alexa to turn on PoE lights (using Cisco-IOS-XE-poe.yang), and retrieve operational data (Cisco-IOS-XE-cpu-process-oper.yang & Cisco-IOS-XE-environment-oper.yang). ",
        "owners": ["Jason F"],
        "features": ["netconf", "yang", "operational", "alexa"],
        "image": "talk.png",
        "code": "talk"
    }
]

@app.route("/", methods=['GET'])
def home():
    '''
    Serve the main web interface for Haciendo
    :return:
    '''
    return render_template("home.html", demos = demos)

if __name__=='__main__':
    # Use ArgParse to retrieve command line parameters.
    from argparse import ArgumentParser
    parser = ArgumentParser("Haciendo Web Server")

    # Retrieve the port and API server address
    parser.add_argument(
        "-p", "--port", help="Port to run web server on.", required=False, default=8080
    )
    args = parser.parse_args()

    web_port = int(args.port)

    # Start the web server
    app.run(debug=True, host='0.0.0.0', port=web_port)
