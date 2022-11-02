#Small calculator for assisting in the subnet pre-lab for CS4121, Fall2022
#Written by Garrett Moore, Nov 2 2022

import math

def getBitSize(n):
    p = 0
    while (math.pow(2,p)<(n+3)):
        p += 1
    return p

def allocateAddresses(firstAddressSpace, hostRequestList):
    hostRequestList.sort(reverse = True)
    numSubnets = len(hostRequestList)
    printInitialize(firstAddressSpace, numSubnets)
    nextAddressSpace = firstAddressSpace
    for x in range(numSubnets):
        print("\nLAN " + str(x) + ":")
        numHosts = hostRequestList[x]
        bitSize = getBitSize(numHosts)
        subnetRange = int(math.pow(2,bitSize))
        nextAddressSpace += subnetRange
        printSubnet(numHosts, bitSize, subnetRange, nextAddressSpace)
    
def printInitialize(firstAddressSpace, numSubnets):
    print("firstAddressSpace= " + str(firstAddressSpace))
    print("numSubnets = " + str(numSubnets))
    
def printSubnet(numHosts, bitSize, subnetRange, nextAddressSpace):
    network = nextAddressSpace - subnetRange
    gateway = network +1
    broadcast = nextAddressSpace -1 
    msg = "   Hosts =  " + str(numHosts)
    msg += "\n   bitSize =  " + str(bitSize)
    msg += "\n   Network Address   =\t10.10.172." + str(network) 
    msg += "\n   Gateway Address   =\t10.10.172." + str(gateway) 
    msg += "\n   Broadcast Address =  10.10.172." + str(broadcast)
    print(msg)
    
def initialize():
    firstAddressSpace = input("Enter first address space as integer: ")
    addMore = True
    hostRequestList = []
    hostRequestList.append(int(input("Enter requested host size: ")))
    addMore = input("Add additional LAN? (y/n): ")
    while (addMore.capitalize() == 'Y'):
        hostRequestList.append(int(input("Enter another requested host size: ")))
        addMore = input("Add additional LAN? (y/n): ")
    allocateAddresses(int(firstAddressSpace),hostRequestList)
    
###############################

initialize()

        
    