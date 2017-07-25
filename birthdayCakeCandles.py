T = int(raw_input())
if T == 0:
    print(0)
S = raw_input()
 
List = map(int, S.split())
 
List1 = sorted(List)
 
Max = max(List1)
count = 0
i = 0
while i < len(List1):
    if Max == List[i]:
        count +=1
    
    i +=  1   
print(count)
