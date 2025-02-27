import random

class HospitalDeliveryRobot:
    def __init__(self):
        self.location = "Medicine Storage"
        self.goal = "Deliver medicines correctly"
        self.medicine_picked = None

    def move_to(self, location):
        self.location = location
        print(f"Robot moved to {location}.")

    def pick_up_medicine(self, medicine):
        self.medicine_picked = medicine
        print(f"Picked up {medicine} from Medicine Storage.")

    def scan_patient_id(self, patient):
        print(f"Scanning ID for Patient {patient}...")
        if random.choice([True, False]):  # Simulating a scan success/failure
            print(f"Patient {patient} ID verified.")
            return True
        else:
            print(f"Patient {patient} ID verification failed! Alerting staff.")
            return False

    def deliver_medicine(self, patient, medicine):
        if self.medicine_picked == medicine:
            print(f"Delivering {medicine} to Patient {patient}...")
            self.medicine_picked = None
            print(f"Medicine {medicine} delivered to Patient {patient} successfully.")

    def alert_staff(self, issue):
        print(f"ALERT: {issue} Staff assistance required!")

class HospitalEnvironment:
    def __init__(self):
        self.patient_schedules = {
            "Room 101": {"patient": "Alice", "medicine": "Painkiller"},
            "Room 102": {"patient": "Bob", "medicine": "Antibiotic"},
            "Room 103": {"patient": "Charlie", "medicine": "Vitamin"},
        }
        self.nurse_station = "Nurse Station"
        self.medicine_storage = "Medicine Storage"

def run_hospital_robot(robot, environment):
    print("\n--- Hospital Delivery Robot Activated ---\n")
    
    for room, details in environment.patient_schedules.items():
        patient = details["patient"]
        medicine = details["medicine"]

        # Step 1: Move to Medicine Storage and Pick Up Medicine
        robot.move_to(environment.medicine_storage)
        robot.pick_up_medicine(medicine)

        # Step 2: Move to Patient Room
        robot.move_to(room)

        # Step 3: Scan Patient ID
        if robot.scan_patient_id(patient):
            # Step 4: Deliver Medicine
            robot.deliver_medicine(patient, medicine)
        else:
            # If ID verification fails, alert staff
            robot.alert_staff(f"Patient {patient} in {room}")

    print("\n--- All Scheduled Deliveries Completed ---\n")


hospital_robot = HospitalDeliveryRobot()
hospital_environment = HospitalEnvironment()
run_hospital_robot(hospital_robot, hospital_environment)
