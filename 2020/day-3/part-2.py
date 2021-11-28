entries = open('input').read().splitlines()

def treesInSlope(xStep, yStep):
    treeCount, xPos, yPos = 0, 0, 0
    while (yPos < len(entries)):
        #RightXSteps
        xPos += xStep
        if xPos > 30: xPos -= 31
        #DownYSteps
        yPos += yStep
        if yPos >= len(entries): break
        if(entries[yPos][xPos] == "#"): treeCount += 1
    return treeCount
totalTrees = treesInSlope(3,1) * treesInSlope(1,1) *  treesInSlope(5,1) * treesInSlope(7,1) * treesInSlope(1,2)
print(totalTrees)