# КлиникБук

[![Header](https://github.com/AsQqqq/clinicbook/blob/master/assets/image/header.png?raw=true)](#клиникбук)

## Введение

"КлиникБук" - это ПО, представляющее собой платформу для управления записью пациентов в поликлинику "Клиник". 

## Что это?

Это приложение написанное на Python (версию 3.6+) для записи пациентов в поликлинику "Клиник".

## Навигация

* [Начало](#клиникбук)
* [Введение](#введение)
* [Что это?](#что-это)
* [Навигация](#навигация)
* [Установка](#установка)
* [Компиляция в exe](#компиляция-в-exe)
* [Создание загрузчика](#создание-загрузчика)
* [Поддержка](#поддержка)

## Установка

Перед установкой вам нужно скачать программу по [ссылке](https://jrsoftware.org/isinfo.php)

* [Навигация](#навигация)

## Компиляция в exe

1. Создайте виртуальное окружение командой:
    * windows
        `python -m venv .venv`
    * linux
        `python3 -m venv .venv`

2. Активируйте виртуальное окружение:
    * windows
        `python .venv\Script\activate`
    * linux
        `python3 .venv/bin/avtivate`

3. Установите все зависимости:
    `pip install -r requirements.txt`

4. Скомпилируйте файлы в exe-файл:
    ВАЖНО! Вы должны находиться в корне проекта, когда выполняете эту команду.

    ```
    pyinstaller --noconfirm --onefile --windowed --icon "assets/image/icon.ico" --add-data "language;language/" --add-data "database.py;." --add-data "local.sqlite;." --add-data "login_layout.py;." --add-data "main_layout.py;." --add-data "register_layout.py;." --add-data "setting_layout.py;." --add-data "source_rc.py;." --add-data "language/en_US.json;." --add-data "language/ru_RU.json;." --add-data "language/settings.json;."  "app.py"
    ```

* [Навигация](#навигация)

## Создание загрузчика

Программа будет запускаться, только если в её корне находится папка `language` и файл `local.sqlite`. Чтобы создать загрузчик, потребуется программа, которую я просил скачать [ранее](#установка).

Скачайте файл по этой [ссылке](https://github.com/AsQqqq/clinicbook/blob/master/scriptInstaller.iss) и выполните компиляцию.

[![Header](https://github.com/AsQqqq/clinicbook/blob/master/assets/image/screen.png?raw=true)](#клиникбук)

Затем просто запустите файл, который находится в папке output.

* [Навигация](#навигация)

## Поддержка

Если у вас возникли проблемы или вопросы, создайте issue на GitHub или свяжитесь со мной напрямую по [Вк](https://vk.com/phonk_danilov).

* [Навигация](#навигация)
