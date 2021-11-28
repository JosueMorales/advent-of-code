entries = open('input').read().splitlines()
count = len(entries)
i = 0
while(i < count):
    j = i + 1
    while(j < count):
        entry1 = int(entries[i])
        entry2 = int(entries[j])
        if(entry1 + entry2 == 2020):
            print("*****BINGOOO*****")
            print(f'{entry1} + {entry2} = 2020')
            print(f'{entry1} x {entry2} = {entry1 * entry2}')
        j+=1
    i+=1
