#
# CS1010S --- Programming Methodology
#
# Mission 13 Template
#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#                                                                               #
# PASTE YOUR MISSION 12 CODE HERE                                               #
#                                                                               #
#################################################################################
class Weapon(Thing):
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg

    def min_damage(self):
        return self.min_dmg

    def max_damage(self):
        return self.max_dmg

    def damage(self):
        return random.randint(self.min_dmg, self.max_dmg)


class Ammo(Thing):
    def __init__(self, name, weapon, quantity):
        super().__init__(name)
        self.weapon = weapon
        self.quantity = quantity
        
    def get_quantity(self):
        return self.quantity

    def weapon_type(self):
        return self.weapon.name

    def remove_all(self):
        self.quantity = 0

class RangedWeapon(Weapon):

    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0

    def shots_left(self):
        return self.shots

    def load(self,ammo):
        if ammo.weapon_type() == super().get_name():
            self.shots += ammo.get_quantity()
            ammo.remove_all()
            
    def damage(self):
        if self.shots_left() == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()


class Food(Thing):
    def __init__(self, name, food_value):
        super().__init__(name)
        self.food_value = food_value

    def get_food_value(self):
        return self.food_value


class Medicine(Food):
    def __init__(self, name, food_value, medicine_value):
        super().__init__(name, food_value)
        self.medicine_value = medicine_value

    def get_medicine_value(self):
        return self.medicine_value

class Animal(LivingThing):
    def __init__(self, name, health, food_value, threshold = random.randint(0,4)):
        super().__init__(name, health, threshold)
        self.food_value = food_value

    def get_food_value(self):
        return Food.get_food_value(self)
        
    def go_to_heaven(self):
        super().go_to_heaven()
        new = Food(super().get_name() + "meat", self.get_food_value())
        BASE.add_object(new)








#################################################################################
#                                                                               #
# MISSION 13                                                                    #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


#############
##  Task 1 ##
#############

class Tribute(Person):

    ############
    #  Task 1a #
    ############
    def __init__(self, name, health):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1)
        self.hunger = 0

    ############
    #  Task 1b #
    ############
    def get_hunger(self):
        return self.hunger

    ############
    #  Task 1c #
    ############
    def add_hunger(self, hunger):
        self.hunger += hunger
        if self.get_hunger() >= 100:
            return super().go_to_heaven()

    ############
    #  Task 1d #
    ############
    def reduce_hunger(self, hunger):
        self.hunger -= hunger
        if self.get_hunger() < 0:
            self.hunger = 0

    #############
    ##  Task 2 ##
    #############
    def eat(self, food):
        if food in self.inventory:
            if isinstance(food, Food) == True:
                reduce_amt = food.get_food_value()
                self.reduce_hunger(reduce_amt)
                super().remove_item(food)
            if isinstance(food, Medicine)== True:
                self.health += Medicine.get_medicine_value(food)
                super().remove_item(food)
        if self.health > 100:
            self.health = 100

    ############
    #  Task 3a #
    ############
    def get_weapons(self):
        inv_list = super().get_inventory()
        weapons = ()
        for i in inv_list:
            if isinstance(i, Weapon) == True:
                weapons += (i,)
            else:
                continue
        return weapons
        
    ############
    #  Task 3b #
    ############
    def get_food(self):
        inv_list = super().get_inventory()
        foods = ()
        for i in inv_list:
            if isinstance(i, Food) == True:
                foods += (i,)
            else:
                continue
        return foods

    ############
    #  Task 3c #
    ############
    def get_medicine(self):
        inv_list = super().get_inventory()
        meds = ()
        for i in inv_list:
            if isinstance(i, Medicine) == True:
                meds += (i,)
            else:
                continue
        return meds

    #############
    ##  Task 4 ##
    #############
    def attack(self, living_thing, weapon):
        if weapon in self.inventory:
            damage_dealt = weapon.damage()
            living_thing.reduce_health(damage_dealt)
        if living_thing.get_health() <= 0:
            self.inventory.append("living_thing.name" + "meat")

#############
##  Task 5 ##
#############
# You can either draw it here; or draw it on a piece of paper,
# then take a picture and upload it.
# Please ensure that your name appears somewhere in your image.




################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
#test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
# test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
#test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

# Uncomment to test task 4
test_task4()
