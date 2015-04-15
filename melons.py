"""This file should have our melon-type classes in it."""

class Melon(object):
    name = None
    base_price = float(5)

    def get_price(self, qty):
        total = self.base_price * qty
        return total

w = Melon()
w.name = "Watermelon"
w.base_price = float(6)

w.get_price(10)

# class WatermelonOrder(object):
#     species = "Watermelon"
#     color = "green"
#     imported = False
#     shape = 'natural'
#     seasons = ['Fall', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         if qty >= 3:
#             total = self.base_price()*.75*float(qty) 
#         else:
#             total = float(5)*float(qty) 

#         return total


# class CantaloupeOrder(object):
#     species = "Cantaloupe"
#     color = "tan"
#     imported = False
#     shape = 'natural'
#     seasons = ['Spring', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""
        
#         if qty >= 5:
#             total = float(5)*.50*float(qty) 
#         else:
#             total = float(5)*float(qty) 

#         return total


# class CasabaOrder(object):
#     species = "Casaba"
#     color = "green"
#     imported = True
#     shape = 'natural'
#     seasons = ['Spring', 'Summer', 'Fall', 'Winter']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(6)*float(qty)*1.5

#         return total

    
# class SharlynOrder(object):
#     species = "Sharlyn"
#     color = "tan"
#     imported = True
#     shape = 'natural'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(5)*float(qty)*1.5

#         return total

    
# class SantaClausOrder(object):
#     species = "Santa Claus"
#     color = "green"
#     imported = True
#     shape = 'natural'
#     seasons = ['Winter', 'Spring']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(5)*float(qty)*1.5

#         return total

    
# class ChristmasOrder(object):
#     species = "Christmas"
#     color = "green"
#     imported = False
#     shape = 'natural'
#     seasons = ['Winter', 'Spring']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(5)*float(qty)                                 

#         return total

    
# class HornedMelonOrder(object):
#     species = "Horned Melon"
#     color = "yellow"
#     imported = True
#     shape = 'natural'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(5)*float(qty)*1.5

#         return total

    
# class XiguaOrder(object):
#     species = "Xigua"
#     color = "black"
#     imported = True
#     shape = 'square'
#     seasons = ['Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(5)*float(qty)*1.5*float(2)    

#         return total

    
# class OgenOrder(object):
#     species = "Ogen"
#     color = "tan"
#     imported = False
#     shape = 'natural'
#     seasons = ['Spring', 'Summer']

#     def get_price(self, qty):
#         """Calculate price, given a number of melons ordered."""

#         total = float(6)*float(qty)  

#         return total
