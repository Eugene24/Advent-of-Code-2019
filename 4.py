import collections

input = "235741-706948"
start = int(input[:input.find('-')])
end = int(input[input.find('-') + 1:])

counter = 0
for line in range(start, end + 1):
    line = str(line)
### LENGTH
    if len(line) != 6:
        continue
### RANGE
    if int(line) < start or int(line) > end:
        continue
### PAIRS
    groups = ([count for item, count in collections.Counter(line).items() if count > 1])
    result = [1 for a in groups if a == 2]
    if len(result) == 0:
        continue
### DECAF
    seq = 0
    for a in range(0, len(line) - 1):
        if int(line[a]) > int(line[a + 1]):
            seq += 1
    if seq > 0:
        continue
    counter += 1
print (counter)
