import jwt
from flask import Flask, request, Response, jsonify


class JWTManager:
    def __init__(self,algorithm):
        self.algorithm=algorithm
        with open("private.pem", "rb") as f:
            self.private_key = f.read()
        with open("public.pem", "rb") as f:
            self.public_key = f.read()

    def encode(self, data):
        try:
            encoded = jwt.encode(data,self.private_key, algorithm=self.algorithm)
            return encoded
        except:
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None


