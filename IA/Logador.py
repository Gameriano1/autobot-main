import os
import time
from winreg import *
import mouse
import pyautogui
import subprocess
import pygetwindow as gw

from intell.IAA import AImg

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

ROBUX = "robux.png"
OITENTAROBUX = "80robux.png"
ENDERECO = "endereco.png"
PRECISAMOS = "precisamos.png"
SELECIONARESTADO = "selecionarestado.png"
AGRIGENTO = "agrigento.png"
CEP = "cep.png"
SALVAR = "salvar.png"
COMPRAR = "comprar.png"
FECHAR = "fechar.png"
FECHARROBUX = "fecharrobux.png"
CLOSE = "close.png"
USEESSACONTA = "useessaconta.png"
AJUDENOS = "ajudenos.png"
PREMIUM = "premium.png"
PAGAR = "pagar.png"


class AutoLogin:
    def __init__(self, logada, txt="accs.txt"):
        self.logada = logada.lower()
        self.txt = txt

    def normal(self):

        with open(self.txt, 'r') as arquivo:
            linhas = arquivo.readlines()
            if not len(linhas):
                raise Exception("sem contas adicionadas no txt!")
            primeiralinha = linhas[0]
            linhas.remove(primeiralinha)

        with open(self.txt, 'w') as arquivo:
            arquivo.writelines(linhas)

        email, senha = str(primeiralinha).split(';')
        print(email + ";" + senha)

        os.system("start ms-settings:")
        time.sleep(1)
        controller = AImg("intell/imgs", 0.9)

        controller.WaitUntil(CONTAS)
        controller.WaitDisappear(CONTAS)

        controller.WaitUntil(CAMERA, True)
        parar = controller.Exists(PARAR_DE_ENTRAR)
        print("parar entrar")
        if parar:
            controller.WaitUntil(PARAR_DE_ENTRAR)

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
        os.system("taskkill /IM SystemSettings.exe /F")

    def roblox(self):

        with open(f"usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
        emails, senhas = [], []
        for l in linhas:
            divisaocontas = str(l).split(";")
            emails.append(divisaocontas[0])
            senhas.append(divisaocontas[1])

        for email, senha in zip(emails, senhas):
            print(email + ";" + senha)
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

            if os.getlogin() == "Black":
                os.startfile(fr"C:\Users\{str(os.getlogin())}\OneDrive\Área de Trabalho\Roblox.lnk")
            else:
                os.startfile(fr"C:\Users\{str(os.getlogin())}\Desktop\Roblox.lnk")
            time.sleep(4)
            controller.WaitUntil(ROBUX)
            controller.WaitUntil(OITENTAROBUX)
            controller.WaitUntil(SENHA)
            pyautogui.write(senha)
            controller.WaitUntil(ENTRARBOTAO)
            valid = controller.WaitIf(ENDERECO, COMPRAR)
            if valid == "1 Valido":
                controller.WaitUntil(ENDERECO)
                controller.WaitUntil(PRECISAMOS, True)
                for i in range(2):
                    time.sleep(0.3)
                    pyautogui.write("asd")
                    pyautogui.press("enter")
                controller.WaitUntil(PRECISAMOS)
                mouse.wheel(-500)
                time.sleep(1)
                controller.WaitUntil(SELECIONARESTADO)
                time.sleep(0.5)
                controller.WaitUntil(AGRIGENTO)
                time.sleep(1)
                controller.WaitUntil(CEP)
                pyautogui.write("11111")
                controller.WaitUntil(SALVAR)
            while True:
                controller.WaitUntil(COMPRAR)
                fecha = controller.WaitIf(FECHAR, CLOSE)
                if fecha == "1 Valido":
                    controller.WaitUntil(FECHAR)
                else:
                    controller.WaitUntil(CLOSE)
                controller.WaitUntil(OITENTAROBUX)
                controller.WaitUntil(SENHA)
                pyautogui.write(senha)
                controller.WaitUntil(ENTRARBOTAO)
                controller.WaitUntil(PREMIUM, True)
                existe = controller.Exists(PAGAR)
                if existe:
                    window = gw.getWindowsWithTitle('Roblox')[0]
                    window.close()
                    break
            primeiralinha = linhas[0]
            linhas.remove(primeiralinha)

            with open(f"usuariostxt/{os.getlogin()}.txt", 'w') as arquivo:
                arquivo.writelines(linhas)

    def loginAPI(self):
        if self.logada == "r":
            return self.roblox()
        elif self.logada == "s":
            return self.normal()
        else:
            raise Exception("digite um valor valido!")

if __name__ == '__main__':
    logada = input("usar para roblox? R para roblox S para normal\n")

    logar = AutoLogin(logada, "accs.txt")
    if logada.lower() == "r":
        key = OpenKey(HKEY_CURRENT_USER, r'Control Panel\International\Geo', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "Name", 0, REG_SZ, "IT")
        SetValueEx(key, "Nation", 0, REG_SZ, "118")
        logar.loginAPI()
    else:
        logar.loginAPI()
