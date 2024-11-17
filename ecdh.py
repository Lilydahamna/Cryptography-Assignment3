import random
import time

#secp160r1 parameters
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFF
a = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF7FFFFFFC
b = 0x1C97BEFC54BD7A8B65ACF89F81D4D4ADC565FA45
Gx = 0x4A96B5688EF573284664698968C38BB913CBFC82
Gy = 0x23A628553168947D59DCC912042351377AC5FB32
order = 0x0100000000000000000001F4C8F927AED3CA752257

#helper function to perform point addition according to textbook
def point_addition(P, Q, p, a):
    if P is None:
        return Q
    if Q is None:
        return P
    
    x1, y1 = P
    x2, y2 = Q

    #in this case Q is the additive inverse of P 
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    #in this case P and Q are distinct 
    if P != Q:
        lam = (y2 - y1) * pow((x2-x1), -1, p) % p
    #point doubling case
    else:
        #division not defined
        if y1 == 0:  
            return None
        lam = (3 * x1**2 + a) * pow((2 * y1), -1, p) % p

    x3 = (lam**2 - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)

#helper function to perform multiplication using double and add algorithm which makes use of the binary representation of k
def multiplication(k, P, p, a):
    bits = bin(k)[2:]  
    result = None  
    temp = P  

    #Process bits from LSB to MSB
    for bit in reversed(bits):  
        if bit == '1':  
            result = point_addition(result, temp, p, a)  
        temp = point_addition(temp, temp, p, a) 

    return result

#helper function to compute secret key and time computations
def compute_secret_key(nX, PY, p, a):
    start_time = time.time() 

    secret_key = multiplication(nX, PY, p, a)

    end_time = time.time() 

    time_taken = end_time - start_time

    return secret_key, time_taken

#private key for A randomly picked from range [1, order-1]
nA = random.randint(1, order - 1)
#private key for B randomly picked from range [1, order-1]
nB = random.randint(1, order - 1)

#public key for A PA = nA * G 
PA = multiplication(nA, (Gx, Gy), p, a)

#public key for B PB = nB * G 
PB = multiplication(nB, (Gx, Gy), p, a)

#compute secret keys
secret_key_A, time_A = compute_secret_key(nA, PB, p, a) 
secret_key_B, time_B = compute_secret_key(nB, PA, p, a)  

# Print results
print(f"Shared Secret Key: {secret_key_A}")
print(f"Shared Secret Key: {secret_key_B}")
print(f"Time Taken by A: {time_A} seconds")
print(f"Time Taken by B: {time_B} seconds")