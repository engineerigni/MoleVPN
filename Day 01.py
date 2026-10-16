#code 1 warm up logic for obfuscating ports
import socket
def reverse_number(n):
    reversed_num = 0
    while n != 0:
         digit = n % 10
         reversed_num = reversed_num * 10 + digit
         n = n // 10
      return reversed_num 
num = 8080
print(f"orignal: {num} -> Reversed: {reversed_number(num)}")

# code2 to get my IP Address_get system IP
hostname = socket.gethostname()
my_ip = socket.gethostbyname(hostname)
print(f"My Hostname: {hostname}")
print(f"My Local IP: {my_ip}")

#code 3 simple socket connection_Basic client server socket
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.blind(('127.0.0.1', 8080))
    server.listen(1)
    print("server listening on 127.0.0.1:8080...")
start_server()

#code 4: simple XOR encryption for data
def encrypt_data(data, key = 122):
      encrypted = ''.join([chr(ord(c)^ key) for c in data])
      return encrypted
msg = "MoleVPN"
enc = encrypt_data(msg)
dec = encrypt_data(enc)# XOR twice = decrypt
print(f"orignal: {msg} -> Encrypted: {enc} -> Decrypted: {dec}")

#code5 create vpn configuration
config ={
    "Vpn_name": "MoleVPN",
    "version": "0.1.0",
    "server_ip": "127.0.0.1",
    "port": reversed_num(8080),
    "protocol": "TCP"
    }
print(congig)
#save it
impot jason
with open('molevpn_config.json', 'w') as f:
    json.dump(config, f, indent=4)
print("config saved!")



