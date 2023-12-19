from colorama import Fore, Style


class CS:

    @staticmethod
    def msgError(msg):
        print(f'{Fore.RED}{msg}{Style.RESET_ALL}')

    @staticmethod
    def msgTrue(msg):
        print(f'{Fore.LIGHTGREEN_EX}{msg}{Style.RESET_ALL}')