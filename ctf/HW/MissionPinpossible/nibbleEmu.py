def _sendChar(value):
    return [_sendNibble((value >> 4 & 0x0f), 1), _sendNibble((value & 0x0f), 1)]

def _sendNibble(halfByte, isData):
    return _write2Wire(halfByte, isData, 1)
    # disable is omitted because we're filtering it

def _write2Wire(halfByte, isData, enabled):
    i2cData = halfByte << 4
    # PCF_RS
    if isData:
      i2cData |= 0x01
    # PCF_EN
    if enabled:
      i2cData |= 0x04
    # PCF_BACKLIGHT
    i2cData |= 0x08
    return i2cData

# Some tests
i2cChars = []
for c in "test":
    i2cChars.append(_sendChar(ord(c)))

string = ""
for high, low in i2cChars:
    string += chr(high & 0xf0 | (low >> 4))

assert string == "test"
