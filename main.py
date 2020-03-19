# Dylan Wachenfeld coding assignment for KARGO engineering
import sys

# check if 3 arguments (file name, then s1, s2)
# if not, exit

if len(sys.argv) != 3:
    # not correct number of arguments
    print("false")
    quit()

s1 = sys.argv[1]
s2 = sys.argv[2]

# check if s1 and s2 are same size
if len(s1) != len(s2):
    print("false")
    quit()

# if indexes in s1 are the same, they must be mapped to the same in s2.

# array holding arrays of duplicate char's indexes that need to be mapped to same thing.
duplicate_indexes = []
# use s1_copy to keep track of initial indexes
# s1 will be changed to ensure no repeat duplicates are documented
s1_copy = s1
for i in range(0, len(s1_copy)):
    char = s1_copy[i]
    duplicates = []
    # when a copy is found, copy becomes true, to make sure that index is documented in duplicate_indexes
    copy = False
    # copy makes sure duplicates isn't added every time when no copies are found
    duplicates.append(i)

    for j in range(i+1, len(s1_copy)):
        # find where the char is duplicated in the string, and it hasn't already been removed
        if s1_copy[j] == char and s1.find(char) != -1:
            duplicates.append(j)
            copy = True
    if copy:
        duplicate_indexes.append(duplicates)
    # removes all places where char is, to make sure its not double counted
    s1 = s1.replace(char, '')


for i in duplicate_indexes:
    # j is index of duplicate s1 char, make sure all j indexes in s2 are also duplicates
    map_char = s2[i[0]]
    for j in i:
        if s2[j] != map_char:
            print("false")
            quit()
print("true")
