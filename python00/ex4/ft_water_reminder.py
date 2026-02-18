def ft_water_reminder():
    last_water = int(input("Days since last watering: "))
    print("Water the plants!" if last_water > 2 else "Plants are fine")
