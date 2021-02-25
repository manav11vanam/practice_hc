import random

filename = input('Enter filename: ')
if filename == '':
    filename = 'a.txt'

streets_dict = {}
with open (filename) as fh:
    duration, intersections, streets, cars, points = list(map(int, fh.readline().split()))
    for _ in range(streets):
        tmp = fh.readline().split() # 2 0 rue-de-londres 1
        street = tmp[2]
        tmp.pop(2)
        tmp = list(map(int, tmp))
        streets_dict[street] = tmp

    routes = []
    for _ in range(cars):
        route = fh.readline().split()[1:]
        routes.append(route)

passing_intersections = set()
for route in routes:
    for street in route[:-1]:
        passing_intersections.add(streets_dict.get(street)[1])

passing_intersections = len(passing_intersections)

with open('output '+ filename, 'w') as f:
    f.write(str(passing_intersections) + '\n')
    # keys = list(streets_dict.keys())
    keys = list(range(intersections))
    for i in range(passing_intersections):
        id = random.choice(keys)
        # print('id', id)
        keys.remove(id)
        # print('keys', keys)
        s = ''
        while s == '':
            for key in streets_dict:
                # print('key',key)
                if streets_dict[key][1] == id:
                    s = key

        # f.write(str(streets_dict[street][1]) + '\n')
        f.write(str(id) + '\n')
        f.write('1\n')
        f.write(s + ' 2\n')
