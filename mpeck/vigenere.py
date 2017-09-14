from itertools import cycle

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encode(plaintext, key):
	
	ciphertext = ""
	
	plaintext = plaintext.strip().upper()
	key_cycle = cycle(key.strip().upper())
	
	for plain_char in plaintext:
				
		if plain_char in ALPHABET:			
			
			key_char = next(key_cycle)
			
			location_plain_char = ALPHABET.find(plain_char)
			
			location_key_char = ALPHABET.find(key_char)						
			
			
			
			cipher_char_location = (location_plain_char + location_key_char) % len(ALPHABET)
						
			cipher_char = ALPHABET[cipher_char_location]
			
			ciphertext += cipher_char
				
		else:
			ciphertext += plain_char
		
	return ciphertext


def decode(ciphertext, key):
	
	plaintext = ""
	
	ciphertext = ciphertext.strip().upper()
	key_cycle = cycle(key.strip().upper())
	
	for cipher_char in ciphertext:
				
		if cipher_char in ALPHABET:			
			
			key_char = next(key_cycle)
			
			location_cipher_char = ALPHABET.find(cipher_char)			
			location_key_char = ALPHABET.find(key_char)						
			
			
			
			plain_char_location = (location_cipher_char - location_key_char) % len(ALPHABET)
						
			plain_char = ALPHABET[plain_char_location]
			
			plaintext += plain_char
				
		else:
			plaintext += cipher_char
		
	return plaintext


def encode_decode(text, key, encode = True):
	transformed_text = ""
	
	text = text.strip().upper()
	key_cycle = cycle(key.strip().upper())
	
	for char in text:
				
		if char in ALPHABET:			
			
			key_char = next(key_cycle)
			
			location_char = ALPHABET.find(char)			
			location_key_char = ALPHABET.find(key_char)						
						
			if encode:
				tranformed_char_location = (location_char + location_key_char) % len(ALPHABET)
			else:				
				tranformed_char_location = (location_char - location_key_char) % len(ALPHABET)
						
			transformed_char = ALPHABET[tranformed_char_location]
			
			transformed_text += transformed_char
				
		else:
			transformed_text += char
		
	return transformed_text

plain_text = raw_input("Enter text to encode: ")
key = raw_input("Enter key to use: ")	

encoded = encode(plain_text, key)
decoded = decode(encoded, key)

print 'encoded: ' + encoded
print 'decoded: ' + decoded

encoded = encode_decode(plain_text, key)
decoded = encode_decode(encoded, key, False)

print 'encoded: ' + encoded
print 'decoded: ' + decoded
