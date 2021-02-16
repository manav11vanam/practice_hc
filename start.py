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
elif people < pizza_count:
    four_pizzas = range(1, four + 1)
    three_pizzas = range(four + 1, four + three + 1)
    two_pizzas = range(four + three + 1, four + three + two + 1)
    delivered_teams = people
else:       # people > pizza_count
    if 2*two == pizza_count:
        two_pizzas = range(1, two+1)
    elif 2*two < pizza_count:
        ans1 = pizza_count - 2*two
        if 3*three > ans1:
            ans1 // 3



teams = {'2': two_pizzas, '3': three_pizzas, '4': four_pizzas}
print(delivered_teams)
for key in teams:
    print(key, end=' ')
    for i in teams[key]:
        print(i, end=' ')
    print()
