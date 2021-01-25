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
    print("Challenge string", challenge)
    print("Random generated string", answer)
    attempt = challenge + answer
    print("Attempt", attempt)

    return attempt, answer

#gen()

hash = hashlib.sha256()

def testAttempt():
    found = False
    start = time.time()
    while(found == False):
        attempt, answer = gen()
        hash.update(attempt.encode())
        solution = hash.hexdigest()
        print("Solution", solution)
        if(solution.startswith("00000")):
            timeTook = time.time() - start
            print("Time", timeTook)
            found = True

testAttempt()
