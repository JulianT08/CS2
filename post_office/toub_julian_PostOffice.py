'''
Name: toub_julian_PostOffice_fixed.py
Description: This code simulates a post office. The user provides the office with dimensions (length, height, width), starting zip code, and destination zip code. The program calculates the shipping cost based on defined zone distances and package types, and offers a cost breakdown with optional CSV export.
'''
from pathlib import Path
import csv

def get_postage_type(length, height, width):
    """
    Determines the postage_type of package based on dimensions.
    Returns a string key or 'unmailable'.
    """
    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and 0.007 <= width <= 0.016:
        return 'reg_post_card'
    elif 4.25 < length < 6 and 6 < height < 11 and 0.007 <= width <= 0.015:
        return 'large_post_card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and 0.016 < width < 0.25:
        return 'envelope'
    elif 6.125 < length < 24 and 11 <= height <= 18 and 0.25 <= width <= 0.5:
        return 'large_envelope'
    elif length >= 24 and width > 0.5 and (length + 2*height + 2*width) <= 84:
        return 'reg_package'
    elif 84 < (length + 2*height + 2*width) < 130:
        return 'large_package'
    else:
        return 'unmailable'

def get_zone(zip_code):
    """
    Maps a 5-digit zip code to a shipping zone (1-6). Returns None if invalid.
    """
    if 1 <= zip_code <= 6999:
        return 1
    elif 7000 <= zip_code <= 19999:
        return 2
    elif 20000 <= zip_code <= 35999:
        return 3
    elif 36000 <= zip_code <= 62999:
        return 4
    elif 63000 <= zip_code <= 84999:
        return 5
    elif 85000 <= zip_code <= 99999:
        return 6
    else:
        return None

def calculate_cost(postage_type, distance):
    """
    Returns the shipping cost based on package type and zone distance.
    """
    rates = {
        'reg_post_card':  (0.20, 0.03),
        'large_post_card':(0.37, 0.03),
        'envelope':       (0.37, 0.04),
        'large_envelope': (0.60, 0.05),
        'reg_package':    (2.95, 0.25),
        'large_package':  (3.95, 0.35)
    }
    if postage_type in rates:
        base, per_zone = rates[postage_type]
        return base + per_zone * distance
    return None

def main():
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        try:
            # Prompt and parse input
            while True:
                user_input = input("Enter Length, Height, Width, Starting Zip, Ending Zip (comma-separated): ")
                parts = [p.strip() for p in user_input.split(',')]
                if len(parts) != 5:
                    print("Error: Please enter exactly 5 values. E.g., 4, 5, 0.01, 06830, 67840.")
                    continue
                try:
                    length = float(parts[0])
                    height = float(parts[1])
                    width = float(parts[2])
                    zip_start = int(parts[3])
                    zip_end = int(parts[4])
                except ValueError:
                    print("Error: Dimensions must be numbers and zip codes must be integers.")
                    continue
                if length < 0 or height < 0 or width < 0:
                    print("Error: Dimensions cannot be negative.")
                    continue
                zone_start = get_zone(zip_start)
                zone_end   = get_zone(zip_end)
                if zone_start is None or zone_end is None:
                    print("Error: Zip codes must be between 00001 and 99999.")
                    continue
                distance = abs(zone_end - zone_start)
                break

            # Determine postage type and rates
            postage_type = get_postage_type(length, height, width)
            if postage_type == 'unmailable':
                print("Package is unmailable.")
                continue

            cost_info = {
                'reg_post_card':  (0.20, 0.03),
                'large_post_card':(0.37, 0.03),
                'envelope':       (0.37, 0.04),
                'large_envelope': (0.60, 0.05),
                'reg_package':    (2.95, 0.25),
                'large_package':  (3.95, 0.35)
            }
            base_cost, per_zone_cost = cost_info[postage_type]
            total_cost = calculate_cost(postage_type, distance)

            # Output cost
            print(f"Total shipping cost: ${total_cost:.2f}")

            # Optional breakdown
            if input("Breakdown cost formula? (y/n): ").strip().lower().startswith('y'):
                print(f"Package type: {postage_type}\n"
                      f"Zones traveled: {distance}\n"
                      f"Base cost: ${base_cost:.2f}\n"
                      f"Cost per zone: ${per_zone_cost:.2f}")

            # Optional CSV export
            if input("Export breakdown to CSV? (y/n): ").strip().lower().startswith('y'):
                filename = 'post_office.csv'
                downloads = Path.home() / "Downloads"
                filepath = downloads / filename
                with open(filepath, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Base Cost', 'Zones', 'Cost per Zone', 'Total Cost'])
                    writer.writerow([f"${base_cost:.2f}", distance, f"${per_zone_cost:.2f}", f"${total_cost:.2f}"])
                print(f"Data exported to {filepath}")

            # Exit after successful calculation
            break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
