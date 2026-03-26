
import bittensor as bt
sub=bt.Subtensor(network="test")
metagraph=sub.metagraph(netuid=1)
print("uids:", metagraph.uids[:20])
print('my miner(178) stake:',metagraph.S[178]) 
print("my validator(178) stake:", metagraph.S[181])
