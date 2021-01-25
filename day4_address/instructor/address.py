# Name: JJ

# pip install base58 ...

import hashlib, base58, binascii, codecs, ecdsa

# step 1: generate private key
privateKey = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
print("Private Key: ", privateKey.to_string().hex())

## step 2: generate a public key
publicKey = "04" + privateKey.get_verifying_key().to_string().hex()
print("\nPublic Key: ", publicKey)

# step 3: get hash
hash = hashlib.sha256(binascii.unhexlify(publicKey)).hexdigest()
print("\nSHA256(Public Key): ", hash)

# step 4: apply RIDEMP160
rip = hashlib.new('ripemd160', binascii.unhexlify(hash))
print("\nripemd160(SHA256(Public Key)): ", rip.hexdigest())

# step 5: prepend 00 as network byte, add version byte
prepend = '00' + rip.hexdigest()

# step 6: Apply double hash to generate checksum
hash1 = prepend
for i in range(1,3):
    hash1 = hashlib.sha256(binascii.unhexlify(hash1)).hexdigest()
    print("\n\t SHA256 # ", i, " : ", hash1)

# step 7: get checksum
checksum = hash1[:8]
print("\nChecksum (first 4 bytes): ", checksum)

# step 8: apppend checksum to the output of ripemd160(SHA256(Public Key))
appendChecksum = prepend + checksum
print("\nripemd160(SHA256(Public Key)) with appended checksum: " + appendChecksum)

# step 8: generate address
address = base58.b58encode(binascii.unhexlify(appendChecksum))
print("\nBitcoin address: ", address.decode('utf8'))
