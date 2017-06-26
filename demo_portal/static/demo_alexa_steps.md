##  Demo Steps
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
