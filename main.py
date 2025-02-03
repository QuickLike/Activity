from random import randint, choice
from time import sleep

from colorama import Fore
from playsound import playsound
from tqdm import tqdm

from cards import cards, get_card
from config import TYPES, TIME_IS_UP_SOUND, TIMER_SOUND, VICTORY_SOUND
from db_reset import reset_db

used_cards = set()


def init_commands():
    commands = {}
    while True:
        commands_count = input('Введите количество команд (от 2х):\t')
        try:
            commands_count = int(commands_count)
        except ValueError('Введите число!'):
            continue
        if commands_count < 2:
            print('Команд не может быть меньше двух!\n')
            continue
        for i in range(commands_count):
            while True:
                command_name = input(f'Введите название команды №{i + 1}\t')
                if command_name not in commands:
                    commands[command_name] = 0
                    break
                print(f'Команда "{command_name}" уже есть в игре.')
                sleep(2)
        return commands


def init_timer():
    while True:
        timer_time = input('Укажите время таймера в секундах (от 10 до 120):\t')
        try:
            timer_time = int(timer_time)
        except ValueError('Необходимо ввести число!'):
            continue
        if not (10 <= timer_time <= 120):
            print('Время таймера должно быть в диапазоне от 10 до 120 секунд.\n')
            continue
        return timer_time


def init_points():
    while True:
        points = input('Укажите количество очков для победы (от 3х до 100):\t')
        try:
            points = int(points)
        except ValueError('Необходимо ввести число!\n'):
            continue
        if not (3 <= points <= 100):
            print('Количество очков должно быть в диапазоне от 10 до 120 секунд.\n')
            continue
        return points


def roll_dice(mx: int):
    return randint(1, mx)


def timer(secs: int):
    for _ in tqdm(range(secs), desc='CTRL + C для остановки'):
        playsound(TIMER_SOUND)
        sleep(0.8)
    print('Время вышло!\n')
    playsound(TIME_IS_UP_SOUND)


def give_card(diff: int) -> tuple:
    while True:
        type_num = (roll_dice(6) - 1) // 2
        card = choice(cards[diff][type_num])
        if card not in used_cards:
            used_cards.add(card)
            return card, TYPES[type_num]


def start_guess(points: int, commands: dict, timer_time: int):
    while True:
        for command_name in commands:
            print('\n' * 20)
            print(f'Очередь команды "{command_name}"\n')
            print('\n' * 8)
            input('Нажмите Enter для раздачи карты\n\n')
            card_text, card_type, card_difficulty, is_red = get_card()
            # difficulty = randint(3, 5)
            # card = give_card(difficulty)
            # card_text = (Fore.RED if True in card[0] else Fore.RESET) + card[0][0]
            card_text = Fore.RED * is_red + card_text
            print('\n' * 20)
            print(card_text)
            print(Fore.RESET + f'Тип карты "{TYPES[card_type - 1]}".')
            print(f'Сложность карты: {card_difficulty}')
            print('\n' * 8)
            input('Нажмите Enter для запуска таймера.\n')
            print('\n' * 20)
            try:
                timer(timer_time)
            except KeyboardInterrupt:
                playsound(TIME_IS_UP_SOUND)
            print('\n' * 20)
            if input('Напишите 0 и нажмите Enter, если не угадали.\nЕсли угадали, просто нажмите Enter.\t') == '0':
                continue
            if is_red:
                while True:
                    win_command = input('Введите название угадавшей команды:\t')
                    if win_command not in commands:
                        print(f'Команды {win_command} нет в игре!\n')
                        continue
                    command_name = win_command
                    break
            print(f'Команда "{command_name}" заработала очки: {card_difficulty}\n\n')
            commands[command_name] += card_difficulty
            if commands[command_name] >= points:
                print('\n' * 8)
                print('Игра окончена!')
                print(f'Победа команды "{command_name}"!\n\n')
                print('Общий счет')
                for name, score in commands.items():
                    print(f'{name}: {score}')
                print('\n' * 8)
                playsound(VICTORY_SOUND)
                return


def main():
    reset_db()
    print('Добро пожаловать в игру "Activity"!\n')
    start_guess(init_points(), init_commands(), init_timer())


if __name__ == '__main__':
    main()
