keys = input("Enter keys: ").split()
values = list(map(int, input("Enter values: ").split()))
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print("\nDictionary:", d)
values_list = list(d.values())
values_list.sort()
sorted_d = {}
for v in values_list:
    for k in d:
        if d[k] == v and k not in sorted_d:
            sorted_d[k] = v
print("Sorted Dictionary:", sorted_d)
keys2 = input("\nEnter keys for second dictionary: ").split()
values2 = list(map(int, input("Enter values for second dictionary: ").split()))
d2 = {}
for i in range(len(keys2)):
    d2[keys2[i]] = values2[i]
merged = d.copy()
merged.update(d2)
print("Merged Dictionary:", merged)
text = input("\nEnter a word: ")
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Frequency:", freq)
set1 = set(map(int, input("\nEnter elements of set1: ").split()))
set2 = set(map(int, input("Enter elements of set2: ").split()))
print("Common Elements:", set1.intersection(set2))
print("Unique Elements:", set1.symmetric_difference(set2))