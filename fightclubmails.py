import re
n = input()

for i in range (int(n)):
    
    email = input()

    emailarr = email.split('@')

    formatflag = 0
    domainflag = 0

    domain = ["fightclub.uk","fightclub.com","fightclub.lk","fightclub.sa","fightclub.cc","fightclub.jp","fightclub.se","fightclub.xy","fightclub.gi","fightclub.rl","fightclub.ss"]

    if len(emailarr[0]) >= 3 and len(emailarr[0]) <= 6: #checks the length of the username is fits
        if (re.match("^[A-Za-z0-9_-]*$",emailarr[0] )):
            
        
            for a in emailarr[0]:
            
                if(a.isupper()):
                    print("INVALID")
                    break
            for i in domain:
                if (i == emailarr[1]):
                    print ("VALID") #or can set the domainflag to 1 and then check after the loop, this is quick
                    domainflag = 1
                    break
                else:
                    domainflag = 0
            if (domainflag == 0):
                print ("INVALID")
        else:
            print ("INVALID")
    else:
        print("INVALID")
