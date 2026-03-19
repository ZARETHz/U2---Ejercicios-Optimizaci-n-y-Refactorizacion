pares = []
for i in range(1, 101):
    if i % 2 == 0:
        pares.append(i)
print(pares)

""" pythonica """
pares = [i for i in range(1, 101) if i % 2 == 0]
print(pares)