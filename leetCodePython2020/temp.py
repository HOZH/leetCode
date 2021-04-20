

strs = ["bella", "label", "roller"]

sets = list(map(lambda x: set([*x]), strs))

print(sets)

print(sets[0]&sets[1]&sets[2])