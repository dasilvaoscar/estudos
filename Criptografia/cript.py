import jwt

encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS512")
decode_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS512"])

print(encoded_jwt)