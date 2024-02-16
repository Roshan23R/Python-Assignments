from internship import InternshipManagementSystem

internship = InternshipManagementSystem()

print("1. Add intern")
print("2. display interns")
print("3. simulate conversion of interns to employees")
print("4. display employees")

while True:

    print("\n")
    num = int(input("Enter your choice "))

    if num == 1:
        internship.add_intern()

    elif num == 2:
        internship.display_interns()

    elif num == 3:
        performance_needed = int(input("Performance rating required: "))
        internship.simulate_conversion_process(performance_needed)
    
    elif num == 4:
        internship.display_employees()

    else:
        print("exited the program")
        break
