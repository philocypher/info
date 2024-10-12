import socket
import requests
import intro

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

if __name__ == "__main__":
    intro.spinner_animation(3)
    while True:
        leave = ''
        user_input = input("Enter an IP address or domain name: ")
        info = get_ip_info(user_input)
        if info:
            print("IP Information:")
            for key, value in info.items():
                print(f"{key}: {value}")
        leave = input("Do u want to contiue? [enter for yes] ")
        if leave != '':
            print("Bye!")
            break
