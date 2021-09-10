import functions

code_symbol, offset = functions.get_offset()

message = "Fletcher Hall is really hot right now"
print(f"Original message: {message}")
print("-" * 30)
encrypted_message = functions.encrypt(message.lower(), code_symbol, offset)
print(f"Encrypted: {encrypted_message}")
print("-" * 30)
decrypted_message = functions.decrypt(encrypted_message)
print(f"Decrypted: {decrypted_message}")
