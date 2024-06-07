#!/usr/bin/python3

import os, time, random, uuid, sys

def clear_screen():
    os.system("clear")

def get_logo(device_mac):
    return """
 ██████   █████  ███    ███ ███████ ██     ██  █████  ██    ██ ███████ 
██       ██   ██ ████  ████ ██      ██     ██ ██   ██ ██    ██ ██      
██   ███ ███████ ██ ████ ██ █████   ██  █  ██ ███████ ██    ██ █████   
██    ██ ██   ██ ██  ██  ██ ██      ██ ███ ██ ██   ██  ██  ██  ██      
 ██████  ██   ██ ██      ██ ███████  ███ ███  ██   ██   ████   ███████ 
                                                                       
======================================================================

Version: Advanced
Firmware: 2.3.5
CPU: NexCore X1 - 16.78 MHz
Mac Address: """ + device_mac + """
Game Library Synced: OK
Preferences Loaded: OK\n"""

def get_professor():
    return """
       .-\"\"\"\"-.
      /  \     \\
      |  .'--. |
      | /_   _`|
      \( a \ a )
       |    > |
       |\  =  /
       | \___/|
   ___/:      :\__
  /`  < `\   /` >  `\\
 /     `\ |__| /`    \\
 ;   [MD] \|  |/ |I!   ;
 |         |  | |\"\"\"|  |
 |   |     \  / \___/  |
"""

def get_house():
    return """    ) )        /\\
   =====      /  \\
  _|___|_____/ __ \____________
 |::::::::::/ |  | \:::::::::::|
 |:::::::::/  ====  \::::::::::|
 |::::::::/__________\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\,,,, ,, ,)
','',,,,' /__________\,,,',',;;
"""

