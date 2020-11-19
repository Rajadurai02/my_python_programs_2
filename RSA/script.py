print("User input")
print("*************************************")
p = int(input("Enter the Prime number P: "))
q = int(input("Enter the Prime number Q: "))
e = int(input("Enter tha value for e: "))
m = int(input("Enter the value for M: "))
print("************************************")
def rsa():
    n = p*q 
    pi_n = (p-1) * (q-1)
    print("the value of n is: "+str(n))
    print("the value of pi_of_n is:"+str(pi_n))
    if e < pi_n:
        div = e
    else:
        div = pi_n
    for i in range(1,div):
        if (e % i == 0) and (pi_n % i == 0):
            gcd = i
    if gcd == 1:
        print("proceeded RSA alogoritm")
        k = 1
        while ((pi_n *k) + 1) % e != 0:
            k += 1
        d = (pi_n * k + 1) / e
        print(d)
        encrypt = (m ** e) % n 
        print("Encrypted cipher text is: "+str(encrypt))
        decrypt = (encrypt**d) % n
        print("Decrypted plain text is: "+str(decrypt))
    else:
        print("invalid e value finded so please enter correct details")
rsa()