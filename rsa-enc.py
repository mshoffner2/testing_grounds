# coding: utf-8
# In[1]:
from random import *
import os
import sys

#finding the modded exponential calculation
def mod_ex(b, e, n):
    bbin=bin(e)[2:]
    #print(bbin)
    blen=len(bbin)
    temp=1
    b1=1
    for i in range(blen-1,-1,-1):
        #print(i)
        b=(b*b1)%n;
        b1=b
        #print(b)
        if bbin[i]=='1':
            temp=(temp*b)%n
            #print (temp)
    return temp

def rsa_enc(message, N, e, size_N):
    i = 0
    total_r = 0
    temp_r = 0
    
    #initialize r to 2, so that I have that byte first
    total_r = 2
    
    #finding how big r should be
    n = (size_N/8)/2
    n = int(n)
    int_msg = int(message, 16)
    len_msg = int(int_msg.bit_length()/8) + 1

    numBytesR = n - len_msg - 3
    numBytesR = int(numBytesR)
    #print(n)
    #print(numBytesR)
    #print(len_msg)

    #generating r bytes of randomness, such that no byte is all 0
    for i in range(numBytesR):
        temp_r = 0
        while (temp_r == 0 or temp_r < 15 or temp_r % 8 == 0):
            temp_r = getrandbits(8)
            #print(temp_r)
        total_r *= (256)
        total_r += temp_r
    
    #r_len = int(total_r.bit_length()/8) + 1
    #print(r_len)
    #adding the null byte
    #print hex(total_r)
    total_r *= 2**8
    temp = hex(total_r)[2:]
    print(temp)

    #making space for the message at the end of total_r
    total_r *= 2**(len_msg * 8)

    temp = hex(total_r)[2:]
    #print(temp)
    
    #adding message to the end. Since message is an AES key, we assume that it's in hex in the file
    padded_msg = total_r + int_msg#int(message, 16)
    r_len = int(padded_msg.bit_length()/8) + 1
    #print(r_len)
    temp = hex(padded_msg)[2:]
    #print(temp)
    
    #find the cipher
    cipher_result = mod_ex(padded_msg, e, N)
    return cipher_result

    



key_f_name = ""
in_f_name = ""
out_f_name = ""

#getting the actual arguments. Yes, I know there's a python lib commands for this. But, this works, so.
#    I'm going with it.
if len(sys.argv) != 7:
    print('usage: rsa-enc -k <key file> -i <input file> -o <output file>')
    exit()
    
if(sys.argv[1] == '-k'):
    key_f_name = sys.argv[2]
elif(sys.argv[3] == '-k'):
    key_f_name = sys.argv[4]
elif(sys.argv[5] == '-k'):
    key_f_name = sys.argv[6]
else:
    print('usage: rsa-enc -k <key file> -i <input file> -o <output file>')
    exit()
    
if(sys.argv[1] == '-i'):
    in_f_name = sys.argv[2]
elif(sys.argv[3] == '-i'):
    in_f_name = sys.argv[4]
elif(sys.argv[5] == '-i'):
    in_f_name = sys.argv[6]
else:
    print('usage: rsa-enc -k <key file> -i <input file> -o <output file>')
    exit()
    
    
if(sys.argv[1] == '-o'):
    out_f_name = sys.argv[2]
elif(sys.argv[3] == '-o'):
    out_f_name = sys.argv[4]
elif(sys.argv[5] == '-o'):
    out_f_name = sys.argv[6]
else:
    print('usage: rsa-enc -k <key file> -i <input file> -o <output file>')
    exit()

    
#open and read in key file
key_file = open(key_f_name, "r")
size_N = key_file.readline()
main_N = key_file.readline()
main_e = key_file.readline()
key_file.close()

#open and read in message file
msg_file = open(in_f_name, "r")
msg_txt = msg_file.read()
msg_file.close()

main_N = int(main_N)
main_e = int(main_e)
size_N = int(size_N)

#call the actual cipher function
result = rsa_enc(msg_txt, main_N, main_e, size_N)

#open and write to output file
end_file = open(out_f_name, "w")
end_file.write(str(result))
end_file.close()



