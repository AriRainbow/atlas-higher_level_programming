#!/usr/bin/python3
print("".join(
   "{}".format (chr(ascii_val)) 
    for ascii_val in range(97, 123)
    if chr(ascii_val) not in ('e', 'q')))
