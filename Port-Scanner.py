import socket, sys, ipaddress

# While statement to acquire target IP while also preventing the user from entering a invalid IP address.
while True:
    ipAddr = input("\nEnter the target IP address: ")
    
    try:
        ip_address_obj = ipaddress.ip_address(ipAddr)
        break
    except:
        print("Invalid IP address entered, please re-enter a valid IP address.")

# While statement to acquire minimum port number and also prevent the user from entering an invalid port number
while True:
    portMin = int(input("\nPlease enter the minimum port number: "))
    
    if portMin < 0 or portMin > 65535:
        print("Invalid port number entered.")
    else:
        break

# While statement to acquire maximum port number and also prevent the user from entering an invalid port number
while True:
    portMax = int(input("\nPlease enter maximum port number: "))
    
    if portMax < 0 or portMax > 65535:
        print("Invalid port number entered.")
    elif portMax < portMin:
        print("\nPlease enter a maximum port number greater than or equal to the minimum port number.")
        print(f"The minimum port number is: {portMin}")
    else:
        break

print("""
\n______               _        _____                                        
| ___ \             | |      /  ___|                                       
| |_/ /  ___   _ __ | |_     \ `--.   ___   __ _  _ __   _ __    ___  _ __ 
|  __/  / _ \ | '__|| __|     `--. \ / __| / _` || '_ \ | '_ \  / _ \| '__|
| |    | (_) || |   | |_     /\__/ /| (__ | (_| || | | || | | ||  __/| |   
\_|     \___/ |_|    \__|    \____/  \___| \__,_||_| |_||_| |_| \___||_|   """)
print()
print("Target IP Address: "+ipAddr)
print(f"Port range: {portMin}-{portMax}")

try:
    # For loop to scan the port number range of the target IP
    for port in range(portMin, portMax+1):
        
        # Creating a socket object as S
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)

           
            result = s.connect_ex((ipAddr, port))
            # if statement to see if the port is open or not as s.connect_ex will return 0 if the connection is succesful
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is not open")
            s.close()
        

# Exit exception if there is a socket error
except socket.error:
    print("\nHost is non-responsive")
    sys.exit()

# Exit exception if the user inputs CRL+C
except KeyboardInterrupt:
    print("\nExiting")
    sys.exit()
