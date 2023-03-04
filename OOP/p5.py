class Train:

    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats 
        
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats availabel in train are {self.seats}")
    
    def fareInfo(self):
        print(f"The fare of the ticket is: Rs {self.fare}")
    
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat is {self.seats}")
            self.seats = self.seats-1
        else:
            print("No seats available")

kuber = Train("Kuber Express",100,2)
kuber.getStatus()
kuber.fareInfo()
kuber.bookTicket()
kuber.getStatus()
kuber.bookTicket()
kuber.bookTicket()
