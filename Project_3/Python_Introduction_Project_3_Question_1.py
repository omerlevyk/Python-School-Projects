printing = int(input())
num = int(input(""))
#first printing
if printing==0:
    list1 = []
    i = 1
    while i <= num:
        list1.append("*")
        i += 1
    #Transforming "*" into spaces
    space = 0
    print ("".join(list1))
    while space < num-1:
        list1.insert(space , " ")
        del list1[-1]
        print ("".join(list1))
        space +=1

# Second Print
else:
    # Defining List 2
    list2 = []
    l = 1
    if num % 2 == 0:
        print("ERROR")
    else:
        while l <= num:
            list2.append(" ")
            l += 1

        # Transforming spaces into "*"
        middle_num = int(num / 2)
        j = 1

        list2.insert(middle_num, "*")
        del list2[middle_num + 1]
        list2_1 = list2 + []
        while list2_1 [-1] == (" "):
            del list2_1[-1]
        print("".join(list2_1))
        print("".join(list2_1))
        left_side = num - (middle_num)
        right_side = num - (middle_num)
        while j <= middle_num:
            list2.insert(middle_num, "*")
            del list2[-1]
            list2.insert((middle_num), "*")
            del list2[0]
            j += 1
            list2_2 = list2 + []
            while list2_2[-1] == (" "):
                del list2_2 [-1]
            print("".join(list2_2))
            print("".join(list2_2))
            #print("".join(str(list2_2)))
            #print("".join(str(list2_2)))
