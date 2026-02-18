def ft_count_harvest_iterative():
    harvest_in = int(input("Days until harvest: "))
    counter = 1
    while counter <= harvest_in:
        print("Day " + str(counter))
        counter += 1
    print("Harvest time!")
