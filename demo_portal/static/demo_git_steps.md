# Demo: "Git-ing" Code 

This demo will show you how IOS XE gives you access to modern developer tools like `git` on your network element. 

## Demo Steps

1. Open Terminal & log into the IOS XE device using SSH

        ssh cisco@10.10.140.1

        password 'cisco'
    
1. Access Guest Shell Environment

        guestshell run bash
            
        # Output
        [guestshell@guestshell ~]$
    
1. Clone down demo repository 

        git clone https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth
        
        # Output
        Cloning into 'clus2017_iosxe_demo_booth'...
        remote: Counting objects: 102, done.
        remote: Compressing objects: 100% (91/91), done.
        remote: Total 102 (delta 2), reused 94 (delta 2), pack-reused 7
        Receiving objects: 100% (102/102), 4.27 MiB | 2.90 MiB/s, done.
        Resolving deltas: 100% (2/2), done.
    
1. Enter directory.  

        cd clus2017_iosxe_demo_booth
    
1. Explore the repository with some `git` commands

        git log
        git status
        git show
    
1. Run code from the repository.  

        cd demo_GitingCode
        python hangman.py 
        
        # Output
        Loading word list from file...
           10 words loaded.
        
        
        +++++Welcome to the game, Hangman!+++++
        
        I am thinking of a word that is 6 letters long.
        
        You have 8 guesses left.
        Available letters: abcdefghijklmnopqrstuvwxyz
        
        Please guess a letter:    
    
1. Play the game... see if you can guess the word.  

1. Let's add some new words to the list.

1. Open the `words.txt` file, a shortcut should be on the desktop.  Add a few words to the list.  

1. On the laptop, open up the terminal for `git demo`.  And follow these steps to add, commit, and push your changes to GitHub.  *Enter your name in the commit message*

        git add words.txt 
        
        git commit -m "Hank added new words to hangman"
        
        # Output    
        [master b6fc0dd] Hank added new words to hangman
        1 file changed, 1 insertion(+), 1 deletion(-)
    
        git push
        
        # Output
        Counting objects: 4, done.
        Delta compression using up to 8 threads.
        Compressing objects: 100% (4/4), done.
        Writing objects: 100% (4/4), 359 bytes | 0 bytes/s, done.
        Total 4 (delta 3), reused 0 (delta 0)
        remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
        To https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth
           08ed8f0..b6fc0dd  master -> master    
    
1. Back on the IOS XE Device, `pull` down your changes.  

        git pull 
        
        # Output
        remote: Counting objects: 4, done.
        remote: Compressing objects: 100% (1/1), done.
        remote: Total 4 (delta 3), reused 4 (delta 3), pack-reused 0
        Unpacking objects: 100% (4/4), done.
        From https://github.com/CiscoDevNet/clus2017_iosxe_demo_booth
           08ed8f0..b6fc0dd  master     -> origin/master
        Updating 08ed8f0..b6fc0dd
        Fast-forward
         demo_git/words.txt | 2 +-
         1 file changed, 1 insertion(+), 1 deletion(-)    
    
## Summary and Cleanup

Great job!  You have seen how having access to developer tools like `git` right on the network elements can make it easy to manage applications, code, and scripts. Develop and test locally, and then use typical DevOps processes and tools to distribute and update code network wide.  

1. Cleanup the device for the next demo by deleting the code directory.  

        cd ~
        rm -Rf clus2017_iosxe_demo_booth    