def get_poketmon(poketmon):
    if poketmon == "Bulbasaurus":
        return """@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+:,:*:@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,,:...S..S*,,@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@,::****...***.......++...+S:@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@:*...***................*.+SS*@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@:++...*.....++..............S+S:@@@@@@\n@@@@@@@,****::,,,,,,,*.+........SS+.***...........S+S+,@@@@@\n@@@@@@:.***.++*******...+..+...***.S..........*..+SS+S.@@@@@\n@@@@@:+.****::::***...+************++...........+++S++++,@@@\n@@@@@++**:::**.+++SSSS+***********..S.......++++++++S++++,@@\n@@@@*.***:::.SSSSSS+.*************..+S+++++++++++++++S++++,@\n@@@*.*****++**+++..***************....S++++++++++++++S+++S.@\n@@*.*++*...+**********.**..S.S+**....S+SS++++++++++++SS+++S:\n@:S:*S+..*****.S.+***+**.:.S++.+*.++.++.+SS++++++++++++++++.\n,+.,S.*.*****+SS..*****+,@SS*@..S....+S.SS..SS++++++++++++++\n*+:,S.********.++*****.:@,S..,+SS.....+++.SSS.SSSSSS++++++S*\n..*:SS+***************+,@@+SS++SS..+++++.+.SSSSS.SS++++++SS,\n.++.******************..::*++++++++++++...+SSSSS.++SS+++SS:@\n,.+S+++..****.**********....++++++++++++++++++++++++S.S+*,@@\n@@,*.+SS.S++++++++++++++SSSSS++...+S+.........+......S+@@@@@\n@@@@@,:+SSSS+++......++SSS++..++++.*******.+.++.....+.+*@@@@\n@@@@@@@*..++++SS+++++++++++++SSS.**..****..SS..+SSS.++++,@@@\n@@@@@@@*.*..+++++SSSSSSSSS+S++S.**+SS.***....+S+SS.+++.+*@@@\n@@@@@@@,+++++S...++++++++++++S+.+S..+***..++*.SSS..+++.S*@@@\n@@@@@@@@*S++SS......+S..SSSSS.+++S*****..+.....+SSS+++.S:@@@\n@@@@@@@@@.+.+......++,@@:+SS.S+SS.****..+SS++++++..+++++@@@@\n@@@@@@@@@@++...+..+.,@@@@@..S+++.***..++:@,.+++++.+++++,@@@@\n@@@@@@@@@@*+*++.+*:@@@@@@@@:+......+++*,@@@@..+++++++*,@@@@@\n@@@@@@@@@@@,@@,,@@@@@@@@@@@:::.*...*:,@@@@@@@@@,,,,,,@@@@@@@"""
    elif poketmon == "Charedmander":
        return """@@@@@@@@@@@,:::**..***::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@,*************.+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@,*.::::**********.+.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@,.*:::************..+.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@..*.***********.*..%++*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@S.**************+*@%?++,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@:%*.*************+%+??.+.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@:%?.*************.%%%...+,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@*S..**************S+SS+.+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@,.******************...+.+*@@@@@@@@@@@@@@@@@@@@@@,,@@@@@\n@@@@:++.*********.****.+++S+.+,@@@@@@@@@@@@@@@@@@@@@@:+*,@@@\n@@@@@*.+++S+....+++++++SSS..+:@@@@@@@@@@@@@@@@@@@@@:,.++:@@@\n@@@@@@,*.++SSSS++..***.S+..+*@@@@@@@@@@@@@@@@@@@@,:**..+*@@@\n@@@@@@@@@,:*.+S+.....++....+,,@@@@@@@@@@@@@@@@@@@,*:*....,@@\n@@@@@@@@@@,,:.++.++++.......****:,,@@@@@@@@@@@@@@,.*...**.*,\n@@@@,,,:**.***....***.++..***********::,:*,@@@@@@:....+.,:*,\n,:.*...*******+*,,,,,,:*.**************..+**,@@,::*:*..:,**:\n:..**********+.,,,,,,,,,:..***********.+.++:@@@:*:::**:,*.*:\n@@:.*........+,,,,,,,,,,,,*..........+++*:,,@@@,:*:::,,:.+*@\n@@@:::,::::,**,,,,,,,,,,,,,*.*.++*::,,,@@@@@@@@@@,*:,::.++,@\n@@@@@@@@@@@@*:,,,,,,,,,,,,,,.****.*@@@@@@@@@@@@@@@@,:..::,@@\n@@@@@@@@@@@@*,,,,,,,,,,,,,,,:.*****.,@@@@@@@@@@@@@@,.*.@@@@@\n@@@@@@@@@@@@*,,,,,,,,,,,,,,,,*******.:@@@@@@@@@@@@,+.*.@@@@@\n@@@@@@@@@,:*.*,,,,,,,,,,,,::,*.******.*@@@@@@@@@,*++.S:@@@@@\n@@@@@@@@:****.*,,,,,,:::::::**:::*****.*,,,,:*.++++++*@@@@@@\n@@@@@@@**:::**+*:::::::::::*.:::*******SS+++++++++++:@@@@@@@\n@@@@@@:.::***..+.*::::::::::+:********...+++++++++*,@@@@@@@@\n@@@@@@*.*........++.***:::::..*****.....SS+++++.*,@@@@@@@@@@\n@@@@@@,++........+.....*:::**+++........S+..*::,@@@@@@@@@@@@\n@@@@@,*.++......+S,@@@@@@@@@@@,*+.......+*,@@@@@@@@@@@@@@@@@\n@@@:*..*+.++...**:@@@@@@@@@@@@@@:+...+..++*,@@@@@@@@@@@@@@@@\n@@@,:.:.*::,,@@@@@@@@@@@@@@@@@@@@*+++.++.++.,@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,:*:*+::*,@@@@@@@@@@@@@@@@"""
    elif poketmon == "Squirturtle":
        return """@@@@@@@@@@@@@@@@@,:::****..**::,@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@,:**:::********...*,@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@:..*::******....**...*,@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@,++**********.+,:S......:@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@,+S.*********.??++?S.....+,@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@:%S**********.###%S+.+++++.@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@,.S.**********S.%S+.++++++++,@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@..***.*********.....++++++++,@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@*S+..++++++++++...+++++++++*@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@*+++++++++++++++++++++++++@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@,*...++++++++++++++++++.+:@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@,,*+S+++++++++++++++SS..S+.,@@@@@@@@@@@@@@@@@@@@\n@@@@@@@,::*........+++++++++SS..+++S.S++:@@@@@@@@@@@@@@@@@@@\n@@@@,:*.*****..::::*****...+.::**..++.SSS*@@@@@@@@@@@@@@@@@@\n,***..******..*::::::*****+.::****.+.SS++S:@@@@@@@@@@@@@@@@@\n@*+++.*****..:,,:::*..***+.*******...SS++.+,@@@@@@@@@@@@@@@@\n:.++++....*S*:,,,,,:**::*+*.+.**....+.++..+:@@@@@@@@@@@@@@@@\n:*****...*.S.:::::::.*::...+++..++.+.:++...*@@@@@@@@@@@@@@@@\n@@@@@@@@@@,***::::::.::+++++++++++S.*:S++.+*@@@@@@@@@@@@@@@@\n@@@@@@@@@@,*:+******.::****.+++..*+*:*S+++.*@@@@,,:::::,@@@@\n@@@@@@@@@@@..*:::***+*******.*****+.**S++SS,@,:*.........*,@\n@@@@@@@@@,*++::::::*.:::::::*.+....+.*SSSS.@:..******..+++.,\n@@@@@@@@,.*:..::::::.:::::**....*****.SS++,*+.....+++++++++.\n@@@@@@@@.*::*.+.****+*******+.********..S*+++++++S++++++++++\n@@@@@@@:.::***.++.........*+.**********SS+++++++S++++++++++*\n@@@@@@@*.***...++++........S.**********+S.++++++S+++++++++.,\n@@@@@@,*+...++++++*,,:::**.++.********.+S+++++++++S++++++*@@\n@@@@@,.+...++++++.@@@@@@@@@@,+........+++*...+++++++++.:,@@@\n@@@@@@,.*.++..*:,@@@@@@@@@@@@:++++++++++*@@@@,,,,,,,@@@@@@@@\n@@@@@@@@@,:,@@@@@@@@@@@@@@@@@@+.+++.++++.,@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::*.+*::*,@@@@@@@@@@@@@@@@@@"""

