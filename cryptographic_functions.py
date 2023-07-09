import hashlib
import ecdsa

def generate_key_pair():
    # Generate a new key pair
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key.to_string().hex(), public_key.to_string().hex()

def generate_address(public_key):
    # Generate a wallet address from the public key
    public_key_bytes = bytes.fromhex(public_key)
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new('ripemd160', sha256_hash).digest()
    address = ripemd160_hash.hex()
    return address
