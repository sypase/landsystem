# invoice.py

import datetime

def generate_invoice_string(customer_name, land_id, land_details, duration, total_amount, fine_amount=0):
    invoice_lines = [
        "=" * 50,
        "                TechnoPropertyNepal",
        "                 Land Rental Invoice",
        "=" * 50,
        f"Customer Name: {customer_name}",
        f"Kitta Number: {land_id}",
        f"City: {land_details['city']}",
        f"Direction: {land_details['direction']}",
        f"Date and Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 50,
        f"Duration of Rent: {duration} months",
        f"Individual Rent Price per Month: NPR {land_details['price']}",
        f"Start Date: {datetime.datetime.now().strftime('%Y-%m-%d')}",
        f"End Date: {(datetime.datetime.now() + datetime.timedelta(days=int(duration) * 30)).strftime('%Y-%m-%d')}",
        "=" * 50,
        f"Fine Amount: NPR {fine_amount}",
        f"Total Amount: NPR {total_amount}",
        "=" * 50,
        "               Thank you for your business!",
        "=" * 50,
    ]

    return "\n".join(invoice_lines)

def display_invoice(customer_name, land_id, land_details, duration, total_rent_amount, fine_amount):
    invoice_string = generate_invoice_string(customer_name, land_id, land_details, duration, total_rent_amount, fine_amount)
    
    print("\n" + "=" * 50)
    print("              Land Rental Invoice")
    print("=" * 50)
    print(invoice_string)
    print("=" * 50 + "\n")