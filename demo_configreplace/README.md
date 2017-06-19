 Demo Steps:


1.	Open the Terminal and log into the IOS XE device using SSH
    ssh cisco@10.10.140.1 

2.	Verify no route-map is configured on the device
    Switch#sh run | sec route-map

3.	Execute ’dir’ on the switch and you will see all the existing files on the flash, “config_rm” is the file you going to replace with running config.
    Switch#dir
      Directory of flash:/

4.	Open another tab in the terminal and enter below cmd
    cd ~/Desktop

5.	Explore the YDK APP
    more config_replace.py

6.	Execute the App in the terminal
    time ./config_replace.py ssh://cisco:cisco@10.10.140.1 –v

7.	Goto the switch tab and verify config has replaced
    Switch#sh run | sec route-map
    route-map Cisco_Live permit 1
      match ip address Catalyst_ACL
      set ip next-hop 12.13.14.15




Cleanup

1.	Execute below script which is on desktop
    time ./reset_replace.py ssh://admin:admin@10.10.140.1 -v

2.	Verify on the Switch config has resetted.
    Switch#sh run | sec route-map

