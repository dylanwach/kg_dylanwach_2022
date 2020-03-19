import sys

# check if 3 arguments (file name, then s1, s2)
# if not, exit

if len(sys.argv) != 3:
    print("Not enough arguments")
    quit()

s1 = sys.argv[1]
s2 = sys.argv[2]

# if 2 characters in init_str are the same, they must be mapped to the same.
# otherwise, the mapping can be anything (as long as same size)

if len(s1) != len(s2):
    print("false")
    quit()

