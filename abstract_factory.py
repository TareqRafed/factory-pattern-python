from abc import ABC, abstractmethod
import os


class IButton(ABC):
    @abstractmethod
    def onClick(func):
        pass


class ISlider(ABC):
    @abstractmethod
    def onSlide(func):
        pass


class WinButton(IButton):
    """Button of Windows design system"""
    def onClick(func):
        func()


class MacButton(IButton):
    """Button of macOS design system"""
    def onClick(func):
        func()


class WinSlider(ISlider):
    """Slider of Windows design system"""
    def onSlide(func):
        func()


class MacSlider(ISlider):
    """Slider of macOS design system"""
    def onSlide(func):
        func()


class IGUI(ABC):

    @abstractmethod
    def create_button() -> IButton:
        pass

    @abstractmethod
    def create_slider() -> ISlider:
        pass


class WinUiFactory(IGUI):
    def create_button():
        return WinButton()

    def create_slider():
        return WinSlider()


class MacUiFactory(IGUI):
    def create_button():
        return MacButton()

    def create_slider():
        return MacSlider()


class UI:
    """Config the current factory"""

    def __init__(self) -> None:
        is_windows = os.name == 'nt'
        self.factory = WinUiFactory() if is_windows else MacUiFactory


def main():
    ui = UI()
    button = ui.factory.create_button()
    slider = ui.factory.create_slider()

    print(button)
    print(slider)


main()
