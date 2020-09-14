# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#  Base class
class Vehicle:
    name = ""

# Vehicle Subclasses
class FlightVehicle(Vehicle):
    pass

class GroundVehicle(Vehicle):
    pass

# FlightVehicle Subclasses
class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

# GroundVehicle Sublcasses
class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass