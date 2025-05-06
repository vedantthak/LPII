# Function for modular exponentiation
def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo //= 2
    return res

# Function for extended Euclidean algorithm to find the modular inverse
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

# Function to find the modular inverse of e modulo phi
def modInverse(e, phi):
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        return -1  # No modular inverse exists
    return x % phi

# Function to compute the gcd of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate RSA keys
def generateKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1
    
    d = modInverse(e, phi)
    if d == -1:
        raise ValueError("No modular inverse found")
    
    return e, d, n

# Function to encrypt a message
def encrypt(m, e, n):
    return power(m, e, n)

# Function to decrypt a message
def decrypt(c, d, n):
    return power(c, d, n)

# Main function to test RSA
def rsa():
    # Take input for prime numbers p and q
    p = int(input("Enter a prime number (p): "))
    if not is_prime(p):
        print("p is not a prime number. Exiting.")
        return
    
    q = int(input("Enter another prime number (q): "))
    if not is_prime(q):
        print("q is not a prime number. Exiting.")
        return
    
    # Generate public and private keys
    e, d, n = generateKeys(p, q)
    
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")
    
    # Encrypt and decrypt a message
    M = int(input("Enter a message (as a number) to encrypt: "))
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")
    
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")

# Run the RSA function
rsa()
