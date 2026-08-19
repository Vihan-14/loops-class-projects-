activites = 4

print("You have {activites} activites to complete today")

completed_count = 0

activity_num = 1

activity_name = ""

while activity_num <= activites:

    if activity_num == 1:

        activity_name = "Make your bed"

    elif activity_num == 2:

        activity_name = "Feed the pet"

    elif activity_num == 3:

        activity_name = "Take out the trash"

    elif activity_num == 4:

        activity_name = "Wash the dishes"


    answer = input(f"Have you finished: {activity_name}? (yes/no): ")


    if answer == "yes":

        completed_count += 1

        activity_num += 1

        print("Great job! Chore completed.")

    else:

        print("Okay, finish it and check again!")


    print("Chores remaining:", activites - completed_count)

    print()