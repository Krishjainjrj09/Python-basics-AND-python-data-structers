from room_booking import is_room_available
import pytest


# call with a boundary value #
booked_slots = {
    ("2026-09-02", "10:00")
}

result = is_room_available(
    booked_slots,
    "2026-09-02",
    "9:00"
)

print(result)