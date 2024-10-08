#built in libs 
from typing import *;
import binascii;

#third party libs
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA


#local libs 
from Block import Block;



MINERS_PUBKEYS_LIST:List[bytes] = [b"liminatedandlimnary"];
MINER_GIFT:int = 2.0;
MINER_PUZZLE_LEVEL:int = 2; #number of zeros to count
HASH_ALGHO = "sha256"
PROTOCOL_SCHEME = "http://";
ENCODING:str = "utf-8";
HexStr = str;


def is_miner(pubkey)->bool:
	return pubkey in MINERS_PUBKEYS_LIST;


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
		verifier.verify(hasher, binascii.unhexlify(signature)); #checking decrypt(signaute, oublick_key) == hash(data);
		return True;
	except:
		return False;
	

def return_file_content(path:str)->str:
	with open(path, mode="r", encoding="utf-8") as f1:
		return f1.read();