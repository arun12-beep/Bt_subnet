##define the synapse
import bittensor as bt
class AddSynapse(bt.Synapse):
    #input : vali send this
    dummy_input:float=0.0

    #output: miner fills this
    dummy_output:float=0.0

def miner_forward(synapse:AddSynapse)->AddSynapse:
    synapse.dummy_output=synapse.dummy_input*2
    print(f"[miner] received input:{synapse.dummy_input}")
    print(f"[miner] sending output:{synapse.dummy_output}")
    return synapse

#create an axon(miner's server) on port8091
wallet=bt.Wallet(name="miner", hotkey="miner123")
axon=bt.Axon(wallet=wallet,port=8091)

#tell the axon: when AddSynapse arrives, call miner_forward
axon.attach(forward_fn=miner_forward)

#start listening
axon.start()
print("[miner] Axon is running on port 8091....")

import time           #keep miner alive
while True:
    time.sleep(1)    ##wait for axon to fully start
  


