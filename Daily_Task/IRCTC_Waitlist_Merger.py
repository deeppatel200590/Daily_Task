counter=[2, 5, 8, 12]
online=[1, 3, 7, 10]

i=0
j=0
merged=[]

while i<len(counter) and j<len(online):
    if counter[i]<online[j]:
        merged.append(counter[i])
        i+=1
    else:
        merged.append(online[j])
        j+=1

while i<len(counter):
    merged.append(counter[i])
    i+=1

while j<len(online):
    merged.append(online[j])
    j+=1

print(merged)