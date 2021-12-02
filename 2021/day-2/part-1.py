entries = open('input').read().splitlines()
depth, horizontal = 0, 0
for entry in entries:
    parts = entry.split(" ")
    instruction = parts[0]
    delta = int(parts[1])
    if(instruction == "up"):
        depth -= delta
    elif(instruction == "down"):
        depth += delta
    else:
        horizontal += delta
result = depth * horizontal
print(f"result = {result}")
