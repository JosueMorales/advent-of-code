entries = open('input').read().splitlines()
increments, previous = 0, None
for entry in entries:
    if(previous is not None and int(entry) > previous): increments+=1
    previous = int(entry)

print(f'increments = {increments}')