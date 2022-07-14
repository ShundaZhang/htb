#!/usr/bin/env python3

import socketserver as sock
import time
import threading
import random
import sys

def build_banner():
    banner = ""
    banner += "__/\\____/\\____/\\____/\\____/\\____/\\____/\\____/\\__\n"
    banner += "\\    /\\    /\\    /\\    /\\    /\\    /\\    /\\    /\n"
    banner += "/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\\n"
    banner += "  \\/    \\/    \\/    \\/    \\/    \\/    \\/    \\/  \n"
    banner += "   __       _   _       ____   ___ ____   ___   \n"
    banner += "  / /  ___ | |_| |_ ___|___ \\ / _ \\___ \\ / _ \\  \n"
    banner += " / /  / _ \\| __| __/ _ \\ __) | | | |__) | | | | \n"
    banner += "/ /__| (_) | |_| || (_) / __/| |_| / __/| |_| | \n"
    banner += "\\____/\\___/ \\__|\\__\\___/_____|\\___/_____|\\___/  \n"
    banner += "                                                \n"
    banner += "__/\\____/\\____/\\____/\\____/\\____/\\____/\\____/\\__\n"
    banner += "\\    /\\    /\\    /\\    /\\    /\\    /\\    /\\    /\n"
    banner += "/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\/_  _\\\n"
    banner += "  \\/    \\/    \\/    \\/    \\/    \\/    \\/    \\/  \n"
    banner += "------------------------------------------------"
    
    print(banner)
    return banner
    

def build_game_board():
    gboard = ""
    gboard += "    ".join(str(x) for x in range(1, 11)) + "\n"
    gboard += "   ".join(str(x) for x in range(11, 21)) + "\n"
    gboard += "   ".join(str(x) for x in range(21, 31)) + "\n"
    gboard += "   ".join(str(x) for x in range(31, 41)) + "\n"
    gboard += "   ".join(str(x) for x in range(41, 51)) + "\n"
    gboard += "   ".join(str(x) for x in range(51, 61)) + "\n"
    gboard += "   ".join(str(x) for x in range(61, 71)) + "\n"
    gboard += "   ".join(str(x) for x in range(71, 81)) + "\n"
    gboard += "   ".join(str(x) for x in range(81, 91)) + "\n"
    gboard += "------------------------------------------------"
    
    print(gboard)
    return gboard
    

def edit_game_board(number):
    if number < 0 or number > 90:
        return
    
    r = 10 - int((number-1) / 10)
    c = int((number-1) % 10)
    
    str_mod = ""
    
    for i in range(r):
        print('\033[A', end="")
        str_mod += '\033[A'
    for i in range(c):
        print('\033[C\033[C\033[C\033[C\033[C', end="")
        str_mod += '\033[C\033[C\033[C\033[C\033[C'
        
    print('\033[32m\033[1m'+str(number)+'\033[0m', end="")
    str_mod += '\033[32m\033[1m'+str(number)+'\033[0m'
    
    for i in range(r):
        print('\033[B', end="")
        str_mod += '\033[B'
    print('\r', end="")
    str_mod += '\r'
    
    return str_mod
    

def build_summary(extracted):
    print("\033[31m[+]\033[0m EXTRACTION: ", end="")
    summary = "\033[31m[+]\033[0m EXTRACTION: "
    for i in extracted:
        print(str(i) + " ", end="")
        summary += str(i) + " "
    print('\r', end="")
    summary += '\r'
    
    return summary
    

class Service(sock.BaseRequestHandler):
    allow_reuse_address = True
    
    # Connection handler
    def handle(self):
        print("[+] Incoming connection")
        
        seed = int(time.time())
        print("[+] Seed:", seed)
        
        banner = build_banner()
        gboard = build_game_board()
        self.send(banner)
        self.send(gboard)
        
        extracted = []
        next_five = []

        # Initialize the (pseudo)random number generator
        random.seed(seed)
        
        # First extraction
        while len(extracted) < 5:
            r = random.randint(1, 90)
            if(r not in extracted):
                extracted.append(r)
                time.sleep(1)
                gboard = edit_game_board(r)
                self.send(gboard, False)
                summary = build_summary(extracted)
                self.send(summary, False)
                
        # Next extraction
        solution = ""
        while len(next_five) < 5:
            r = random.randint(1, 90)
            if(r not in next_five):
                next_five.append(r)
                solution += str(r) + " "
        solution = solution.strip()
        print("\n[+] SOLUTION: " + solution)
        
        question = "\n\033[33m[?]\033[0m Guess the next extraction!!!"
        self.send(question)
        response = self.receive()
        
        # CHECK
        print("[>] Sent:", summary[25:])
        print("[<] Recv:", response)
        
        if str(response) == solution:
            self.send("Good Job!\nHTB{f4k3_fl4g_f0r_t3st1ng}")
        else:
            self.send("Nope! Try again.")

    # Function to send the challenge to clients
    def send(self, string, newline=True):
        if newline: string = string + "\n"
        self.request.sendall(string.encode())

    # Function to receive responses from clients
    def receive(self, prompt="\033[33m[?]\033[0m Put here the next 5 numbers: "):
        self.send(prompt, newline=False)
        return self.request.recv(4096).strip().decode('ASCII')
        
    
class ThreadService(sock.ThreadingMixIn, sock.TCPServer, sock.DatagramRequestHandler):
    pass
    

def main():
    host = '0.0.0.0'
    port = 1337
    
    s = Service
    server = ThreadService((host, port), s)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    print ("[ Server started on port: ", str(port), "]")

    while(True): time.sleep(1)


if (__name__=="__main__"): 
    main()

