import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health

    def attack(self, enemy):
        damage = random.randint(15, 25)
        enemy.health -= damage
        print(f"{self.name} attacked {enemy.name} for {damage} damage!")

    def heal(self):
        heal = random.randint(5, 10)
        self.health += min(self.max_health, self.max_health - heal)
        print(f"{self.name} healed {heal} HP")

    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name="Goblin", health=60):
        self.name = name
        self.health = health

    def attack(self, hero):
        damage = random.randint(5, 10)
        hero.health -= damage
        print(f"{self.name} attacked {hero.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

def show_title():
    print("####################################")
    print("          HERO'S STAND")
    print("####################################")
    print("   A small Python adventure game\n")

# def clear_screen():
#    print("\033[2J\033[H", end="", flush=True)

def show_status(hero, enemy):
    print("       YOU ARE UNDER ATTACK!")
    print(f"-----------------------------------")
    print(f"          HEALTH STATUS")
    print(f"{hero.name}: {hero.health}/{hero.max_health} HP   |   {enemy.name}: {enemy.health} HP")
    print(f"-----------------------------------")

def game_play():
    hero = Hero(input("Name of hero: ").strip() or "Hero")
    frodo = Hero(input("Name of hero: ").strip() or "Frodo")
    enemy = Enemy(input("Name of enemy: ").strip() or "Lex")
    enemy2 = Enemy(input("Name of enemy: ").strip() or "Grok")

    print(f"\nA {enemy.name} ambushes {hero.name}!")
    enemy.attack(hero)

    input("Press any key to continue...")

    rounds = 0

    while hero.is_alive() and enemy.is_alive():
        show_title()
        show_status(hero, enemy)
        rounds += 1
        print(f"What do you want to do in round {rounds}?")
        print("\n1. Attack")
        print("2. Heal")
        choice = input("Your choice: ").strip()
        if choice == "1":
            hero.attack(enemy)
        elif choice == "2":
            hero.heal()
        else:
            print("Please choose a valid option!")
            continue

        if enemy.is_alive():
            grok.attack(enemy)

        input("Press any key to continue...")

    if hero.is_alive():
        print(f"\nVIKTORY! {hero.name} defeats the {enemy.name}")
    else:
        print(f"\nDEFEAT! {enemy.name} defeats {hero.name}")

def main():
    show_title()
    print("1. Start game\n")
    print("2. Exit game\n")

    choise = input("Your choice: ").strip()
    if choise == "1":
        while True:
            game_play()

            print("\n1. Play again")
            print("2. Main menu")
            print("3. Exit")

            next_choice = input("Your choice: ").strip()

            if next_choice == "1":
                continue
            elif next_choice == "2":
                break
            elif next_choice == "3":
                print("\nThanks for playing!")
                return
            else:
                print("Please choose 1, 2 or 3")
                input("Press Enter to continue...")
    else:
        return


main()