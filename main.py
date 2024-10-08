from __future__ import annotations;
"""
SOME RULES:
	1.USE BYTE DIGEST FOR LOCAL STORAGE 
	AND HEX DIGEST FOR EXTERNAL TRANSFER
	OF HASHES

"""

from flask import Flask, request, redirect
import requests;
import hashlib;
from binascii import unhexlify;
from typing import *
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import jinja2
import time;



MINERS_PUBKEYS_LIST:List[bytes] = [b"liminatedandlimnary"];
MINER_GIFT:int = 2.0;
MINER_PUZZLE_LEVEL:int = 2; #number of zeros to count
HASH_ALGHO = "sha256"
PROTOCOL_SCHEME = "http://";
ENCODING:str = "utf-8";
HexStr = str;


def is_miner(pubkey)->bool:
	return spubkey in MINERS_PUBKEYS_LIST;


def fit_text(text:str, chars_per_line:int=85)->str:
	text = str(text);
	output = "";
	counter = 0;
	for i1 in text:
		counter += 1;
		if counter % chars_per_line == 0:
			output += "\n"
		output += i1;
	return output;



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
		zero_count += 1;
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


	






class GenesisiBlock(Block):
	def __init__(self):
		Block.__init__(self);
		self.has_nonce = True;
		self.block_number = 0;
		self.timestamp = 0;
		self.data = b"GENESIS";
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
		self.chain.append(
			GenesisiBlock()
		)

	def add_block(self, target:Block)->None:
		target.block_number = self.chain_len;
		target.timestamp = time.time_ns();
		target.prev_hash = self.last_block.hash();
		if target.has_nonce == False:
			target.nonce = 0;
			target.proof_of_work();
		#self.transaction.clear();
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
		for node in self.nodes.copy():
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



def return_file_content(path:str)->str:
	with open(path, mode="r", encoding="utf-8") as f1:
		return f1.read();





blockchain:BlockChain = BlockChain();
app:Flask = Flask("la_block_chain");

a = Block();
a.data = b"""
Commands: 
29c1b289e7522195b362e44f54e05470b69ad20540ab60a18a05e5bf6951f13d 
-------BEGIN PRIVATE KEY----- 
MIGEAgEAMBAGByqGSM49AgEGBSuBBAAKBG0wawIBAQQgVz5EV8fPg5fNpmkSeWHG 
cg+uf/HOs/3GvRmkKEYhPGqhRANCAAR5KCjELYoOiJ4SMWjbBSwySYiNvgf8erQE 
FsN8WsaDFEmTdOMFfRdt2P2zcoOLTv572+AhTCJQx8DazHc52s9e 
-----END PRIVATE KEY----- 
 
signed commands 
3045022100cafa9a4ddaf45ada09c57689d5cbb73f4074d7412e6e49840320b5b2aabf875602205d63a561075e45f5f18601ebafb7740bba954c6221dbb7c15868131dabb562e4
"""
a.has_nonce = True;
blockchain.add_block(a)

@app.route("/ui/")
def hh__option():
	return return_file_content("templates/ui_index.html");


@app.route("/ui/block_viewer")
def hh__block_viewer():
	template:jinja2.Template = jinja2.Template(
		return_file_content("templates/block_viewer.html")
	);
	output:str = template.render(chain=blockchain.chain, fit_text=fit_text);
	#chain will be a List[Block]
	return output;


@app.route("/ui/add_block")
def hh__add_block()->str:
	template:jinja2.Template = jinja2.Template(
		return_file_content("templates/add_block.html")
	);
	return template.render();


@app.route("/ui/mining_plz_wait")
def hh__ui_mining_plz_wait()->str:
	return jinja2.Template(
		return_file_content("templates/mining_plz_wait.html")
	).render();



#api things
@app.route("/api/add_block")
def hh__api_add_block()->str:
	given_data:str = request.args.get("data", "NO DATA")
	print("-------------------")
	print(request.args.keys())
	print("-------------------")
	block:Block = Block();
	block.data = given_data.encode("utf-8");
	blockchain.add_block(target=block);
	return redirect("/ui/mining_plz_wait");
	

