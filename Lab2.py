from collections import defaultdict

# 1. Classes for Meeting Room Management


class MeetingRoom:
    def __init__(self, room_id, capacity, floor_location):
        self.room_id = room_id
        self.capacity = capacity
        self.floor_location = floor_location

class ZoomMeetingRoom(MeetingRoom):
    def __init__(self, room_id, capacity, floor_location, zoom_device_id, zoom_account_id):
        super().__init__(room_id, capacity, floor_location)
        self.zoom_device_id = zoom_device_id
        self.zoom_account_id = zoom_account_id

class Booking:
    def __init__(self, employee_id, room_id, meeting_date, meeting_time, duration):
        self.employee_id = employee_id
        self.room_id = room_id
        self.meeting_date = meeting_date
        self.meeting_time = meeting_time
        self.duration = duration

class BookingManager:
    def __init__(self):
        self.bookings_by_date = defaultdict(list)

    def add_booking(self, booking):
        self.bookings_by_date[booking.meeting_date].append(booking)

    def get_bookings_by_date(self, date):
        return self.bookings_by_date.get(date, [])

# Example usage:
if __name__ == "__main__":
    room1 = MeetingRoom("R101", 10, 2)
    room2 = ZoomMeetingRoom("R102", 8, 3, "ZD001", "ZA001")
    manager = BookingManager()
    booking1 = Booking("E001", "R101", "2024-06-10", "10:00", 2)
    booking2 = Booking("E002", "R102", "2024-06-10", "11:00", 1)
    manager.add_booking(booking1)
    manager.add_booking(booking2)
    print("Bookings on 2024-06-10:")
    for b in manager.get_bookings_by_date("2024-06-10"):
        print(vars(b))

# 2. Welcome Message Function

def welcome_message(name):
    return f"Welcome, {name}!"

print(welcome_message("Alice"))

# 3. Largest Number Function

def largest_number(a, b, c):
    return max(a, b, c)

print("Largest:", largest_number(5, 12, 7))

# 4. Print Digits in Words

def print_digits_in_words(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit in str(number):
        print(words[int(digit)])

print("Digits in words for 427:")
print_digits_in_words(427)