entries = open('input').read().splitlines()
count = len(entries)
valid = 0
for entry in entries:
    firstSplit = entry.split(": ")
    policy = firstSplit[0]
    password = firstSplit[1]
    secondSplit = policy.split(" ")
    pRange = secondSplit[0]
    thirdSplit = pRange.split("-")
    lowest = int(thirdSplit[0])
    highest = int(thirdSplit[1])
    letterToRepeat = secondSplit[1]
    print(f"{lowest} - {highest} {letterToRepeat}: {password}")
    ocurrences = password.count(letterToRepeat)
    print(f'ocurrences = {ocurrences}')
    if(ocurrences in range(lowest, highest + 1)):
        print("is valid")
        valid+=1
    else:
        print("is not valid")
print(valid)
    