from wallet import Wallet
from transaction import Transaction

# Create a new wallet
wallet = Wallet()
wallet.generate_wallet()
wallet.display_wallet_info()

# Create a transaction
recipient = "Recipient's Address"
amount = 10
transaction = Transaction(wallet.address, recipient, amount)
transaction.sign_transaction(wallet.private_key)
