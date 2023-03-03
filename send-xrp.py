from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import safe_sign_and_autofill_transaction
from xrpl.transaction import send_reliable_submission

# Define the network client
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet
test_wallet = generate_faucet_wallet(client, debug=True)
print(test_wallet.classic_address)

# Prepare payment
my_tx_payment = Payment(
    account=test_wallet.classic_address,
    amount=xrp_to_drops(22),
    destination="rsMPCD2AZUs7FafNDeTAqbszsFvauVSm59",
)

# Sign the transaction
my_tx_payment_signed = safe_sign_and_autofill_transaction(
    my_tx_payment, test_wallet, client
)

# Submit and send the transaction
tx_response = send_reliable_submission(my_tx_payment_signed, client)

if tx_response.is_successful():
    print("Transaction successful")
else:
    print("Transaction unsuccessful")
