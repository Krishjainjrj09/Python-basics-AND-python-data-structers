# step-1 Pick a small rull From previous conditions #

#1. View Room Availability #

# Rule: Check whether a requested room date/time is already booked.#

'''def is_room_available(booked_slots, requested_date, requested_time):

    if requested_date == "" or requested_time == "":
        raise ValueError("Date and time are required")

    requested_slot = (requested_date, requested_time)

    if requested_slot in booked_slots:
        return False
    else:
        return True'''




def is_room_available(booked_slots, requested_date, requested_time): #Creating a def function
    """Returns True if the requested room slot is available.""" # write doc string explain with return value
    
    if requested_date == "" or requested_time == "": #logic #
        raise ValueError("Date and time are required") #logic #

    return (requested_date, requested_time) not in booked_slots #logic #
