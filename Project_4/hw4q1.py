def funfun(x,y):
# Join x from a list to a single number:
    x_as_a_single_number = 0
    for integers in x:
        x_as_a_single_number += integers
        x_as_a_single_number = x_as_a_single_number * 10
    x_as_a_single_number = x_as_a_single_number // 10

# join (x + y):
    x_as_a_single_number = int(x_as_a_single_number) + y
    x_as_a_single_number = str(x_as_a_single_number)

# switching x back to list:
    x = []
    for i in range(len(x_as_a_single_number)):
       x.append(int(x_as_a_single_number[i]))
    print(x)
    return (x)

x = [int(s) for s in input("").split(",")]
y = int(input(""))
funfun(x,y)