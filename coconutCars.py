val=raw_input()
tree=[]
ll=[]
rounds=val.split(" ")
Q=int(rounds[0])
M=int(rounds[1])
 
for i in range(0,M):
    par=raw_input()
    pair=par.split(" ")
     
##    for a in tree:
##        if(a==int(pair[0])):
##            break
##    tree.append(int(pair[0]))
##    
##    for b in tree:
##        if(b==int(pair[1])):
##            break
##    tree.append(int(pair[1]))
    
    
    tree.append(int(pair[0]))
    tree.append(int(pair[1]))
 
P=int(raw_input())
 
for j in range(0,P):
    qp=raw_input()
    ll.append(qp.split(" "))
 
for k in ll:
    if(int(k[0]) in tree and int(k[1]) in tree):
        print("YES")
    else:
        print("NO")
    
