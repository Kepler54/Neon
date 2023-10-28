from bext import goto
from pyowm import OWM
from time import sleep
from calendar import month
from random import randint
from datetime import datetime
from os import system as sys
from threading import Thread
from psutil import sensors_battery
from keyboard import press_and_release
from platform import system, machine, version, release as os_release
from matrix import Matrix
from system import System


class Widgets(System, Matrix):
    def __init__(self):
        super().__init__()
        self.owm = OWM(self.get_user_data(self._weather_key))
        self._city = (self.get_user_data(self._city))
        self.temp = self.owm.weather_manager().weather_at_place(self._city).weather.temperature('celsius')
        self.mgr = self.owm.weather_manager()
        self.observation = self.mgr.weather_at_place(self._city)
        self.w = self.observation.weather

    def get_vertical_bar(self, wdt_wind, count_hgt_wind, wdt_full, count_hgt_full):
        global counter

        if self.width == 120 and self.height == 30:
            counter = count_hgt_wind
        else:
            counter = count_hgt_full

        for i in range(int(self.height // 3.75)):
            if self.width == 120 and self.height == 30:
                goto(wdt_wind, counter)
            else:
                goto(wdt_full, counter)
            self.color.print(f'{self.third_color}│{self.width // 4 * " "}│')
            counter += 1

    def get_start_screen(self):
        sys(self.get_system_command())

        self.get_coordinates(0, 7, 0, int(self.height // 3.3))
        self.color.print(f'{self.first_color}{(self.width - 1) * "─"}')

        self.get_coordinates(
            45, 10, int(self.width // 2.66),
            int(self.height // self.get_symbol_resolution(2.76, 2.64))
        )
        self.color.print(f'{self.third_color}┌{self.width // 4 * "─"}┐')

        self.get_vertical_bar(45, 11, int(self.width // 2.66), int(self.height // 2.61))

        self.get_coordinates(50, 13, int(self.width // 2.25), int(self.height // 2.15))
        self.color.print(
            f'{self.first_color}{machine()}, {self.get_user_data(self._name)}'
            f'{self.change_language("-ЭВМ", "-PC")}'
        )
        self.get_coordinates(50, 16, int(self.width // 2.25), int(self.height // 1.80))
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language(self.tui_neon_shell_ru, self.tui_neon_shell_eng)}'
            f'{self.ver}'
        )
        self.get_coordinates(45, 19, int(self.width // 2.66), int(self.height // 1.54))
        self.color.print(f'{self.third_color}└{self.width // 4 * "─"}┘')
        self.get_coordinates(0, 22, 0, int(self.height // 1.42))
        self.color.print(f'{self.first_color}{(self.width - 1) * "─"}')

        if self.width == 120 and self.height == 30:
            Matrix().get_matrix_move(-1, self.height // 4.61, float(f'{0.0}{randint(6, 9)}'))
            Matrix().get_matrix_move(
                22, self.height // 4.61, float(f'{0.0}{randint(6, 9)}')
            )
            press_and_release('enter')
            Thread(target=Matrix().break_function).start()
            sleep(3.5)
            input()
        else:
            Matrix().get_matrix_move(0, self.height // 4, float(f'{0.0}{randint(6, 9)}'))
            Matrix().get_matrix_move(int(self.height // 1.38), self.height // 4,
                                     float(f'{0.0}{randint(6, 9)}'))
            press_and_release('enter')
            Thread(target=Matrix().break_function).start()
            sleep(6)
            input()

    def get_settings(self):
        self.get_taskbar()

        self.get_coordinates(self.middle_width, self.middle_height - 2, self.middle_width, self.middle_height - 1)
        self.color.print(f'{self.get_user_data(self._name)}{self.change_language("-ЭВМ", "-PC")}')
        self.get_coordinates(self.middle_width, self.middle_height - 1, self.middle_width, self.middle_height)
        self.color.print(
            f'{self.first_color}{self.change_language("Процессор: ", "CPU: ")}'
            f'{self.second_color}{machine()}'
        )
        self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height + 1)
        self.color.print(
            f'{self.first_color}{self.change_language("Разрешение: ", "Resolution: ")}'
            f'{self.second_color}{self.width} x {self.height}'
        )
        self.get_coordinates(self.middle_width, self.middle_height + 1, self.middle_width, self.middle_height + 2)
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language("Текстовый интерфейс: ", "Text interface: ")}'
            f'{self.second_color}{self.change_language(self.tui_neon_shell_ru, self.tui_neon_shell_eng)}{self.ver}'
        )
        self.get_coordinates(self.middle_width, self.middle_height + 2, self.middle_width, self.middle_height + 3)
        self.color.print(
            f'{self.first_color}'
            f'{self.change_language("Операционная система: ", "Operating system: ")}'
            f'{self.second_color}'
            f'{system()} {os_release()} ({self.change_language("Версия ", "Version ")}'
            f'{version()}{self.second_color})'
        )

    def get_taskbar(self):
        sys(self.get_system_command())
        self.get_coordinates(1, 0, 1, 0)

        if self.width == 120 and self.height == 30:
            value = 1.03
        else:
            value = 1.02

        self.color.print(f'{self.third_color}┌{(int(self.width // value)) * "─"}┐')
        self.get_coordinates(1, 1, 1, 1)
        self.color.print(f'{self.third_color}│')

        if self.get_user_data(self._language) == 'russian' or self.get_user_data(self._language) == 'русский':
            self.get_coordinates(4, 1, int(self.width // 6), 1)
            self.color.print(f"{self.first_color}Инфо")
            self.get_coordinates(11, 1, int(self.width // 4.8), 1)
            self.color.print(f"{self.first_color}Опции")
            self.get_coordinates(19, 1, int(self.width // 3.90), 1)
            self.color.print(f"{self.first_color}Каталог")
            self.get_coordinates(29, 1, int(self.width // 3.12), 1)
            self.color.print(f"{self.first_color}Команды")
            self.get_coordinates(39, 1, int(self.width // 2.63), 1)
            self.color.print(f"{self.first_color}Заметки")
            self.get_coordinates(49, 1, int(self.width // 2.30), 1)
            self.color.print(f"{self.first_color}Программы")
            self.get_coordinates(61, 1, int(self.width // 1.97), 1)
            self.color.print(f"{self.first_color}YouTube")
            self.get_coordinates(71, 1, int(self.width // 1.76), 1)
            self.color.print(f"{self.first_color}Погода")
            self.get_coordinates(80, 1, int(self.width // 1.61), 1)
            self.color.print(f"{self.first_color}Календарь")
            self.get_coordinates(92, 1, int(self.width // 1.44), 1)
            self.color.print(f'{self.first_color}{datetime.now():{f"Время"} %H:%M}')
            self.get_coordinates(106, 1, int(self.width // 1.29), 1)
            self.color.print(f'{self.first_color}{datetime.now():%d.%m.%Y}')
        else:
            self.get_coordinates(4, 1, int(self.width // 6), 1)
            self.color.print(f"{self.first_color}Info")
            self.get_coordinates(11, 1, int(self.width // 4.8), 1)
            self.color.print(f"{self.first_color}Settings")
            self.get_coordinates(22, 1, int(self.width // 3.65), 1)
            self.color.print(f"{self.first_color}Catalog")
            self.get_coordinates(32, 1, int(self.width // 3), 1)
            self.color.print(f"{self.first_color}Сommands")
            self.get_coordinates(43, 1, int(self.width // 2.50), 1)
            self.color.print(f"{self.first_color}Notes")
            self.get_coordinates(51, 1, int(self.width // 2.23), 1)
            self.color.print(f"{self.first_color}Programs")
            self.get_coordinates(62, 1, int(self.width // 1.95), 1)
            self.color.print(f"{self.first_color}YouTube")
            self.get_coordinates(72, 1, int(self.width // 1.75), 1)
            self.color.print(f"{self.first_color}Weather")
            self.get_coordinates(82, 1, int(self.width // 1.58), 1)
            self.color.print(f"{self.first_color}Сalendar")
            self.get_coordinates(93, 1, int(self.width // 1.43), 1)
            self.color.print(f'{self.first_color}{datetime.now():{f"Time"} %H:%M}')
            self.get_coordinates(106, 1, int(self.width // 1.29), 1)
            self.color.print(f'{self.first_color}{datetime.now():%d.%m.%Y}')

        self.get_coordinates(self.width - 2, 1, int(self.width // 1.01), 1)
        self.color.print(f'{self.third_color}│')
        self.get_coordinates(1, 2, 1, 2)
        self.color.print(f'{self.third_color}└{(int(self.width // value)) * "─"}┘')

    def get_weather_view(self):
        self.get_coordinates(2, 3, 2, int(self.height // 4.23))
        self.color.print(
            f'{self.first_color}{self.change_language("Температура ", "Temperature ")}'
            f'{self.change_language("в городе ", "in ")}'
            f'{self._city}: {self.second_color}{self.temp["temp"]}{self.first_color}'
            f'{self.change_language(" градусов по Цельсию", " degrees Celsius")}'
        )
        self.get_coordinates(2, 4, 2, int(self.height // 4.13))
        self.color.print(
            f'{self.first_color}{self.change_language("Макс.: ", "Max.: ")}'
            f'{self.second_color}{self.temp["temp_max"]}°{self.first_color}'
            f'{self.change_language(", мин.: ", ", min.: ")}{self.second_color}'
            f'{self.temp["temp_min"]}°{self.first_color}'
            f'{self.change_language(", чувствуется как: ", ", feels like: ")}'
            f'{self.second_color}{self.temp["feels_like"]}°'
        )
        self.get_coordinates(
            2, 5, 2, int(self.height // self.get_symbol_resolution(4.04, 4.07))
        )
        self.color.print(
            f'{self.first_color}{self.change_language("Сила ветра: ", "Wind speed: ")}'
            f'{self.second_color}{self.w.wind()["speed"]}{self.first_color}'
            f'{self.change_language(" м/с, влажность: ", "m/s, humidity:")}'
            f'{self.second_color}{self.w.humidity}%'
        )

    def get_detailed_status(self):
        if self.get_user_data(self._language) == 'russian' or self.get_user_data(self._language) == 'русский':
            if self.w.detailed_status == str('clear sky'):
                self.w.detailed_status = str('ясно')
            if self.w.detailed_status == str('few clouds'):
                self.w.detailed_status = str('облачно')
            if self.w.detailed_status == str('overcast clouds'):
                self.w.detailed_status = str('пасмурно')  # полотемнота, сделана облаком
            if self.w.detailed_status == str('heavy intensity shower rain'):
                self.w.detailed_status = str('проливной дождь')
            if self.w.detailed_status == str('broken clouds'):
                self.w.detailed_status = str('облачно с прояснениями')
            if self.w.detailed_status == str('light rain'):
                self.w.detailed_status = str('лёгкий дождь')
            if self.w.detailed_status == str('scattered clouds'):
                self.w.detailed_status = str('кучевые облака')
            if self.w.detailed_status == str('light intensity shower rain'):
                self.w.detailed_status = str('лёгкий, но интенсивный дождь')
            if self.w.detailed_status == str('light intensity drizzle rain'):
                self.w.detailed_status = str('лёгкий, но интенсивный моросящий дождь')
            if self.w.detailed_status == str('light intensity drizzle'):
                self.w.detailed_status = str('моросящий дождь')
            if self.w.detailed_status == str('moderate rain'):
                self.w.detailed_status = str('небольшой дождь')
            if self.w.detailed_status == str('mist') or self.w.detailed_status == str('fog'):
                self.w.detailed_status = str('туман')
            if self.w.rain == 'rain':
                self.w.rain = ', дождь'
        else:
            f'{self.w.detailed_status}'

    def get_detailed_weather(self, grad_first, grad_second, status):
        self.get_detailed_status()
        self.get_coordinates(
            2, 6, 2, int(self.height // self.get_symbol_resolution(4.04, 4.01))
        )
        if int(grad_first) <= self.temp['feels_like'] <= int(grad_second):
            self.color.print(f"{self.first_color}{status}, {self.w.detailed_status}")

    def get_weather(self):
        try:
            self.get_weather_view()
            self.get_detailed_weather(-60, -51, self.change_language(
                "На улице холод опасный для жизни", "It's life-threatening cold outside")
                                      )
            self.get_detailed_weather(-50, -41, self.change_language(
                "На улице трескучие морозы", "It's bitter cold outside")
                                      )
            self.get_detailed_weather(-40, -31, self.change_language(
                "На улице жуткий дубак", "It's terribly cold outside")
                                      )
            self.get_detailed_weather(-30, -21, self.change_language(
                "На улице сильный мороз", "Сold frost outside")
                                      )
            self.get_detailed_weather(-20, -11, self.change_language(
                "На улице мороз", "Frost outside")
                                      )
            self.get_detailed_weather(-10, -1, self.change_language(
                "На улице заморозки", "It's cold outside")
                                      )
            self.get_detailed_weather(0, 10, self.change_language(
                "На улице прохладно", "It's lukewarm outside")
                                      )
            self.get_detailed_weather(11, 20, self.change_language(
                "На улице тепло", "It's warm outside")
                                      )
            self.get_detailed_weather(21, 30, self.change_language(
                "На улице очень тепло", "It's very warm outside")
                                      )
            self.get_detailed_weather(31, 40, self.change_language(
                "На улице жарко", "It's pretty hot outside")
                                      )
            self.get_detailed_weather(41, 50, self.change_language(
                "На улице очень жарко", "It's very hot outside")
                                      )
            self.get_detailed_weather(51, 60, self.change_language(
                "На улице жуткая жарища", "It's terribly hot outside")
                                      )
        except:
            self.get_coordinates(
                2, 5, 2, int(self.height // self.get_symbol_resolution(4.04, 4.07))
            )
            self.color.print(
                self.first_color + self.change_language(
                    "Что-то пошло не так...", "Something's gone wrong..."
                )
            )

    def get_wallpaper(self, fc, sc):
        self.get_coordinates(self.width // 2, self.middle_height - 7, self.width // 2, self.middle_height - 6)
        self.color.print(f'{fc}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 6, self.width // 2, self.middle_height - 5)
        self.color.print(f'{fc}░░░░░░░░░░░░░░░░▄{sc}▄▄█▄██▄▄{fc}░░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 5, self.width // 2, self.middle_height - 4)
        self.color.print(f'{fc}░░░▄█▀███▄▄█████{sc}███████████████▄▄███▀█{fc}░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 4, self.width // 2, self.middle_height - 3)
        self.color.print(f'{fc}░░░░█{sc}░░{fc}▀█████{sc}██████████████████████{fc}█{sc}░░█{fc}░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 3, self.width // 2, self.middle_height - 2)
        self.color.print(f'{fc}░░░░░█▄{sc}░░{fc}▀█████{sc}████████{fc}███{sc}███████{fc}█{sc}░░░▄▀{fc}░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 2, self.width // 2, self.middle_height - 1)
        self.color.print(f'{fc}░░░░░░▀█▄▄████▀▀▀{sc}░░░░█{fc}█{sc}░░░{fc}▀▀▀{sc}█████▄▄█▀{fc}░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height - 1, self.width // 2, self.middle_height)
        self.color.print(f'{fc}░░░░░░▄███▀▀{sc}░░░░░░░░░█{fc}█{sc}░░░░░░░░░▀███▄{fc}░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height, self.width // 2, self.middle_height + 1)
        self.color.print(f'{fc}░░░░░▄██▀{sc}░░░░░▄▄▄██▄▄██░▄██▄▄▄░░░░░▀██▄{fc}░░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 1, self.width // 2, self.middle_height + 2)
        self.color.print(f'{fc}░░░▄██▀{sc}░░░▄▄▄███ ▄█████████ ▄██▄▄▄{sc}░░░▀█▄{fc}░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 2, self.width // 2, self.middle_height + 3)
        self.color.print(f'{fc}░░░▀██▄▄████{sc}██████▀░███▀▀▀█████████▄▄▄█▀{fc}░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 3, self.width // 2, self.middle_height + 4)
        self.color.print(f'{fc}░░░░░▀█████████{sc}█▀░░░█{fc}█{sc}█░░░▀███████████▀{fc}░░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 4, self.width // 2, self.middle_height + 5)
        self.color.print(f'{fc}░░░░░░░▀▀▀██████{sc}░░░{fc}██{sc}███▄░░▀██████▀▀{fc}░░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 5, self.width // 2, self.middle_height + 6)
        self.color.print(f'{fc}░░░░░░░░░░░░▀▀▀▀▄{sc}░░█{fc}██{sc}██▀░▄█▀▀▀{fc}░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 6, self.width // 2, self.middle_height + 7)
        self.color.print(f'{fc}░░░░░░░░░░░░░░░░░▀▀▄▄▄▄▄▀▀{fc}░░░░░░░░░░░░░░░░░')
        self.get_coordinates(self.width // 2, self.middle_height + 7, self.width // 2, self.middle_height + 8)
        self.color.print(f'{fc}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')

    def get_battery(self):
        self.get_coordinates(
            2, 24, int(self.width // self.width + 1), int(self.height - self.height // 4.27)
        )
        try:
            self.color.print(
                self.second_color + self.change_language(
                    "Аккумулятор заряжен на ", "The battery is charged for "
                ) + f'{sensors_battery()[0]}%'
            )
        except:
            print('')

    def get_shutdown_or_reboot(self, download_text):
        count = 0
        while count < 4:
            sys(self.get_system_command())
            self.get_coordinates(self.middle_width, self.middle_height, self.middle_width, self.middle_height)
            self.color.print(self.first_color + self.get_loading_points(download_text, count))
            count += 1
            sleep(0.3)

    @staticmethod
    def get_month_calendar():
        return f'{month(int(f"{datetime.now():%Y}"), int(f"{datetime.now():%m}"), 3, 2)}'