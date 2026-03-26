import bittensor as bt
sub=bt.Subtensor(network="test")
metagraph=sub.metagraph(netuid=1)
my_hotkey=bt.Wallet(name="miner",hotkey="miner123").hotkey.ss58_address
for uid in range(len(metagraph.uids)):
  if metagraph.hotkeys[uid]==my_hotkey:
    axon=metagraph.axons[uid]
    print("found your miner")
    print(f"UID: {uid}")
    print(f"Axons: {axon.ip}:{axon.port}")
    print(f"Stake: {metagraph.S[uid].item():.4f}")
