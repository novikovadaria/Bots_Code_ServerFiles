import random
all_cities = ['Абакан', 'Азов', 'Александров', 'Альметьевск', 'Анапа', 'Ангарск', 'Анжеро-Судженск', 'Апатиты', 'Арзамас', 'Армавир', 'Арсеньев', 'Артем', 'Архангельск',
              'Асбест', 'Астрахань', 'Ачинск', 'Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Барнаул', 'Батайск', 'Белгород', 'Белебей', 'Белово', 'Белорецк', 'Белореченск', 'Бердск',
              'Березники', 'Березовский', 'Бийск', 'Биробиджан', 'Благовещенск', 'Бор', 'Борисоглебск', 'Боровичи', 'Братск', 'Брянск', 'Бугульма', 'Буденновск', 'Бузулук', 'Буйнакск',
              'Великие Луки', 'Великий Новгород', 'Верхняя Пышма', 'Видное', 'Владивосток', 'Владикавказ', 'Владимир', 'Волгоград', 'Волгодонск', 'Волжск', 'Волжский', 'Вологда', 'Вольск',
              'Воркута', 'Воронеж', 'Воскресенск', 'Воткинск', 'Всеволожск', 'Выборг', 'Выкса', 'Вязьма', 'Гатчина', 'Геленджик', 'Георгиевск', 'Глазов', 'Горно-Алтайск', 'Грозный', 'Губкин',
              'Гудермес', 'Гуково', 'Гусь-Хрустальны', 'Дербент', 'Дзержинск', 'Димитровград', 'Дмитров', 'Долгопрудный', 'Домодедово', 'Донской', 'Дубна', 'Евпатория', 'Егорьевск', 'Ейск',
              'Екатеринбург', 'Елабуга', 'Елец', 'Ессентуки', 'Железногорск', 'Жигулевск', 'Жуковский', 'Заречный', 'Зеленогорск', 'Зеленодольск', 'Златоуст', 'Иваново', 'Ивантеевка', 'Ижевск',
              'Избербаш', 'Иркутск', 'Искитим', 'Ишим', 'Ишимбай', 'Йошкар-Ола', 'Казань', 'Калининград', 'Калуга', 'Каменск-Уральский', 'Каменск-Шахтинский', 'Камышин', 'Канск', 'Каспийск',
              'Кемерово', 'Керчь', 'Кинешма', 'Кириши', 'Киров', 'Кирово-Чепецк', 'Киселевск', 'Кисловодск', 'Клин', 'Клинцы', 'Ковров', 'Когалым', 'Коломна', 'Комсомольск-на-Амуре', 'Копейск'
              'Королев', 'Кострома', 'Котлас', 'Красногорск', 'Краснодар', 'Краснокаменск', 'Краснокамск', 'Краснотурьинск', 'Красноярск', 'Кропоткин', 'Крымск', 'Кстово', 'Кузнецк',
              'Кумертау', 'Кунгур', 'Курган', 'Курск', 'Кызыл', 'Лабинск', 'Лениногорск', 'Ленинск-Кузнецкий', 'Лесосибирск', 'Липецк', 'Лиски', 'Лобня', 'Лысьва', 'Лыткарино',
              'Люберцы', 'Магадан', 'Магнитогорск', 'Майкоп', 'Махачкала', 'Междуреченск', 'Мелеуз', 'Миасс', 'Минеральные Воды', 'Минусинск', 'Михайловка', 'Мичуринск', 'Москва',
              'Мурманск', 'Муром', 'Мытищи', 'Набережные Челны', 'Назарово', 'Назрань', 'Нальчик', 'Наро-Фоминск', 'Находк', 'Невинномысск', 'Нерюнгри', 'Нефтекамск', 'Нефтеюганск',
              'Нижневартовск', 'Нижнекамск', 'Нижний Новгород', 'Нижний Тагил', 'Новоалтайск', 'Новокузнецк', 'Новокуйбышевск', 'Новомосковск', 'Новороссийск', 'Новосибирск', 'Новотроицк',
              'Новоуральск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск', 'Новый Уренгой', 'Ногинск', 'Норильск', 'Ноябрьск', 'Нягань', 'Обнинск', 'Одинцово',
              'Озерск', 'Октябрьский', 'Омск', 'Орел', 'Оренбург', 'Орехово-Зуево', 'Орск', 'Павлово', 'Павловский Посад', 'Пенза', 'Первоуральск', 'Перм', 'Петрозаводск', 'Петропавловск-Камчатский',
              'Подольск', 'Полевской', 'Прокопьевск', 'Прохладный', 'Псков', 'Пушкино', 'Пятигорск', 'Раменское', 'Ревда', 'Реутов', 'Ржев', 'Рославль', 'Россошь', 'Ростов-на-Дону',
              'Рубцовск', 'Рыбинск', 'Рязань', 'Салават', 'Сальск', 'Самара', 'Санкт-Петербург', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Свободный', 'Севастополь', 'Северодвинск', 'Северск', 'Сергиев Посад', 'Серов', 'Серпухов', 'Сертолово', 'Сибай', 'Симферополь', 'Славянск-на-Кубани', 'Смоленск', 'Соликамск', 'Солнечногорск', 'Сосновый Бор',
              'Сочи', 'Ставрополь', 'Старый Оскол', 'Стерлитамак', 'Ступино', 'Сургут', 'Сызрань', 'Сыктывкар', 'Таганрог', 'Тамбов', 'Тверь', 'Тимашевск', 'Тихвин', 'Тихорецк',
              'Тобольск', 'Тольятти', 'Томск', 'Троицк', 'Туапсе', 'Туймазы', 'Тула', 'Тюмень', 'Узловая', 'Улан-Удэ', 'Ульяновск', 'Урус-Мартан', 'Усолье-Сибирское', 'Уссурийск',
              'Усть-Илимск', 'Уфа', 'Ухта', 'Феодосия', 'Фрязино', 'Хабаровск', 'Ханты-Мансийск', 'Хасавюрт', 'Химки', 'Чайковский', 'Чапаевск', 'Чебоксары', 'Челябинск', 'Черемхово',
              'Череповец', 'Черкесск', 'Черногорск', 'Чехов', 'Чистополь', 'Чита', 'Шадринск', 'Шали', 'Шахты', 'Шуя', 'Щекино', 'Щелково', 'Электросталь', 'Элиста',
              'Энгельс', 'Южно-Сахалинск', 'Юрга', 'Якутск', 'Ялта', 'Ярославль']

allowed_cities = list(all_cities)
random.shuffle(allowed_cities)
# первый ход бота
bot_answer = allowed_cities.pop()
print(bot_answer)
print(f"Вам на букву '{bot_answer[-1]}'")
print()

# возможные действия
game_over = False
while not game_over:
    player_answer = input("Ваша очередь.\n")
    if player_answer.lower()[0] != bot_answer[-1]:
        print(f"Неверно. Город должен начинаться на букву '{bot_answer[-1]}'")
    elif player_answer not in all_cities:
        print("Такого города нет в России, повторите попытку.\n")
        print()
    elif player_answer not in allowed_cities:
        print("Этот город уже был.")
        print()
    else:
        print("Верно!")
        print(f"Мне на букву {player_answer[-1]}")
        allowed_cities.remove(player_answer)
# цикл для ответа бота
        for possib in allowed_cities:
            if possib.lower()[0] == player_answer[-1]:
                bot_answer = possib
                allowed_cities.remove(possib)
                print(f"Мой ответ - {possib}")
                print(f"Вам на букву {possib[-1]}")
                print()
                break
        else:
            game_over = True
            print(
                f"Я больше не знаю городов на букву {possib[-1]}. Вы победили!")
