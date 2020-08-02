import statistics

working = []

for x in range (2, 51):
    for y in range(2, 51):
        for z in range(3, 51):
            n = x * y * z
            if n <= 50:
                working.append(n)

print(working)
print(statistics.mode(working))