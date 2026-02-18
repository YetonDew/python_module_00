def ft_garden_summary():
    name = input("Enter garden name: ")
    plants = int(input("Enter number of plants: "))
    print("Garden: " + name)
    print("Plants: " + str(plants))
    print("Status: Growing well!"
          if plants > 25 else "Status: We need more effort! :(")
