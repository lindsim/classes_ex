# Add attributes for things like their name/color/shape/origin/seasons

# Add a method with the following signature:

# def get_price(qty):
#Determine price for this quantity of melons of this type.
#Return a float of the total price.
# 




class Melons(object):

    #SUPER FANCY way to check all of the species attributes in the subclasses
    #and then make it if you can
    #if not, i'll return an error message
    #didn't add it yet though
    def __init__(self):
         self.species

    def get_base(self):
        base = 5.00
        return base

class Watermelon(Melons):
    species = "watermelon"
    color = "green"
    imported = False
    shape = "natural"
    season = ['Fall', 'Summer']

    def get_price(self, qty):

        cost = super(Watermelon, self).get_base()  * qty
        if qty >= 3:
            cost = cost * .75
        return cost


class Cantaloupe(Melons):
    species = "canteloupe"
    color = "tan"
    imported = False
    shape = "natural"
    season = ['Spring', 'Summer']

    def get_price(self, qty):

        cost = super(Cantaloupe, self).get_base() * qty
        if qty >= 5:
            cost = cost * .5
        return cost

class Casaba(Melons):
    species = "casaba"
    color = "green"
    imported = True
    shape = "natural"
    season = ['Spring', 'Summer', 'Fall', 'Winter']

    def get_price(self, qty):

        cost =  (super(Casaba, self).get_base() + 1) * 1.5 * qty
        return cost


class Sharlyn(Melons):
    species = "sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    season = [ 'Summer']
    
    def get_price(self, qty):
        
        cost =  super(Sharlyn, self).get_base() * 1.5 * qty
        return cost


class SantaClaus(Melons):
    species = "santa claus"
    color = "green"
    imported = True
    shape = "natural"
    season = ['Winter', 'Spring']

    def get_price(self, qty):
        
        cost =  super(SantaClaus, self).get_base()  * 1.5 * qty
        return cost

class Christmas(Melons):
    species = "christmas"
    color = "green"
    imported = False
    shape = "natural"
    season = ['Winter']

    def get_price(self, qty):

        cost = super(Christmas, self).get_base()  * qty
        return cost


class HornedMelon(Melons):
    species = "horned melon"
    color = "yellow"
    imported = True
    shape = "natural"
    season = ['Summer']
    
    def get_price(self, qty):
        
        cost =  super(HornedMelon, self).get_base() * 1.5 * qty
        return cost


class Xigua(Melons):
    species = "xigua"
    color = "black"
    imported = True
    shape = "square"
    season = ['Summer']

    def get_price(self, qty):
#cost is the base cost times 1.5 for importing and times 2 for imported
        cost = super(Xigua, self).get_base()  * 1.5 * 2 * qty
        return cost


class Ogen(Melons):
    species = "ogen"
    color = "tan"
    imported = False
    shape = "natural"
    season = ['Spring', 'Summer']

    def get_price(self, qty):
        cost =  (super(Ogen, self).get_base()  + 1) * qty
        return cost


