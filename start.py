filename = 'b_example.txt'
with open(filename) as fh:
    pizza_count, two, three, four = map(int, fh.readline().split())
    pizzas = []
    for _ in range(pizza_count):
        pizzas.append(fh.readline().split())

# print(pizza_count, two, three, four, pizzas)
people = 2*two + 3*three + 4*four
delivered_teams = 0
if people == pizza_count: # sabko pizza milega
    four_pizzas = range(1, four + 1)
    three_pizzas = range(four + 1, four + three + 1)
    two_pizzas = range(four + three + 1, four + three + two + 1)
    delivered_teams = pizza_count



teams = {'2': two_pizzas, '3': three_pizzas, '4': four_pizzas}
print(delivered_teams)
for key in teams:
    print(key, end=' ')
    for i in teams[key]:
        print(i, end=' ')
    print()
