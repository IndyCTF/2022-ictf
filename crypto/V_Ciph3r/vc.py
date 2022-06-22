import base64
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))

def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

if _name_ == "_main_":
	string = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	keyword = base64.b64encode(b"XXXXXX")
	key = generateKey(string, str(keyword))
	cipher_text = cipherText(string,key)
	print("Ciphertext :", cipher_text)
# Ciphertext : CIXYSXNXARPOEICXMKHCJSF
# he told the pincode to be EASY64
# wrap the flag with ictf{XXXXXX}
