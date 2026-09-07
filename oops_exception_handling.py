# Step 1 — Pick something from your exercise #

'''From My Conference Room Booking System, Will choose a Conference Room.

A room has data:

room name
capacity
booked slots

And it has behavior:

check whether a slot is available
book a room

So our class will be:'''

# class ConferenceRoom:#

 # Step 2 — Create the class and __init__ #

class ConferenceRoom:
    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.booked_slots = set()

# Step 3 — Add one method using self #

'''def book_room(self, date, time):
    slot = (date, time)

    if slot in self.booked_slots:
        return False

    self.booked_slots.add(slot)
    return True'''

class ConferenceRoom:

    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.booked_slots = set()

    def book_room(self, date, time):
        slot = (date, time)

        if slot in self.booked_slots:
            return False

        self.booked_slots.add(slot)
        return True


# Step 4 — Add Exception Handling #

'''so  here I will take the try/except block function'''

try:
    capacity = int(input("Enter room capacity: "))
except ValueError:
    print("Capacity must be a number")


 # Step 5 — Create TWO objects #

room1 = ConferenceRoom("Room A", 10)
room2 = ConferenceRoom("Room B", 20)

# book a slot in Room A:#
room1.book_room("2026-09-03", "10:00")

# check Room B:#

room2.book_room("2026-09-03", "10:00")

# final programme #
class ConferenceRoom:

    def __init__(self, room_name, capacity):
        self.room_name = room_name
        self.capacity = capacity
        self.booked_slots = set()

    def book_room(self, date, time):
        slot = (date, time)

        if slot in self.booked_slots:
            return False

        self.booked_slots.add(slot)
        return True


try:
    capacity1 = int(input("Enter Room A capacity: "))
    capacity2 = int(input("Enter Room B capacity: "))

    room1 = ConferenceRoom("Room A", capacity1)
    room2 = ConferenceRoom("Room B", capacity2)

    print(room1.book_room("2026-09-03", "10:00"))
    print(room1.book_room("2026-09-03", "10:00"))

    print(room2.book_room("2026-09-03", "10:00"))

except ValueError:
    print("Capacity must be a number")