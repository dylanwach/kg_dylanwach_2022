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

# array holding arrays of duplicate chars indexes that need to be mapped to same thing.
duplicate_indexes = []
s1_copy = s1
for i in range(0, len(s1_copy)):
    char = s1_copy[i]
    # search for instances other than initial and store them in
    duplicates = []
    # copy is false until copy found, then becomes true, indicating that the duplicates indexes should be documented
    copy = False
    duplicates.append(i)
    for j in range(i+1, len(s1_copy)):
        # find where the char is found in copied string, and it hasn't already been removed (documented)
        if s1_copy[j] == char and s1.find(char) != -1:
            duplicates.append(j)
            copy = True
    if copy:
        duplicate_indexes.append(duplicates)
    s1 = s1.replace(char, '')

print(duplicate_indexes)
