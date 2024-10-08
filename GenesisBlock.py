
#local libs
from Block import Block;

class GenesisBlock(Block):
	def __init__(self):
		Block.__init__(self);
		self.has_nonce = True;
		self.block_number = 0;
		self.timestamp = 0;
		self.data = b"GENESIS";
		self.nonce = 0;
		self.prev_hash = "0";