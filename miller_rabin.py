#Miller Rabin probabilistic primality test implementation

import random


#n is the number to test and a is the witness number
def miller_rabin(n, a):
    #we first factor n-1 into 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    #compute a^d % n
    x = pow(a, d, n) 

    if x == 1 or x == n - 1:
        return True 

    for _ in range(s - 1):
        #xi = (xi-1)^2 mod n
        x = pow(x, 2, n) 

        #inconclusive
        if x == n - 1:
            return True

    return False 
    
while True:
    #generate candidate 14-bit number
    n = random.randint(2**13, 2**14 - 1)  
    
    is_probable_prime = True

    #keep track of used witnesses for each number n 
    used_witnesses = set()

    #execute miller rabin for 7 iterations with different witness numbers
    for _ in range(7):  
        #generate a random witness and make sure it was not used in previous iterations
        while True:
            a = random.randint(2, n - 2)
            if a not in used_witnesses:
                used_witnesses.add(a)
                break

        if not miller_rabin(n, a): 
            is_probable_prime = False
            break
    
    if is_probable_prime:
        print("14-bit probable prime:", n)
        break
