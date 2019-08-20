import serial
import struct
import hashlib

def Checksum(dataList):
    checksum = 0xFF - (sum(dataList) & 0xFF)
    return checksum

def constructPacket():
    header = 0x7E
    length = 0x000E
    frameType = 0x10
    frameID = 0x01
    longAddressHigh = 0x0013A200
    longAddressLow = 0x40C14304
    shortAddress = 0xFFFE
    broadcastRadius = 0x00
    options = 0x00
    configureData = [frameType, frameID, longAddressHigh, longAddressLow,
                     shortAddress, broadcastRadius, options]
    dataPayload = ['H', 'e', 'l', 'l', 'o', '6'] #
    dataPayloadHex = [ord(x) for x in dataPayload]
    length = length + len(dataPayload)
    checksumDataPre = configureData + dataPayloadHex
    checksumDataStr = struct.pack('>BBIIHBB%dB' % len(dataPayload), *checksumDataPre)
    checksumData = list(struct.unpack('>%dB' % length, checksumDataStr))
    # print(checksumData)
    checksum = Checksum(checksumData)
    # print(checksum)
    allData = [header, length] + checksumDataPre + [checksum]
    byteStr = struct.pack('>BHBBIIHBB%dBB' % len(dataPayload), *allData)
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
