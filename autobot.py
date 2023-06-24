import glob
import json
import os
import random
import sys
import threading
import time
from winreg import *
import pygetwindow as gw
import shutil
import datetime
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib3
import subprocess
import pytz
import keyboard
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import string
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
            principal = input("Digite 1 para definir o usuario principal\n>> ") if not ismain else None

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
            quantia = int(input("Quantos usuarios vão ser feitos?\n>> ")) if not quantidade else None

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
            controller = IAA.AImg("intell/imgs", 0.8)
            valid = controller.WaitIf("simfiddler.png", "fiddlerdocument.png")
            if valid == "1 Valido":
                controller.WaitUntil("simfiddler.png")
            controller.WaitUntil("fiddlerdocument.png", True)
            time.sleep(2)
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
        controller = IAA.AImg("intell/imgs", 0.9)
        valid = controller.WaitIf("experimente.png", "detalhamento.png", "localizacao.png")
        if valid == "1 Valido":
            controller.WaitUntil("experimente.png")
            controller.WaitUntil("detalhamento.png", True)
            time.sleep(4)
        elif valid == "2 Valido":
            controller.WaitUntil("detalhamento.png", True)
            time.sleep(4)
        elif valid == "3 Valido":
            subprocess.run("taskkill /IM Microsoft.Rewards.Xbox.exe /F", stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            time.sleep(3.5)
            self.rewards()
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
        controller = IAA.AImg("intell/imgs", 0.9)
        controller.WaitUntil("xboxg.png", True)
        time.sleep(1.5)
        existe = controller.Exists("entrar.png")
        if not existe:
            time.sleep(3)
            print("A conta já esta logada no xbox\n\n")
        else:
            controller.WaitUntil("entrar.png")
            controller.WaitUntil("entrarxbox.png")
            controller.WaitDisappear("configs.png")
            time.sleep(4)
            ife = controller.WaitIf("xbox.png", "gamepass.png", "entrar2.png")
            if ife == "1 Valido" or ife == "3 Valido":
                if ife == "3 Valido":
                    controller.WaitUntil("entrar2.png")
                controller.WaitUntil("xbox.png", True)
                time.sleep(2.5)
                controller.WaitUntil("vamosjogar.png")
                valido = controller.WaitIf("tentarnovamente.png", "gamepass.png")
                if valido == "1 Valido":
                    controller.WaitUntil("tentarnovamente.png")
                    controller.WaitUntil("gamepass.png", True)
                    time.sleep(4)
                else:
                    time.sleep(4)
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
        self.delay = 25
        self.cookiesbing = None

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
            driver.maximize_window()
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
            self.cookiesbing = driver.get_cookies()

            driver.quit()
            print("Site logado\n\n")

        except:
            pass

    def checkpesquisa(self, pais):
        while True:
            try:
                with open(f"rewards/{os.getlogin()}.txt", "r") as v:
                    x = v.readlines()
                    authorization = [linha for linha in x if linha.__contains__("Authorization: ")]
                    authorization = authorization[0].strip()
                    authorization = authorization.replace("Authorization: ", "")
                saldo, pesquisa = checkpesquisa(authorization, pais)
                return int(saldo), int(pesquisa)
            except:
                continue

    def pesquisa(self, pontos: int, cookiesb, pais, quantidade=155):

        quantidade1, pesquisadas1 = self.checkpesquisa(pais)

        executor = ThreadPoolExecutor(max_workers=40)
        tasks = []

        for _ in range(int(quantidade) + 20):
            task = executor.submit(self.pesquisareq, self.cookiesbing)
            tasks.append(task)

        for task in as_completed(tasks):
            task.result()

        executor.shutdown(wait=True)

        quantidade2, pesquisadas2 = self.checkpesquisa(pais)
        sys.stdout.write("\rA Quantidade de Pontos ainda é: " + str(quantidade2))
        sys.stdout.flush()
        if int(pesquisadas1) == int(pesquisadas2):
            if int(pesquisadas2) < 50:
                if pais != "brazil":
                    print("\nA vpn provavelmente bugou, reconectando e refazendo")
                    self.connect(pais) if ismain else None
                    self.pesquisa(pontos, cookiesb, pais, quantidade=50 - int(pesquisadas2))
                else:
                    print("\nA vpn provavelmente bugou, reconectando e refazendo")
                    self.connect("", True) if ismain else None
                    self.pesquisa(pontos,cookiesb,pais, quantidade=50 - int(pesquisadas2))
        if int(quantidade2) < pontos:
            print("\nFazendo mais pesquisas!")
            self.pesquisa(pontos, cookiesb, pais, quantidade=50 - int(pesquisadas2))
        print("\nPesquisa Completa! \n\n")

    def pesquisareq(self, cookiesb):

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25",
            "sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.134", "Google Chrome";v="114.0.5735.134"',
            "Upgrade-Insecure-Requests": "1"
        }

        cookies_requests = {}

        for cookie in cookiesb:
            name = cookie['name']
            value = cookie['value']
            cookies_requests[name] = value

        palavra_aleatoria = ''.join(random.choices(string.ascii_lowercase, k=10))
        while True:
            try:
                response = requests.get(f"https://www.bing.com/search?q={palavra_aleatoria}", cookies=cookies_requests, headers=headers, verify=False)
                break
            except:
                continue
        if response.status_code != 200:
            print('Erro:', response.status_code)

    def verifica_velocidade_conexao(self):
        url = "https://www.bing.com"
        tempo_maximo = 7
        try:
            start_time = time.time()
            response = requests.get(url, timeout=tempo_maximo, verify=False)
            end_time = time.time()
            tempo_resposta = end_time - start_time

            if response.status_code == 200 and tempo_resposta <= tempo_maximo:
                return True
            else:
                return False
        except:
            return False

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
        if len(linhas) >= quantidade:
            deleta = input("Tem contas antigas catalogadas, deseja deletar elas? (S/N)\n>> ")
            if deleta.lower() == "s":
                os.remove(f"IA/usuariostxt/{os.getlogin()}.txt")
                open(f"IA/usuariostxt/{os.getlogin()}.txt", 'w').close()
                with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
                    linhas = arquivo.readlines()
            else:
                pass

        while len(linhas) < quantidade:
            print("Desbugando contas")
            desbugador = Desbug(quantidade - len(linhas), "1116093603199057961")
            desbugador.main(True)
            with open(f"IA/usuariostxt/{os.getlogin()}.txt", 'r') as arquivo:
                linhas = arquivo.readlines()
            print("Contas desbugadas\n\n")

    def get_location(self, pais):
        tries = 0
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
            tries += 1
            if ismain:
                if tries == 23:
                    self.connect(pais)
                    tries = 0

    def connect(self, pais, *disconnect):
        country = str(pais).replace(" ", "")
        if not disconnect:
            print("Conectando a vpn")
            subprocess.run("taskkill /IM openvpn.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run("taskkill /IM openvpn-gui.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            while True:
                try:
                    if os.path.isfile(f"IA/vpns/{country}.ovpn"):
                        os.remove(f"IA/vpns/{country}.ovpn")
                    if country == "newzealand":
                        ae = random.randint(83, 107)
                        url_servidor_nz = f"https://downloads.nordcdn.com/configs/files/ovpn_legacy/servers/nz{str(ae)}.nordvpn.com.udp1194.ovpn"
                    else:
                        ae = random.randint(186, 286)
                        url_servidor_nz = f"https://downloads.nordcdn.com/configs/files/ovpn_legacy/servers/it{str(ae)}.nordvpn.com.udp1194.ovpn"
                    resposta = requests.get(url_servidor_nz, verify=False)
                    if resposta.status_code != 200:
                        continue
                    else:
                        conteudo_config = resposta.text
                        break
                except:
                    print("não consegui conectar, tentando denovo")
                    continue
            nome_arquivo_config = f"IA/vpns/{country}.ovpn"

            with open(nome_arquivo_config, "w") as arquivo_config:
                arquivo_config.write(conteudo_config)

            with open(nome_arquivo_config, "a") as arquivo_config:
                arquivo_config.write("\nauth-user-pass auth.txt")
                arquivo_config.write('\npull-filter ignore "auth-token"')

            openvpn_gui_executable = r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe"'

            # Comando para importar o arquivo de configuração usando o OpenVPN GUI
            command = f'{openvpn_gui_executable} --connect "{country}"'
            subprocess.Popen(command, shell=True)

            self.get_location(pais)
            if ismain:
                conectado = self.verifica_velocidade_conexao()
                if conectado:
                    print("Conectado a " + pais + "\n\n")
                else:
                    self.connect(pais)
        else:
            print("Desconectando a vpn")
            try:
                subprocess.run("taskkill /IM openvpn.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run("taskkill /IM openvpn-gui.exe /F", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                pass
            self.get_location("brazil")
            print("Desconectado\n\n")

if __name__ == '__main__':

    while not keyboard.is_pressed("'"):

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

            if os.path.exists("IA/usuariostxt/users"):
                shutil.rmtree(f'IA/usuariostxt/users')

        print("------------------ Começando ------------------")
        login.connect("", True) if ismain else None
        login.get_location("brazil")
        time.sleep(2.5)
        login.desbugar(1)
        autofarm.getaccs(1)
        autofarm.getacc()

        autofarm.logar()
        autofarm.fiddler()
        time.sleep(1.5)
        autofarm.rewards()
        while not os.path.isfile(f"rewards/{os.getlogin()}.txt"):
            print("Refazendo o rewards por falta de txt.")
            autofarm.rewards()
            time.sleep(5)
        autofarm.sincronizar(quantidade=usuarios)
        autofarm.xbox()
        while not os.path.isfile(f"xbox/{os.getlogin()}xbox.txt"):
            autofarm.xbox()
            time.sleep(5)
        autofarm.fiddler("close")
        autofarm.sincronizar(quantidade=usuarios)
        time.sleep(2)

        if autofarm.ismain:
            print("Fazendo as tasks do aplicativo/conquista do xbox")
            rewardsthread = threading.Thread(target=autofarm.processrewards)
            xboxthread = threading.Thread(target=autofarm.farmxbox)
            logarsite = threading.Thread(target=login.logarsite, args=(autofarm.email, autofarm.senha))
            rewardsthread.start()
            xboxthread.start()
            logarsite.start()
            rewardsthread.join()
            xboxthread.join()
            logarsite.join()
            print("Tasks feitas!\n\n")
        else:
            login.logarsite(autofarm.email, autofarm.senha)

        while login.cookiesbing is None or not len(login.cookiesbing):
            login.logarsite(autofarm.email, autofarm.senha)

        autofarm.sincronizar(quantidade=usuarios)
        login.connect("italy") if ismain else None
        login.get_location("italy")
        autofarm.sincronizar(quantidade=usuarios)
        autofarm.fiddler()
        print("Pesquisando")
        login.pesquisa(1000, login.cookiesbing, "italy")
        autofarm.sincronizar(quantidade=usuarios)

        hora_atual = login.obter_horario_brasilia()
        if 20 > int(hora_atual) > 9:
            login.connect("new zealand") if ismain else None
            login.get_location("new zealand")
            print("Pesquisando")
            autofarm.sincronizar(quantidade=usuarios)
            login.pesquisa(2000, login.cookiesbing, "new zealand")
        else:
            login.connect("", True) if ismain else None
            login.get_location("brazil")
            print("Pesquisando")
            autofarm.sincronizar(quantidade=usuarios)
            time.sleep(3)
            login.pesquisa(2000, login.cookiesbing, "brazil")

        autofarm.sincronizar(quantidade=usuarios)
        autofarm.fiddler("close")
        autofarm.getaccs(1, True)
        print("!!!!!!!!!!!!!!!!!!FINALIZADO!!!!!!!!!!!!!!!!!!!\n\n")
