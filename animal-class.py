class Animals:


    def __init__(self, name, size, diet_type, legs):
        self.name=name
        self.size=size
        self.diet_type=diet_type
        self.legs=legs

    def eat(self):
        if self.diet_type=="carnivore":
            return self.name + ' is a ' + self.diet_type + ' and hence only eats meat'
        elif self.diet_type=="herbivore":
            return self.name + 'is a' + self.diet_type + 'and hence only eats plant species'
        elif self.diet_type=="omnivore":
            return self.name + 'is a' + self.diet_type + 'so it eats both plants and animals'

    def running_speed(self):
        if self.size=="large" or self.size=="medium":
            return self.name + 'should be a fast runner'
        elif self.size=="small":
            return self.name + 'is a slow runner'

class feline(Animals):

    def __init__(self, name, size, diet_type, legs, color, fur_pattern):
        Animals.__init__(self, name, size, diet_type, legs)
        self.color=color
        self.fur_pattern=fur_pattern

    def pet_worthy(self):
        if self.diet_type=='herbivore':
            return 'yes, a' + self.name + 'can be your pet'
        elif self.diet_type=='carnivore' and self.size=='large':
            return 'no, let' + self.name + 'live in the jungle'

    def looks(self):
        if self.fur_pattern=="spotted" or self.fur_pattern=='striped':
            return "that's a good looking animal"
        elif self.fur_pattern=="plain":
            return  self.name + "doesn't look that great"

class canine(Animals):

    def __init__(self, name, size, diet_type, legs, color, fur_pattern):
        Animals.__init__(self, name, size, diet_type, legs)
        self.color=color
        self.fur_pattern=fur_pattern

    def pet_worthy(self):
        if self.diet_type=='herbivore':
            return 'yes, a' + self.name + 'can be your pet'
        elif self.diet_type=='carnivore' and self.size=='large':
            return 'no, let' + self.name + 'live in the jungle'

    def looks(self):
        if self.fur_pattern=="spotted" or self.fur_pattern=='striped':
            return "that's a good looking animal"
        elif self.fur_pattern=="plain":
            return  self.name + "doesn't look that great"

class dog(canine):
    def __init__(self, name, size, diet_type, legs, color, fur_pattern, breed):
        canine.__init__(self, name, size, diet_type, legs, color, fur_pattern)
        self.breed=breed

    def attitude(self):
        if self.breed=='beagle' or self.breed=='pug':
            return "you've got a lazy dog"
        else:
            return "you've got an active dog"

class wolf(canine):
    def __init__(self, name, size, diet_type, legs, color, fur_pattern):
        canine.__init__(self, name, size, diet_type, legs, color, fur_pattern)

    def eat(self):
        return  'your animal is a wolf so it would eat red meat'

class hybrid_animal(dog,wolf):
    def __init__(self, name, size, diet_type, legs, color, fur_pattern):
        dog.__init__(self, name, size, diet_type, legs, color, fur_pattern)
        wolf.__init__(self, name, size, diet_type, legs, color, fur_pattern)

    def eat(self):
        return 'eats all nonveg stuff'

animal1=Animals('dog', 'small', 'carnivore',4)
animal2=canine('dog', 'small', 'carnivore', 4, 'brown', 'spotted')
animal3=wolf('wolf', 'small', 'carnivore', 4, 'brown', 'spotted')
animal4=dog('dog', 'small', 'carnivore', 4, 'brown', 'spotted', 'pug')
animal5=hybrid_animal('hybrid', 'small', 'carnivore', 4, 'brown', 'spotted')

print(animal1.eat())
print(animal5.eat())
print(animal2.eat())