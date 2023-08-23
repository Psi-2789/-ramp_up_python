import re
import os
import subprocess

# Function to validate IP address using regular expression
def is_valid_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip)

# Function to check if an IP is pinging
def is_pinging(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

# Main program
pinning_ips = []
non_pinning_ips = []

while True:
    ip = input("Enter an IP address (or 'exit' to stop): ")

    if ip.lower() == "exit":
        break

    if not is_valid_ip(ip):
        print("Invalid IP address format. Please enter a valid IP.")
        continue

    if is_pinging(ip):
        pinning_ips.append(ip)
    else:
        non_pinning_ips.append(ip)

    choice = input("Do you want to continue? (Yes/No): ")
    if choice.lower() != "yes":
        break

# Write pinning and non-pinning IPs to files
with open("pinning_ips.txt", "w") as pinning_file:
    for ip in pinning_ips:
        pinning_file.write(ip + "\n")

with open("non_pinning_ips.txt", "w") as non_pinning_file:
    for ip in non_pinning_ips:
        non_pinning_file.write(ip + "\n")

print("Pinning IPs:")
print(pinning_ips)
print("Non-pinning IPs:")
print(non_pinning_ips)
