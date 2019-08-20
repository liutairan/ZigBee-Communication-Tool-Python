import struct

class FrameType:
    frameTypeDict = {}
    frameTypeDict['ATCommand'] = 0x08
    frameTypeDict['ATCommandQueueRegisterValue'] = 0x09
    frameTypeDict['TransmitRequest'] = 0x10
    frameTypeDict['ExplicitAddressingCommandFrame'] = 0x11

class ATCommandFrame:
    def __init__(self):
        pass

class ATCommandQueueRegisterValue:
    def __init__(self):
        pass
