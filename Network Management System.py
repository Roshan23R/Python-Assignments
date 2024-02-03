def shop():
    ''' Welcome to the Online Shopping Cart!
        1. Add Devices
        2. Display Devices
        3. Search for a Device
        4. Filter Devices by Type
        5. Remove Device
        6. Exit
    '''

def addDevice(name, deviceType, Ip):
    network.append([name, deviceType, Ip])
    print("Device Added Successfully")

def displayDevices():
    if len(network) == 0:
        print("network is empty!!")
    else:
        print("Network Devices: ")
        for item in network:
            print(f"Name: {item[0]}, Type: {item[1]}, IP Address: {item[2]}")

def removeDevice(name):
    for item in network:
        if item[0]==name:
            network.remove(item)
    print("Device removed from the network")

def searchDevice(name):
    found = -1
    for item in network:
        if item[0] == name:
            found = 1
            print("Device Found: ",)
            print(f"Name: {item[0]}, Type: {item[1]}, IP Address: {item[2]}")
            break
    if found == -1: 
        print("Device not Found!!")

def filterDevices(deviceType):
    print("Filtered Devices: ")
    for item in network:
        if item[1] == deviceType:
            print(f"- {item[0]}")

    
def doTask(choice):
    if choice == '1':
        name = input("Enter device name: ")
        deviceType = input("Enter device type: ")
        Ip = input("Enter IP address: ")
        addDevice(name, deviceType, Ip)
    elif choice == '2':
        displayDevices()
    elif choice == '5':
        name = input("Enter device name to remove: ")
        removeDevice(name)
    elif choice == '4':
        deviceType = input("Enter device type to filter: ")
        filterDevices(deviceType)
    elif choice == '3':
        name = input("Enter device name to search: ")
        searchDevice(name)
    else:
        exit()
    

def main():
    global network
    network = []

    print(shop.__doc__)
    while True:
        choice = input("Enter your Choice (1-6): ")
        doTask(choice)

main()
