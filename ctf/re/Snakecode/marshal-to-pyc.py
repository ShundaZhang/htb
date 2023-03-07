from __future__ import print_function

import marshal
import struct
import sys
import time
#import uncompyle6

def _pack_uint32(val):
    """ Convert integer to 32-bit little-endian bytes """
    return struct.pack("<I", val)

def code_to_bytecode(code, mtime=0, source_size=0):
    """
    Serialise the passed code object (PyCodeObject*) to bytecode as a .pyc file

    The args mtime and source_size are inconsequential metadata in the .pyc file.
    """

    # Get the magic number for the running Python version
    if sys.version_info >= (3,4):
        from importlib.util import MAGIC_NUMBER
    else:
        import imp
        MAGIC_NUMBER = imp.get_magic()

    # Add the magic number that indicates the version of Python the bytecode is for
    #
    # The .pyc may not decompile if this four-byte value is wrong. Either hardcode the
    # value for the target version (eg. b'\x33\x0D\x0D\x0A' instead of MAGIC_NUMBER)
    # or see trymagicnum.py to step through different values to find a valid one.
    data = bytearray(MAGIC_NUMBER)

    # Handle extra 32-bit field in header from Python 3.7 onwards
    # See: https://www.python.org/dev/peps/pep-0552
    if sys.version_info >= (3,7):
        # Blank bit field value to indicate traditional pyc header
        data.extend(_pack_uint32(0))

    data.extend(_pack_uint32(int(mtime)))

    # Handle extra 32-bit field for source size from Python 3.2 onwards
    # See: https://www.python.org/dev/peps/pep-3147/
    if sys.version_info >= (3,2):
        data.extend(_pack_uint32(source_size))

    data.extend(marshal.dumps(code))

    return data

if len(sys.argv) < 2:
    print("Usage %s <marshal-dump-file>" % sys.argv[0])
    sys.exit(1)

path = sys.argv[1]
pycFile = path + ".pyc"
pythonFile = path + ".py"

# Open raw code that was saved using marshal.dump()
#
# It isn't strictly necessary to unmarshal this to write back as a .pyc file,
# but this validates that the marshalled code content is valid (an exception
# is thrown otherwise)
with open(path, 'rb') as handle:
    code = marshal.load(handle)
    pyc = code_to_bytecode(code, time.time())

    with open(pycFile, 'wb') as out:
        out.write(pyc)

# Use uncompyle6 to decompile the bytecode and write it to disk alongside the .pyc
#with open(pythonFile, 'w') as decompiled:
#    uncompyle6.main.decompile_file(pycFile, decompiled)
