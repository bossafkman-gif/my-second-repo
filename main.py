from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Slime", 100, 2)

    print(hero)
    print(enemy)
    print(enemy2)
    print()

    while hero.is_alive() and enemy.is_alive():
        hero.attack(enemy)
        if enemy.is_alive():
            enemy.attack(hero)
        print(hero)
        print(enemy)
        print()

    if hero.is_alive():
        print(f"{hero.name} kill the {enemy.name}")
    else:
        print(f"{enemy.name} wins!")

    print('Next enemy Slime')

    while hero.is_alive() and enemy2.is_alive():
            hero.attack(enemy2)
            if enemy2.is_alive():
                enemy2.attack(hero)
            print(hero)
            print(enemy2)
            print()

    print("Battle over!")

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy2.name} wins!")

if __name__ == "__main__":
    main()
