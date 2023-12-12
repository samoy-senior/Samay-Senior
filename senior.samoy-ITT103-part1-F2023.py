Author:Samoy Senior Date:december 12,2023 Course:ITT103 Purpose:To reserve a seat without error on the UCC bus system.
#UCC_signature_expres_limited#
#reservation options
  #first_class(f/F)
  #Business_class(B/b)
  #economy_class(E/e)
  #Quit/cancel(q/Q)
#Please_select_an_option:
# Initialize variables
first_class_seats = 27
business_class_seats = 38
economy_class_seats = 56
SEAT_STATUS = {
    "F": [[0] * 1 for _ in range(first_class_seats)],
    "B": [[0] * 1 for _ in range(business_class_seats)],
    "E": [[0] * 1 for _ in range(economy_class_seats)],
}


def display_menu_and_get_choice():
    """
    Displays the menu and gets user choice
    """
    print("UCC Signature Express Limited")
    print("Reservation Options:")
    print("  First Class (F/f)")
    print("  Business Class (B/b)")
    print("  Economy Class (E/e)")
    print("  Quit or Cancel (Q/q)")
    choice = input("Please select an option: ").upper()
    return choice


def reserve_seat(class_type, row, column):
    """
    Checks for available seats and reserves one if found
    """
    seats = SEAT_STATUS[class_type]

    if 0 <= row < len(seats) and 0 <= column < len(seats[0]):
        if seats[row][column] == 0:
            seats[row][column] = 1
            print(f"Reserving seat: row {row + 1}, column {column + 1}")
            return True
        else:
            print(f"Seat at row {row + 1}, column {column + 1} is already reserved.")
            main()
    else:
        print(f"Invalid seat selection.")
        print(f"Row must be between 1 and {len(seats)}")
        print(f"Column must be between 1 and {len(seats[0])}")

    return False


def display_reservation_summary(class_type):
    """
    Displays the total number of seats and reserved seats for a class
    """
    seats = SEAT_STATUS[class_type]
    total_seats = len(seats) * len(seats[0])
    reserved_seats = sum(sum(row) for row in seats)
    print(f"\nReservation Type: {class_type}")
    print(f"Total number of seats: {total_seats}")
    print(f"Total number of seats reserved: {reserved_seats}")


def main():
    """
    Main program logic for the reservation system
    """
    choice = ""
    while choice.upper() not in ["Q", "F", "B", "E"]:
        choice = display_menu_and_get_choice()

        if choice.upper() == "Q":
            # Display reservation summary for each class
            for class_type in SEAT_STATUS:
                display_reservation_summary(class_type)
            print("\nThank you for using UCC Signature Express Limited!")
            break

        if choice.upper() in ["F", "B", "E"]:
            try:
                row = int(input("Enter desired row number: ")) - 1
                column = int(input("Enter desired column number: ")) - 1
                if reserve_seat(choice.upper(), row, column):
                    print("Reservation Approved for row:", row+1, "column:", column+1)
                    main()
            except ValueError:
                print("Invalid input. Please enter integers for row and column.")

if __name__ == "__main__":
    main()
