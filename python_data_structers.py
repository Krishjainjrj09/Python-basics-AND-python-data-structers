# step-1: take a piece of data #

# I need to store multiple booked room slots.#

booked_slots = {
    ("2026-09-02", "10:00"),
    ("2026-09-02", "11:00"),
    ("2026-09-03", "10:00")
}



# Step 2: Ask the questions

'''1. Does order matter?

No

 I don't care whether the slots are stored as 10:00, 11:00, or 10:00 next day.

2. Do duplicates matter? 

No

 The same booking slot should not be stored multiple times.

3. Does it need a key?

 No.

 I don't need key-value pairs such as:

 Room A → 10:00 
 Room B → 11:00 

 4. Is membership important? 

 Yes.

 I mainly need to check: 

 "Is this requested date and time already booked?" '''


# Step 3: Pick the data structure #

'''Based on my answers:

Order →  Not important
Duplicates →  Not required
Key → Not required
Membership →  Important

Therefore, I choose a:

Set'''

booked_slots = {
    ("2026-09-02", "10:00"),
    ("2026-09-02", "11:00"),
    ("2026-09-03", "10:00")
}

# Step 4: Perform one real operation #

requested_slot = ("2026-09-02", "10:50")

if requested_slot in booked_slots:
    print("Room is already booked")
else:
    print("Room is available")


