entries = open('input').read().splitlines()
treeCount, xPos, yPos = 0, 0, 0
while (yPos < len(entries)):
    #RightThree
    xPos += 3
    if xPos > 30: xPos -= 31
    #DownOne
    yPos += 1
    if yPos == len(entries): break
    if(entries[yPos][xPos] == "#"): treeCount += 1
print(f"Tree Count = {treeCount}")