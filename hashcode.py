'''
6 (seconds) 4 (intersections) 5 (streets) 2 (cars) 1000 (points)
2 0 rue-de-londres 1
0 1 rue-d-amsterdam 1
3 1 rue-d-athenes 1
2 3 rue-de-rome 2
1 2 rue-de-moscou 3
4 rue-de-londres rue-d-amsterdam rue-de-moscou rue-de-rome
3 rue-d-athenes rue-de-moscou rue-de-londres
'''

# dict_streets = {
#     'london' : 1,
#     'amsterdam' : 2,
#     'athens'
# }

class Route:
    def __init__(start, stop, name, time):
        self.start = start
        self.stop = stop
        self.name = name
        self.time = time

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

print('streets_dict', streets_dict)
print(passing_intersections)
print(routes)

for k,v in streets_dict.items():
    print(f'{k}: {v}')

print(streets_dict)
