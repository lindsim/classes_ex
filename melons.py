# Add attributes for things like their name/color/shape/origin/seasons

# Add a method with the following signature:

# def get_price(qty):
#Determine price for this quantity of melons of this type.
#Return a float of the total price.
# 

BASE_MELON_COST = 5.00

class Watermelon(object):
    species = "watermelon"
    color = "green"
    imported = False
    shape = "natural"
    season = ['Fall', 'Summer']

    def get_price(self, qty):

        cost =  BASE_MELON_COST * qty
        if qty >= 3:
            cost = cost * .75
        return cost


class Canteloupe(object):
    species = "canteloupe"
    color = "tan"
    imported = False
    shape = "natural"
    season = ['Spring', 'Summer']

    def get_price(self, qty):

        cost =  BASE_MELON_COST * qty
        if qty >= 5:
            cost = cost * .5
        return cost

class Casaba(object):
    species = "casaba"
    color = "green"
    imported = True
    shape = "natural"
    season = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):

        cost =  (BASE_MELON_COST + 1) * 1.5 * qty
        return cost


class Sharlyn(object):
    species = "sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    season = [ 'Summer']
    
    def get_price(self, qty):
        
        cost =  (BASE_MELON_COST) * 1.5 * qty
        return cost


class SantaClaus(object):
    species = "santa claus"
    color = "green"
    imported = True
    shape = "natural"
    season = ['Winter', 'Spring']

    def get_price(self, qty):
        
        cost =  (BASE_MELON_COST) * 1.5 * qty
        return cost

class Christmas(object):
    species = "christmas"
    color = "green"
    imported = False
    shape = "natural"
    season = ['Winter']

    def get_price(self, qty):

        cost = BASE_MELON_COST * qty
        return cost


class HornedMelon(object):
    species = "horned melon"
    color = "yellow"
    imported = True
    shape = "natural"
    season = ['Summer']
    
    def get_price(self, qty):
        
        cost =  (BASE_MELON_COST) * 1.5 * qty
        return cost


class Xigua(object):
    species = "xigua"
    color = "black"
    imported = True
    shape = "square"
    season = ['Summer']

    def get_price(self, qty):
#cost is the base cost times 1.5 for importing and times 2 for imported
        cost =  (BASE_MELON_COST) * 1.5 * 2 * qty
        return cost


class Ogen(object):
    species = "ogen"
    color = "tan"
    imported = False
    shape = "natural"
    season = ['Spring', 'Summer']

    def get_price(self, qty):
        cost =  (BASE_MELON_COST + 1) * qty
        return cost



# melons = [
#     ('Watermelon', 'green', False, 'natural', ['Fall', 'Summer']),
#     ('Cantaloupe', 'tan', False, 'natural', ['Spring', 'Summer']),
#     ('Casaba', 'green', True, 'natural', ['Spring', 'Summer', 'Fall', 'Winter']),
#     ('Sharlyn', 'tan', True, 'natural', ['Summer']),
#     ('Santa Claus', 'green', True, 'natural', ['Winter', 'Spring']),
#     ('Christmas', 'green', False, 'natural', ['Winter']),
#     ('Horned Melon', 'yellow', True, 'natural', ['Summer']),
#     ('Xigua', 'black', True, 'square', ['Summer']),
#     ('Ogen', 'tan', False, 'natural', ['Spring', 'Summer'])
# ]