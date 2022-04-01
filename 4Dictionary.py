
characterA = {"strength": 12,
              "dexterity": 10,
              "constitution": 15,
              "intelligence": 8,
              "wisdom": 9,
              "charisma": 13}

print(characterA)
for (key, value) in characterA.items():
    print(key, ":", value)

print()
if "strength" in characterA.keys():
    print('strength :', characterA["strength"])
else:
    print("strength isn't a character stat.")
if "speed" in characterA.keys():
    print('speed :', characterA["speed"])
else:
    print("speed isn't a character stat.")
