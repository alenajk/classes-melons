"""This file should have our melon-type classes in it."""

class Melon(object):
    # name = None
    # color = None
    # imported = None
    # shape = None
    # seasons = None

    def __init__(self, name=None, color=None, imported=None, shape="natural",
    seasons=None, base_price = float(5)):
        self.name = name
        self.color = color
        self.imported = imported
        self.shape = shape
        self.seasons = seasons
        self.base_price = base_price


    def get_price(self, qty):
        total = self.base_price * qty
        return total

class Watermelon(Melon):
    
    def __init__(self):
        return super(Watermelon, self).__init__(name ="Watermelon",
        color = "green", imported = False,
        seasons = ["Fall", "Summer"])
    
    def get_price(self, qty):

        if qty >= 3:
            total = self.base_price*float(qty)*.75
        else:
            total = self.base_price * float(qty)
        
        return total


class Cantaloupe(Melon):
    
    def __init__(self):
        return super(Cantaloupe, self).__init__(name ="Cantaloupe",
        color = "tan", imported = False,
        seasons = ["Summer", "Spring"])
    
    def get_price(self, qty):

        if qty >= 5:
            total = self.base_price*float(qty)*.50
        else:
            total = self.base_price * float(qty)
        
        return total


class Casaba(Melon):
    
    def __init__(self):
        return super(Casaba, self).__init__(name ="Casaba",
        color = "green", imported = True,
        seasons = ["Spring", "Summer", "Fall", "Winter"])
    
    def get_price(self, qty):

        total = (self.base_price + 1) * 1.5 *float(qty)
   
        return total


class Sharlyn(Melon):
    
    def __init__(self):
        return super(Sharlyn, self).__init__(name ="Sharlyn",
        color = "tan", imported = True,
        seasons = ["Summer"])
       
    def get_price(self, qty):
    
        total = self.base_price * 1.5 *float(qty)
   
        return total


class SantaClaus(Melon):
    
    def __init__(self):
        return super(SantaClaus, self).__init__(name ="Santa Claus",
        color = "green", imported = True,
        seasons = ["Winter", "Spring"])
    
    def get_price(self, qty):

        total = self.base_price * 1.5 *float(qty)
   
        return total

class ChristmasMelon(Melon):

    def __init__(self):
        return super(ChristmasMelon, self).__init__(name ="Christmas Melon",
        color = "green", imported = False,
        seasons = ["Winter", "Spring"])

    
class HornedMelon(Melon):

    def __init__(self):
        return super(HornedMelon, self).__init__(name ="Horned Melon",
        color = "yellow", imported = True,
        seasons = ["Summer"])
    
    def get_price(self, qty):

        total = self.base_price * 1.5 *float(qty)
   
        return total
    
class Xigua(Melon):

    def __init__(self):
        return super(Xigua, self).__init__(name ="Xigua",
        color = "black", imported = True,
        seasons = ["Summer"], shape = "square")
    
    def get_price(self, qty):

        total = self.base_price * 1.5 * float(2) *float(qty)
   
        return total
 
class Ogen(Melon):

    def __init__(self):
        return super(Ogen, self).__init__(name ="Ogen",
        color = "tan", imported = False,
        seasons = ["Spring", "Summer"])
    
    def get_price(self, qty):

        total = (self.base_price + 1) * float(qty)
   
        return total