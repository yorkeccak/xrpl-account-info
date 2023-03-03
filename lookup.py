from xrpl.models.requests.account_info import AccountInfo
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.core import addresscodec

# Define the network client
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet
test_wallet = generate_faucet_wallet(client, debug=True)
print(f"Created wallet with address: {test_wallet.classic_address}")

# Derive an x-address from the classic address (starts with T for testnet)
print(
    f"With X-address: {addresscodec.classic_address_to_xaddress(test_wallet.classic_address, tag=12345, is_test_network=True)}"
)

# Look up information about your account
acct_info = AccountInfo(
    account=test_wallet.classic_address,
    ledger_index="validated",
    strict=True,
)

# Request account information
print("Requesting account info...")
response = client.request(acct_info)
result = response.result
print(f"Response status: {response.status}\n")

# Print account address and balance
print(f"Wallet address: {result['account_data']['Account']}")
print(f"Wallet balance: {result['account_data']['Balance']}")
