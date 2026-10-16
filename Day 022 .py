import tkinter as tk
import socket, threading, time

def encrypt_data(data, key=122):
    return ''.join([chr(ord(c) ^ key) for c in data])

def decrypt_data(data, key=122):
    return ''.join([chr(ord(c) ^ key) for c in data])

def start_server(log_func):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)
    log_func("[SERVER] Listening on 127.0.0.1:5000")
    conn, addr = server.accept()
    data = conn.recv(1024).decode()
    log_func(f"[SERVER] Got encrypted: {data}")
    log_func(f"[SERVER] Decrypted: {decrypt_data(data)}")
    conn.sendall(b"ACK - TUNNEL OK")
    conn.close()
    server.close()
    log_func("[INFO] Tunnel established successfully")

# --- GUI LIKE THUNDER VPN ---
root = tk.Tk()
root.title("MoleVPN - MUST Project")
root.geometry("350x500")
root.configure(bg="#0f1117")

tk.Label(root, text="MoleVPN", font=("Arial", 22, "bold"), bg="#0f1117", fg="white").pack(pady=10)
status = tk.Label(root, text="● Disconnected", bg="#0f1117", fg="gray", font=("Arial", 11))
status.pack()

log_box = tk.Text(root, height=12, bg="#171923", fg="#4ade80", font=("Consolas", 9))
log_box.pack(padx=15, pady=15, fill="both")

def log(msg):
    log_box.insert(tk.END, msg+"\n")
    log_box.see(tk.END)

def connect():
    status.config(text="● Encrypted Tunnel Active", fg="#4ade80")
    log("[INFO] Initializing VPN tunnel...")
    btn.config(text="DISCONNECT", bg="#ef4444")
    threading.Thread(target=lambda: start_server(log), daemon=True).start()
    time.sleep(0.5)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    msg = encrypt_data("HELLO VPN")
    log("[CLIENT] Sending: HELLO VPN")
    client.sendall(msg.encode())
    reply = client.recv(1024).decode()
    log(f"[CLIENT] Reply: {reply}")
    client.close()

btn = tk.Button(root, text="CONNECT", command=connect, bg="#22c55e", fg="white",
                font=("Arial", 14, "bold"), height=2, width=20, bd=0)
btn.pack(pady=20)

root.mainloop()
