num = int(input(""))
j = 1
while j <= 10:
    first_mun = j * num
    if first_mun >= 100:
        while first_mun >= 100:
            first_mun -= 100
    row = [first_mun , first_mun]
    adds = first_mun
    multip = first_mun
    i = 1
    while i < 5:
        new_adds = first_mun + adds
        while new_adds >= 100:
            new_adds -= 100
        new_multip = first_mun * multip
        while new_multip >= 100:
            new_multip -= 100
        row.append(new_adds)
        row.append(new_multip)
        adds += first_mun
        multip = multip * first_mun
        i += 1
    j += 1
    print(str(row[0])+" "+str(row[1])+" "+str(row[2])+" "+str(row[3])+" "+str(row[4])+" "+str(row[5])+" "+str(row[6])+" "+str(row[7])+" "+str(row[8])+" "+str(row[9]))
