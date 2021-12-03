entries = open('input').read().splitlines()

counts_of_ones = [0,0,0,0,0,0,0,0,0,0,0,0]

for entry in entries:
    for i in range(12):
        if(entry[i] == "1"): counts_of_ones[i] = counts_of_ones[i]+1

gamma_rate = "".join([ "0" if counts_of_ones[i] < 500 else "1" for i in range(len(counts_of_ones))])
epsilon_rate = "".join([ "1" if counts_of_ones[i] < 500 else "0" for i in range(len(counts_of_ones))])
gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)
consumption = gamma_rate_dec * epsilon_rate_dec

print(f"consumption = {consumption}")

