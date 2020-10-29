Num = 0
larg_data = -1
small_data = None
while True:
    Num = input("have to input you data : ")
    if string == "Done" :
        break
    try :
        number = int(Num)
    except :
        print('Invalid input')
    if small_data is None :
        small_data = number
    elif number < small_data :
        small_data = number
    elif number > larg_data :
        larg_data = number
print("Maximum is", larg_data)
print("Minimum is", small_data)
