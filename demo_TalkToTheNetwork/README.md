# Alexa fun

This repo is a small fun repo with simple code! Let's set the stage:
* There's an Alexa near you somewhere.
* There's a CSR in AWS under jafrazie that you can play with.
* There's a simple Python app running on an Ubuntu instance that Alexa talks to.

## What is being used:
Flask-Ask -- ask.intent is used to handle alexa asks.
Flask -- app.route is used to handle direct REST calls.

## Dos and Don'ts
OK, there are not many don'ts. Here are the Do's:
* Always begin with "**Alexa, ask Davis**".
This is the name of my oldest, and I should be utilizing the sessions parameter
more with Alexa, but it's truly PoC code as you'll see.
* CSR access is **ssh cisco@ec2-52-91-174-10.compute-1.amazonaws.com**.
Yeah I know, we are network geeks. This will be good to show in a window to
verify get information, or set information when things change.
* Enunciate well! It might get finicky otherwise, or maybe me struggling with a
Souther accent.
* Use the utterances below. I have more, or can add anything you like upon
request.

## DEMO SCRIPT
1. Pull up POSTMAN, and SSH into the CSR.
Show off a few things, whatever.
2. "***Alexa, ask Davis, Hello***""
This is hello world. You don't need to do this if you're confident things are
working as they should.
3. "***Alexa, ask Davis Get C P U***"
Like it reads. This will read the top line, and report back the 5sec and 1min
.CPU
4. "***Alexa, ask Davis, Tell me the status of interface gigabit ethernet one***"
Like it reads. This will tell you the status of G1 on the CSR. Show it on the
CSR too.
5. "***Alexa, ask Davis, Tell me the status of interface loop one***"
Like it reads. This will tell you the status of LO1 on the CSR. Show it on the
CSR too.
6. "***Alexa, ask Davis, Save the config***"
Like it reads. This will do a 'wr mem' on the box and readout the JSON repsonse.
7. "***Alexa, ask Davis, Create interface loop two***"
Like it reads. This will create a loopback2 on the CSR. Show it.
7. "***Alexa, ask Davis, Destroy interface loop two***"
Like it reads. This will create a loopback2 on the CSR. Show it.
8. "***Alexa, ask Davis, Disable RESTCONF***"
Easter egg. Just messin' around!
9. "***Alexa, ask Davis, roll back the demo***"
Reset everything to the start. Do this whenever. As a bonus, you can show off
config-replace, since it uses this to reset things.

## ALL ELSE FAILS
Just pull these videos. Turn the sound down. You can talk through them and don't
have to listen to me!

[RESTCONF-only](https://sharevideo.cisco.com/#/videos/ba89acc8-3e60-4c0b-b5f5-e17dc1e5deec) -- Calls to the CSR that Alexa does.

[Full-example](https://sharevideo.cisco.com/#/videos/f66bf8f9-b91e-49ec-a80b-23b351b38e2b) -- If something happens, just show the full video!

## Folders:
**RESTCONF** -- This folder contains the actual instructions sent to Alexa when you
play. This is always good to show first thing. You can set the stage for the
demo. I exported these RESTCONF calls for you to be run in POSTMAN. They should
work for you out of the box. Don't modify them! You can create some of your own,
but of course .. take care and don't mess things up too much.

**BOOKMARKS** -- This folder is a collection of bookmarks to show folks the REST (or
Flask) equivalent of what Flask-Ask is doing with Alexa. It's really easy, and
for a code writer, might want to start with Flask before going to Flask-Ask.
Either way, you can import the bookmarks into your own browser, and just show
some data if you want .. if you're tied of asking Alexa.

**CODE** -- This folder is the code. There are 2 files in here. One file called
"common_funcs.py" is the file that does the heavy-lifting for our Alexa app. It
technically creates all the function calls through RESTCONF. The file called
"iosrest.py" is our Alexa app. It's essentially really easy flask-ask defining
intents and asking for output!
