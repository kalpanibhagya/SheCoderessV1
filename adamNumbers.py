T = raw_input()
T_num = int(T)
rev_T = T[::-1]
rev_T_num = int(rev_T)
 
squre_num = str(T_num*T_num)
square_rev = str(rev_T_num * rev_T_num)
        
if square_rev == squre_num[::-1]:
    print("yes")
else:
    print("no")
