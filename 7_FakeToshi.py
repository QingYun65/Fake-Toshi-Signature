from ecc import S256Point, Signature, G, N
from random import randint
# key from genesis block coinbase transaction
# 4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
GENESIS_BLOCK_PUBKEY = '04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f'
point = S256Point.parse(bytes.fromhex(GENESIS_BLOCK_PUBKEY))
# generate random u and v values
# (these will be different every time this script is run)
u = randint(0, N)
v = randint(0, N)

# calculate the x-coordinate of r
r = (u*G+v*point).x.num % N

# calculate s and z using Fermat's Little Theorem
s = r * pow(v, N-2, N) % N
z = u * s % N

# instantiate the Signature class
sig = Signature(r, s)

# This will crash if the signature is invalid:
assert point.verify(z, sig) is True

print("Valid signature of a garbage message:")
print("z: ", z)
print(sig)
