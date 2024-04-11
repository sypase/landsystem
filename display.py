# display.py

def display_table(data, headers):
    max_col_widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]
    max_col_widths = [max(len(header), width) for header, width in zip(headers, max_col_widths)]

    separator = "+" + "+".join("-" * (width + 2) for width in max_col_widths) + "+"
    header_row = "|" + "|".join(f" {header:<{width}} " for header, width in zip(headers, max_col_widths)) + "|"

    print(separator)
    print(header_row)
    print(separator)

    for row in data:
        data_row = "|" + "|".join(f" {str(item):<{width}} " for item, width in zip(row, max_col_widths)) + "|"
        print(data_row)

    print(separator)

def display_all_lands(land_info):
    print("=" * 30)
    print("     Available Lands")
    print("=" * 30)

    available_lands = [
        [kitta, details['city'], details['direction'], details['area'], details['status'].strip()]
        for kitta, details in land_info.items()
        if details['status'].strip() == 'Available'
    ]

    if available_lands:
        display_table(available_lands, ["Kitta", "City", "Direction", "Area", "Status"])
    else:
        print("No available lands.")

    print("\n" + "=" * 30)
    print("      Rented Lands")
    print("=" * 30)

    rented_lands = [
        [kitta, details['city'], details['direction'], details['area'], details['status'].strip()]
        for kitta, details in land_info.items()
        if details['status'].strip() == 'Not Available'
    ]

    if rented_lands:
        display_table(rented_lands, ["Kitta", "City", "Direction", "Area", "Status"])
    else:
        print("No lands are currently rented out.")

def display_starting_page():
    print("=" * 50)
    print("   Welcome to TechnoPropertyNepal")
    print("        Land Renting System")
    print("=" * 50)
    print("This system allows you to rent and return lands.")
    print("You can also generate and print invoices for rented lands.")
    print("\nPlease select an option from the menu below to proceed:")
    print("1. Rent land")
    print("2. Return land")
    print("3. Exit")
    print("=" * 50)