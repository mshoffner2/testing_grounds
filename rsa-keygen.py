# coding: utf-8
# In[1]:
import binascii
from random import *
import array
import sys

#finding the value of e, just trying out small primes until one works
def find_e(a):
    potential_e = array.array('i', [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43])
    
    for i in potential_e:
        if(a % i != 0):
            return i

#finding the multiplicative inverse of d
def find_d(e,n):
    q=0
    r1=n
    r2=e
    s1=1
    s2=0
    t1=0
    t2=1
    while(r2!=0):                                   
    #updating quotient
        q=r1//r2
    #updating remainder
        temp=r2
        r2=r1-q*r2   
        r1=temp
    #updating s1
        temp=s2
        s2=s1-q*s2
        s1=temp
    #updating t1
        temp=t2
        t2=t1-q*t2
        t1=temp
    
    if (t1<0):
        t1=n+t1
    return t1
    
#finding the factors of a number n    
def factoring(n):
    s=0
    odd=0
    d=n
    while odd!=1:
        
        
        if(d%2!=0):
            
            odd=1
        else:
            s=s+1
            d=d//2
        
    return (s,d)
    
#determining if a number is prime
def is_prime(n):
    
    #2 is a prime number
    if n == 2:
        return 1
    
    #if the number is even, it is composite
    if n%2 == 0:
        return 0

    r,s=factoring(n-1)
    k=10
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return 0
    return 1
        




#generating the public and private key
def rsa_keygen(pubname, privname, size):
#generating p    
    high_bit = 2 ** (size-1)
    my_test_rand = getrandbits(size)
    if(my_test_rand < high_bit):
        my_test_rand = my_test_rand + high_bit
    
    while(is_prime(my_test_rand)== 0):
        my_test_rand = getrandbits(size)
        if(my_test_rand < high_bit):
            my_test_rand = my_test_rand + high_bit
        
    p = my_test_rand
#generating q
    my_test_rand = getrandbits(size)
    if(my_test_rand < high_bit):
        my_test_rand = my_test_rand + high_bit
    while(is_prime(my_test_rand) == 0):
        my_test_rand = getrandbits(size)
        if(my_test_rand < high_bit):
            my_test_rand = my_test_rand + high_bit
    
    q = my_test_rand
    
    #if q accidently is the same as p, re-find q
    while(q == p):
        my_test_rand = getrandbits(size)
        if(my_test_rand < high_bit):
            my_test_rand = my_test_rand + high_bit
        while(is_prime(my_test_rand) == 0):
            my_test_rand = getrandbits(size)
            if(my_test_rand < high_bit):
                my_test_rand = my_test_rand + high_bit

        q = my_test_rand
    
    #print "p: " + str(p) + "  " + "{0:b}".format(p)
    #print "q: " + str(q) + "  " + "{0:b}".format(q)
#calculating the order of the group    
    orderN = (p-1) * (q-1)
#calculating the value of n    
    N = p * q
    #print "N: " + str(N)
    #print "Order of N: " + str(orderN)
#finding e    
    e = find_e(orderN)
    #print "e: " + str(e)
#finding d    
    d = find_d(e, orderN)
    #print "d: " + str(d)
#calculating the number of bits in N    
    bit_n = N.bit_length()
    #print "Bits: " + str(bit_n)
#writing the public key to a file    
    pub_file = open(pubname, "w")
    pub_file.write(str(bit_n)+'\n')
    pub_file.write(str(N)+'\n')
    pub_file.write(str(e))
    pub_file.close()
#writing the private key to a file    
    priv_file = open(privname, "w")
    priv_file.write(str(bit_n)+'\n')
    priv_file.write(str(N)+'\n')
    priv_file.write(str(d))
    priv_file.close()
    




pub_f_name = ""
priv_f_name = ""
length_n = 0

if len(sys.argv) != 7:
    print('usage: rsa-keygen -p <public key file> -s <private key file> -n <number of bits>')
    exit()
    
if(sys.argv[1] == '-p'):
    pub_f_name = sys.argv[2]
elif(sys.argv[3] == '-p'):
    pub_f_name = sys.argv[4]
elif(sys.argv[5] == '-p'):
    pub_f_name = sys.argv[6]
else:
    print('usage: rsa-keygen -p <public key file> -s <private key file> -n <number of bits>')
    exit()
    
if(sys.argv[1] == '-s'):
    priv_f_name = sys.argv[2]
elif(sys.argv[3] == '-s'):
    priv_f_name = sys.argv[4]
elif(sys.argv[5] == '-s'):
    priv_f_name = sys.argv[6]
else:
    print('usage: rsa-keygen -p <public key file> -s <private key file> -n <number of bits>')
    exit()
    
    
if(sys.argv[1] == '-n'):
    length_n = sys.argv[2]
elif(sys.argv[3] == '-n'):
    lenght_n = sys.argv[4]
elif(sys.argv[5] == '-n'):
    length_n = sys.argv[6]
else:
    print('usage: rsa-keygen -p <public key file> -s <private key file> -n <number of bits>')
    exit()
length_n = int(length_n)    
rsa_keygen(pub_f_name, priv_f_name, length_n)

