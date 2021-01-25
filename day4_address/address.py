# pip install bitcoin

# Name:William Haden

import haslib, base58, binascii, codesc, ecdsa

#step 1:generate private key
privatekey = ecdsa.SigningKey.gnerate(curve=ecdsa.SECP256k1)
print(privatekey.to_string().hex())

##step 2:generate a public key
publicKey = "04" + privateKey.get_verifying_key().to string().hex()
print(prvateKEY)

#step 3: get hash
hash = hashlib.sha256(binascii.unhexlify(publicKey)).hexdigest

##step 4: apply  RIDEMP160
rip = hashlib.new('ripemed160' , binascii.unhexlify(hash))
print(rip)

##step 5: prepend 00 as network byte
prepend = '00' + rip

##step 6:Apply double dash
hash1 = prepend
for i in range(1.3):
    hash1 = hashlib.sha256(binascii.unhexlify(hash1)).hexdigest()

##step 7: get checksum
checksum = hash1[:8]

appendChecksum = prepend + checksum
