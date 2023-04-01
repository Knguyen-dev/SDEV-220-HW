"""
Author: Kevin Nguyen
File name: Nguyen_M03_Case_Study.py
Program Description: Create a program that allows hte user to enter attributes for a car, then create a car object and display the attributes/information of that car.
Description of Variables used:

+ These variables represent the user's input for the respective attributes of the car or Automobile class
- inputCarYear
- inputCarMake
- inputCarModel
- inputNumDoors
- inputRoofType
- userCar

+ Variables in the class 
- vehicleType: Attribute that represents the type of vehicle, in this case, for class Automobile it'll be "car"
- carYear: The year the car was made
- carMake: The make of the car
- carModel: The model of the car
- numDoors: Number of doors the Automobile or car has, which can only be values 2 or 4
- roofType: The type of roof they have on the car, which is 'solid' or 'sun roof' 
"""

# Base class of 'Vehicle' that will be inherited from
class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
    
    def getVehicleType(self):
        return self.vehicleType

# Derived class of automobile that inherits from vehicle
class Automobile(Vehicle):
    def __init__(self, carYear, carMake, carModel, numDoors, roofType):
		# Use the base class's constructor to assign vehicleType attribute, then set all other attributes 
        super().__init__("Car")
        self._carYear = carYear
        self._carMake = carMake
        self._carModel = carModel
        # Number of doors and roof type are validated before we set the attributes to the user's input, if they're invalid these functions will raise an error
        self._numDoors = numDoors
        self._roofType = roofType
    
    # get functions that return the car's attributes for output
    def getYear(self):
        return self._carYear
    def getMake(self):
        return self._carMake
    def getModel(self):
        return self._carModel
    def getNumDoors(self):
        return self._numDoors
    def getRoofType(self):
        return self._roofType
    
def main():    
	# Prompt input for basic attributes of automobile
    inputCarYear = int(input("Enter the year the car was made: "))
    inputCarMake = input("Enter the make of the car: ")
    inputCarModel = input("Enter the model of the car: ")
    
    inputNumDoors = int(input("Enter the number of doors on the car (2 or 4 doors only): "))
    # keep looping if number of doors doesn't equal 2 or 4 to validate input
    while inputNumDoors != 2 and inputNumDoors != 4:
        inputNumDoors = int(input("Please enter 2 or 4 for the doors: "))
    
    inputRoofType = input("Enter the roof type of the car ('solid' or 'sun roof' only): ")
    # keeping looping if roofType doesn't equal a valid value
    while inputRoofType != "solid" and inputRoofType != "sun roof":
        inputNumDoors = input("Enter 'solid' or 'sun roof': ")

    # Create car instance
    userCar = Automobile(inputCarYear, inputCarMake, inputCarModel, inputNumDoors, inputRoofType)
    
    # display attributes of car instance
    print(f"Vehicle type: {userCar.getVehicleType()}")
    print(f"Year: {userCar.getYear()}")
    print(f"Make: {userCar.getMake()}")
    print(f"Model: {userCar.getModel()}")
    print(f"Number of doors: {userCar.getNumDoors()}")
    print(f"Type of roof: {userCar.getRoofType()}")
main()
	
	

		  