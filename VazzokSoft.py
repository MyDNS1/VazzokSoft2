import phonenumbers
import os
from colorama import Fore, Style, init
from phonenumbers import geocoder, carrier, timezone, number_type, is_valid_number, is_possible_number, PhoneNumberFormat

init(autoreset=False)

banner = f"""{Fore.GREEN}
▗▖  ▗▖ ▗▄▖ ▗▄▄▄▄▖▗▄▄▄▄▖ ▗▄▖ ▗▖ ▗▖
▐▌  ▐▌▐▌ ▐▌   ▗▞▘   ▗▞▘▐▌ ▐▌▐▌▗▞▘
▐▌  ▐▌▐▛▀▜▌ ▗▞▘   ▗▞▘  ▐▌ ▐▌▐▛▚▖ 
 ▝▚▞▘ ▐▌ ▐▌▐▙▄▄▄▖▐▙▄▄▄▖▝▚▄▞▘▐▌ ▐▌              
 ▗▄▄▖ ▗▄▖ ▗▄▄▄▖▗▄▄▄▖             
▐▌   ▐▌ ▐▌▐▌     █               
 ▝▀▚▖▐▌ ▐▌▐▛▀▀▘  █               
▗▄▄▞▘▝▚▄▞▘▐▌     █   

— by @uservazzok
"""

def main():
    os.system("clear" if os.name == "posix" else "cls")
    print(banner)
    print(f"{Fore.GREEN}1. {Fore.LIGHTGREEN_EX}Поиск по номеру телефона")
    print(f"{Fore.GREEN}2. {Fore.LIGHTGREEN_EX}Выход{Style.RESET_ALL}")
    choice = input(f"\n{Fore.GREEN}Выберите функцию — {Fore.LIGHTGREEN_EX}")
    if choice == "1":
        phonesearch()
    elif choice == "2":
        exit()

def get_number_type(num_type):
    types = {
        phonenumbers.PhoneNumberType.MOBILE: "Мобильный",
        phonenumbers.PhoneNumberType.FIXED_LINE: "Стационарный",
        phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Стационарный или мобильный",
        phonenumbers.PhoneNumberType.TOLL_FREE: "Бесплатный",
        phonenumbers.PhoneNumberType.PREMIUM_RATE: "Платный",
        phonenumbers.PhoneNumberType.SHARED_COST: "Разделённая стоимость",
        phonenumbers.PhoneNumberType.VOIP: "VoIP (Интернет-телефония)",
        phonenumbers.PhoneNumberType.PERSONAL_NUMBER: "Персональный номер",
        phonenumbers.PhoneNumberType.PAGER: "Пейджер",
        phonenumbers.PhoneNumberType.UAN: "UAN (универсальный номер)",
        phonenumbers.PhoneNumberType.VOICEMAIL: "Голосовая почта",
        phonenumbers.PhoneNumberType.UNKNOWN: "Неизвестный тип"
    }
    return types.get(num_type, "Неизвестный тип")

def phonesearch():
    os.system("clear" if os.name == "posix" else "cls")
    print(banner)

    try:
        number = input(f"\n{Fore.LIGHTGREEN_EX}Введите номер телефона (пример: +79999999999): ")
        parsed_number = phonenumbers.parse(number)

        country = geocoder.description_for_number(parsed_number, "ru")
        operator = carrier.name_for_number(parsed_number, "ru")
        timezones = timezone.time_zones_for_number(parsed_number)
        num_type = number_type(parsed_number)
        valid = is_valid_number(parsed_number)
        possible = is_possible_number(parsed_number)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        country_code = parsed_number.country_code
        national_number = parsed_number.national_number
        e164_format = phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)
        international_format = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
        national_format = phonenumbers.format_number(parsed_number, PhoneNumberFormat.NATIONAL)

        print(f"\n{Fore.GREEN}Страна: {Fore.LIGHTGREEN_EX}{country}")
        print(f"{Fore.GREEN}Оператор: {Fore.LIGHTGREEN_EX}{operator}")
        print(f"{Fore.GREEN}Часовые пояса: {Fore.LIGHTGREEN_EX}{', '.join(timezones)}")
        print(f"{Fore.GREEN}Тип номера: {Fore.LIGHTGREEN_EX}{get_number_type(num_type)}")
        print(f"{Fore.GREEN}Код страны: {Fore.LIGHTGREEN_EX}{country_code}")
        print(f"{Fore.GREEN}Национальный номер: {Fore.LIGHTGREEN_EX}{national_number}")
        print(f"{Fore.GREEN}Регион: {Fore.LIGHTGREEN_EX}{region_code}")
        print(f"{Fore.GREEN}Валидный номер: {Fore.LIGHTGREEN_EX}{valid}")
        print(f"{Fore.GREEN}Возможный номер: {Fore.LIGHTGREEN_EX}{possible}")
        print(f"{Fore.GREEN}Формат E.164: {Fore.LIGHTGREEN_EX}{e164_format}")
        print(f"{Fore.GREEN}Международный формат: {Fore.LIGHTGREEN_EX}{international_format}")
        print(f"{Fore.GREEN}Национальный формат: {Fore.LIGHTGREEN_EX}{national_format}")

    except phonenumbers.NumberParseException:
        print(f"\n{Fore.RED}Ошибка: Некорректный формат номера!")

    print(f"\n{Fore.GREEN}Нажмите ENTER, чтобы продолжить...")
    input()
    main()

main()