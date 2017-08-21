 # Demo: DevOps Workflow 

This demo shows how you can use device APIs to enable a DevOps workflow to manage configurations of network elements using a golden config. Requires IOS XE 16.3.1.

## Demo Steps

1. Open Terminal & log into the IOS XE device using SSH

        ssh cisco@172.26.244.91

        password 'cisco' 
    
1. Verify no route-map is configured on the device

        Switch#sh run | sec route-map
    
1. Execute ’dir’ on the switch and you will see all the existing files on the flash, “GoldenConfig” is the file you are going to use to replace the running config. 

        Switch#dir | i Gold
        Directory of flash:/
    
1. Open another tab in Terminal and enter below cmd.  

        cd ~
    
1. Explore the Python script that will execute the config replace.

        more GoldenConfig.py
    
1. Execute the script in the terminal.  

        time ./GoldenConfig.py ssh://cisco:cisco@172.26.244.91 -v
    
1. Go to the switch tab and verify config has been replaced.  

        Switch#sh run | sec route-map 
        route-map Cisco_Live permit 1
        match ip address Catalyst_ACL
        set ip next-hop 12.13.14.15
    
## Summary and Cleanup

Great job!  You have seen how you can use IOS XE programmability features to manage your network elements using a DevOps workflow to manage a golden config.  

1. Cleanup the device for the next demo by executing the script below which is on desktop.  

        time ./VegasConfig.py ssh://cisco:cisco@172.26.244.91 -v

1. Verify on the Switch config has been reset.  

        Switch#sh run | sec route-map 
