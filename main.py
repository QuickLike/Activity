from random import randint, choice
from time import sleep

from colorama import Fore
from playsound import playsound
from tqdm import tqdm

from cards import cards, types

used_cards = set()


def init_commands():
    commands = {}
    while True:
        commands_count = input('Введите количество команд (от 2х):\n')
        try:
            commands_count = int(commands_count)
        except ValueError('Введите число!'):
            continue
        if commands_count < 2:
            print('Команд не может быть меньше двух!')
            continue
        for i in range(commands_count):
            commands[input(f'Введите название команды №{i + 1}\n')] = 0
        return commands


def init_timer():
    while True:
        timer_time = input('Укажите время таймера в секундах (от 10 до 120):\n')
        try:
            timer_time = int(timer_time)
        except ValueError('Необходимо ввести число!'):
            continue
        if not (10 <= timer_time <= 120):
            print('Время таймера должно быть в диапазоне от 10 до 120 секунд.')
            continue
        return timer_time


def init_points():
    while True:
        points = input('Укажите количество очков для победы (от 3х до 100):\n')
        try:
            points = int(points)
        except ValueError('Необходимо ввести число!'):
            continue
        if not (3 <= points <= 100):
            print('Количество очков должно быть в диапазоне от 10 до 120 секунд.')
            continue
        return points


def roll_dice(mx: int):
    return randint(1, mx)


def timer(secs: int):
    for _ in tqdm(range(secs), desc='CTRL + C для остановки'):
        playsound(r'D:\Python\Activity\sounds\beep.wav')
        sleep(0.8)
    print('Время вышло!\n')
    playsound(r'D:\Python\Activity\sounds\time_is_up.wav')


def give_card(diff: int) -> tuple:
    while True:
        type_num = (roll_dice(6) - 1) // 2
        card = choice(cards[diff][type_num])
        if card not in used_cards:
            used_cards.add(card)
            return card, types[type_num]


def start_guess(points: int, commands: dict, timer_time: int):
    while True:
        for command_name in commands:
            print(f'Очередь команды "{command_name}"')
            input('Нажмите Enter для раздачи карты\n')
            difficulty = randint(3, 5)
            card = give_card(difficulty)
            card_text = (Fore.RED if True in card[0] else Fore.RESET) + card[0][0]
            print(card_text)
            print(Fore.RESET + f'Тип карты "{card[1]}".')
            print(f'Сложность карты: {difficulty}')
            print()
            input('Нажмите Enter для запуска таймера.\n')
            try:
                timer(timer_time)
            except KeyboardInterrupt:
                playsound(r'D:\Python\Activity\sounds\time_is_up.wav')
            if input('Напишите 0 и нажмите Enter, если не угадали.\nЕсли угадали, просто нажмите Enter.\n') == '0':
                continue
            if True in card[0]:
                while True:
                    win_command = input('Введите название угадавшей команды:\n')
                    if win_command not in commands:
                        print(f'Команды {win_command} нет в игре!\n')
                        continue
                    command_name = win_command
                    break
            print(f'Команда "{command_name}" заработала очки: {difficulty}\n')
            commands[command_name] += difficulty
            if commands[command_name] >= points:
                print('Игра окончена!')
                print(f'Победа команды "{command_name}"!\n')
                sleep(3)
                print('Общий счет')
                for name, score in commands.items():
                    print(f'{name}: {score}')
                sleep(5)
                return


def main():
    print('Добро пожаловать в игру "Activity"!\n')
    start_guess(init_points(), init_commands(), init_timer())


if __name__ == '__main__':
    main()
