import os
import time
import pyautogui
import subprocess
from .intell.IAA import AImg

CONTAS = "contas.png"
EMALIS = "emalis.png"
UPDATE = "upd.png"
PARAR_DE_ENTRAR = "parar_entrar.png"
CAMERA = "camera.png"
EMAILS_E_CONTAS = "emailsecontas.png"
MS_LOGO = "mslogo.png"
REMOVERBOTAO = "removerbotao.png"
SIMREMOVER = "simremover.png"
ADICIONAR_CONTA = "adicionarconta.png"
OUTLOOK_COM = "outlookcom.png"
CONTINUARBUTAO = "continuarbotao.png"
EMAIL = "email.png"
PROXIMOBOTAO = "proximobotao.png"
SENHA = "senha.png"
ENTRARBOTAO = "entrarbotao.png"
PROXIMOUSARESSACONTA = "proximousaressaconta.png"
CONCLUIDOBOTAO = "concluidobotao.png"
AGUARDE = "aguarde.png"


class AutoLogin:
    def __init__(self, logada, txt="accs.txt", delete=True):
        self.logada = logada.lower()
        self.txt = txt
        self.delete = delete

    def normal(self, email, senha):

        # with open(self.txt, 'r') as arquivo:
        #     linhas = arquivo.readlines()
        #     if not len(linhas):
        #         raise Exception("sem contas adicionadas no txt!")
        #     self.primeiralinha = linhas[0]
        #     if self.delete:
        #         linhas.remove(self.primeiralinha)
        #
        #         with open(self.txt, 'w') as arquivo:
        #             arquivo.writelines(linhas)

        # self.email, self.senha = str(self.primeiralinha).split(';')
        # print(self.email + ";" + self.senha)

        os.system("start ms-settings:")
        time.sleep(1)
        controller, imprimir = AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                    0.8), AImg.Printer()

        controller.WaitUntil(CONTAS)
        controller.WaitDisappear(UPDATE)

        controller.WaitUntil(CAMERA, True)
        parar = controller.Exists(PARAR_DE_ENTRAR)
        print("parar entrar")
        if parar:
            controller.WaitUntil(PARAR_DE_ENTRAR)
            time.sleep(1.5)

        controller.WaitUntil(EMAILS_E_CONTAS)
        controller.WaitUntil(EMALIS)
        time.sleep(1.5)
        para = controller.Exists(MS_LOGO)
        if para:
            controller.WaitUntil(MS_LOGO)
            controller.WaitUntil(REMOVERBOTAO)
            controller.WaitUntil(SIMREMOVER)
        controller.WaitUntil(ADICIONAR_CONTA)
        controller.WaitUntil(OUTLOOK_COM)
        controller.WaitUntil(CONTINUARBUTAO)
        controller.WaitUntil(EMAIL)
        pyautogui.write(email)
        controller.WaitUntil(PROXIMOBOTAO)
        controller.WaitUntil(SENHA)
        pyautogui.write(senha)
        controller.WaitUntil(ENTRARBOTAO)
        controller.WaitUntil(PROXIMOUSARESSACONTA)
        controller.WaitDisappear(AGUARDE)
        subprocess.run("taskkill /IM SystemSettings.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def loginAPI(self, email, senha):
        if self.logada == "s":
            return self.normal(email,senha)
        else:
            raise Exception("digite um valor valido!")

if __name__ == '__main__':
    logada = input("usar para roblox? R para roblox S para normal\n")

    logar = AutoLogin(logada, "accs.txt")
    logar.loginAPI()
