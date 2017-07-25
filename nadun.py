T = int(raw_input())
S = raw_input()
 
weight_list = map(int, S.split())
 
i=0
 
weight_list1 = sorted(weight_list)
 
h =0
 
for i in weight_list1 :
    h = i +4
    count = 0
    for l in weight_list1:
        if l <=  h and l >= i:
            count += 1
        
 
print(count+2)
