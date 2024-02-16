Simple port scanner tool that uses the socket module to check whether a port is open or not on a target IP address.

- The tool takes in an IP address and verifies that it is a valid IP address otherwise it will loop until a valid IP is entered or the user quits with CRL+C.
- Then takes in both a minimum and maximum port number verifiying both as valid.
- Then the tool finally procedes to scan the IP address's ports and return if the port is opened or closed.
