from SYS_FUNCTIONS import *
from INTRINSICS import *
#### Script name:UTIL_UUID

import random

def uuid4():
    """Generate a random UUID."""

    result = ''

    # eb6305c9-1f7f-49de-aed0-16487c27b42d

    for i in range(16):
        if i in (4,6,8,10):
           result += '-'
        result += '%02x' % random.randrange(256)

    y = '%1x' % (random.randrange(4) + 8)

    result = result[0:14] + '4' + result[15:19] + y + result[20:]
    return result

def main():
    for i in range(300):
        print(uuid4())
