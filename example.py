from wallet import mnemonic_to_creds, BSC

# Seed phrase BIP39
mnemonic = 'foam defense twice onion'

# Get the private key and wallet address using the Seed phrase
address, private_key = mnemonic_to_creds(mnemonic)
print(f'{private_key=}')
print(f'{address=}')

# Construct from private_key and address
wallet = BSC(private_key, address)

# Get wallet balance
balance = wallet.balance()
print(f'{balance=}')

# Send BNB specifying the recipient's address and the number of coins
tx_hash = wallet.send_transaction('0x0000000000000000000000000000000000000000', 0)
print(f'{tx_hash[1]=}')

if tx_hash[0]:
    # Check the transaction status
    while True:
        status = wallet.status_transaction(tx_hash[1])
        print(f'{status=}')
        if status:
            break
