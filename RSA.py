import random
import time
from sympy import randprime, mod_inverse, gcd

#helper function to generate/initialize RSA parameters
def generate_parameters():
    while True:
        #Generate 1024-bit primes p and q
        p = randprime(2**1023, 2**1024)
        q = randprime(2**1023, 2**1024)

        #Compute/initialize RSA parameters
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = 65537

        #Ensure e is coprime with phi_n
        if gcd(e, phi_n) == 1:
            break  

    #Compute the private key
    d = mod_inverse(e, phi_n)

    return p, q, n, phi_n, e, d

#Encrypt m using public key
def rsa_encrypt(m, e, n):
    #Encrypt the message m
    c = pow(m, e, n)

    return c

#decrypt using CRT following textbook description
def rsa_decrypt_crt(c, d, p, q, n):
    start_crt = time.time()

    d_p = d % (p - 1)
    d_q = d % (q - 1)

    Vp = pow(c, d_p, p)
    Vq = pow(c, d_q, q)

    p_inv = mod_inverse(p, q)
    q_inv = mod_inverse(q, p)

    Xp = q * q_inv
    Xq = p * p_inv

    h = (Vp * Xp) +  (Vq * Xq)
    m_decrypted_crt = h % n

    end_crt = time.time() 
    time_taken_crt = end_crt - start_crt

    return m_decrypted_crt, time_taken_crt

#decrypt without crt
def rsa_decrypt_no_crt(c, d, n):
    start_no_crt = time.time()
    m_decrypted_no_crt = pow(c, d, n)
    end_no_crt = time.time()

    time_taken_no_crt = end_no_crt - start_no_crt

    return m_decrypted_no_crt, time_taken_no_crt


#parameters
p, q, n, phi_n, e, d = generate_parameters()
#message
m = 476931823457909

#Encrypt the message
c = rsa_encrypt(m, e, n)

#Decrypt the message using CRT
m_decrypted_crt, time_crt = rsa_decrypt_crt(c, d, p, q, n)

#Decrypt the message without CRT
m_decrypted_no_crt, time_no_crt = rsa_decrypt_no_crt(c, d, n)


print("\nMessage to encrypt:", m)
print("Ciphertext (c):", c)
print("\nDecrypted message without CRT:", m_decrypted_no_crt)
print("Decrypted message with CRT:", m_decrypted_crt)
print(f"\nDecryption time without CRT: {time_no_crt} seconds")
print(f"Decryption time with CRT: {time_crt} seconds")
