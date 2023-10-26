from bext import goto
from os import system as sys
from ast import literal_eval


class Enigma:
    @staticmethod
    def _split_text(text):
        return [i for i in text]

    @staticmethod
    def __get_coding_or_decoding_dict():
        coding_decoding_dict = [
            {
                'А': ' ', 'Б': '_', 'В': '/', 'Г': 't', 'Д': ')', 'Е': 'В', 'Ё': '{', 'Ж': '-', 'З': 'a', 'И': '!',
                'Й': 'r',
                'К': '+', 'Л': 'э', 'М': 'K', 'Н': 'i', 'О': '[', 'П': "'", 'Р': ';', 'С': 'Й', 'Т': 'з', 'У': 'd',
                'Ф': '"',
                'Х': 'b', 'Ц': '0', 'Ч': 'W', 'Ш': '#', 'Щ': '}', 'Ъ': '%', 'Ы': '$', 'Ь': 'и', 'Э': '|', 'Ю': '?',
                'Я': 's',

                'а': 'k', 'б': 'G', 'в': 'l', 'г': 'H', 'д': 'B', 'е': 'y', 'ё': 'А', 'ж': 'o', 'з': 'A', 'и': 'R',
                'й': 'E',
                'к': 'N', 'л': 'Р', 'м': 'j', 'н': 'F', 'о': 'U', 'п': 'Y', 'р': 'D', 'с': 'n', 'т': 'а', 'у': 'И',
                'ф': 'в',
                'х': 'с', 'ц': 'T', 'ч': 'Н', 'ш': 'u', 'щ': 'К', 'ъ': 'р', 'ы': 'Е', 'ь': '`', 'э': '~', 'ю': '—',
                'я': '–',

                'A': '(', 'B': '2', 'C': '<', 'D': 'х', 'E': '&', 'F': 'т', 'G': '7', 'H': 'Л', 'I': 'б', 'J': ':',
                'K': 'г',
                'L': 'м', 'M': '4', 'N': 'ц', 'O': '№', 'P': ']', 'Q': 'Ё', 'R': 'О', 'S': '^', 'T': 'щ', 'U': 'Ъ',
                'V': 'л',
                'W': '*', 'X': 'f', 'Y': ',', 'Z': 'д', '\\': 'λ',

                'a': 'Ю', 'b': '@', 'c': 'Т', 'd': 'Ц', 'e': 'Щ', 'f': 'C', 'g': 'я', 'h': 'ш', 'i': 'У', 'j': 'e',
                'k': 'M',
                'l': 'Ш', 'm': 'J', 'n': 'O', 'o': '1', 'p': 'X', 'q': 'P', 'r': 'ь', 's': 'Д', 't': 'п', 'u': 'Ь',
                'v': 'Я',
                'w': 'Э', 'x': 'S', 'y': 'm', 'z': 'С',

                '1': 'Z', '2': 'у', '3': '=', '4': 'q', '5': 'М', '6': 'I', '7': 'ъ', '8': 'h', '9': '>', '0': 'н',
                '`': 'L',
                '!': '3', '@': 'g', '#': 'ы', '$': 'w', "%": 'ю', '^': 'ё', '&': 'й', '*': '9', '(': 'о', ')': 'Ы',
                '_': '8',
                '-': 'v', '–': 'Г', '—': '6', '=': 'ч', '+': 'Б', '[': 'ж', ']': '5', '{': 'Ф', '}': 'З', ';': 'ф',
                '|': 'Q',
                ' ': '.', '"': 'x', ',': 'z', '.': 'p', "'": 'к', '?': 'Ч', '/': 'V', '<': 'Х', '>': 'c', '№': 'Ж',
                ':': 'е',
                '~': 'П'
            },
            {
                ' ': "463", '_': "835", '/': "935", 't': "104", ')': "772", 'В': "958", '{': "921", '-': "473",
                'a': "262",
                '!': "178", 'r': "793", '+': "634", 'э': "808", 'K': "235", 'i': "183", '[': "624", "'": "679",
                ';': "195",
                'Й': "836", 'з': "278", 'd': "218", '"': "934", 'b': "378", '0': "937", 'W': "946", '#': "905",
                '}': "926",
                '%': "468", '$': "856", 'и': "285", '|': "745", '?': "903", 's': "380",

                'k': '626', 'G': '274', 'l': '984', 'H': '477', 'B': '556', 'y': '457', 'А': '780', 'o': '234',
                'A': '967',
                'R': '356', 'E': '746', 'N': '289', 'Р': '174', 'j': '965', 'F': '375', 'U': '346', 'Y': '316',
                'D': '568',
                'n': '360', 'а': '957', 'И': '255', 'в': '674', 'с': '366', 'T': '846', 'Н': '677', 'u': '438',
                'К': '894',
                'р': '546', 'Е': '645', '`': '298', '~': '783', '—': '334', '–': '444',

                '(': '166', '2': '763', '<': '956', 'х': '398', '&': '374', 'т': '896', '7': '224', 'Л': '222',
                'б': '176',
                ':': '837', 'г': '962', 'м': '888', '4': '232', 'ц': '141', '№': '641', ']': '111', 'Ё': '631',
                'О': '687',
                '^': "555", 'щ': '964', 'Ъ': '275', 'л': '906', '*': '236', 'f': '924', ',': '505', 'д': '999',
                'λ': '816',

                'Ю': "620", '@': "393", 'Т': "593", 'Ц': "399", 'Щ': "406", 'C': "303", 'я': "579", 'ш': "578",
                'У': "997",
                'e': "595", 'M': "594", 'Ш': "695", 'J': "706", 'O': "867", '1': "474", 'X': "357", 'P': "216",
                'ь': "635",
                'Д': "853", 'п': "830", 'Ь': "569", 'Я': "636", 'Э': "948", 'S': "352", 'm': "388", 'С': "454",

                'Z': '735', 'у': '786', '=': '253', 'q': '897', 'М': '335', 'I': '673', 'ъ': '944', 'h': '678',
                '>': '365',
                'н': '368', 'й': '395', 'g': '726', 'е': '456', 'z': '284', 'p': '834', 'к': "638", 'x': '478',
                'Ч': '741',
                'V': '744', 'ч': '701', 'Б': '412', 'v': '379', 'о': '426', 'Ы': '526', '3': '736', '.': '553',
                'ы': '676',
                'w': '776', 'ю': '778', '9': '961', '8': '765', '6': '654', 'Г': '847', 'Х': '424', 'c': '637',
                'З': '563',
                'Ф': '854', '5': '345', 'ж': '146', 'Q': '523', 'Ж': '488', 'L': '848', 'ё': '459', 'ф': '742',
                'П': '367'
            },
            {
                '463': ' ', '835': '_', '935': '/', '104': 't', '772': ')', '958': 'В', '921': '{', '473': '-',
                '262': 'a',
                '178': '!', '793': 'r', '634': '+', '808': 'э', '235': 'K', '183': 'i', '624': '[', '679': "'",
                '195': ';',
                '836': 'Й', '278': 'з', '218': 'd', '934': '"', '378': 'b', '937': '0', '946': 'W', '905': '#',
                '926': '}',
                '468': '%', '856': '$', '285': 'и', '745': '|', '903': '?', '380': 's',

                '626': 'k', '274': 'G', '984': 'l', '477': 'H', '556': 'B', '457': 'y', '780': 'А', '234': 'o',
                '967': 'A',
                '356': 'R', '746': 'E', '289': 'N', '174': 'Р', '965': 'j', '375': 'F', '346': 'U', '316': 'Y',
                '568': 'D',
                '360': 'n', '957': 'а', '255': 'И', '674': 'в', '366': 'с', '846': 'T', '677': 'Н', '438': 'u',
                '894': 'К',
                '546': 'р', '645': 'Е', '298': '`', '783': '~', '334': '—', '444': '–', '701': 'ч',

                '166': '(', '763': '2', '956': '<', '398': 'х', '374': '&', '896': 'т', '224': '7', '222': 'Л',
                '176': 'б',
                '837': ':', '962': 'г', '888': 'м', '232': '4', '141': 'ц', '641': '№', '111': ']', '631': 'Ё',
                '687': 'О',
                '555': '^', '964': 'щ', '275': 'Ъ', '906': 'л', '236': '*', '924': 'f', '505': ',', '999': 'д',
                '816': 'λ',

                '620': 'Ю', '393': '@', '593': 'Т', '399': 'Ц', '406': 'Щ', '303': 'C', '579': 'я', '578': 'ш',
                '997': 'У',
                '595': 'e', '594': 'M', '695': 'Ш', '706': 'J', '867': 'O', '474': '1', '357': 'X', '216': 'P',
                '635': 'ь',
                '853': 'Д', '830': 'п', '569': 'Ь', '636': 'Я', '948': 'Э', '352': 'S', '388': 'm', '454': 'С',
                '459': 'ё',

                '735': 'Z', '786': 'у', '253': '=', '897': 'q', '335': 'М', '673': 'I', '944': 'ъ', '678': 'h',
                '365': '>',
                '368': 'н', '848': 'L', '736': '3', '726': 'g', '676': 'ы', '776': 'w', "778": 'ю', '456': 'е',
                '395': 'й',
                '961': '9', '426': 'о', '526': 'Ы', '765': '8', '379': 'v', '847': 'Г', '654': '6', '741': 'Ч',
                '412': 'Б',
                '146': 'ж', '345': '5', '854': 'Ф', '563': 'З', '742': 'ф', '523': 'Q', '553': '.', '478': 'x',
                '284': 'z',
                '834': 'p', "638": 'к', '739': 'Ч', '744': 'V', '424': 'Х', '637': 'c', '488': 'Ж', '858': 'е',
                '367': 'П'
            },
            {
                ' ': "А", '_': "Б", '/': "В", 't': "Г", ')': "Д", 'В': "Е", '{': "Ё", '-': "Ж", 'a': "З", '!': "И",
                'r': "Й",
                '+': "К", 'э': "Л", 'K': "М", 'i': "Н", '[': "О", "'": "П", ';': "Р", 'Й': "С", 'з': "Т", 'd': "У",
                '"': "Ф",
                'b': "Х", '0': "Ц", 'W': "Ч", '#': "Ш", '}': "Щ", '%': "Ъ", '$': "Ы", 'и': "Ь", '|': "Э", '?': "Ю",
                's': "Я",

                'k': 'а', 'G': 'б', 'l': 'в', 'H': 'г', 'B': 'д', 'y': 'е', 'А': 'ё', 'o': 'ж', 'A': 'з', 'R': 'и',
                'E': 'й',
                'N': 'к', 'Р': 'л', 'j': 'м', 'F': 'н', 'U': 'о', 'Y': 'п', 'D': 'р', 'n': 'с', 'а': 'т', 'И': 'у',
                'в': 'ф',
                'с': 'х', 'T': 'ц', 'Н': 'ч', 'u': 'ш', 'К': 'щ', 'р': 'ъ', 'Е': 'ы', '`': 'ь', '~': 'э', '—': 'ю',
                '–': 'я',

                '(': 'A', '2': 'B', '<': 'C', 'х': 'D', '&': 'E', 'т': 'F', '7': 'G', 'Л': 'H', 'б': 'I', ':': 'J',
                'г': 'K',
                'м': 'L', '4': 'M', 'ц': 'N', '№': 'O', ']': 'P', 'Ё': 'Q', 'О': 'R', '^': "S", 'щ': 'T', 'Ъ': 'U',
                'л': 'V',
                '*': 'W', 'f': 'X', ',': 'Y', 'д': 'Z', 'λ': '\\',

                'Ю': "a", '@': "b", 'Т': "c", 'Ц': "d", 'Щ': "e", 'C': "f", 'я': "g", 'ш': "h", 'У': "i", 'e': "j",
                'M': "k",
                'Ш': "l", 'J': "m", 'O': "n", '1': "o", 'X': "p", 'P': "q", 'ь': "r", 'Д': "s", 'п': "t", 'Ь': "u",
                'Я': "v",
                'Э': "w", 'S': "x", 'm': "y", 'С': "z",

                'Z': '1', 'у': '2', '=': '3', 'q': '4', 'М': '5', 'I': '6', 'ъ': '7', 'h': '8', '>': '9', 'н': '0',
                'й': '&',
                'g': '@', 'е': ':', 'z': ',', 'p': '.', 'к': "'", 'x': '"', 'Ч': '?', 'V': '/', 'ч': '=', 'Б': '+',
                'v': '-',
                'о': '(', 'Ы': ')', '3': '!', '.': ' ', 'ы': '#', 'w': '$', 'ю': '%', '9': '*', '8': '_', '6': '—',
                'Г': '–',
                'Х': '<', 'c': '>', 'З': '}', 'Ф': '{', '5': ']', 'ж': '[', 'Q': '|', 'Ж': '№', 'L': '`', 'ё': '^',
                'ф': ';',
                'П': '~'
            }
        ]
        return coding_decoding_dict

    @property
    def get_cd_dict(self):
        return self.__get_coding_or_decoding_dict()

    def coding(self, path, text) -> None:
        """
        Метод принимает строковую или числовую информацию и
        возвращает её в кодированном строковом виде.

        :param path: str
        :param text: str or int
        :return: None
        """
        try:
            transfer_first = []
            transfer_second = []

            for i in self._split_text(str(text)):
                transfer_first.append(self.get_cd_dict[0][i])
            for i in self._split_text(''.join(transfer_first)):
                transfer_second.append(self.get_cd_dict[1][i])
            with open(path, 'w') as code:
                code.write(str([''.join(transfer_second)]))

        except KeyError:
            sys('cls')
            goto(24, 14)
            print("Ошибка кодирования! Переустановите ТПИ Неон!")
            goto(24, 15)
            input("Coding Error! Reinstall TUI Neon!")

    def decoding(self, path) -> str:
        """
        Метод принимает строковый или числовой код и
        возвращает информацию в декодированном строковом виде.

        :param path: str or int
        :return: str
        """
        try:
            with open(path) as read_code:
                code = literal_eval(read_code.read())

            iteration_value = len(str(code[0]))
            counter = 0

            transfer_first = []
            transfer_second = []
            transfer_third = []

            for i in range(iteration_value // 3):
                transfer_first.append(''.join(str(code[0])[counter:3 + counter]))
                counter += 3
            for i in transfer_first:
                transfer_second.append(self.get_cd_dict[2][i])
            for i in transfer_second:
                transfer_third.append(self.get_cd_dict[3][i])

            return ''.join(transfer_third)

        except KeyError:
            sys('cls')
            goto(24, 14)
            print("Ошибка декодирования! Переустановите ТПИ Неон!")
            goto(24, 15)
            input("Decoding error! Reinstall TUI Neon!")
