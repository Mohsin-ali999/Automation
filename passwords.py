import base64

#Function to encode the given values
def encoded_password(value):
    string = value.encode('utf-8')
    encoded_bytes = base64.b64encode(string)
    return encoded_bytes

#Function to decode the output of the encoded values
def decoded_password(encoded_bytes):
    string = encoded_bytes.decode('utf-8')
    decoded_password = base64.b64decode(string)
    return decoded_password

#Conversion of the values
def instances(values):
    if isinstance(values,bytes):
        values = values.decode('utf-8')
    elif isinstance(values,int):
        values = str(values)
    return values


user_name = ''
password = ''


