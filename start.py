filename = input('Enter file name: ')
with open(filename) as fh:
    pizza_count, two, three, four = map(int, fh.readline().split())
    pizzas = []
    for _ in range(pizza_count):
        pizzas.append(fh.readline().split())

two_pizzas, three_pizzas, four_pizzas = [], [], []
# print(pizza_count, two, three, four, pizzas)
people = 2*two + 3*three + 4*four
delivered_teams = 0
if people == pizza_count: # sabko pizza milega
    four_pizzas = list( range(1, four + 1))
    three_pizzas = list( range(four + 1, four + three + 1))
    two_pizzas = list( range(four + three + 1, four + three + two + 1))
    delivered_teams = pizza_count
elif people < pizza_count:
    four_pizzas = list( range(1, four + 1))
    three_pizzas = list( range(four + 1, four + three + 1))
    two_pizzas = list( range(four + three + 1, four + three + two + 1))
    delivered_teams = people
else:       # people > pizza_count
    if 2 * two == pizza_count:
        two_pizzas = list(range(1, two+1))
    elif 2 * two < pizza_count:
        ans1 = pizza_count - 2 * two
        if 3 * three > ans1:
            two_pizzas = list(range(1, 2*two+1))
            three_pizzas = list(range(2*two+1, 2*two + 1 + ans1 // 3 + 1 + 1))
        elif 3 * three == ans1:
            three_pizzas = list(range(1, three + 1))
        else:
            ans2 = ans1 - 3*three
            if ans2 == 4 * four:
                four_pizzas = list(range(1, ans2 // 4))
            elif 4 * four == ans2:
                four_pizzas = list(range(1, four + 1))
            else:
                four_pizzas = list(range(1, ans2 // 4))
    else:
        q, r = divmod(pizza_count/2)
        if r == 1:
            two_pizzas = list(range(1, q))
            three_pizzas = q
        else:
            two_pizzas = list( range(1, q+1))

teams = {'2': two_pizzas, '3': three_pizzas, '4': four_pizzas}
# print(two_pizzas)
# print(three_pizzas)
# print(four_pizzas)
with open ('output' + filename, 'w') as write_file:
    write_file.write(str(delivered_teams) + '\n')
    for key in teams:
        write_file.write(key + ' ')
        for i in teams[key]:
            write_file.write(str(i) + ' ')
        write_file.write('\n')
