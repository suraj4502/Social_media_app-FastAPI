from urllib.parse import quote_plus

password = ""
encoded_password = quote_plus(password)
print(encoded_password)
# Use encoded_password in your database URL    