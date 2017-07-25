raws=int(raw_input())
x1=0
x2=0
count=0
mid =raws/2
array=[]
i=0
while(i<raws):
    line=raw_input()
    array.append(line)
    i+=1
    
for c in array[mid]:
    count+=1
    if(c=="#"):
        if(x1 ==0):
            x1=count
        else:
            x2=count
radius =(x2-x1)/2
 
print(radius)
    

