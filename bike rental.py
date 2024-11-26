class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def displaybikes(self):
        print("total available bike in stockyard = ",self.stock)
    def rentforbike(self,quantity):
        if quantity <= 0:
            print("enter valid number or greater than zero")
        elif quantity > self.stock:
            print("enter the less value ")
        else:
            print("rental price of bike is = ",quantity*100 )
            print("total bike availbale in stock",self.stock-quantity)

while True:
    obj = BikeShop(500)
    uc = int(input("""
    1.display bike in stock yard
    2.rent for bike
    3.exit
    =
    """))

    if uc == 1:
        obj.displaybikes()
    elif uc == 2:
        n=int(input("enter bike you want for on rent ="))
        obj.rentforbike(n)

    else:
        break