import cv2
import pydirectinput
from mss import mss
import mss.tools as mss_tools
import ctypes
import os


class AImg:
    bbox = None
    def __init__(self, localimg,localsrc, src, vvar):
        self.LOCALSRC = localsrc
        self.VVAR = vvar
        self.THRESHOLD = False
        self.SRC = src
        self.READSCR = None
        self.READIMG = None
        self.LOCALIMG = localimg
        self.RESULT = None

        self.MAX_LOC = None

        self.W = None
        self.H = None
        self.max_val = None

    def analyzer(self, img):
        self.READSCR = cv2.imread(self.LOCALSRC + '/' + self.SRC, cv2.IMREAD_ANYCOLOR)
        self.READIMG = cv2.imread(self.LOCALIMG + '/' + img, cv2.IMREAD_ANYCOLOR)

        self.RESULT = cv2.matchTemplate(self.READSCR, self.READIMG, cv2.TM_CCOEFF_NORMED)

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
        def __init__(self, *app):
            with mss():
                hwnd = ctypes.windll.user32.FindWindowW(0, app[0] if app else "Configurações")
                rect = ctypes.wintypes.RECT()
                ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))

            AImg.bbox = (rect.left, rect.top, rect.right, rect.bottom)

        def printar(self, nome, diretorio):
            with mss() as sct:
                shot = sct.grab(AImg.bbox)
                mss_tools.to_png(shot.rgb, shot.size, output=diretorio + '/' + nome)

    def Mouse(self):
        return AImg.Clicker(self)

    def WaitUntil(self, source, *click):
        self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
        self.analyzer(source)
        while not self.THRESHOLD:
            self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
            self.analyzer(source)
        if not click:
            self.Mouse().clicar()

    def WaitDisappear(self, source):
        self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
        self.analyzer(source)
        while self.THRESHOLD:
            self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
            self.analyzer(source)

    def WaitIf(self, source1, source2):
        self.THRESHOLD = False
        while not self.THRESHOLD:
            self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
            self.analyzer(source1)
            if self.THRESHOLD:
                return "1 Valido"
            else:
                self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
                self.analyzer(source2)
                if self.THRESHOLD:
                    return "2 Valido"

    def Exists(self, source):
        self.Printer.printar(self, str(os.getlogin()) + '.png', "intell/imgs/users")
        self.analyzer(source)
        if self.THRESHOLD:
            return True
        else:
            return False


if __name__ == '__main__':

    cu, imprimir = AImg("imgs", "screen.png", 0.9), AImg.Printer("whatsapp")

    imprimir.printar("screen.png", "imgs")
    cu.analyzer("remove.png")

    cu.WaitUntil(cu, imprimir, "remove.png")


