#!/usr/bin/python3

from platform import node
import requests
from Models.transaction import Transaction
from Models.wallet import Wallet
import readline
import hashlib
import os
from Models.block import Block

wallet = None

SERVICE_URL = "http://127.0.0.1:5000"

def valid_proof(last_proof, proof, last_hash):
    """
    Validates the Proof

    :param last_proof: <int> Previous Proof
    :param proof: <int> Current Proof
    :param last_hash: <str> The hash of the Previous Block
    :return: <bool> True if correct, False if not.

    """

    guess = f'{last_proof}{proof}{last_hash}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"

def mine():
    global wallet
    if wallet is None:
        print("[!] Please generate/load a wallet first!")
        return -1
    print("[+] Mining!")
    r_last_block = requests.get(f"{SERVICE_URL}/last_block").json()
    last_block = Block.from_json(r_last_block)

    last_proof = last_block.proof
    last_hash = last_block.hash()

    proof = 0
    while valid_proof(last_proof, proof, last_hash) is False:
        proof += 1

    tx = Transaction("0", wallet.address, 1)
    sig = hex(wallet.sign_message(str(tx)))[2:]

    #required = ['recipient', "signature", "proof"]
    r = requests.post(f"{SERVICE_URL}/mine", json={"recipient": wallet.address, "signature": sig, "proof": proof})
    j = r.json()

    if r.status_code == 200:
        print(f"[+] Done! - {j['message']} ({j['index']})")
    else:
        print(f"[!] Done - {j['message']}")


def get_wallet_balance(addr=None):
    global wallet
    if addr is None:
        addr = wallet.address
    balance = requests.post(f"{SERVICE_URL}/balance", json={"address": addr}, headers={"Content-Type": "application/json"}).json()['amount']
    return balance

def wallet_show():
    global wallet
    if wallet is None:
        print("[!] Please generate/load a wallet first!")
        return -1
    
    print(f"[+] Address: {wallet.address}")
    balance = get_wallet_balance()
    print(f"[+] Balance: {balance}")

def balance():
    global wallet
    i = input("Enter Address (or blank for own)> ")
    print(f"Address: {i}")
    print(f"Balance: {get_wallet_balance(i)}")

def wallet_generate():
    global wallet
    wallet = Wallet()

def wallet_save():
    global wallet
    if wallet is None:
        print("[!] Please generate/load a wallet first!")
        return -1
    while True:
        i = input("Enter Wallet File Name> ")
        if os.path.exists(i):
            choice = input("File Exists, are you sure? [Y/N]").lower()
            if choice == 'y':
                wallet.save(i)
                break
        else:
            wallet.save(i)
            break

def wallet_load():
    global wallet
    i = None
    while True:
        i = input("Enter Wallet File Name (q to quit)> ")
        if i == "q":
            return
        if not os.path.exists(i):
            print("File does not exist")
        else:
            try:
                wallet = Wallet(i)
                break
            except Exception as e:
                print(f"Error when loading file: {e}")
                
    wallet = Wallet(i)

def nodes():
    r = requests.get(f"{SERVICE_URL}/nodes").json()
    print(f"[+] {r['length']} Nodes:")
    for n in r['nodes']:
        print("-" * 30)
        print(f"Address: {n}")
        print(f"Balance: {r['nodes'][n]}")

    print("-" * 30)

def help():
    print("Options: ")
    print(" | ".join(options))

def transaction():
    global wallet
    if wallet is None:
        print("[!] Please generate/load a wallet first!")
        return -1
    recipient = input("Enter Recipient> ")
    while True:
        amount = input("Amount> ")
        if amount.isdigit():
            if int(amount) > get_wallet_balance():
                print("[+] Cannot send more coin than you have!")
            else:
                break
        else:
            print("[+] NaN")
    data = input("Enter Data> ")
            
    tx = Transaction(wallet.address, recipient, int(amount))
    tx.data = data
    tx.sig = hex(wallet.sign_message(str(tx)))[2:]

    #required = ['sender', 'recipient', 'amount', 'signature']
    r = requests.post(f"{SERVICE_URL}/transactions/new", json={"sender": wallet.address, "recipient": recipient, "amount": int(amount), "signature": tx.sig, "data": data})
    print(f"[+] Sent Transaction: {r.json()['message']}")

def pending_transactions():
    r = requests.get(f"{SERVICE_URL}/tx_pool").json()
    print(f"[+] {r['length']} transactions")
    for transaction in r['transactions']:
        tx = Transaction.from_json(transaction)
        print("-" * 30)
        print(f"From:\t\t{tx.sender}")
        print(f"To:\t\t{tx.recipient}")
        print(f"Amount:\t\t{tx.amount}")
        print(f"Data:\t\t{tx.data}")

    print("-" * 30)

def blocks():
    r = requests.get(f"{SERVICE_URL}/chain")
    chain = r.json()['chain']
    for block in [Block.from_json(x) for x in chain]:
        print("-" * 30)
        print(f"Index:\t\t\t\t{block.index}")
        print(f"Previous hash:\t\t\t{block.previous_hash}")
        print(f"Proof:\t\t\t\t{block.proof}")
        print(f"Timestamp:\t\t\t{block.timestamp}")
        print(f"Number of Transactions:\t\t{len(block.transactions)}")

    print("-" * 30)

def transactions():
    i = 0
    while True:
        i = input("Enter Block Index> ")
        try:
            i = int(i)
            break
        except:
            print("Error: not a number")

    r = requests.get(f"{SERVICE_URL}/chain")
    chain = r.json()['chain']
    for block in [Block.from_json(x) for x in chain]:
        if block.index == i:
            for tx in block.transactions:
                print("-" * 30)
                print(f"From:\t\t{tx.sender}")
                print(f"To:\t\t{tx.recipient}")
                print(f"Amount:\t\t{tx.amount}")
                print(f"Data:\t\t{tx.data}")

    print("-" * 30)

options = {
            "help": help, 
            "wallet show": wallet_show, 
            "wallet generate": wallet_generate,
            "wallet load": wallet_load,
            "wallet save": wallet_save,
            "transaction": transaction,
            "mine": mine,
            "pending transactions": pending_transactions,
            "balance": balance,
            "nodes": nodes,
            "blocks": blocks,
            "transactions": transactions
}

if __name__ == "__main__":
    help()
    while True:
        i = input("Blockchain> ")
        if i in options:
            options[i]()
