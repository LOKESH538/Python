"""  Substring Check (Bug Funny)
     Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise.
     First two lines of input:
     1010110010          10110
     1110111011           10011
     First two lines of output:
     1
   0"""

A=input("Enter string A : ")
B=input("Enter string B : ")
if B in A:
    print("1")
else:
    print("0")
