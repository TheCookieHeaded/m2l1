from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1351)
        self.img = self.get_img
        self.name = self.get_name
        self.hp=randint(400,600)
        self.power=randint(30,60)
        Pokemon.pokemons[pokemon_trainer] = self



    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['sprites']['other']['showdown']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/showdown/15.gif"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"""
Имя твоего покемона: {self.name},
Очки здоровья: {self.hp},
Сила удара: {self.power}.
        """

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chancewiz = randint(1,5)
            if chancewiz == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


class Wizard(Pokemon):
    pass
class Fighter(Pokemon):
    def attack(self, enemy):
        def attack(self, enemy):
            ultrapower = randint(5,15)
            self.power += ultrapower
            result = super().attack(enemy)
            self.power -= ultrapower
            return result + f"\nБоец применил супер-атаку силой:{self.ultrapower}!!!"

#if __name__ == '__main__':
    #wizard = Wizard("username1")
    #fighter = Fighter("username2")
    #print(wizard.info())
    #print()
    #print(fighter.info())
    #print()
    #print(fighter.attack(wizard))