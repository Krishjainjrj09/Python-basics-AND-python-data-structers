# Day 6–11 Exercises – Testing & Python Data Structures

## Overview

This repository contains the exercises and documentation completed during Day 6–11 training.

The exercises cover:

1. Python Data Structures
2. Regression Testing
3. End-to-End (E2E) Testing

The examples are based on the **Conference Room Booking System** use case.

---

# 1. Python Data Structures

## Objective

The objective of this exercise is to understand how to select the appropriate Python data structure based on the requirements of the problem rather than choosing one based on habit.

## Step 1: Take a Piece of Data

From the Conference Room Booking System, I used booked room slots containing a date and time.

```python
booked_slots = {
    ("2026-09-02", "10:00"),
    ("2026-09-02", "11:00"),
    ("2026-09-03", "10:00")
}
```

Each item represents a booked room slot.

## Step 2: Analyze the Requirements

I asked the following questions:

* Does order matter? **No**
* Do duplicates matter? **No**
* Does it need a key? **No**
* Is membership checking important? **Yes**

The main requirement is to check whether a requested date and time is already booked.

## Step 3: Choose the Data Structure

Based on the requirements, I selected a **Set**.

A set is appropriate because:

* Order is not important.
* Duplicate values are not required.
* A key-value relationship is not required.
* Membership checking is important.

## Step 4: Perform a Real Operation

```python
requested_slot = ("2026-09-02", "10:00")

if requested_slot in booked_slots:
    print("Room is already booked")
else:
    print("Room is available")
```

### Output

```text
Room is already booked
```

## Step 5: Why Set?

I chose a set because the order of booked slots does not matter, duplicate slots are not required, and the main operation is checking whether a particular slot exists.

Therefore, a **set** is the appropriate container for this use case.

---

# 2. Regression Testing

## Objective

Regression testing is performed to make sure that existing functionality continues to work correctly after making changes to the application.

For the Conference Room Booking System, regression testing helps verify that changes to one functionality do not break previously working functionality.

## Example

Suppose a new feature is added to the booking system.

For example:

* A new validation is added to the booking process.
* The room availability functionality already worked correctly.

After making the change, we should test the existing room availability functionality again.

### Existing functionality

```text
Check whether a room is available for a particular date and time.
```

### Regression test

```text
Given a slot is already booked
When the user checks the same date and time
Then the system should return "Room is not available"
```

## Why Regression Testing Matters

Regression testing helps ensure that:

* Existing features continue to work.
* New changes do not introduce unexpected problems.
* Previously fixed bugs do not come back.
* The overall application remains stable after changes.

---

# 3. End-to-End (E2E) Testing

## Objective

End-to-End testing verifies the complete application flow from the user's perspective.

Instead of testing only one function, E2E testing checks whether the complete workflow works correctly.

## Conference Room Booking Example

A complete booking flow can be:

```text
User
  ↓
View Room Availability
  ↓
Select Date and Time
  ↓
Check Availability
  ↓
Book Conference Room
  ↓
Booking Confirmation
```

## Example E2E Scenario

### Test Case: Successfully Book a Room

**Given:** A room is available for the requested date and time.

**When:**

1. The user views room availability.
2. The user selects a date and time.
3. The system confirms that the room is available.
4. The user books the room.

**Then:**

* The booking should be created successfully.
* The selected slot should become unavailable.
* The user should receive a booking confirmation.

## Why E2E Testing Matters

E2E testing helps verify that:

* Different components work together correctly.
* The complete user workflow works as expected.
* Data flows correctly through the application.
* The application behaves correctly from the user's perspective.

---

# 4. Difference Between Regression and E2E Testing

| Regression Testing                                                | End-to-End Testing                                        |
| ----------------------------------------------------------------- | --------------------------------------------------------- |
| Checks that existing functionality still works after changes      | Checks the complete application workflow                  |
| Can test individual features or multiple existing features        | Tests the system from start to finish                     |
| Focuses on preventing new changes from breaking old functionality | Focuses on validating the complete user journey           |
| Example: Check room availability after a code change              | Example: View availability → Book room → Get confirmation |

---

# 5. Key Learnings

Through these exercises, I learned:

* How to select Python data structures based on requirements.
* How a `set` can be useful for membership checking.
* The purpose of regression testing.
* The importance of checking existing functionality after changes.
* How End-to-End testing validates a complete user workflow.
* The difference between testing an individual functionality and testing a complete application flow.

## Conclusion

These exercises helped me understand both **data structure selection** and **software testing concepts** using a practical Conference Room Booking System.

The main takeaway is to choose the right data structure and testing approach based on the actual requirements of the application.
