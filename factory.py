from abc import ABC, abstractmethod


class Localizer(ABC):
    @abstractmethod
    def localize(self, msg):
        """ Translate message """
        pass


class GermanLocalizer(Localizer):
    "German version"

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "Ich spreache deutsch"}

    def localize(self, msg):
        """Returns msg in German"""
        return self.translations.get(msg, msg)


class ArabicLocalizer(Localizer):
    """Arabic version"""

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "اتكلم العربية"}

    def localize(self, msg):
        """Returns msg in Arabic"""
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    """English version"""

    def __init__(self):
        """ Setup translations """
        self.translations = {"main.header": "I speak English"}

    def localize(self, msg):
        """Returns msg in English"""
        return self.translations.get(msg, msg)


class Translate:

    @staticmethod
    def get_localizer(option="1") -> Localizer:
        """Factory Method"""
        localizers = {
            "1": EnglishLocalizer,
            "2": GermanLocalizer,
            "3": ArabicLocalizer,
        }

        return localizers[option]()


def main():

    print("Please select your language:")
    print("1. English")
    print("2. German")
    print("3. Arabic")

    option = input("Please select an option then hit enter:")

    local = Translate.get_localizer(option)

    msg = "main.header"
    print(local.localize(msg))


main()
