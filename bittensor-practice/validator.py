import bittensor as bt
class AddSynapse(bt.Synapse):
    dummy_input:float=0.0
    dummy_output:float=0.0

def score_response(input_val:float,output_val:float)->float:
    expected=input_val*2
    if output_val==expected:
        return 1.0    
    elif output_val==0.0:
        return 0.0
    else:
        diff=abs(output_val-expected)
        return max(0.0,1.0-diff/expected)
            



wallet=bt.Wallet(name="validator",hotkey="validator123")
dendrite=bt.Dendrite(wallet=wallet)
synapse=AddSynapse(dummy_input=5.0)
print(f"[validator] sending input: {synapse.dummy_input}")

response=dendrite.query(
    axons=bt.AxonInfo(
        version=1,
        ip='62.72.43.192',
        port=8091,
        ip_type=4,
        hotkey="5HVzmN7xkdoPFTfDhE3sySTEsiXxB2Ej3ELXniskTXr79JG2",
        coldkey="5GmePLDxxu7TjrWcHwcYfGgVb8fE2pMCAy4h7sW8dkb9ZRTp"
    ),
    synapse=synapse,
    timeout=5
    )
print(f"[validator] got back output:{response.dummy_output}")

##score miner
score=score_response(synapse.dummy_input,response.dummy_output)
print(f"[validator] miner score:{score}")
