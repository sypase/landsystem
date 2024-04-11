from invoice import generate_invoice_string
from display import display_all_lands
from utils import save_land_info, save_rental_info
import datetime

def rent_land(land_info):
    while True:
        display_all_lands(land_info)
        customer_name = input("Enter customer name: ")
        rented_lands = []

        print("\nEnter the land IDs you want to rent (enter 'done' to finish):")
        while True:
            land_id_input = input("Land ID: ")
            if land_id_input.lower() == 'done':
                break

            if not land_id_input.strip().isdigit():
                print("Invalid input. Please enter a valid land ID or 'done' to finish.")
                continue

            land_id = int(land_id_input)
            if land_id not in land_info:
                print(f"Land {land_id} does not exist. Please enter a valid land ID.")
                continue

            if land_info[land_id]['status'].strip() != 'Available':
                print(f"Land {land_id} is not available for rent. Please choose another land.")
                continue

            duration_input = input(f"Enter duration of rent for land {land_id} (in months): ")
            if not duration_input.isdigit() or int(duration_input) <= 0:
                print("Invalid duration. Please enter a positive integer value.")
                continue

            rented_lands.append((land_id, int(duration_input)))
            print(f"Land {land_id} added to the rental list.")

        if rented_lands:
            customer_invoice_string = f"\nInvoice for {customer_name}:\n"
            total_amount = 0

            for land_id, duration in rented_lands:
                land = land_info[land_id]
                total_amount += land['price'] * duration

                # Update land status to 'Not Available'
                land_info[land_id]['status'] = 'Not Available'

                # Save the duration information
                save_rental_info("data/rental_info.txt", {land_id: duration})

                # Generate invoice string for the rented land
                customer_invoice_string += f"\nLand ID: {land_id}\n"
                customer_invoice_string += generate_invoice_string(customer_name, land_id, land, duration, land['price'] * duration)
                customer_invoice_string += "\n"

            # Save the updated land_info
            save_land_info("data/land_info.txt", land_info)

            # Generate file name based on the customer's name, current date, and time
            current_datetime = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            file_name = f"{customer_name}_{current_datetime}_rent_invoice.txt"

            # Save the invoice to a file
            with open(file_name, 'w') as file:
                file.write(customer_invoice_string)

            # Print the invoice and success message
            print("\n" + "=" * 40)
            print("          Land Rental Invoice")
            print("=" * 40)
            print(customer_invoice_string)
            print("=" * 40)
            print(f"\nInvoice has been saved as '{file_name}'")
            print("=" * 40 + "\n")
        else:
            print("No valid lands selected for rent.")

        choice = input("Do you want to rent lands for another customer? (yes/no): ")
        if choice.lower() != 'yes':
            break