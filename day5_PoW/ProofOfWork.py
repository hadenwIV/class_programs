# Name:

import string
import random
import hashlib
import time

# create a random string - challenge string
challenge1 = "2Tsfx37pRaxkR85wlxmBeqll"

# method add something random to the end of the challenge string
def gen(challenge = challenge1, size = 25):
    answer = "".join(random.choice(string.ascii_lowercase +
                                    string.ascii_uppercase +
                                    string.digits) for x in range(size))
    # to complete

def testAttempt():
    # to complete

testAttempt()
