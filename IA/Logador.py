import os
import time

import mouse
import pyautogui

from intell.IAA import AImg

CONTAS = "contas.png"
EMALIS = "emalis.png"
PARAR_DE_ENTRAR = "parar_entrar.png"
UPDATE = "upd.png"
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
        controller, imprimir = AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                    0.8), AImg.Printer()

        controller.WaitUntil(CONTAS)
        controller.WaitDisappear(UPDATE)

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

    def roblox(self, quantidade: int):

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
            controller, imprimir = AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                        0.8), AImg.Printer()

            controller.WaitUntil(CONTAS)
            controller.WaitDisappear(UPDATE)

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

            if os.getlogin() == "Black":
                os.startfile(fr"C:\Users\{str(os.getlogin())}\OneDrive\Área de Trabalho\Roblox.lnk")
            else:
                os.startfile(fr"C:\Users\{str(os.getlogin())}\Desktop\Roblox.lnk")
            time.sleep(4)
            controller, imprimir = AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                        0.8), AImg.Printer("Roblox")
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
            controller.WaitUntil(COMPRAR)
            fecha = controller.WaitIf(FECHAR, CLOSE)
            if fecha == "1 Valido":
                controller.WaitUntil(FECHAR)
            else:
                controller.WaitUntil(CLOSE)
            for _ in range(quantidade):
                controller.WaitUntil(OITENTAROBUX)
                controller.WaitUntil(SENHA)
                pyautogui.write(senha)
                controller.WaitUntil(ENTRARBOTAO)
                controller.WaitUntil(COMPRAR)
                fecha = controller.WaitIf(FECHAR, CLOSE)
                if fecha == "1 Valido":
                    controller.WaitUntil(FECHAR)
                else:
                    controller.WaitUntil(CLOSE)
            controller.WaitUntil(FECHARROBUX)
            primeiralinha = linhas[0]
            linhas.remove(primeiralinha)

            with open(f"usuariostxt/{os.getlogin()}.txt", 'w') as arquivo:
                arquivo.writelines(linhas)

    def loginAPI(self, *quantidade):
        if self.logada == "r":
            return self.roblox(quantidade[0])
        elif self.logada == "s":
            return self.normal()
        else:
            raise Exception("digite um valor valido!")

if __name__ == '__main__':
    logada = input("usar para roblox? R para roblox S para normal\n")

    logar = AutoLogin(logada, "accs.txt")
    if logada.lower() == "r":
        quantidade = int(input("comprar quantas vezes robux? PARA BOT MANUAL: 3, PARA O AUTOMATICO: 1\n")) if logada.lower() == "r" else None
        logar.loginAPI(quantidade)
    else:
        logar.loginAPI()