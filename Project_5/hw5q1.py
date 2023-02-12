import pandas as pd
import matplotlib.pyplot as plt

####################################################### uploed flie
def load_dataset(virus):
    table = pd.read_csv("virus.csv")
    id_list = table["id"].values.tolist()
    virus_count_list = table["virus count"].values.tolist()
    print(table.head(4))
    print(f"The number of citizens in the database is: {len(id_list)}")
    return virus_count_list, id_list

####################################################### first histogram
def virus_count_hist(virus_count_list,max_val ,min_val):
    #min_val = min(virus_count_list)
    #max_val = max(virus_count_list)
    hist = [0 for _ in range (max_val+1)]
    for i in virus_count_list:
        hist[i] += 1
    plt.bar(range(len(hist)), hist)
    plt.show()
    return(hist)

####################################################### custom histogram
def custom_histogram_fun(virus_count_list, max_val, min_val, step):
    #min_val = min(virus_count_list)
    #max_val = max(virus_count_list)
    custom_virus_count_list = [int(val/step) for val in virus_count_list]
    custom_hist = [0 for _ in range (int(max_val/step)+1)]
    for i in custom_virus_count_list:
        custom_hist[i] += 1
    hist_range = []
    for i in range(len(custom_hist)):
        low_cap = i*step
        top_cap = int((i+1)*step)-1
        hist_range.append(str(low_cap)+str("-")+str(top_cap))
        if top_cap >= 100:
            if low_cap == 100:
                hist_range[-1] = str(low_cap)
            if low_cap < 100:
                hist_range[-1] = str(low_cap)+str("-")+str(100)
    plt.bar(hist_range, custom_hist)
    plt.xticks(rotation='vertical')
    plt.show()

####################################################### sick families
def sick_families(id_list,virus_count_list,virus_count):
    family_number = []
    complication = [0]*len(id_list)
    family_check = [0]*len(id_list)
    for i in range(len(virus_count_list)):
        if complication[i] == 0:
            complication[i] = 1
            if virus_count_list[i] >= virus_count:
                family_id = str(id_list[i])[5:7]
                family_countdown = [id_list[i]]
                family_count = [id_list[i]]
                #print(len(family_count))
                print("Sick citizen found:",str(id_list[i])+",","number of virus:",virus_count_list[i])
                for j in range(len(virus_count_list)):
                    if str(id_list[j])[5:7] == family_id:
                        if id_list[j] == id_list[i]:
                            pass
                        else:
                            print("    Family member:", str(id_list[j])+",", "number of virus:",virus_count_list[j])
                            complication[j] = 1
                            family_count.append(id_list[j])
                            #print(len(family_count))
                            #family_count = [id_list[j]]
                            if family_check[int(str(id_list[i])[5:7])] == 0:
                                #family_count.append(id_list[j])
                                #print(len(family_count))
                                if virus_count_list[j] >= virus_count:
                                    family_check[int(str(id_list[i])[5:7])] = 1
                                    family_countdown.append(id_list[j])
                                    #family_countdown.append(id_list[j])
                                    #family_number.append(id_list[j])
                if len(family_countdown) >= 2:
                    print("        QUARANTINE REQUIRED!")
                    family_number.append(id_list[i])
    for i in range(len(family_number)):
        family_number[i] = int(str(family_number[i])[5:7])
    return(family_number)

####################################################### giving a vaccine
def cure_families(id_list, virus_count_list, family_number, high_bound, low_bound):
    cured = 0
    hist = [0] * ((high_bound - low_bound) + 1)
    for i in range(len(family_number)):
        hist [int(family_number[i])] = 1
    for i in range(len(id_list)):
        #print(str(id_list[i])[5:7])
        if hist[int(str(id_list[i])[5:7])] == 1:
            cured += 1
            virus_count_list[i] = 0
    print(cured,"citizen have beed cured!")
    return(virus_count_list)

virus_count_list,id_list = load_dataset("virus.csv")                            #A
hist = virus_count_hist(virus_count_list, 100, 0)                               #B
step = (int(input("Please insert histogram range step: ")))                     #C
custom_histogram_fun(virus_count_list, 100, 0, step)
virus_count = int(input("Please insert virus count limit: "))                   #D
family_number = sick_families(id_list,virus_count_list,virus_count)
cure_families(id_list, virus_count_list, family_number, 100, 0)                 #E
custom_histogram_fun(virus_count_list, 100, 0, step)


