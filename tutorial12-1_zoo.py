import random  # Importing random to generate random values

# Define the base class "Animal"
class Animal:
    def __init__(self, species):
        # Initialize the attributes for species and sound
        self.species = species

    # Method to display the details of the animal
    def show_details(self):
        return f"Species: {self.species}"

# Define the subclass "Bird", which inherits from "Animal"
class Bird(Animal):
    def __init__(self, species, can_fly):
        # Initialize the attributes inherited from Animal
        super().__init__(species)
        # Add a new attribute that's specific to birds
        self.can_fly = can_fly

    # Method to show if the bird can fly
    def show_flight_ability(self):
        return f"Can fly: {self.can_fly}"

# Create a list to hold animal objects
zoo = []

# Generate some random animals
for _ in range(5):  # Create 5 objects for demonstration
    species  = random.choice(["Parrot ", "Penguin", "Eagle  "])  # Randomly pick a species
    can_fly  = species != "Penguin"    # Penguins can't fly, others can
    new_bird = Bird(species, can_fly)  # Create a new Bird object
    zoo.append(new_bird)               # Add it to the zoo

# Display the details of all the animals in the zoo
for bird in zoo:
    print(bird.show_details(), end="\t")    # Show species and sound
    print(bird.show_flight_ability())       # Show if it can fly
