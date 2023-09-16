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
    total_bus=5
    total_bus_list=[]
    
    flag=1
    def add_bus(self):
        bus_no=int(input("Enter Bus No: "))
        
        for w in self.total_bus_list:
            if bus_no ==w['coach'] :
                print('Bus is Alreay Added ')
                flag=0
                break
            
        
        if flag :
            bus_driver=input("Enter bus Driver Name : ")
            bus_arrival=input("Bus Arraival Time: ")
            bus_departure=input("Enter Bus departure time: ")
            from_destination=input("Enter Bus start From: ")
            bus_to=input("Enter Bus Destination : ")
            self.new_bus=Bus(bus_no,bus_driver,bus_arrival,bus_departure,from_destination,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\n Bus Added Successfully ")
            
            
        
        
        