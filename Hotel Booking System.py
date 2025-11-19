#Base Class: Room
class Room:
    def __init__(self, room_number, base_price, is_available=True):
        self.room_number = room_number
        self.base_price = base_price
        self.__is_available = is_available

    def get_availability(self):
        return self.__is_available

    def set_availability(self, status):
        if not isinstance(status, bool):
            return "Status must be True or False"
        self.__is_available = status
        return f"Room {self.room_number} availability set to {self.__is_available}"

    def get_price(self):
        return self.base_price

    def info(self):
        status = "Available" if self.__is_available else "Not Available"
        return f"Room {self.room_number} | Price: {self.base_price} | Status: {status}"


#StandardRoom (inherits Room)
class StandardRoom(Room):
    def __init__(self, room_number, base_price, is_available, bed_type):
        super().__init__(room_number, base_price, is_available)
        self.bed_type = bed_type

    def get_price(self):
        # No change in price logic yet, but overridden for polymorphism
        return self.base_price

    def info(self):
        status = "Available" if self.get_availability() else "Not Available"
        return (
            f"Standard Room {self.room_number} | Price: {self.base_price} "
            f"| Bed Type: {self.bed_type} | Status: {status}"
        )


#DeluxeRoom (inherits Room)
class DeluxeRoom(Room):
    def __init__(self, room_number, base_price, is_available, has_sea_view, extra_charge):
        super().__init__(room_number, base_price, is_available)
        self.has_sea_view = has_sea_view
        self.extra_charge = extra_charge

    def get_price(self):
        return self.base_price + self.extra_charge

    def info(self):
        sea_view = "Yes" if self.has_sea_view else "No"
        status = "Available" if self.get_availability() else "Not Available"
        total_price = self.get_price()

        return (
            f"Deluxe Room {self.room_number} | Base Price: {self.base_price} "
            f"| Extra Charge: {self.extra_charge} | Total/Night: {total_price} "
            f"| Sea View: {sea_view} | Status: {status}"
        )


#Guest Class
class Guest:
    def __init__(self, name, phone, id_proof):
        self.name = name
        self.phone = phone
        self.id_proof = id_proof

    def info(self):
        return f"Guest: {self.name} | Phone: {self.phone} | ID: {self.id_proof}"


#Booking Class
class Booking:
    def __init__(self, guest, room, nights):
        self.guest = guest          # Guest object
        self.room = room            # Room object (Standard or Deluxe)
        self.nights = nights
        self.__total_amount = 0     # private

        # Mark room unavailable when booking is created
        self.room.set_availability(False)

    def calculate_bill(self):
        self.__total_amount = self.room.get_price() * self.nights
        return self.__total_amount

    def get_total(self):
        return self.__total_amount

    def booking_summary(self):
        # Make sure bill is calculated
        if self.__total_amount == 0:
            self.calculate_bill()

        # Determine room type name nicely
        room_type = self.room.__class__.__name__  # e.g., StandardRoom, DeluxeRoom

        summary = []
        summary.append(f"Guest: {self.guest.name}")
        summary.append(f"Room: {self.room.room_number} ({room_type})")
        summary.append(f"Nights: {self.nights}")
        summary.append(f"Amount: ₹{self.__total_amount}")
        return "\n".join(summary)


# Helper function: find first available room
def find_available_room(room_list):
    for room in room_list:
        if room.get_availability():
            return room
    return None


# ============================
# ============================

# Create mixed list of rooms (Standard + Deluxe)
rooms = [
    StandardRoom(101, 2000, True, "Queen"),
    DeluxeRoom(201, 3500, True, True, 500),
    StandardRoom(102, 1800, True, "Twin"),
    DeluxeRoom(202, 4000, True, False, 300),
]


print("=== ROOM POLYMORPHISM DEMO ===")
for r in rooms:
    print(r.info())
    print("Nightly price:", r.get_price())
    print("-" * 40)

# Create some guests
guest1 = Guest("Rishi", "9876543210", "AADHAR-1234")
guest2 = Guest("Neha", "9123456780", "AADHAR-5678")
guest3 = Guest("Asha", "9988776655", "AADHAR-9999")

guests = [guest1, guest2, guest3]

# List to store bookings
bookings = []

# Try to create bookings for 3 guests
print("\n=== CREATING BOOKINGS ===")
for guest in guests:
    room = find_available_room(rooms)
    if room is not None:
        booking = Booking(guest, room, nights=3)
        booking.calculate_bill()
        bookings.append(booking)
        print(f"Booking created for {guest.name} in Room {room.room_number}")
    else:
        print(f"No available room for {guest.name}")

# Print all booking summaries
print("\n=== ALL BOOKINGS SUMMARY ===")
for b in bookings:
    print(b.booking_summary())
    print("-" * 40)

# Show room availability after bookings
print("\n=== ROOM AVAILABILITY AFTER BOOKINGS ===")
for r in rooms:
    status = "Available" if r.get_availability() else "Occupied"
    print(f"Room {r.room_number}: {status}")
