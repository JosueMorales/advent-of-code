entries = open('input').read().splitlines()
depth, horizontal, aim = 0, 0, 0
for entry in entries:
    parts = entry.split(" ")
    instruction = parts[0]
    delta = int(parts[1])
    if(instruction == "up"):
        aim -= delta
    elif(instruction == "down"):
        aim += delta
    else:
        horizontal += delta
        depth += aim * delta
result = depth * horizontal
print(f"result = {result}")
