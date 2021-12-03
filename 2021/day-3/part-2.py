entries = open('input').read().splitlines()
entries_ox_gen_entries = entries
co2_scrub_entries = entries


for i in range(12): 
    counts_of_ones = 0
    for entry in entries_ox_gen_entries:
        if(entry[i] == "1"): counts_of_ones+=1    
    most_common_bit = "1" if counts_of_ones >= len(entries_ox_gen_entries)/2 else "0"
    entries_ox_gen_entries = [x for x in entries_ox_gen_entries if x[i] == most_common_bit]
    if (len(entries_ox_gen_entries) == 1): break
ox_gen_rating = int(entries_ox_gen_entries[0], 2)


for i in range(12): 
    counts_of_ones = 0
    for entry in co2_scrub_entries:
        if(entry[i] == "1"): counts_of_ones+=1
    less_common_bit = "0" if counts_of_ones >= len(co2_scrub_entries)/2 else "1"
    co2_scrub_entries = [x for x in co2_scrub_entries if x[i] == less_common_bit]
    if (len(co2_scrub_entries) == 1): break
co2s_scrub_rating = int(co2_scrub_entries[0], 2)

print(f"ox_gen_rating={ox_gen_rating}")
print(f"co2s_scrub_rating={co2s_scrub_rating}")
print(f"life support rating = {ox_gen_rating*co2s_scrub_rating}")