t = (19,42,21,234,6,2.2,1234,2,1.31, 1,2,2,2)
print(f"The {len(t)} numbers are: ", end='')
for i, num in enumerate(t):
    if (i == len(t) - 1):
        print(f"{num}")
    else:
        print(f"{num}, ", end='')