def print_ascii_box(content, text, min_width=60, min_height=10):
    max_content_width = max(len(line) for line in content.split("\n"))
    max_text_width = len(text)
    box_width = max(max_content_width, max_text_width, min_width) + 4

    content_lines = content.split("\n")
    content_height = len(content_lines)
    total_height = max(content_height + 4, min_height)
    empty_lines_needed = total_height - content_height - 4

    def print_line(char, length):
        print(char * length)

    def print_centered(line, width):
        print(f"*{line.center(width - 2)}*")

    print_line("*", box_width)

    print(f"*{" " * (box_width - 2)}*")
    for line in content_lines:
        print_centered(line, box_width)
    for _ in range(empty_lines_needed):
        print(f"*{" " * (box_width - 2)}*")

    print_line("*", box_width)

    print(f"*{" " * (box_width - 2)}*")
    print_centered(text, box_width)
    print(f"*{" " * (box_width - 2)}*")
    print_line("*", box_width)
    sys.stdout.flush()
    time.sleep(2)

def dialog(text):
    print(text)
    sys.stdout.flush()
    time.sleep(2)

def get_mac():
    mac = [random.randint(0x00, 0xff) for _ in range(6)]
    return ":".join("{:02x}".format(x) for x in mac)

def lcg(seed, a=1664525, c=1013904223, m=2**32):
    return (a * seed + c) % m

def generate_ids(seed):
    random.seed(seed)
    tid = random.randint(0, 65535)
    sid = random.randint(0, 65535)
    return tid, sid

