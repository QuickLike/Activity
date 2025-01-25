types = ('Рисунок', 'Говорение', 'Жесты')


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
