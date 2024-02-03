def record_attendees(attendees_set):
    while True:
        attendee_name = input("Enter attendee name (or type 'exit' to finish): ")
        if attendee_name.lower() == 'exit':
            break
        attendees_set.add(attendee_name)
    print("Attendees recorded successfully.")

def display_attendees(attendees_set):
    print("List of Attendees:")
    for attendee in attendees_set:
        print(attendee)

def check_attendance(attendees_set):
    attendee_to_check = input("Enter the name of the attendee to check: ")
    if attendee_to_check in attendees_set:
        print(f"{attendee_to_check} is present at the event.")
    else:
        print(f"{attendee_to_check} is not present at the event.")

def remove_attendee(attendees_set):
    attendee_to_remove = input("Enter the name of the attendee to remove: ")
    if attendee_to_remove in attendees_set:
        attendees_set.remove(attendee_to_remove)
        print(f"{attendee_to_remove} has been removed from the event.")
    else:
        print(f"{attendee_to_remove} not found in the list of attendees.")

def calculate_statistics(attendees_set):
    total_attendees = len(attendees_set)
    print(f"Total number of attendees: {total_attendees}")

def event_attendance_system():
    attendees = set()
    print("\nEvent Attendance System Menu:")
    print("1. Record Attendees")
    print("2. Display Attendees")
    print("3. Check Attendance")
    print("4. Remove Attendee")
    print("5. Calculate Attendance Statistics")
    print("6. Exit System")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            record_attendees(attendees)
        elif choice == '2':
            display_attendees(attendees)
        elif choice == '3':
            check_attendance(attendees)
        elif choice == '4':
            remove_attendee(attendees)
        elif choice == '5':
            calculate_statistics(attendees)
        elif choice == '6':
            print("Exiting the Event Attendance System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Main program
if __name__ == "__main__":
    event_attendance_system()
