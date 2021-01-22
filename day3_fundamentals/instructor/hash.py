# Name: JJ

import hashlib

with open("input.txt", "r") as file:
    input = file.read()

output = hashlib.sha256(input.encode()).hexdigest()

print(input)
print(output)
