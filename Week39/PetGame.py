class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

class Owner:
    def __init__(self, name):
        self.name = name


def main():
    owners_name = input("Name of owner: ")
    pets_name = input("Name of pet: ")

    owner = Owner(owners_name)
    pet = Pet(pets_name)

    print(f"Pets name is {pet.name}")
    print(f"Owners name is {owner.name}")


main()