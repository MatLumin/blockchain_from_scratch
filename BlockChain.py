#builtin libs 
from typing import *;
import time;

#third party libs
import requests

#local libs 
from Block import Block;
from GenesisBlock import GenesisBlock;
from Transaction import Transaction;
from Node4AddressBook import Node4AddressBook;
from shared import *;


class BlockChain:
	def __init__(self):
		self.transactions:List[Transaction] = [];
		self.nodes:List[Node4AddressBook] = []; 
		self.chain:List[Transaction] = [];
		self.chain.append(
			GenesisBlock()
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
		if self.is_node_addrs_registred_already() == True:
			return -1;
		self.nodes.append(Node4AddressBook(addrs));
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
