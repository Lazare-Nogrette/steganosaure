import string
string.printable = string.printable.replace("\r", "à")

def cesar_ciffer(message, key):
	if type(key) != int :
		print("la clef doit être un entier")
		return None

	message = str(message)

	list_of_crypted_caracs = []
	
	for carac in message:
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_carac = string.printable[crypted_index]
	
		list_of_crypted_caracs.append(crypted_carac)
	
	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message

def cesar_decrypt(crypted_message, key):
	return cesar_ciffer(crypted_message, -key)




def vigenere(message, password, ciffer):
	if ciffer:
		list_of_keys = [string.printable.index(password_carac) for password_carac in password]
	else:
		list_of_keys = [- string.printable.index(password_carac) for password_carac in password]
	
	list_of_crypted_caracs = []

	for index_carac, carac in enumerate(message):
		current_key = list_of_keys[index_carac % len(list_of_keys)]
		list_of_crypted_caracs.append(cesar_ciffer(carac, current_key))

	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message


# crypted_message = cesar_ciffer("j'ai envie de manger gratin de pates avec des lardons", 104)
# print(crypted_message)

# # print(crypted_message)
# # print(cesar_decrypt(crypted_message, 762))


# # print("Je suis un hacker")
# # print("#"*30)
# # for possible_key in range(0, len(string.printable)):
# # 	print(cesar_decrypt(crypted_message, possible_key))
# # print("#"*30)


print(vigenere(message="hakim", password="abc", ciffer=True))
print(vigenere(message="rlwsx", password="abc", ciffer=False))
