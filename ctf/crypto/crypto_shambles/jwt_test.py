import json, os, time, jwt, datetime
payload = {
    "username": "D-Cryp7",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(days = 1)
}
JWT_SECRET = os.urandom(32)
token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
pt = token[:16]

print(token)
print(pt)
