import random

# num = [i for i in range(1,26)]
# random.shuffle(num)
# print(num)

shuffled = [ 5, 23, 21,  3, 17,
            24, 25, 15,  6,  2,
            16, 14, 20,  8, 12,
            19, 11,  7, 22,  9,
            18, 13,  1,  4, 10]

horses =[   [],
            [],
            [],
            [],
            []
        ]

for i in range(5):
    for j in range(5):
        horses[j].append(shuffled.pop())

for race in horses:
    race.sort()

for race in horses:
    print(race)

def last(x):
    return x[-1]

new_horses = sorted(horses,key=last,reverse=True)
for race in new_horses:
    print(race)