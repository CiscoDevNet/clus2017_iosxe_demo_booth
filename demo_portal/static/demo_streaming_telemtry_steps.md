# Demo: Streaming Telemetry 

This demo shows how to stream telemetry off a Catalyst 9300. Data is pushed off the network element in a structured format that can easily be integrated with other tools. In this case we will use [Kafka](https://kafka.apache.org/) and an [ELK stack](https://www.elastic.co/products) (Elasticsearch, Logstash, and Kibana) to visualize the data streaming off the device. Requires IOS XE 16.6.1

## Demo Steps

1. Open Terminal & log into the IOS XE device using SSH

        ssh cisco@172.26.244.91

        password 'cisco' 
    
1. Check to make sure there are not any active telemetry subscriptions

        show telemetry ietf subscriptions all
    
1. Open Chrome and click on the bookmark for Kibana.

        Notice that there is no data in our dashboard because we haven't setup the telemetry subscriptions yet.

1. Open VMWare Fusion

![](static/img/vmware_fusion_icon.png)

1. Login to the VM  

        password 'kafka'
        
        Note that Kafka & ELK are already running on the VM, but there is no data until we setup a 
        telemetry subscription to push data from the device
    
1. Select the terminal called 'IETF Client' and launch the IETF Client

        python3 /home/kafka/telemetry/demo/ietf_client.py --uut_ip '10.10.130.1' --kafka 'localhost' --user cisco --password cisco
    
1. Select the terminal called 'Telemetry Subscriptions' and look at the telemetry subscriptions you will be setting up.  

        
        cat subscribe_me.sh
        
1. Now execute the subscribe_me.sh file to setup the subscriptions.

        ./subscribe_me.sh
            
1. Back on the terminal connected to the Catalyst 9300 verify the subscriptions.

        show telemetry ietf subscriptions all

        #Output 

1. Now go back to Chrome

        The dashboards are now populating with telemetry data that is being pushed from the Catalyst 9300
    
## Summary and Cleanup

Great job! You've successfully setup a subscription for telemetry and seen how easy it is to integrate with open source tools thanks to the standards based APIs and structured data available on IOS XE and the Catalyst 9300.

1. On the VM select the terminal called 'IETF Client' and then press ctrl+c twice.
