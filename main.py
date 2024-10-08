from __future__ import annotations;
"""
SOME RULES:
	1.USE BYTE DIGEST FOR LOCAL STORAGE 
	AND HEX DIGEST FOR EXTERNAL TRANSFER
	OF HASHES

"""
#buildins
import hashlib;
from binascii import unhexlify;
from typing import *
import time;

#third party
#flask
from flask import Flask, request, redirect
import requests
#crypto
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
#jinja2
import jinja2

#local libs
from Block import Block;
from GenesisBlock import GenesisBlock;
from Transaction import Transaction;
from Node4AddressBook import Node4AddressBook;
from BlockChain import BlockChain;
from shared import *;







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
	

