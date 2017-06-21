 # Demo: DevOps Workflow 

## Demo Steps

1. Open the Terminal & log into the IOS XE device using SSH

        ssh admin@10.10.140.1 
    
1. Verify no route-map is configured on the device

        Switch#sh run | sec route-map
    
1. Execute ’dir’ on the switch and you will see all the existing files on the flash, “config_rm” is the file you going to replace with running config. 

        Switch#dir
        Directory of flash:/
    
1. Open another tab in the terminal and enter below cmd.  

        cd ~/Desktop
    
1. Explore the YDK AP

        more config_replace.py
    
1. Execute the App in the terminal.  

        time ./config_replace.py ssh://cisco:cisco@10.10.140.1 –v
    
1. Go to the switch tab and verify config has been replaced.  

        Switch#sh run | sec route-map 
        route-map Cisco_Live permit 1
        match ip address Catalyst_ACL
        set ip next-hop 12.13.14.15
    
## Summary and Cleanup

Great job!  You have seen how having access to developer tools like `git` right on the network elements can make it easy to manage applications, code, and scripts.  Develop and test locally, and then use typical DevOps processes and tools to distribute and update code network wide.  

1. Cleanup the device for the next demo by executing the script below which is on desktop.  

        time ./reset_replace.py ssh://admin:admin@10.10.140.1 -v

1. Verify on the Switch config has been reset.  

        Switch#sh run | sec route-map 

