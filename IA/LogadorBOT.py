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
SIMREMOVER = "yes.png"
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
GERENCIAR = "gerenciar.png"
INFOS = "suasinformacoes.png"


class AutoLogin:
    def __init__(self, logada, txt="accs.txt", delete=True):
        self.logada = logada.lower()
        self.txt = txt
        self.delete = delete

    def normal(self, email, senha):

        os.system("start ms-settings:")
        time.sleep(1)
        controller = AImg("intell/imgs", 0.9)

        controller.WaitUntil(CONTAS)

        controller.WaitUntil(CAMERA, True)
        parar = controller.Exists(PARAR_DE_ENTRAR)
        print("parar entrar")
        if parar:
            controller.WaitUntil(PARAR_DE_ENTRAR)
            controller.WaitDisappear(PARAR_DE_ENTRAR)
            time.sleep(3)

        controller.WaitUntil(EMAILS_E_CONTAS)
        controller.WaitUntil(EMALIS, True)
        if parar:
            while True:
                time.sleep(3.5)
                existe = controller.Exists(MS_LOGO)
                if existe:
                    controller.WaitUntil(MS_LOGO)
                    time.sleep(1)
                    existe = controller.Exists(REMOVERBOTAO)
                    if existe:
                        controller.WaitUntil(REMOVERBOTAO)
                    while not existe:
                        controller.WaitUntil(INFOS)
                        controller.WaitUntil(CAMERA, True)
                        existe = controller.Exists(PARAR_DE_ENTRAR)
                        if existe:
                            controller.WaitUntil(PARAR_DE_ENTRAR)
                            controller.WaitDisappear(PARAR_DE_ENTRAR)
                            time.sleep(3)
                        controller.WaitUntil(EMAILS_E_CONTAS)
                        controller.WaitUntil(MS_LOGO)
                        existe = controller.Exists(REMOVERBOTAO)
                        if existe:
                            controller.WaitUntil(REMOVERBOTAO)
                    controller.WaitUntil(SIMREMOVER)
                    controller.WaitUntil(INFOS)
                    controller.WaitUntil(CAMERA, True)
                    controller.WaitUntil(EMAILS_E_CONTAS)
                    controller.WaitUntil(EMALIS, True)
                    time.sleep(1.5)
                    controller.WaitDisappear(MS_LOGO)
                    break
                else:
                    break

        controller.WaitUntil(ADICIONAR_CONTA)
        controller.WaitUntil(OUTLOOK_COM)
        controller.WaitUntil(CONTINUARBUTAO)
        controller.WaitUntil(EMAIL)
        pyautogui.write(email)
        controller.WaitUntil(PROXIMOBOTAO)
        controller.WaitUntil(SENHA)
        pyautogui.write(senha)
        controller.WaitUntil(ENTRARBOTAO)
        existe = controller.WaitIf(PROXIMOUSARESSACONTA, PROXIMOBOTAO)
        if existe == "1 Valido":
            controller.WaitUntil(PROXIMOUSARESSACONTA)
        if existe == "2 Valido":
            controller.WaitUntil(PROXIMOBOTAO)
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
