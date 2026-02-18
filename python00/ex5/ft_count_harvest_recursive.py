def ft_count_harvest_recursive(counter=1, harvest_in=None):
    if harvest_in is None:
        harvest_in = int(input("Days until harvest: "))
    if counter <= harvest_in:
        print("Day " + str(counter))
        ft_count_harvest_recursive(counter + 1, harvest_in)
    else:
        print("Harvest time!")
