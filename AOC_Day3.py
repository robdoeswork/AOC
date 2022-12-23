#split string into 2 parts
#def split_string(string):
#    compartment = len(string)//2
#    rucksack = []
#    for i in range(2):
#        start = i * compartment
#       end = start + compartment
#        rucksack.append(string[start:end])

#    return rucksack

#find the common character
def find_item(string1,string2,string3):
    # Convert the strings to sets
    set1 = set(string1)
    set2 = set(string2)
    set3 = set(string3)

    # Find the intersection of the sets
    common_chars = set1.intersection(set2, set3) 

    # Return the first common character, or None if there are no common characters
    return next(iter(common_chars))

#count total priority
def count_priority(item_list: list):
    mapping = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o':15, 'p': 16, 'q': 17, 'r': 18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y': 25, 'z':26}
    mapping.update({'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32,'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O':41,'P': 42, 'Q': 43, 'R': 44, 'S':45, 'T':46, 'U':47, 'V': 48, 'W':49, 'X':50, 'Y': 51, 'Z':52})
    priority_total = 0
    for item in range(len(item_list)):
        key = item_list[item]
        priority = mapping.get(key)
        priority_total = priority_total + priority
    return priority_total

#parse file and return a list of items in each rucksack
def parse_file(filename: str):
    with open(filename, 'r') as f:
        lines = f.readlines()
    item_list = []
    index3 = 0
    rucksack = []
    for line in lines:
         rucksack.append(line.strip())
         #compartments = split_string(rucksack)
         index3 += 1
         if index3 == 3:
            item = find_item(rucksack[0], rucksack[1], rucksack[2])
            item_list.append(item)
            index3 = 0
            rucksack.clear()
    return item_list


items = parse_file("inputd3.txt")
print(count_priority(items))