entries = open('input').read().splitlines()
increments, previous, i = 0, None, 2
while(i < len(entries)):
    current = int(entries[i-2]) + int(entries[i-1]) + int(entries[i])
    if(previous is not None and current > previous): increments+=1
    previous = current
    i+=1
print(f'increments = {increments}')