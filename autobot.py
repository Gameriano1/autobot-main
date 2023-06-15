import glob
import json
import os
import threading
import time
from winreg import *
import pygetwindow as gw
import shutil
import datetime
import requests
import urllib3
import subprocess
import pytz
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import keyboard
from IA import LogadorBOT
from IA.intell import IAA
from source import *
from selenium import webdriver


class AutoFarm:
    def __init__(self):
        key = OpenKey(HKEY_CURRENT_USER, r'Control Panel\International\Geo', 0, KEY_ALL_ACCESS)
        SetValueEx(key, "Name", 0, REG_SZ, "BR")
        SetValueEx(key, "Nation", 0, REG_SZ, "32")
        self.diretorio_atual = os.getcwd()
        self.caminho_filho = os.path.join(self.diretorio_atual, 'IA')
        self.email = None
        self.senha = None
        self.primeiralinha = None
        self.ismain = None
        self.quantidade = None

    def start(self):
        ismain = False
        if os.path.isfile("IA/configs/user.json"):
            with open("IA/configs/user.json", "r") as user:
                userlido = json.load(user)
                ismain = True if userlido["UserPrincipal"] == os.getlogin() else None

        if ismain is not None:
            principal = input("Digite 1 para definir o usuario principal\n") if not ismain else None

        if not os.path.isfile("IA/configs/user.json"):
            if principal == "1":
                with open("IA/configs/user.json", "a") as user:
                    userjson = json.dumps({"UserPrincipal": os.getlogin()})
                    user.write(userjson + "\n")
                    exit()
        self.ismain = ismain
        return ismain

    def getacc(self):
        with open(f"IA/usuariostxt/farmando/{os.getlogin()}bot.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
            if not len(linhas):
                raise Exception("sem contas adicionadas no txt!")
            self.primeiralinha = linhas[0]
            self.email, self.senha = str(self.primeiralinha).split(';')
            linhas.remove(self.primeiralinha)

        with open(f"IA/usuariostxt/farmando/{os.getlogin()}bot.txt", 'w') as arquivo:
            arquivo.writelines(linhas)

    def quantidadeusuarios(self):
        quantidade = False
        if os.path.isfile("IA/configs/quantidade.json"):
            with open("IA/configs/quantidade.json", "r") as user:
                userlido = json.load(user)
                quantidade = int(userlido["Quantidade"]) if int(userlido["Quantidade"]) > 0 else None

        if quantidade is not None:
            quantia = int(input("Quantos usuarios vão ser feitos?\n")) if not quantidade else None

        if not os.path.isfile("IA/configs/quantidade.json"):
            if quantia > 0:
                with open("IA/configs/quantidade.json", "a") as user:
                    userjson = json.dumps({"Quantidade": quantia})
                    user.write(userjson + "\n")
                    exit()
        self.quantidade = quantidade
        return quantidade

    def logar(self):
        print("Logando contas no windows")
        logador = LogadorBOT.AutoLogin("s", f"IA/usuariostxt/farmando/{os.getlogin()}.txt", delete=False)
        os.chdir(self.caminho_filho)
        logador.loginAPI(self.email, self.senha)
        os.chdir(self.diretorio_atual)
        print("Contas logadas no windows\n\n")

    def fiddler(self, method="open"):
        os.chdir(self.caminho_filho)
        if method == "open":
            print("Abrindo o Fiddler")
            if os.getlogin() == "Black":
                os.startfile(fr"C:\Users\{str(os.getlogin())}\OneDrive\Área de Trabalho\Fiddler Classic.lnk")
            else:
                os.startfile(fr"C:\Users\{str(os.getlogin())}\Desktop\Fiddler Classic.lnk")
            time.sleep(2.5)
            controller, imprimir = IAA.AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                            0.8), IAA.AImg.Printer("Progress Telerik Fiddler Classic")
            valid = controller.WaitIf("simfiddler.png", "fiddlerdocument.png")
            if valid == "1 Valido":
                controller.WaitUntil("simfiddler.png")
            time.sleep(2.5)
            print("Fiddler aberto\n\n")
        elif method.lower() == "close":
            window = gw.getWindowsWithTitle('Progress Telerik Fiddler Classic')[0]
            window.close()
            print("Fiddler fechado\n\n")
        os.chdir(self.diretorio_atual)

    def rewards(self):
        print("Logando no rewards")
        os.chdir(self.caminho_filho)
        if os.getlogin() == "Black":
            os.startfile(fr"C:\Users\{str(os.getlogin())}\OneDrive\Área de Trabalho\Microsoft Rewards.lnk")
        else:
            os.startfile(fr"C:\Users\{str(os.getlogin())}\Desktop\Microsoft Rewards.lnk")
        time.sleep(2.5)
        controller, imprimir = IAA.AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                        0.8), IAA.AImg.Printer("Microsoft Rewards")
        valid = controller.WaitIf("experimente.png", "detalhamento.png")
        if valid == "1 Valido":
            controller.WaitUntil("experimente.png")
            controller.WaitUntil("detalhamento.png", True)
            time.sleep(4)
        elif valid == "2 Valido":
            controller.WaitUntil("detalhamento.png", True)
            time.sleep(4)
        subprocess.run("taskkill /IM Microsoft.Rewards.Xbox.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.chdir(self.diretorio_atual)
        print("Rewards logado\n\n")

    def xbox(self):
        print("Logando no xbox")
        os.chdir(self.caminho_filho)

        if os.getlogin() == "Black":
            os.startfile(fr"C:\Users\{str(os.getlogin())}\OneDrive\Área de Trabalho\Xbox.lnk")
        else:
            os.startfile(fr"C:\Users\{str(os.getlogin())}\Desktop\Xbox.lnk")
        time.sleep(2.5)
        controller, imprimir = IAA.AImg("intell/imgs", "intell/imgs/users", str(os.getlogin()) + '.png',
                                        0.8), IAA.AImg.Printer("Xbox")
        controller.WaitUntil("xboxg.png", True)
        time.sleep(1.5)
        existe = controller.Exists("entrar.png")
        if not existe:
            time.sleep(2)
            print("A conta já esta logada no xbox\n\n")
        else:
            controller.WaitUntil("entrar.png")
            controller.WaitUntil("entrarxbox.png")
            time.sleep(3.5)
            ife = controller.WaitIf("xbox.png", "pausa.png")
            if ife == "1 Valido":
                controller.WaitUntil("xbox.png", True)
                time.sleep(2.5)
                controller.WaitUntil("vamosjogar.png")
                valido = controller.WaitIf("tentarnovamente.png", "pausa.png")
                if valido == "1 Valido":
                    controller.WaitUntil("tentarnovamente.png")
                    controller.WaitUntil("pausa.png", True)
                    time.sleep(2.5)
                else:
                    time.sleep(2.5)
                print("Xbox logado\n\n")
            else:
                time.sleep(2)
                print("a conta já esta logada no xbox\n\n")
        subprocess.run("taskkill /IM XboxPcApp.exe /F", stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        subprocess.run("taskkill /IM XboxApp.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        os.chdir(self.diretorio_atual)
        return

    def processrewards(self):
        countries = ['ITIT', 'ENNZ', 'PTBR']
        cc = ['IT', 'NZ', 'BR']
        mscv = []
        auth = []
        cookies = []

        my_files = glob.glob('rewards\*.txt')
        if not len(my_files):
            raise Exception("Arquivos Faltando")
        for s in my_files:
            try:
                with open(s, "r") as v:
                    x = v.readlines()
                    authorization = [linha for linha in x if linha.__contains__("Authorization: ")]
                    authorization = authorization[0].strip()
                    authorization = authorization.replace("Authorization: ", "")
                    auth.append(authorization)

                    ms = [linha for linha in x if linha.__contains__("MS-CV: ")]
                    ms = ms[0].strip()
                    ms = ms.replace("MS-CV: ", "")
                    mscv.append(ms)

                    cookie = [linha for linha in x if linha.__contains__("Cookie: ")]
                    cookie = cookie[0].strip()
                    cookie = cookie.replace("Cookie: ", "")
                    cookies.append(cookie)
                threads = []
                for v, i, u in zip(auth, mscv, cookies):
                    for country, count in zip(countries, cc):
                        t = threading.Thread(target=Farm.RewardsRun, args=(v, i, u, country, count))
                        threads.append(t)
                        t.start()
                for t in threads:
                    t.join()
            except:
                os.remove(s)
                raise Exception("Arquivo " + s + " é uma bosta e nois vai deletar ele kk")

    def farmxbox(self):

        xuid = []
        authrewards = []
        auth = []

        my_files = glob.glob('xbox\*.txt')
        if not len(my_files):
            raise Exception("Arquivos Faltando")

        for s in my_files:
            x2 = s.replace("xbox\\", "")
            x2 = x2.replace("xbox", "")
            try:
                with open("rewards/" + x2, "r") as f:
                    x = f.readlines()
                    authorization = [linha for linha in x if linha.__contains__("Authorization: ")]
                    authorization = authorization[0].strip()
                    authorization = authorization.replace("Authorization: ", "")
                    authrewards.append(authorization)
            except:
                print("Arquivos rewards faltando ou deletados")
                return

            with open(s, "r") as f:
                x = f.readlines()
                authorization = [linha.replace("authorization: ", "") for linha in x if
                                 linha.__contains__("Authorization: ") or linha.__contains__("authorization: ")]
                authorization = [linha.replace("Authorization: ", "") for linha in authorization]
                auth.append(authorization[0].strip())

                xuide = [linha.strip() for linha in x if linha.__contains__("users")]
                xuide = [linha.replace("HTTP/1.1", "") for linha in xuide]
                xuide = str(''.join(i for i in xuide[0] if i.isdigit()))
                xuid.append(xuide)
        threads = []
        for x, i, a in zip(xuid, auth, authrewards):
            t = threading.Thread(target=Xbox.conquista, args=(x, i, a))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

    def getaccs(self, quantidade, delete: bool = False):

        with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
        primeiras_linhas = linhas[:quantidade]
        if not delete:
            with open(f"IA/usuariostxt/farmando/{os.getlogin()}bot.txt", "w") as contabot:
                for l in primeiras_linhas:
                    divisaocontas = str(l).split(";")
                    contabot.write(divisaocontas[0] + ";" + divisaocontas[1])
        else:
            with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'w') as arquivo:
                arquivo.writelines(linhas[quantidade:])
            with open(f"IA/usuariostxt/concluido/{os.getlogin()}completas.txt", 'a') as arquivo:
                arquivo.writelines(linhas[:quantidade])

    def sincronizar(self, quantidade, pasta="users"):
        try:
            os.mkdir(f"IA/usuariostxt/{pasta}")
        except:
            pass
        arquivo_temporario = str(os.getlogin()) + ".txt"

        while True:
            try:
                open(f"IA/usuariostxt/{pasta}/" + arquivo_temporario, "w").close()
                break
            except:
                pass
        print("Esperando todos os usuarios sincronizarem")
        try:
            while not len(os.listdir(f"IA/usuariostxt/{pasta}")) >= quantidade:
                continue
        except:
            pass
        if not self.ismain:
            while os.path.exists(f"IA/usuariostxt/{pasta}"):
                continue
        else:
            while True:
                try:
                    shutil.rmtree(f'IA/usuariostxt/{pasta}')
                    break
                except:
                    pass
        print("Sincronizado\n\n")


class Login:
    def __init__(self):
        self.delay = 8

        self.chrome_options = ChromeOptions()

        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome_options.add_argument('--log-level=3')

        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")

    def bingantibug(self,
                    xpath, driverz):
        try:
            WebDriverWait(driverz, self.delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            raise Exception('A Pagina nao carregou a tempo')

    def logarsite(self, email, senha):

        print("Começando a Logar no Site")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                  options=self.chrome_options)
        try:
            driver.get(
                'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1%26sig%3d387A7E8F86D465B53DD36C1487C06411&wp=MBI_SSL&lc=1046&CSRFToken=68214017-1e42-4484-bc17-b8a7323b9b91&aadredir=1')

            self.bingantibug('//*[@id="i0116"]', driver)
            driver.find_element('xpath', '//*[@id="i0116"]').send_keys(email)

            self.bingantibug('//*[@id="idSIButton9"]', driver)
            driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
            time.sleep(2)

            self.bingantibug('//*[@id="i0118"]', driver)
            driver.find_element('xpath', '//*[@id="i0118"]').send_keys(senha)

            self.bingantibug('//*[@id="idSIButton9"]', driver)
            driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
            titulo = driver.title
            while titulo == "Continuar":
                titulo = driver.title
            while titulo == "Ajude-nos a proteger sua conta":
                try:
                    self.bingantibug('//*[@id="iShowSkip"]', driver)
                    driver.find_element('xpath', '//*[@id="iShowSkip"]').click()
                except:
                    pass
                titulo = driver.title
            time.sleep(1.5)
            titulo = driver.current_url
            if titulo.__contains__("bing"):
                pass
            else:
                self.bingantibug('//*[@id="idSIButton9"]', driver)
                driver.find_element('xpath', '//*[@id="idSIButton9"]').click()
            driver.get("https://bing.com/")
            time.sleep(4)
            cookiesbing = driver.get_cookies()

            driver.quit()
            print("Site logado\n\n")

            return cookiesbing

        except Exception as e:
            raise Exception(e)

    def checkpesquisa(self):
        while True:
            try:
                with open(f"rewards/{os.getlogin()}.txt", "r") as v:
                    x = v.readlines()
                    authorization = [linha for linha in x if linha.__contains__("Authorization: ")]
                    authorization = authorization[0].strip()
                    authorization = authorization.replace("Authorization: ", "")
                saldo = checkpesquisa(authorization)
                return int(saldo)
            except:
                continue

    def pesquisa(self, pontos: int, cookiesb, pais):
        print("Pesquisando")

        os.chdir(autofarm.diretorio_atual)
        with open("source/tampermonkey.js") as file:
            tampermonkey_script = file.read()
        chrome_options = ChromeOptions()

        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')

        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36")

        driverabs = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driverabs.get("https://bing.com/")
        self.delay = 6
        while True:
            try:
                self.bingantibug('//*[@id="sb_form_c"]', driverabs)
                break
            except:
                login.connect(pais) if autofarm.ismain else None
                login.get_location(pais)
                time.sleep(2.5)
                while True:
                    try:
                        driverabs.get("https://bing.com")
                        break
                    except:
                        time.sleep(1.5)
                        continue
                continue
        for cookie in cookiesb:
            driverabs.add_cookie(cookie)
        driverabs.refresh()
        while True:
            try:
                self.bingantibug('//*[@id="sb_form_c"]', driverabs)
                break
            except:
                login.connect(pais) if autofarm.ismain else None
                login.get_location(pais)
                time.sleep(2.5)
                while True:
                    try:
                        driverabs.get("https://bing.com")
                        break
                    except:
                        time.sleep(1.5)
                        continue
                continue
        self.delay = 8
        time.sleep(1.5)
        quantidade = self.checkpesquisa()
        tries = 0
        while int(quantidade) < pontos:
            if tries > 5:
                login.connect(pais) if autofarm.ismain else None
                login.get_location(pais)
                time.sleep(2.5)
                print("Depois de executar o tampermonkey mais 5 vezes, sua quantidade de pontos ainda é: " + str(quantidade))
                tries = 0
            driverabs.execute_script(tampermonkey_script)
            quantidade = self.checkpesquisa()
            tries += 1
        driverabs.quit()
        print("Pesquisa Completa! \n\n")

    def obter_horario_brasilia(self):
        tz_brasilia = pytz.timezone('America/Sao_Paulo')
        horario_atual_brasilia = datetime.datetime.now(tz_brasilia)
        hora_atual_brasilia = horario_atual_brasilia.hour

        return hora_atual_brasilia

    def desbugar(self, quantidade):
        if not os.path.isfile(f"IA/usuariostxt/{os.getlogin()}.txt"):
            open(f"IA/usuariostxt/{os.getlogin()}.txt", 'w').close()

        with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
            linhas = arquivo.readlines()
        while len(linhas) < quantidade:
            print("Desbugando contas")
            desbugador = Desbug(quantidade - len(linhas), "1116093603199057961")
            desbugador.main(True)
            with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
                linhas = arquivo.readlines()
            print("Contas desbugadas\n\n")

    def get_location(self, pais):
        urllib3.disable_warnings()
        while True:
            try:
                ip_address = requests.get('https://www.trackip.net/ip?json', verify=False).json()
                ip_address = ip_address["IP"]
                response = requests.get(f"https://api.findip.net/{ip_address}/?token=f3038d016cbc4511b927e2f792342c38",
                                        verify=False).json()
                if response["country"]["names"]["en"].lower() == pais.lower():
                    return
            except:
                pass

    def connect(self, pais, *disconnect):
        if not disconnect:
            print("Conectando a vpn")
            subprocess.Popen(["nordvpn", "-c", "-g", pais], shell=True, cwd='C:/Program Files/NordVPN',
                             stdout=-3)
            self.get_location(pais)
            print("Conectado a " + pais + "\n\n")
        else:
            print("Desconectando a vpn")
            subprocess.Popen(["nordvpn", "-d"], shell=True, cwd='C:/Program Files/NordVPN', stdout=-3)
            self.get_location("brazil")
            print("Desconectado\n\n")


if __name__ == '__main__':

    while not keyboard.is_pressed("q"):

        autofarm = AutoFarm()
        login = Login()

        ismain = autofarm.start()
        usuarios = autofarm.quantidadeusuarios()
        if ismain:
            rewards = os.listdir("rewards")
            xbox = os.listdir("xbox")

            if len(xbox) > 0:
                for arquivox in xbox:
                    caminho_completox = os.path.join("xbox", arquivox)
                    os.remove(caminho_completox)

            if len(rewards) > 0:
                for arquivor in rewards:
                    caminho_completor = os.path.join("rewards", arquivor)
                    os.remove(caminho_completor)
        print("--------------- Começando ---------------\n\n")
        login.connect("",True) if autofarm.ismain else None
        login.get_location("brazil")
        time.sleep(2.5)
        login.desbugar(1)
        autofarm.getaccs(1)
        autofarm.getacc()

        autofarm.logar()
        autofarm.fiddler()
        autofarm.rewards()
        while not os.path.isfile(f"rewards/{os.getlogin()}.txt"):
            print("Refazendo o rewards por falta de txt.")
            autofarm.rewards()
            time.sleep(2)
        autofarm.sincronizar(quantidade=usuarios)
        autofarm.xbox()
        while not os.path.isfile(f"xbox/{os.getlogin()}xbox.txt"):
            autofarm.xbox()
            time.sleep(2)
        autofarm.fiddler("close")
        autofarm.sincronizar(quantidade=usuarios)
        time.sleep(2)

        if autofarm.ismain:
            print("Fazendo as tasks do aplicativo/conquista do xbox")
            rewardsthread = threading.Thread(target=autofarm.processrewards)
            xboxthread = threading.Thread(target=autofarm.farmxbox)
            rewardsthread.start()
            xboxthread.start()
            rewardsthread.join()
            xboxthread.join()
            print("Tasks feitas!\n\n")

        autofarm.sincronizar(quantidade=usuarios)
        cookiesbing = login.logarsite(autofarm.email, autofarm.senha)
        while cookiesbing is None:
            cookiesbing = login.logarsite(autofarm.email, autofarm.senha)

        autofarm.sincronizar(quantidade=usuarios)
        login.connect("italy") if autofarm.ismain else None
        login.get_location("italy")
        autofarm.sincronizar(quantidade=usuarios)
        autofarm.fiddler()
        login.pesquisa(1000, cookiesbing, "italy")
        autofarm.sincronizar(quantidade=usuarios)

        hora_atual = login.obter_horario_brasilia()
        if int(hora_atual) < 20:
            login.connect("new zealand") if autofarm.ismain else None
            login.get_location("new zealand")
            autofarm.sincronizar(quantidade=usuarios)
            login.pesquisa(2000, cookiesbing, "new zealand")
        else:
            login.connect("brazil") if autofarm.ismain else None
            login.get_location("brazil")
            autofarm.sincronizar(quantidade=usuarios)
            login.pesquisa(2000, cookiesbing, "brazil")

        autofarm.sincronizar(quantidade=usuarios)
        autofarm.fiddler("close")
        autofarm.getaccs(1, True)
        # driver.close()
        print("FINALIZADO!!!!!!!!!!!!!!!!!!!\n\n")
