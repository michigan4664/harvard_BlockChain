import random
import ecdsa
import hashlib
import codecs

#1
#create private key of Alice
alice = ''.join(['%x' % random.randrange(16) for x in range(16)]).encode('utf-8')
#try_ele

#2
#encode the private key of Alice
private_key_alice = codecs.encode(alice, 'hex_codec')
len(private_key_alice)

#3
#apply the ecdsa to the private key of Alice
sk_alice = ecdsa.SigningKey.from_string(private_key_alice, curve = ecdsa.SECP256k1)

#4
#the signing key of Alice
sk_alice

#5
#create the public key of Alice
vk_alice = sk_alice.verifying_key

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
#Charlie verifys the message was signed by Alice
assert vk_alice.verify(signature_alice, orig_message)

#10
#create private key of Charlie
charlie = ''.join(['%x' % random.randrange(16) for x in range(16)]).encode('utf-8')
#try_ele

#12
#encode the private key of Charlie
private_key_charlie = codecs.encode(charlie, 'hex_codec')
len(private_key_charlie)

#13
#apply the ecdsa to the private key of Charlie
sk_charlie = ecdsa.SigningKey.from_string(private_key_charlie, curve = ecdsa.SECP256k1)

#14
#the signing key of Charlie
sk_charlie

#15
#create the public key of Charlie
vk_charlie = sk_charlie.verifying_key

#16
#create the message
message_str_new = 'Second message'

#17
#encode the message
new_message = message_str_new.encode('utf-8')

#18
#sign the message with Charlie's private key
signature_charlie = sk_charlie.sign(new_message)

#19
#Bob verifys the message was signed by Charlie
assert vk_charlie.verify(signature_charlie, new_message)