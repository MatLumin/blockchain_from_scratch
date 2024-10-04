from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import hashlib



data = b"lumnated and lumin";

h = hashlib.new("sha256");
h.update(data);

print(h.hexdigest());



