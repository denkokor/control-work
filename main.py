import utils
from classes.basic_word import BasicWord
from classes.player import Player

PATH = "https://jsonkeeper.com/b/N99F"

print("Ввведите имя игрока")

user_input = input()
player = Player(user_input)

print(f"Привет, {player.get_name()}")

basic_word = utils.load_random_word(PATH)

print(f"Составьте {basic_word.number_of_sub_words()} слов из слова {basic_word.value.upper()}")
print("Слова должны быть не короче 3 букв")
print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"")
print("Поехали, ваше первое слово?")



while player.count_used_words() < basic_word.number_of_sub_words():

    print()

    user_input = input().strip().lower()


    if user_input in ["стоп","stop"]:
        print("Игра завершена")
        break

    if not basic_word.has_sub_word(user_input):
        print("Такого слова нет")
        continue

    if not player.has_newer_seen(user_input):
        print("Такое слово было")
        continue

    player.add_word(user_input)
    print("верно")

print("слова закончились, игра завершена!")
print(f"вы угадали {player.count_used_words()} слов!")