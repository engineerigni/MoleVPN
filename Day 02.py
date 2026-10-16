import socket
import threading
import time

def reverse_number(n):
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

def encrypt_data(data, key=122):
    return ''.join([chr(ord(c) ^ key) for c in data])

def decrypt_data(data, key=122):
    return ''.join([chr(ord(c) ^ key) for c in data])

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)
    print("[SERVER] Listening on 127.0.0.1:5000")
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    print(f"[SERVER] Got encrypted: {data}")
    print(f"[SERVER] Decrypted: {decrypt_data(data)}")
    conn.sendall(b"ACK - TUNNEL OK")
    conn.close()
    server.close()

def start_client():
    time.sleep(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    msg = encrypt_data("HELLO VPN")
    print(f"[CLIENT] Sending: HELLO VPN")
    client.sendall(msg.encode())
    reply = client.recv(1024).decode()
    print(f"[CLIENT] Server reply: {reply}")
    client.close()

t1 = threading.Thread(target=start_server)
t2 = threading.Thread(target=start_client)
t1.start()
t2.start()
t1.join()
t2.join()
print("Day 2 Done - Tunnel Working!")
