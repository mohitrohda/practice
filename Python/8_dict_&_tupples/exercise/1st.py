#We have following information on countries and their population (population is in crores),

population = {"china":143, 
     "india":136,
     "usa":32,
     "pakistan":21}

print_pouplation = input("Type print to see all country population:").lower()

if print_pouplation == "print":
    for key in population:
        print(key,"==>",population[key])



if print_pouplation == "add":
    cntry_name = input("Enter country name for adding =").lower()
    if cntry_name in population:
        print("Country is already listed")
    else:
        popu = int(input("enter popululation"))   
        population[cntry_name]= popu
        print(population)       

if print_pouplation == "remove":
    dlt_cntry = input("enter country name to dlt = ")
    del population[dlt_cntry]
    print(population)

if print_pouplation == "query":
    query_cntry = input("enter country name for query =")
    print(population[query_cntry])
