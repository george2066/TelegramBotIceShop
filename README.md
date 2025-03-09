## Проект

    TelegramBotIceShop
    George Rodionov
    GitHub: george2066
    george2066@yandex.ru

Также создана таблица events со следующими полями:

    id   int NOT NULL PRIMARY KEY
    is_waiter bool

В проекте использован плагин ptbcontrib roles.
Чтобы установить его:

    poetry add git+https://github.com/python-telegram-bot/ptbcontrib.git@main -E roles
