import random
import ecdsa
import hashlib
import codecs

#1
#create private key of Alice
alice = ''.join(['%x' % random.randrange(16) for x in range(16)]).encode('utf-8')
#try_ele

#1
#create private key of Bob
bob = ''.join(['%x' % random.randrange(16) for x in range(16)]).encode('utf-8')
#try_ele

#2
#encode the private key of Alice
private_key_alice = codecs.encode(alice, 'hex_codec')
len(private_key_alice)

#2
#encode the private key of Bob
private_key_bob = codecs.encode(bob, 'hex_codec')
len(private_key_alice)

#3
#apply the ecdsa to the private key of Alice
sk_alice = ecdsa.SigningKey.from_string(private_key_alice, curve = ecdsa.SECP256k1)

#3
#apply the ecdsa to the private key of Bob
sk_bob = ecdsa.SigningKey.from_string(private_key_bob, curve = ecdsa.SECP256k1)

#4
#the signing key of Alice
sk_alice

#4
#the signing key of Bob
sk_bob

#5
#create the public key of Alice
vk_alice = sk_alice.verifying_key

#5
#create the public key of Bob
vk_bob = sk_bob.verifying_key

#6
#create the message
message_str = 'Second message'

#7
#encode the message
orig_message = message_str.encode('utf-8')

#8
#sign the message with Alice's private key
signature_alice = sk_alice.sign(orig_message)

#9
#sign the message with Bob's private key
signature_bob = sk_bob.sign(orig_message)

#10
#Charlie verifies the process
assert vk_alice.verify(signature_alice, orig_message)
assert vk_bob.verify(signature_bob, orig_message)