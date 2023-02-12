list = []
while True:
    index = int(input(""))
    if index > 8:
        break
    if index == 0:
        id_num = int(input(""))
        grede = int(input(""))
        list.extend([id_num, grede])
        print("")
    if index == 1:
        id_num = str(input(""))
        list_of_errors = []
        i = 0
        while i < len(list):
            if str(list[i]).endswith(id_num) == 1:
                del list[i]
                del list[i]
                list_of_errors.append(i)
            i += 2
        if len(list_of_errors) == 0:
            print("ERROR")
        print("")
    if index == 2:
        id_num = int (input(""))
        if id_num in list:
            print(bool(1))
        else:
            print(bool(0))
        print("")
    if index == 3:
        sec_index = int(input(""))
        list_of_grade = []
        if sec_index == 0:
            min_grade = 80
        else:
            min_grade = 90
        i = 1
        while i <= len(list):
            if list[i] >= min_grade:
                list_of_grade.append(list[i])
            else:
                pass
            i += 2
        print(len(list_of_grade))
        print("")
    if index == 4:
        summ = 0
        summ_list = []
        i = 1
        while i < len(list):
            summ += list[i]
            summ_list.append(list[i])
            i += 2
        if len(summ_list) != 0:
            avg = summ / len(summ_list)
            print(f"{avg:.2f}")
        print("")
    if index == 5:
        id_num = str(input(""))
        id_list = []
        i = 0
        while i < len (list):
            if str(list[i]).endswith(id_num) == 1:
                if list[i] > 100:
                    id_list.append(list [i] )
                    id_list.append(list [i+1] )
            else:
                pass
            i += 2
        if len(id_list) != 0:
            i = 0
            while i+1 < len(id_list):
                print(str(id_list[i]) + " " + str(id_list[i+1]))
                i +=2
        print("")
    if index == 6:
        summ = 0
        summ_list = []
        i = 1
        p = 1
        while i <= len(list):
            if list[i] <= 55:
                summ += list[i]
                summ_list.append(list[i])
                p +=1
            else:
                pass
            i += 2
        if len(summ_list) == 0:
            print("0.00")
        else:
            omer_is_doing_slicing_become_he_must = summ_list[0:p]
            if omer_is_doing_slicing_become_he_must == 10000000000:
                #print("do nothing become this is useless")
                pass
            else:
                avg = len(summ_list) / (len(list)*0.5)
                print(f"{avg:.2f}")
        print("")
    if index == 7:
        print("")
        break
    if index == 8:
        print(list)