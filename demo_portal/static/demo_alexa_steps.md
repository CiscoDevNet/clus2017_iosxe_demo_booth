# Demo: Talk to the Network 

This demo shows how you can use device APIs to seamlessly interact with other systems or apps. In this case we have used the device APIs to create an Alexa skill that lets you talk to the network device through Alexa.

##  Demo Steps
1. Open Terminal & log into the IOS XE device using SSH

        ssh gsxcisco@ec2-52-37-181-235.us-west-2.compute.amazonaws.com

1.  Check the CPU utilization (5 sec and 1 min CPU)

        sh proc cpu
        
        Alexa, ask Cisco get CPU

1. Check the status of GigabitEthernet1/0/1 then check the status of Loopback1

        sh ip int br
        
        Alexa, ask Cisco, Tell me the status of interface gigabit ethernet one

        Alexa, ask Cisco, Tell me the status of interface loop one

1. Create Loopback2

        Alexa, ask Cisco, create interface loop two
        
        sh ip int br
        
1. Delete Loopback2

        Alexa, ask Cisco, destroy interface loop two

        sh ip int br

1. Save the config

        Alexa, ask Cisco, Save the config

1. Disable RESTCONF

        Alexa, ask Cisco, Disable RESTCONF

1. Reset the demo

        Alexa, ask Cisco, roll back the demo
