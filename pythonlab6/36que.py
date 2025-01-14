from datetime import datetime, timedelta

# Dictionary for time zone offsets (relative to Eastern Time Zone)
time_zones = {
    'Eastern': 0,      # Eastern is 0 offset
    'Central': -1,     # Central is 1 hour behind Eastern
    'Mountain': -2,    # Mountain is 2 hours behind Eastern
    'Pacific': -3      # Pacific is 3 hours behind Eastern
}

# Function to convert 12-hour time to 24-hour format
def convert_to_24hr(time_str):
    return datetime.strptime(time_str, '%I:%M%p')

# Function to convert 24-hour time to 12-hour format
def convert_to_12hr(time_obj):
    return time_obj.strftime('%I:%M%p').lower()

# Main program
def convert_time():
    # Get user input
    time_str = input("Enter time (e.g. 11:48pm): ")
    start_zone = input("Starting zone (Eastern, Central, Mountain, Pacific): ")
    end_zone = input("Ending zone (Eastern, Central, Mountain, Pacific): ")

    # Convert the time to 24-hour format
    start_time = convert_to_24hr(time_str)

    # Calculate the time difference between zones
    zone_difference = time_zones[end_zone] - time_zones[start_zone]

    # Convert the time by adding the difference in hours
    new_time = start_time + timedelta(hours=zone_difference)

    # Output the new time in 12-hour format
    print(f"Converted time: {convert_to_12hr(new_time)}")

# Run the program
convert_time()
