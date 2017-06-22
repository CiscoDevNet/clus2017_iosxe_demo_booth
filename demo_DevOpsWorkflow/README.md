 # Demo: DevOps Workflow 

This demo shows how you can use device APIs to enable a DevOps workflow to manage configurations of network elements using a golden image.

## Demo Steps

1. Open Terminal & log into the IOS XE device using SSH

        ssh cisco@10.10.140.1

        password 'cisco' 
    
1. Verify no route-map is configured on the device

        Switch#sh run | sec route-map
    
1. Execute ’dir’ on the switch and you will see all the existing files on the flash, “GoldenImage” is the file you are going to use to replace the running config. 

        Switch#dir
        Directory of flash:/
    
1. Open another tab in Terminal and enter below cmd.  

        cd ~
    
1. Explore the Python script that will execute the config replace.

        more GoldenImage.py
    
1. Execute the script in the terminal.  

        time ./GoldenImage.py ssh://cisco:cisco@10.10.140.1 –v
    
1. Go to the switch tab and verify config has been replaced.  

        Switch#sh run | sec route-map 
        route-map Cisco_Live permit 1
        match ip address Catalyst_ACL
        set ip next-hop 12.13.14.15
    
## Summary and Cleanup

Great job!  You have seen how you can use IOS XE programmability features to manage your network elements using a DevOps workflow to manage a golden image config.  

1. Cleanup the device for the next demo by executing the script below which is on desktop.  

        time ./reset_replace.py ssh://admin:admin@10.10.140.1 -v

1. Verify on the Switch config has been reset.  

        Switch#sh run | sec route-map 
