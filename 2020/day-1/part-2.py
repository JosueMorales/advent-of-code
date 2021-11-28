entries = open('input').read().splitlines()
count = len(entries)
i = 0
while(i < count):
    j = i + 1
    while(j < count):
        k = j + 1
        while(k < count):
            entry1 = int(entries[i])
            entry2 = int(entries[j])
            entry3 = int(entries[k])
            if(entry1 + entry2 + entry3 == 2020):
                print("*****BINGOOO*****")
                print(f'{entry1} + {entry2} + {entry3} = 2020')
                print(f'{entry1} x {entry2} = {entry1 * entry2 * entry3}')
            k+=1
        j+=1
    i+=1