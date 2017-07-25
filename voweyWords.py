import math

T = int(raw_input())

rounds = 0
Arry = []
while rounds < T:
    string = raw_input()
    Arry.append(string)
    rounds += 1

for j in Arry:
    vowel_count = 0
    List = list(j)
    for i in List:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel_count += 1

    total = len(List)
    if vowel_count % 2 == 0 and vowel_count <= math.sqrt(total):
        print("YES")


    else:
        print("NO")