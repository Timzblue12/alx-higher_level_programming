#!/usr/bin/python3
# prints the ASCII alphabet, in lowercase, not followed by a new line.
for alpha_letters in range(97, 123):
    if alpha_letters == 101 or alpha_letters == 113:
        continue
    print("{}".format(chr(alpha_letters)), end="")
