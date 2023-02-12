def print_binary(num):
    if num < 2:
        #print(num)
        return (num)

    elif num % 2 == 1:
        #print(num)
        return (1 + 10*print_binary(num//2))
    else:
        #print(num)
        return (0 + 10*print_binary(num//2))

num = int(input(""))
num = print_binary(num)
print(int(num))
