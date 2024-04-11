from invoice import generate_invoice_string
from display import display_all_lands
from utils import delete_returned_lands_info, calculate_fine_amount
import datetime

def return_land(land_info):
    while True:
        display_all_lands(land_info)
        rented_land_ids = [int(land_id) for land_id in land_info if land_info[land_id]['status'].strip() == 'Not Available']

        if not rented_land_ids:
            print("No lands are currently rented out.")
            break

        print("Rented Land IDs:", rented_land_ids)

        customer_name = input("Enter customer name: ")
        returned_lands = []

        print("\nEnter the land IDs you want to return (enter 'done' to finish):")
        while True:
            land_id_input = input("Land ID: ")
            if land_id_input.lower() == 'done':
                break

            if not land_id_input.strip().isdigit():
                print("Invalid input. Please enter a valid land ID or 'done' to finish.")
                continue

            land_id = int(land_id_input)
            if land_id not in rented_land_ids:
                print(f"Land {land_id} is not currently rented out. Please enter a valid rented land ID.")
                continue

            duration_input = input(f"Enter duration of rent for land {land_id} (in months): ")
            if not duration_input.isdigit() or int(duration_input) <= 0:
                print("Invalid duration. Please enter a positive integer value.")
                continue

            returned_lands.append((land_id, int(duration_input)))
            print(f"Land {land_id} added to the return list.")

        if returned_lands:
            customer_invoice_string = f"\nInvoice for {customer_name}:\n"
            total_fine_amount = 0

            for land_id, duration in returned_lands:
                land_info[land_id]['status'] = 'Available'  # Update land status
                land = land_info[land_id]
                fine_amount, total = calculate_fine_amount(land_id, duration, land_info)
                total_fine_amount += fine_amount

                customer_invoice_string += f"\nLand ID: {land_id}\n"
                customer_invoice_string += generate_invoice_string(customer_name, land_id, land, duration, total, fine_amount)
                customer_invoice_string += "\n"

            customer_invoice_string += f"\nTotal Fine Amount: NPR {total_fine_amount}\n"

            delete_returned_lands_info("data/rental_info.txt", [land_id for land_id, _ in returned_lands])

            # Generate file name based on the customer's name, current date, and time
            current_datetime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            file_name = f"{customer_name}_{current_datetime}_return_invoice.txt"

            with open(file_name, 'w') as file:
                file.write(customer_invoice_string)

            print("\n" + "=" * 40)
            print("          Land Return Invoice")
            print("=" * 40)
            print(customer_invoice_string)
            print("=" * 40)
            print(f"\nInvoice has been saved as '{file_name}'")
            print("=" * 40 + "\n")
        else:
            print("No lands selected for return.")

        choice = input("Do you want to return lands for another customer? (yes/no): ")
        if choice.lower() != 'yes':
            break