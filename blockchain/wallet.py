from blockchain.wallet import Wallet

wallet = Wallet('ada4e4b6-3c9f-11e4-baad-164230d1df67', 'password123', 'http://localhost:3000')

print wallet.get_balance() 