import cv2
import pydirectinput
from mss import mss
import numpy as np
import os
import time

class AImg:
    bbox = None
    def __init__(self, localimg, vvar):
        self.VVAR = vvar
        self.THRESHOLD = False
        self.READSCR = None
        self.READIMG = None
        self.LOCALIMG = localimg
        self.RESULT = None

        self.MAX_LOC = None

        self.W = None
        self.H = None
        self.max_val = None

    def analyzer(self, imagem, source):
        self.READIMG = cv2.imread(self.LOCALIMG + '/' + imagem, cv2.COLOR_BGRA2BGR)

        self.RESULT = cv2.matchTemplate(source, self.READIMG, cv2.TM_CCOEFF_NORMED)

        min_val, self.max_val, min_loc, self.MAX_LOC = cv2.minMaxLoc(self.RESULT)

        if self.max_val >= self.VVAR:
            self.W = self.READIMG.shape[1]
            self.H = self.READIMG.shape[0]
            self.THRESHOLD = True
        else:
            self.THRESHOLD = False

    class Clicker:
        def __init__(self, pai):
            self.pai = pai
            self.X = (pai.MAX_LOC[0] + int(pai.W / 2) + AImg.bbox[0]) if pai.THRESHOLD else None
            self.Y = (pai.MAX_LOC[1] + int(pai.H / 2) + AImg.bbox[1]) if pai.THRESHOLD else None
            if not pai.THRESHOLD:
                return

        def clicar(self):
            pydirectinput.click(self.X, self.Y)

        def mover(self):
            pydirectinput.moveTo(self.X, self.Y)

    class Printer:
        def printar(self):
            with mss() as sct:
                # Configurar as opções de captura
                monitor = sct.monitors[1]  # Índice do monitor (0 para o primeiro monitor, 1 para o segundo, etc.)
                capture_options = {
                    "top": monitor["top"],  # Posição superior do monitor
                    "left": monitor["left"],  # Posição esquerda do monitor
                    "width": monitor["width"],  # Largura do monitor
                    "height": monitor["height"],  # Altura do monitor
                }
                screenshot = sct.grab(capture_options)
                screenshot_np = np.array(screenshot)

                screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_BGRA2BGR)
                AImg.bbox = (capture_options["left"], capture_options["top"], capture_options["left"] + capture_options["width"], capture_options["top"] + capture_options["height"])
                return screenshot_cv

    def Mouse(self):
        return AImg.Clicker(self)

    def WaitUntil(self, source, *click):
        screen = self.Printer.printar(self)
        self.analyzer(source, screen)
        while not self.THRESHOLD:
            screen = self.Printer.printar(self)
            self.analyzer(source, screen)
        if not click:
            self.Mouse().clicar()

    def WaitDisappear(self, source):
        screen = self.Printer.printar(self)
        self.analyzer(source, screen)
        while self.THRESHOLD:
            screen = self.Printer.printar(self)
            self.analyzer(source, screen)

    def WaitIf(self, *sources):
        self.THRESHOLD = False
        while not self.THRESHOLD:
            for num, source in enumerate(sources, start=1):
                screen = self.Printer.printar(self)
                self.analyzer(source, screen)
                if self.THRESHOLD:
                    return f"{num} Valido"

    def Exists(self, source):
        screen = self.Printer.printar(self)
        self.analyzer(source, screen)
        if self.THRESHOLD:
            return True
        else:
            return False


if __name__ == '__main__':
    aiai = AImg("imgs", 0.9)

    aiai.WaitUntil("sarvo.png")


