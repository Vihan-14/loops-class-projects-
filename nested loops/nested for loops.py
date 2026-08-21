
# nested for loop

for i in range(1,6):
    for j in range(1,11):
        print(j, end=" ")
     
    print()


    print("---------------------------")


    i = 1
    while i < 6:

        j = 1 
        while j < 11 :
            print(j, end=" ")
            j = j + 1

        print()
        i = i + 1