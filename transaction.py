import hashlib
import ecdsa

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None

    def sign_transaction(self, private_key):
        # Sign the transaction using the private key:
        signing_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        signature = signing_key.sign(self.get_transaction_hash())
        self.signature = signature.hex()

    def get_transaction_hash(self):
        # Calculate the hash of the transaction data
        transaction_data = self.sender + self.recipient + str(self.amount)
        return hashlib.sha256(transaction_data.encode()).digest()
