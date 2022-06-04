# ************ HEALTH MANAGEMENT SYSTEM ****************
def getdate():
    import datetime
    return datetime.datetime.now()


harry = 0
rohan = 1
hammad = 2
print("Client numbers: \nHarry = 0\nRohan = 1\nHammad = 2")
client = int(input("Enter the client number: "))

if client == 0:
    activity = int(input("Enter 0 to access food or 1 to access exercise: "))
    if activity == 0:
        food1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if food1 == 0:
            h = open("harry_food.txt", "a")
            inp_food = input("Enter the food you ate: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Food item: ")
            h.write(inp_food)
            h.close()
        elif food1 == 1:
            h = open("harry_food.txt", "r")
            content = h.read()
            print(content)
            h.close()

    elif activity == 1:
        exercise1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if exercise1 == 0:
            h = open("harry_exe.txt", "a")
            inp_exercise = input("Enter the exercise you did: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Exercise name: ")
            h.write(inp_exercise)
            h.close()
        elif exercise1 == 1:
            h = open("harry_exe.txt", "r")
            content = h.read()
            print(content)
            h.close()

elif client == 1:
    activity = int(input("Enter 0 to access food or 1 to access exercise: "))
    if activity == 0:
        food1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if food1 == 0:
            h = open("rohan_food.txt", "a")
            inp_food = input("Enter the food you ate: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Food item: ")
            h.write(inp_food)
            h.close()
        elif food1 == 1:
            h = open("rohan_food.txt", "r")
            content = h.read()
            print(content)
            h.close()

    elif activity == 1:
        exercise1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if exercise1 == 0:
            h = open("rohan_exe.txt", "a")
            inp_exercise = input("Enter the exercise you did: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Exercise name: ")
            h.write(inp_exercise)
            h.close()
        elif exercise1 == 1:
            h = open("rohan_exe.txt", "r")
            content = h.read()
            print(content)
            h.close()

elif client == 2:
    activity = int(input("Enter 0 to access food or 1 to access exercise: "))
    if activity == 0:
        food1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if food1 == 0:
            h = open("hammad_food.txt", "a")
            inp_food = input("Enter the food you ate: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Food item: ")
            h.write(inp_food)
            h.close()
        elif food1 == 1:
            h = open("hammad_food.txt", "r")
            content = h.read()
            print(content)
            h.close()

    elif activity == 1:
        exercise1 = int(input("Enter 0 to add a log or 1 to retrieve the logs: "))
        if exercise1 == 0:
            h = open("hammad_exe.txt", "a")
            inp_exercise = input("Enter the exercise you did: ")
            time1 = str(getdate())
            h.write("\n[ ")
            h.write(time1)
            h.write(" ]- Exercise name: ")
            h.write(inp_exercise)
            h.close()
        elif exercise1 == 1:
            h = open("hammad_exe.txt", "r")
            content = h.read()
            print(content)
            h.close()

else:
    print("Invalid client details")






