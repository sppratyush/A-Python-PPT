#Track vehicle entry/exit, available spots, and compute parking fees.
class Vehicle:
    def __init__(self, license_plate, entry_time):
        self.license_plate = license_plate
        self.entry_time = entry_time
class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = {}
        self.parking_fee_per_hour = 5.0

    def vehicle_entry(self, license_plate, entry_time):
        if len(self.occupied_spots) >= self.total_spots:
            print("Parking lot is full. Cannot accommodate more vehicles.")
            return False
        if license_plate in self.occupied_spots:
            print("Vehicle with this license plate is already parked.")
            return False
        self.occupied_spots[license_plate] = Vehicle(license_plate, entry_time)
        print(f"Vehicle {license_plate} entered at {entry_time}.")
        return True

    def vehicle_exit(self, license_plate, exit_time):
        if license_plate not in self.occupied_spots:
            print("Vehicle with this license plate is not found in the parking lot.")
            return False
        vehicle = self.occupied_spots.pop(license_plate)
        parking_duration = (exit_time - vehicle.entry_time).total_seconds() / 3600  # Convert to hours
        fee = parking_duration * self.parking_fee_per_hour
        print(f"Vehicle {license_plate} exited at {exit_time}. Parking duration: {parking_duration:.2f} hours. Fee: ${fee:.2f}")
        return True

    def available_spots(self):
        return self.total_spots - len(self.occupied_spots)
    def display_status(self):
        print(f"Total spots: {self.total_spots}")
        print(f"Occupied spots: {len(self.occupied_spots)}")
        print(f"Available spots: {self.available_spots()}")
    