def generate_poketmon(seed, tid, sid, name):
    random.seed(seed)
    stats = {
        "HP": random.randint(20, 31),
        "Attack": random.randint(20, 31),
        "Defense": random.randint(20, 31),
        "Speed": random.randint(20, 31),
        "Special Attack": random.randint(20, 31),
        "Special Defense": random.randint(20, 31)
    }
    natures = ["Adamant", "Bashful", "Bold", "Brave", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
    nature = random.choice(natures)
    pid = random.randint(0, 2**32 - 1)
    shiny_value = ((tid ^ sid) ^ (pid & 0xFFFF) ^ (pid >> 16))
    is_shiny = shiny_value < 8

    return {
        "name": name,
        "stats": stats,
        "nature": nature,
        "is_shiny": is_shiny
    }

def main():
    device_mac = get_mac()
    clear_screen()
    dialog(get_logo(device_mac))

    boot_time = time.time()
    system_time = time.time()
    dialog(f"[!] Booting up - Poketmon Emerald Version")

    battery_died = True

    if battery_died:
        dialog(f"[!] The device's battery has died, time reset to system defaults")
        system_time = 0

    clear_screen()
    print_ascii_box(get_professor(), "...")
    clear_screen()
    print_ascii_box(get_professor(), "Hello there! Welcome to the world of Poketmon!")
    clear_screen()
    print_ascii_box(get_professor(), "My name is Josheph! People call me the Poketmon Prof!")
    clear_screen()
    print_ascii_box(get_professor(), "This world is inhabited by creatures called Poketmon!")
    clear_screen()
    print_ascii_box(get_professor(), "For some people, Poketmon are pets. Others use them for fights.")
    clear_screen()
    print_ascii_box(get_professor(), "Myself, I study Poketmon as a profession.")
    clear_screen()
    print_ascii_box(get_professor(), "First, what is your name?")
    
    while True:
        print("")
        player_name = input("Enter your name: ").strip()
        if player_name:
            break
        
        clear_screen()        
        print_ascii_box(get_professor(), "Name cannot be empty. Please enter your name.")

    time_passed = time.time() - boot_time
    dialog_time = system_time + time_passed
    formatted_time = int(dialog_time)

    initial_seed = int(formatted_time + int(device_mac.replace(":", ""), 16))
    seed = lcg(initial_seed)
    tid, sid = generate_ids(seed)

    clear_screen()
    print_ascii_box(get_professor(), f"Right! So your name is {player_name}!")
    clear_screen()
    print_ascii_box(get_professor(), "Your very own Poketmon legend is about to unfold!") 
    clear_screen()
    print_ascii_box(get_professor(), "A world of dreams and adventures with Poketmon awaits! Let's go!")
    clear_screen()
    print_ascii_box(get_professor(), "But first, you need to choose your first Poketmon. Come to my lab!")
    clear_screen()
    print_ascii_box(get_house(), "You arrive at Professor Joshephs's lab.")

    starter_names = ["Bulbasaurus", "Charedmander", "Squirturtle"]
    starter_poketmons = [generate_poketmon(seed + i, tid, sid, starter_names[i]) for i in range(3)]

    print("")
    for i, Poketmon in enumerate(starter_poketmons):
        print(f"{i + 1}. {Poketmon['name']}")

    dialog("\nYou can choose one of these three Poketmon.\n")

    while True:
        try:
            choice = int(input("Choose your starter Poketmon (1, 2, or 3): ")) - 1
            chosen_poketmon = starter_poketmons[choice]
            
            if choice in range(3):
                break
            else:
                clear_screen()
                print_ascii_box(get_house(), "Invalid choice. Please choose 1, 2, or 3.")
        except Exception:
            clear_screen()
            print_ascii_box(get_house(), "Invalid input. Please enter a number (1, 2, or 3).")

    clear_screen()
    print_ascii_box(get_poketmon(chosen_poketmon["name"]), f"Congratulations! You chose {chosen_poketmon['name']}!")
    clear_screen()
    print_ascii_box(get_poketmon(chosen_poketmon["name"]), "Take good care of your Poketmon")
    clear_screen()
    print_ascii_box(get_poketmon(chosen_poketmon["name"]), "And embark on your journey to become the Poketmon Champion!")

    print(f"\nYour Poketmon: {chosen_poketmon['name']}")
    print(f"Nature: {chosen_poketmon['nature']}")
    print(f"Stats: {chosen_poketmon['stats']}")
    print(f"Shiny: {'Yes' if chosen_poketmon['is_shiny'] else 'No'}")

    if chosen_poketmon["is_shiny"]:
        clear_screen()
        print_ascii_box(get_poketmon(chosen_poketmon["name"]), "Congratulations! You have obtained a shiny Poketmon!")
        clear_screen()
        print_ascii_box(get_poketmon(chosen_poketmon["name"]), "This is a very rare and special Poketmon")
        clear_screen()
        print_ascii_box("HTB{f4k3_fl4g_f0r_t35t1ng}", "Take this as a gift for this rare find")

    print("\nGood luck on your adventure!")

if __name__ == "__main__":
    main()
