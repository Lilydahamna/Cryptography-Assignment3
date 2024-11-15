#ElGamal Implementation following description from the textbook

import random

q = 89    # Prime
a = 13    # Primitive root
X = 5     # Private key
Y = 74    # Public key

#Encryption
def encrypt(q, a, Y, k, message):
    #if k is not given, then we generate some k such that 1<= k <= q-1
    if k is None:
      k = random.randint(1, q - 1)
    
    #compute key K using k 
    K = pow(Y, k, q)

    #compute C1
    C1 = pow(a, k, q)

    #compute C2
    C2 = (K * message) % q

    #We return ciphertext as tuple (C1, C2)
    return (C1, C2)

#Decryption
def decrypt(C1, C2, X, q):
   #compute key K using C1 and X
   K = pow(C1, X, q)

   #compute inverse of K by taking K^(q-2), since By Fermat's Little Theorem K^(q-1) = 1 mod q
   K_inverse = pow(K, q - 2, q)

   #compute message from C2 and K_inverse
   message = (C2 * K_inverse) % q

   return message

m1 = 72
m2 = random.randint(1, q - 1)  
k = 41 

# Encrypt m1 and m2
ciphertext_m1 = encrypt(q, a, Y, k, m1)
ciphertext_m2 = encrypt(q, a, Y, k, m2)

# Output the results
print("Original Message m1:", m1)
print("Ciphertext for m1 (C1, C2):", ciphertext_m1)
print("----------")
print("Original Message m2:", m2)
print("Ciphertext for m2 (C1, C2):", ciphertext_m2)

print("Decrypted m2:", decrypt(35, 20, X, q))