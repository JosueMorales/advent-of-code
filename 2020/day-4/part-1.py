entries = open('input').read().splitlines()
i = -1
data_dict = []
new_entry = True
fields_ok_to_miss = ['cid']
for entry in entries:
    if(entry == ''):
        new_entry = True
        continue
    if(new_entry):
        i+=1
        data_dict.append([])
        new_entry = False
    data_dict[i].extend(entry.split(' '))
valid = 0
for data in data_dict:
    if len(data) < 7: continue
    for entry in data:
        if entry.startswith('cid'): 
            valid +=1
            break

print(valid)
