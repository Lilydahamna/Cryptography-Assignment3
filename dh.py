import random
import time

# Predefined prime and generator values
p = int(
    "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B61"
    "6073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BF"
    "ACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0"
    "A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371", 16
)

g = int(
    "A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31"
    "266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4"
    "D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A"
    "D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5", 16
)

#Private keys for A and B
XA = random.randint(1, p - 1)  
XB = random.randint(1, p - 1)  

#Public keys for A and B
YA = pow(g, XA, p)  
YB = pow(g, XB, p)  

#Time the computation of the shared secret for A
start_time_A = time.time()
s_A = pow(YB, XA, p) 
time_taken_A = time.time() - start_time_A

#Time the computation of the shared secret for B
start_time_B = time.time()
s_B = pow(YA, XB, p)  
time_taken_B = time.time() - start_time_B

# Output the results
print(f"Shared Secret (s) computed by A: {s_A}")
print(f"Shared Secret (s) computed by B: {s_B}")
print(f"Time Taken by Alice to Compute s: {time_taken_A:} seconds")
print(f"Time Taken by Bob to Compute s: {time_taken_B:} seconds")


