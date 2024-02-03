def dev():
    ''' Welcome to the Log Enteries!
        1. Add Log Entries
        2. Display Log Entries 
        3. Search for Log Entries By IP
        4. Calculate Total Bytes Transferred
        5. Filter Log Entries By Protocol
        6. Exit
    '''

def addLogEnteries(sourceIP, destinationIP, protocol, bytesTransfer):
    networkTraffic.append((sourceIP, destinationIP, protocol, bytesTransfer))
    print("Log entry added successfully")

def displayLogEnteries():
    if len(networkTraffic) == 0:
        print("Log Entries is empty!!")
    else:
        print("Network Devices: ")
        for item in networkTraffic:
            print(f"SourceIP: {item[0]} , DestianationIP: {item[1]} ,Protocol : {item[2]} , Enter Bytes Transferred: {item[3]}")

def bytesTransfer():
    total_bytes = 0
    for item in networkTraffic:
        total_bytes = total_bytes + item[3]
    # return total_bytes
    print("Total Bytes Transferred: ", total_bytes)

def searchLogEntries(IP):
    searched_entries = list(filter(lambda x: (x[1] == IP or x[0]==IP), networkTraffic))

    if not list(searched_entries):
        print(f"No log entries found for IP: {IP}")
    else:
        print(f"Log Entries for IP {IP}: ")
        for item in searched_entries:
            print(f"- SourceIP: {item[0]}, DestianationIP: {item[1]}, Protocol: {item[2]}, Bytes Transferred: {item[3]}")

def filterLogEntries(protocol):
    filtered_entries = list(filter(lambda x: x[2] == protocol , networkTraffic))

    if not list(filtered_entries):
        print(f"No log entries found for protocol: {protocol}")
    else:
        print(f"Filtered Log Entries for Protocol {protocol}: ")
        for item in filtered_entries:
            print(f"SourceIP: {item[0]}, DestianationIP: {item[1]}, Protocol: {item[2]}, Bytes Transferred: {item[3]}")

    
def doTask(choice):
    if choice == '1':
        sourceIP = input("Enter source IP: ")
        destinationIP = input("Enter destination IP: ")
        protocol = input("Enter protocol: ")
        bytesTransfered = int(input("Enter bytes transferred: "))
        addLogEnteries(sourceIP, destinationIP, protocol, bytesTransfered)
    elif choice == '2':
        displayLogEnteries()
    elif choice == '3':
        IP = input("Enter the IP address to search: ")
        searchLogEntries(IP)
    elif choice == '4':
        bytesTransfer()
    elif choice == '5':
        protocol = input("Enter the protocol to filter: ")
        filterLogEntries(protocol)
    else:
        exit()
    

if __name__ == "__main__":
    global networkTraffic
    networkTraffic = []

    print(dev.__doc__)
    while True:
        choice = input("Enter your Choice (1-6): ")
        doTask(choice)

