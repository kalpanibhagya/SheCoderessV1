#0110110001110101011000
#011100000111100101110100011010000110111101101110
 
n = input()
for x in range (int(n)):
    bitstream = input()
    length = 8
    wordarr=[]
 
    ##arr=[bitstream[i:i+n] for i in range(0, len(bitstream), n)]
    ##
    ##for frame in arr:
    ##    frame = int(frame)
    ##    char = chr(frame)
    ##    print (char)
 
    input_l = [bitstream[i:i+length] for i in range(0,len(bitstream),length)]
    for set in input_l:
        if (len(set) == 8):
            wordarr.append(chr(int(set,base=2)))
 
    word = ''.join(wordarr)
    print (word)
 
