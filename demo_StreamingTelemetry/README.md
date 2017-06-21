# Demo: Telemetry  

## Demo Steps

1. Open AnyConnect and connect to the Cisco lab

        TBD 
    
1. Open VNC to connect to the virtual machine

        ott-spectre:24
        asr123

1. In the bottom left window start the ietf client. This is how we will collect the telemetry data from the switch 

        python ietf_client.py --uut_ip 5.30.15.59
    
1. Enter the directory.  

        cd clus2017_iosxe_demo_booth
    
1. Explore the repository with some `git` commands

        curl -d '{"xpath":"/if:interfaces-state/interface[name=&quot;GigabitEthernet1/0/4&quot;]/statistics/out-octets", "period": 1000, "incident_id": '1234'}' -H 'Content-Type: application/json' http://127.0.0.1:8320/sendrpc
        
        curl -d '{"xpath":"/if:interfaces-state/interface[name=&quot;GigabitEthernet1/0/3&quot;]/statistics/in-octets", "period": 1000, "incident_id": '1234'}' -H 'Content-Type: application/json' http://127.0.0.1:8320/sendrpc
        
        curl -d '{"xpath": "/process-cpu-ios-xe-oper:cpu-usage/cpu-utilization/five-seconds","period": 1000, "incident_id": '1234'}' -H 'Content-Type: application/json' http://127.0.0.1:8320/sendrpc
    
1. Now that the subscriptions are setup, open Chrome and launch Kibana.  

        http://ott-kafka-1:5601 
    
1. Click on Visualize and then select a 'Line chart'.

![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/Telemetry2.png)

1. We will be creating this visualization 'From a new search'.

![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/Telemetry3.png)

1. Select the index pattern 'telemetry-*' from the drop down menu.  

![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/Telemetry4.png)

1. Now we are going to build the visualization. Select the following details

![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/Telemetry5.png)
        
![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/Telemetry6.png)
    
1. Save the visualization.  

![](https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth/blob/master/demo_telemetry/images/save.png)
    
## Summary

Great job!  You have seen how having access to developer tools like `git` right on the network elements can make it easy to manage applications, code, and scripts.  Develop and test locally, and then use typical DevOps processes and tools to distribute and update code network wide.  
