from cryptographic_functions import generate_key_pair, generate_address

class Wallet:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.address = None

    def generate_wallet(self):
        # Generate a new wallet with a key pair and address
        private_key, public_key = generate_key_pair()
        self.private_key = private_key
        self.public_key = public_key
        self.address = generate_address(public_key)

    def display_wallet_info(self):
        # Display the wallet's information
        print("Wallet Information:")
        print("Address:", self.address)
        print("Public Key:", self.public_key)
        print("Private Key:", self.private_key)
