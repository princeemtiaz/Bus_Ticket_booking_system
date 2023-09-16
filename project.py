#bus ticket Booking system

#admin
# 1.Add a new bus 

# 2.Check Avaible buses

# 3.Can check bus info

#user
# 1. check avaible buses
# 2. can check bus info
# 3. can reverse seat
class User:
    def __init__(self,username,password):
        self.username=username
        self.password=password

class Bus:
    def __init__(self, coach, driver, arrival, departure, from_destination, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_destination = from_destination
        self.to = to
        self.seat = ["Empty" for _ in range(20)]  # Initialize seats with "Empty"

# b = Bus(2, "rahim", "12PM", "12:30PM", "dhaka", "Natore")
# print(b)

class Phitron:
    total_bus = 5
    total_bus_list = []

    def add_bus(self):
        bus_no = int(input("Enter Bus No: "))
        
        flag = True  # Initialize flag as True

        for bus in self.total_bus_list:
            if bus_no == bus.coach:
                print('Bus is Already Added')
                flag = False  # Set flag to False if bus is already added
                break

        if flag:
            bus_driver = input("Enter bus Driver Name: ")
            bus_arrival = input("Bus Arrival Time: ")
            bus_departure = input("Enter Bus departure time: ")
            from_destination = input("Enter Bus start From: ")
            bus_to = input("Enter Bus Destination: ")
            new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, from_destination, bus_to)
            self.total_bus_list.append(new_bus)
            print("\nBus Added Successfully")

# company=Phitron()
# company.add_bus()
            
class Counter(Phitron):
    def reservation(self):
        try:
            bus_no = int(input("Enter Bus No: "))
        except ValueError:
            print("Invalid input. Please enter a valid Bus No (an integer).")
            return  # Exit the method if the input is not a valid integer

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger = input("Enter Your Name: ")
                seat_no = int(input("Enter Seat No: "))

                if seat_no > 20:
                    print("No Seat Available....!!! ")

                elif w['seat'][seat_no - 1] != "Empty":
                    print("Seat Already Booked....!!! ")

                else:
                    w['seat'][seat_no - 1] = passenger
            else:
                print("No Bus Available...!!!")
        for bus in self.total_bus_list:
            print(bus['seat'])
    
    def show_ticket(self):
        bus_no = int(input("Enter Bus Number: "))

        for w in self.total_bus_list:
            if bus_no == w.coach:  # Use dot notation to access class attributes
                print("*" * 50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f" Bus Number: {bus_no}\t\t\t Driver: {w.driver}")
                print(f"Arrival: {w.arrival}\t\t\tDeparture Time: {w.departure}\nFrom: {w.from_destination}\t\t\tto: {w.to}")

                
                print()

        a = 1
        for i in range(5):
            for j in range(2):
               print(f'{a}.{w.seat[a-1]}', end="\t")
               a += 1
            for j in range(2):
                print(f"{a}. {w.seat[a-1]}", end="\t")
                a += 1
            print()  # Add a newline after each row
            print("*" * 50)

# Create an instance of the Bus class to use it as a base class for Counter
company = Phitron()
company.add_bus()

doremmon = Counter()
doremmon.show_ticket()




                
                
                
            
        
        
    
        
        
        