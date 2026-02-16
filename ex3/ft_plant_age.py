def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    print("Plant is ready to harvest!" if plant_age > 60 else "Plant needs more time to grow.")


ft_plant_age()
