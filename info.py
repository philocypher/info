#! /usr/bin/env python3

import sys
import socket
import requests
import intro
import signal 
import whois


def signal_handler(sig, frame):
    print('\nExiting...')
    sys.exit(0)

def domain_info(dom):
    w = whois.whois(dom)
    try:
        for name, val in w.items():
            if type(val) == list:
                 for item in val:
                     print(f"{name}---> {len(val) - len(val) + 1}{item}")
            else:
             print(f"{name} --> {val}")
    except Exception as e:
        print(e)


def get_ip_info(ip_or_domain):
    try:
        # Get the IP address from the domain name
        ip_address = socket.gethostbyname(ip_or_domain)
        print(f"IP Address of {ip_or_domain}: {ip_address}")

        # Use an external API to get more information about the IP address
        response = requests.get(f'https://ipapi.co/{ip_address}/json/')
        if response.status_code == 200:
            ip_info = response.json()
            return ip_info
        else:
            print(f"Unable to retrieve information for {ip_address}.")
            return None

    except socket.gaierror:
        print(f"Error: Unable to resolve {ip_or_domain}. Please check the domain name.")
        return None

def dns_info(ip):
    pass



if __name__ == "__main__":
    intro.spinner_animation(3)
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        leave = ''
        user_input = input("Enter an IP address or domain name: ")
        # info = get_ip_info(user_input)
        domain_info(user_input)
       # if info:
       #     print("IP Information:")
       #     for key, value in info.items():
       #         print(f"{key}: {value}")
        leave = input("Do u want to contiue? [enter for yes] ")
        if leave != '':
            print("Bye!")
            sys.exit(0)
