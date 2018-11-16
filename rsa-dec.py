# coding: utf-8
# In[1]:

import sys
import os
import math

#finding the modular exponent
def mod_exp(b,e,n):
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

def rsa_dec(ciphertext, N, d, size_N):
    padded_msg = mod_exp(ciphertext, d, N)
    temp = hex(padded_msg)[2:]
    print(temp)
    #gotta remove padding: check for null byte
    
    #find size of the padded message in bits
    i = math.log(padded_msg, 2)
    
    #convert to bytes
    i = int(i)
    i = i / 8
    #print "i"
    #print(i)
    #print int(i)
    i = int(i)
    print(i)

    #search for the null byte marking the changeover from r bytes to message bytes
    while(padded_msg/(2**(i*8)) % 256 != 0):
        i = i - 1
    #print "i"
    print(i)
    #print(padded_msg/(2**(i*8)) % 256)

    #remove r
    #temp = hex(padded_msg)[2:]
    #print(temp)


    result = padded_msg % (2**(i*8))
    #change back to hex, remove extra characters added
    #result = padded_msg
    #result = hex(result)[2:]
    #i = len(result)-1
    #keep_going = 1

    #while(keep_going == 1 and i < len(result) - 1):
    #    if(result[i] == '0' and result[i + 1] == '0'):
    #        keep_going = 0
    #    i = i - 1
    #result = result[i:]
    #result = int(result, 16)
    result = hex(result)[2:]
    #print "result"
    print(result)
    
    return(result)
    





key_f_name = ""
in_f_name = ""
out_f_name = ""

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


in_file = open(in_f_name, "r")
my_text = in_file.read()
in_file.close()

key_file = open(key_f_name, "r")
size_N = key_file.readline()
main_N = key_file.readline()
main_d = key_file.readline()
key_file.close()

main_N = int(main_N)
main_d = int(main_d)

result = rsa_dec(int(my_text), main_N, main_d, int(size_N))
#open and write to output file

out_file = open(out_f_name, "w")
out_file.write(result)
out_file.close()

