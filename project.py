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
    user_list=[]     #user list nilam
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
            
            
    def get_users(self):
        return self.user_list
            
    def create_account(self):
        name=input("Enter your User name: ")
        password=input("Enter your Password: ")
        self.new_user=User(name,password)
        self.user_list.append(vars(self.new_user))
        
    def avaiable_buses(self):
        if len(self.total_bus_list)==0:
            print("No BUses Available\n")
        else :
            print('*'*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Bus Number : {bus['coach']}\t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time : {bus['departure']} \n From: \t{bus['from_destination']}\t\t To : \t{bus['to']}")   
                
                print("*"*50)   
                 
                 
# Create a single instance of the Phitron class
company = Phitron()

while True:
    print("1. Create an account\n2. Login to your account\n3. EXIT")
    
    user_input = int(input("Enter Your Choice: "))
    
    if user_input == 3:
        break
    elif user_input == 1:
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        company.create_account(username, password)
    elif user_input == 2:
        name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        
        flag = 0
        isAdmin = False
        
        if name == "admin" and password == "123":
            isAdmin = True
        if isAdmin is False:
            for user in company.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10} Welcome to BUS TICKET BOOKING SYSTEM")
                    print("1. Available Buses\n2. Show Bus Info\n3. Reservation\n4. EXIT")
                
                    a = int(input("Enter Your Choice: "))
                    if a == 4:
                        break
                    elif a == 1:
                        company.available_buses()
                    elif a == 2:
                        company.show_ticket()
                    elif a == 3:
                        company.reservation()
            else:
                print("No Username Found")
        else:
            while True:
                print(f"\n{' '*10} Welcome to BUS TICKET BOOKING SYSTEM")
                print("1. Add Bus\n2. Available Buses\n3. Show Bus Info\n4. Reservation\n5. EXIT")
                
                a = int(input("Enter Your Choice: "))
                
                if a == 5:
                    break
                elif a == 1:
                    company.add_bus()
                elif a == 2:
                    company.available_buses()
                elif a == 3:
                    company.show_ticket()

                    
                
            
            
            
        

# Create an instance of the Bus class to use it as a base class for Counter
# company = Phitron()
# company.add_bus()

# doremmon = Counter()
# doremmon.show_ticket()


# Global 
#     1.create An Account
#     2. Login to YOur Account
#     3.exit
      
    #   User
    #     1. Bus info
    #     2.Reserver/ticket booking
    #     3. avaible buses
    #     4.exit
    
#     Admin :
#         1.Add Bus
#         2.Available Buses
#         3.Can check bus info
#         4. Exit



                
                
                
            
        
        
    
        
        
        