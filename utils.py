import os

def save_land_info(file_path, land_info):
    """Save land information to a file."""
    with open(file_path, 'w') as file:
        file.write("Land ID,City,Direction,Area,Price,Status\n")
        for land_id, details in land_info.items():
            status = details.get('status', 'Available')
            file.write(f"{land_id},{details['city']},{details['direction']},{details['area']},{details['price']},{status}\n")

def read_land_info(file_path):
    """Read land information from a file."""
    land_info = {}
    if not os.path.exists(file_path):
        return land_info

    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            line = line.strip()
            if line:
                try:
                    land_id, city, direction, area, price, status = line.split(',')
                    land_info[int(land_id)] = {
                        'city': city,
                        'direction': direction,
                        'area': float(area),
                        'price': float(price),
                        'status': status
                    }
                except ValueError:
                    print(f"Error reading line: {line}. Skipping...")
    return land_info

def save_rental_info(file_path, rental_info):
    """Save rental information to a file."""
    with open(file_path, 'a') as file:
        for land_id, duration in rental_info.items():
            file.write(f"{land_id},{duration}\n")

def read_rental_info(file_path):
    """Read rental information from a file."""
    rental_info = {}
    if not os.path.exists(file_path):
        return rental_info

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    land_id, duration = map(int, line.split(','))
                    rental_info[land_id] = duration
                except ValueError:
                    print(f"Error reading line: {line}. Skipping...")
    return rental_info

def calculate_fine_amount(land_id, new_duration, land_info):
    """Calculate the fine amount based on the newly entered duration and rented duration."""
    fine_percent = 0.1
    total = 0
    rental_info = read_rental_info("data/rental_info.txt")

    if land_id in rental_info:
        rented_duration = rental_info[land_id]
        rented_price = land_info[land_id]['price'] * rented_duration

        remaining_duration = new_duration - rented_duration
        if remaining_duration > 0:
            fine = remaining_duration * land_info[land_id]['price'] * fine_percent
        else:
            fine = 0
        total = rented_price + fine
    else:
        fine = 0
        total = new_duration * land_info[land_id]['price']

    return fine, total

def delete_returned_lands_info(file_path, returned_lands):
    """Delete the information of returned lands from the rental_info file."""
    rental_info = read_rental_info(file_path)
    for land_id in returned_lands:
        if land_id in rental_info:
            del rental_info[land_id]

    with open(file_path, 'w') as file:
        for land_id, duration in rental_info.items():
            file.write(f"{land_id},{duration}\n")