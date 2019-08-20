'''This is an example of using python to send data to a XBee and let it send the
data packet to another XBee module.'''

import serial
import struct

def Checksum(dataList):
    checksum = 0xFF - (sum(dataList) & 0xFF)
    return checksum

def constructPacket():
    header = 0x7E
    length = 0x0014
    frameType = 0x11
    frameID = 0x01
    longAddressHigh = 0x0013A200
    longAddressLow = 0x40C14304
    shortAddress = 0xFFFE
    sourceEndpoint = 0xE8
    destinationEndpoint = 0xE8
    clusterID = 0x0011
    profileID = 0xC105
    broadcastRadius = 0x00
    options = 0x00
    configureData = [frameType, frameID, longAddressHigh, longAddressLow,
                     shortAddress, sourceEndpoint,destinationEndpoint, clusterID,
                     profileID, broadcastRadius, options]
    dataPayload = ['H', 'e', 'l', 'l', 'o', '5'] #
    dataPayloadHex = [ord(x) for x in dataPayload]
    length = length + len(dataPayload)
    checksumDataPre = configureData + dataPayloadHex
    checksumDataStr = struct.pack('>BBIIHBBHHBB%dB' % len(dataPayload), *checksumDataPre)
    checksumData = list(struct.unpack('>%dB' % length, checksumDataStr))
    # print(checksumData)
    checksum = Checksum(checksumData)
    # print(checksum)
    allData = [header, length] + checksumDataPre + [checksum]
    byteStr = struct.pack('>BHBBIIHBBHHBB%dBB' % len(dataPayload), *allData)
    packet = byteStr
    return packet

def parsePacket(packet):
    data = []
    for byte in packet:
        data.append(hex(byte))
    print(data)

def main():
    packet = constructPacket()
    # print(packet)
    # with serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1) as ser:
    with serial.Serial('/dev/tty.usbserial-AL00FMGX', 115200, timeout=1) as ser:
        ser.write(packet)
        allReadData = ser.readline()
        parsePacket(allReadData)

if __name__ == "__main__":
    main()
