from pandas import Panda

panda1 = Panda("sosii", 3, 43, "nee york")
panda2 = Panda("koro", 9, 44, "africa")
panda3 = Panda("bombba", 6, 55, "america")
panda4 = Panda("rori", 5, 30, "tokyo")

print(panda1.name)

for panda in [panda1, panda2, panda3, panda4]:
    print(panda.eat())
    print(panda.sleep())