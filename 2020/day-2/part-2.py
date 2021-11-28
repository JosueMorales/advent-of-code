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
    pos1 = int(thirdSplit[0])
    pos2 = int(thirdSplit[1])
    letterToRepeat = secondSplit[1]
    ##
    print(f"{pos1} - {pos2} {letterToRepeat}: {password}")
    pos1ContainsLetter = password[pos1-1] == letterToRepeat
    pos2ContainsLetter = password[pos2-1] == letterToRepeat
    if(pos1ContainsLetter ^ pos2ContainsLetter):
        print("is valid")
        valid+=1
    else:
        print("is not valid")
print(valid)
    