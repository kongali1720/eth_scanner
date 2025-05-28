import time
import requests
from eth_account import Account

ETHERSCAN_API_KEY = "masukkan_api_key_anda_di_sini"

def generate_wallet():
    acct = Account.create()
    return acct.key.hex(), acct.address

def get_eth_balance(address):
    url = f"https://api.etherscan.io/api"
    params = {
        "module": "account",
        "action": "balance",
        "address": address,
        "tag": "latest",
        "apikey": ETHERSCAN_API_KEY
    }
    response = requests.get(url, params=params)
    result = response.json()
    if result["status"] == "1":
        return int(result["result"]) / (10 ** 18)
    return 0.0

if __name__ == "__main__":
    print("🔍 Mencari wallet Ethereum yang memiliki saldo...")

    while True:
        priv, addr = generate_wallet()
        balance = get_eth_balance(addr)
        if balance > 0:
            print(f"\n🎉 DITEMUKAN!")
            print(f"🔑 Private Key: {priv}")
            print(f"📮 Address    : {addr}")
            print(f"💰 Balance    : {balance:.18f} ETH")
            break
        else:
            print(f"❌ Empty: {addr} | Balance: {balance:.6f} ETH")
        time.sleep(1)  # hindari limit Etherscan
