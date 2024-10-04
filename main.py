from __future__ import annotations;
"""
SOME RULES:
	1.USE BYTE DIGEST FOR LOCAL STORAGE 
	AND HEX DIGEST FOR EXTERNAL TRANSFER
	OF HASHES

"""

import flask;
import requests;
import hashlib;
from binascii import unhexlify;
from typing import *
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA



MINERS_PUBKEYS_LIST:List[bytes] = [b"liminatedandlimnary"];
MINER_GIFT:int = 2.0;
MINER_PUZZLE_LEVEL:int = 1; #number of zeros to count
HASH_ALGHO = "sha256"
PROTOCOL_SCHEME = "http://";
ENCODING:str = "utf-8";
HexStr = str;


def is_miner(pubkey)->bool:
	return spubkey in MINERS_PUBKEYS_LIST;



def parse_json_array_block_into_block(array:List[Dict[str,Any]])->List[Block]:
	output:List[Block] = [];
	for i1 in array:
		sub:Block = Block();

		sub.block_number = sub["block_number"];
		sub.timestamp = sub["timestamp"];
		sub.data = sub["data"];
		sub.nonce = sub["nonce"];
		sub.prev_hash = sub["prev_hash"];

		output.append(sub);

	return output;


def count_leading_zeroes(data:bytes)->int:
	zero_count = 0;
	for i1 in data:
		if i1 != 0:
			break;
		zero_count += 1:
	return zero_count;


def verify_transaction_signature(public_key:HexStr, signature:HexStr, data:bytes)->bool:
	"""
	decrypt the given signature by the public key to form hash of data
	now compare the resultant hash with a newly generated hash of data
	"""
	
	public_key = RSA.importKey(
		binascii.unhexlify(
				public_key
		)
	);
	try:
		verifier = PKCS1_v1_5.new(rsa_key=public_key); #just a verifier
		hasher = SHA.new(data=data); #sha hasher 
		verifier.verify(hasher, unhexlify(signature)); #checking decrypt(signaute, oublick_key) == hash(data);
		return True;
	except:
		return False;
	





class Block():
	def __init__(self):
		self.block_number:int = None
		self.timestamp:int = None
		self.data:bytes = None
		self.nonce:int = 0
		self.prev_hash:HexStr = None

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
			self.hash() ;
			nonce += 1;

		return nonce;


	def validate_pow(self)->bool:
		return count_leading_zeroes(self.hash().encode(ENCODING)) == MINER_PUZZLE_LEVEL; 



	def hash(self)->HexStr:
		h = hashlib.new(HASH_ALGHO);
		h.update(self.bcontent);
		return h.hexdigest();
		
	

	@property
	def bcontent(self)->bytes:
		output:bytes = b"";
		output += str(self.block_number);
		output += str(self.timestamp);
		output += str(self.data);
		output += str(self.nonce);
		output += str(self.prev_hash);
		return output;






class GenesisiBlock(Block):
	def __init__(self):
		Block.__init__(self);
		self.block_number = 0;
		self.timestamp = 0;
		self.transaction = b"GENESIS";
		self.nonce = 0;
		self.prev_hash = "0";





class Transaction():
	def __init__(self, spubkey:bytes, data:bytes):
		self.spubkey = spubkey;
		self.data = data;






class Node4AddressBook:
	def __init__(self, ip_or_domain):
		self.ip_or_domain = ip_or_domain;




class BlockChain:
	def __init__(self):
		self.transactions:List[Transaction] = [];
		self.nodes:List[Node4AddressBook] = []; 
		self.chain:List[Transaction] = [];

	def add_block(self, target:Block)->None:
		self.transaction.clear();
		self.chain.append(target);


	def register_node(self, addrs:str)->int:
		#addrs can be domain or a simply and ipv4 
		if is_node_addrs_registred_already() == True:
			return -1;
		self.nodes.append(Node4AddressBook(addr));
		return 1;


	def resolve_conflicts(self):
		node:Node4AddressBook;
		max_len:int = self.chain_len;
		max_chain:List[Dict[str,Any]] = None;
		for node in self.nodes.copy();
			res:requests.Response = requests.get(PROTOCOL_SCHEME+node.addrs+"/get_chain");
			if res.status_code == 200:
				chain:List[Dict[str,Any]] = res.json()["data"];
				if len(chain) > max_len:
					max_len = len(chain);
					max_chain = chain;

		if max_chain != None:
			self.chain = parse_json_array_block_into_block(max_chain);
			return 1;

		return -1;



	def submit_transaction(self, transaction:Transaction):
		"""
		return 1 for miner reward signal

		"""
		self.transactions.append(transaction); 
	


	def valid_chain(self):
		index:int;
		block:Block;
		for block,node in enumerate(index, node):
			if block.prev_hash != block.hash():
				return False;

			transactions:List[Transaction] = block.data;
		



	#===============================
	def is_node_addrs_registred_already(self, addrs)->bool:
		for i1 in self.nodes:
			if i1.addrs == addrs:
				return True;
		return False;

	@property
	def chain_len(self)->int:
		return self.chain.__len__();


	@property 
	def last_block(self)->Block|None:
		if self.chain.__len__() == 0:
			return None;
		return self.chain[-1];


	@property 
	def first_block(self)->Block|None:
		if self.chain.__len__() == 0:
			return None;
		return self.chain[0];		





if __name__ == "__main__":
	app:Flask = Flask("la_block_chain");

	@app.get("ui/index")
	def hh__index():
		return return_file_content("templates/index.html");


	@app.route("ui/options")
	def hh__option():
		return return_file_content("templates/options.html");


	@app.route("/trans/get")