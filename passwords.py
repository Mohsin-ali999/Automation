import base64

def encoded_password(value):
    string = value.encode('utf-8')
    encoded_bytes = base64.b64encode(string)
    return encoded_bytes

def decoded_password(encoded_bytes):
    string = encoded_bytes.decode('utf-8')
    decoded_password = base64.b64decode(string)
    return decoded_password

def instances(values):
    if isinstance(values,bytes):
        values = values.decode('utf-8')
    elif isinstance(values,int):
        values = str(values)
    return values

user_name = 'admin'
password = 'Admin@78666'

# def encode_password(password):
#     password_bytes = password.encode('utf-8')  # Convert string to bytes
#     encoded_bytes = base64.b64encode(password_bytes)  # Encode the bytes
#     encoded_password = encoded_bytes.decode('utf-8')  # Convert bytes back to string
#     return encoded_password

# def decode_password(encoded_password):
#     encoded_bytes = encoded_password.encode('utf-8')  # Convert string to bytes
#     decoded_bytes = base64.b64decode(encoded_bytes)  # Decode the bytes
#     decoded_password = decoded_bytes.decode('utf-8')  # Convert bytes back to string
#     return decoded_password
