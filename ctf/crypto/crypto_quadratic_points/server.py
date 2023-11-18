from Crypto.Util.number import *
#from secret import FLAG
#from utils import *
import random
import sys, time, signal
FLAG = 'HTB{f4k3_f149_4_7357!!}'

def get_input_with_timeout(prompt, timeout):
    def alarm_handler(signum, frame):
        print("\nTime limit exceeded. Exiting...")
        sys.exit()

    #signal.signal(signal.SIGALRM, alarm_handler)
    #signal.alarm(timeout)

    try:
        input_data = input(prompt).strip()
        return int(input_data)
    except KeyboardInterrupt:
        pass
    finally:
        signal.alarm(0)  # Disable the alarm

    return None


for i in range(10):
    #x = find_valid_quadratic_coefficients()
    x = random.randint(0,2**32)
    print(f'Hello Cryptographer, please enter the coefficients of the quadratic equation to proceed, hint: a*x^2 + b*x + c == 0, x = {x}\n')
    ai = get_input_with_timeout("a: ", 2)
    bi = get_input_with_timeout("b: ", 2)
    ci = get_input_with_timeout("c: ", 2)
    res = ai*x**2 + bi*x + ci
    print(res)
    res *= 10**12 # did you think I would be that careless?
    print(res)
    if int(res) != 0 or all(c == 0 for c in [ai, bi, ci]):
    	print("Nope!")
    	exit()

print("You passed the first test, now onto the second\n")

p = getPrime(40)
E = EllipticCurve(p, [bi, ci])
G = E.random_point()
flag = bytes_to_long(FLAG)
Gn = E.mul(flag, G)

print(f"G = {G.xy()}")
print(f"Gn = {Gn.xy()}")
print(f"p = {E.p}")

