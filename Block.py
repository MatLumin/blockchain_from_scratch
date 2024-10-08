#built in libs
from typing import *;
import hashlib
#local libs
from shared import *;


class Block():
	def __init__(self):
		self.block_number:int = None
		self.timestamp:int = None
		self.data:bytes = None
		self.nonce:int = 0
		self.prev_hash:HexStr = None
		self.has_nonce = False;

	def to_dict(self)->Dict[str, Any]:
		output:Dict[str, Any] = dict();
		output["block_number"] = self.block_number;
		output["time_stamp"]  = self.time_stamp;
		output["transaction"] = self.transaction;
		output["nonce"] = self.nonce;
		output["prev_hash"] = self.prev_hash;
		return output;


	def proof_of_work(self)->int:
		#generating nonce for block
		nonce:int = 0;
		while True:
			self.nonce = nonce;
			if self.validate_pow():
				break
			nonce += 1;

		return nonce;


	def validate_pow(self)->bool:
		output:int =  count_leading_zeroes(self.hash().encode(ENCODING)); 
		print("zero count", output);
		return output == MINER_PUZZLE_LEVEL;



	def hash(self)->HexStr:
		print(self.block_number, self.data);
		h = hashlib.new(HASH_ALGHO);
		h.update(self.bcontent);
		return h.hexdigest();
		
	

	@property
	def bcontent(self)->bytes:
		output:bytes = b"";
		output += str(self.block_number).encode(ENCODING);
		output += str(self.timestamp).encode(ENCODING);
		output += self.data;
		output += str(self.nonce).encode(ENCODING);
		output += str(self.prev_hash).encode(ENCODING);
		return output;

