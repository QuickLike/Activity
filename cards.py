import sqlite3
from random import choice

from config import DB_NAME


def get_card():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        try:
            card = choice(
                cur.execute('SELECT id, text, type, difficulty, is_red FROM cards WHERE is_taken = 0').fetchall()
            )
        except IndexError:
            cur.execute('UPDATE cards SET is_taken = 0 WHERE is_taken = 1')
            card = choice(
                cur.execute('SELECT id, text, type, difficulty, is_red FROM cards WHERE is_taken = 0').fetchall()
            )
        cur.execute('UPDATE cards SET is_taken = 1 WHERE id = ?', (card[0], ))
        conn.commit()
        return card[1:]


#  Ключи словаря - сложность. Значения - кортежи, где [0] - рисунок, [1] - говорение, [2] - жесты.
#  Объекты загадок - кортежи, где [0] - сама загадка, [1] - является ли загадка красной.
cards = {
    3: (
        (
            ('Кузнечик', ),
            ('Молоток', ),
            ('Филе щуки', ),
            ('Манеж для новорожденного', True),
            ('Ежевика', ),
            ('Кнут', ),
        ),
        (
            ('Кожура апельсина', ),
            ('Выемка почты', ),
            ('Усталый часовщик', ),
            ('Трёхдневная щетина', ),
            ('Навязчивый доктор', ),
            ('Неразорвавшаяся граната', True),
        ),
        (
            ('Три желания', ),
            ('Мудрая мысль', ),
            ('Радиоведущий', ),
            ('Солнечная лужайка', ),
            ('Кислая капуста', ),
            ('Пухленькая блондинка', ),
        ),
    ),
    4: (
        (
            ('Школьный рюкзак', ),
            ('Лекало', ),
            ('Долина', ),
            ('Клетка в зоопарке', True),
            ('Астрологический прогноз', ),
            ('Купе', ),
        ),
        (
            ('Клей', ),
            ('Артиллерийский снаряд', ),
            ('Вторая жизнь', ),
            ('Дезодорант', ),
            ('Амур', ),
            ('Найденный клад', ),
        ),
        (
            ('Мачо', ),
            ('Свадебный подарок', ),
            ('Штраф за парковку', ),
            ('Красивый макияж', ),
            ('Амур', ),
            ('Найденный клад', ),
        ),
    ),
    5: (
        (
            ('Примус', ),
            ('Камера хранения', ),
            ('Клавишный инструмент', ),
            ('Маленькая порция', ),
            ('Пограничная полоса', True),
            ('Треснутая кружка', ),
        ),
        (
            ('Сын бизнесмена', ),
            ('Кавказский акцент', ),
            ('Утешительный приз', ),
            ('Женский доктор', ),
            ('Замороженная клубника', ),
            ('День святого Валентина', ),
        ),
        (
            ('Крепостной крестьянин', True),
            ('Чистый воздух', ),
            ('Детективный сериал', ),
            ('Прехорошенькая бортпроводница', ),
            ('Добыча нефти', ),
            ('Пасха', ),
        ),
    ),
}


if __name__ == '__main__':
    print(get_card())
