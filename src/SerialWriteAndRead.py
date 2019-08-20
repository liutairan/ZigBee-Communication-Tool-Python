import serial
import struct
import hashlib



def constructPacket():
    total_data = [0x7E, 0x00, 0x04, 0x08, 0x01, 0x49, 0x44]
    byteStr = struct.pack('<4B', *total_data[3:len(total_data)])
    checksum = 0xFF - (sum(total_data[3:]) & 0xFF)
    # for i in "".join( chr(x) for x in byteStr):
    #     checksum = checksum ^ ord(i)
    total_data.append(checksum)
    # print(total_data)
    packet = struct.pack('<8B', *total_data)
    return packet

def parsePacket(packet):
    data = []
    for byte in packet:
        data.append(hex(byte))
    print(data)

def main():
    packet = constructPacket()
    with serial.Serial('/dev/tty.SLAB_USBtoUART', 115200, timeout=1) as ser:
        ser.write(packet)
        allReadData = ser.readline()
        parsePacket(allReadData)

if __name__ == "__main__":
    main()
