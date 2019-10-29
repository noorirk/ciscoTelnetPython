import datetime
import os
import subprocess
import telnetlib
import time

username = "cisco"
unamepw = "xgm!!66"
ip = "192.168.16.6"

tn = telnetlib.Telnet(ip)
time.sleep(2)
response = tn.read_until(b"User Name:", 5)
print(response)

if b"User Name:" in response:
	print("found")
	tn.write(username.encode('ascii') + b"\n")
	output = tn.read_until(b":", 5)
	print(output)
	tn.write(unamepw.encode('ascii') + b"\n")
	output = tn.read_until(b"#", 5)
	print(output)
	
else:
	print("not found")
	tn.write(telnetpw.encode('ascii') + b"\n")
	tn.read_until(b">", 5)

tn.write(b"show vlan" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"configure terminal" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"vlan 333" + b"\n")
output = tn.read_until(b"#", 5)
print(output)


tn.write(b"end" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.write(b"show vlan" + b"\n")
output = tn.read_until(b"#", 5)
print(output)

tn.close()


                    