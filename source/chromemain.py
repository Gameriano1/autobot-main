from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import threading
import requests
import random
import time
import requests as r
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import pychrome
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


class login:
    def __init__(self, email, senha, canal):

        veio = r.get("https://contas2-b9481-default-rtdb.firebaseio.com/" + "Informações/.json",
                            verify=False).json()
        token = veio["token"]

        self.delay = 6
        self.chrome_options = ChromeOptions()
        self.chrome_options.page_load_strategy = 'none'
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.chrome_options.add_argument('--log-level=3')

        self.emails = email
        self.senhas = senha
        self.contas = []
        self.canal = canal
        self.token = token


    def bingantibug(self,
                    xpath, driverz):
        try:
            WebDriverWait(driverz, self.delay).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            raise Exception('A Pagina nao carregou a tempo')

    def logar(self, email, senha):
        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.chrome_options)
            driver.get(
                'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttps%253a%252f%252fwww.bing.com%252f%253ftoWww%253d1%2526redig%253d3389C7EB769248EB8086CD884D2595CF%2526wlexpsignin%253d1%26sig%3d0A6C406EFB686EA604025253FA7C6FDA&wp=MBI_SSL&lc=1046&CSRFToken=9399de60-9308-4156-8667-596b86a444d0&aadredir=1')
            browser = pychrome.Browser(url=driver.command_executor._url)
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
                self.bingantibug('//*[@id="iShowSkip"]', driver)
                driver.find_element('xpath', '//*[@id="iShowSkip"]').click()
                titulo = driver.title
            driver.get("https://bing.com")
            try:
                driver.find_element('xpath', '//*[@id="iShowSkip"]').click()
            except:
                pass
            url = driver.current_url
            while not url.startswith("https://www.bing.com"):
                driver.get("https://www.bing.com")
                url = driver.current_url
            self.delay = 20
            self.bingantibug('//*[@id="id_n"]', driver)
            self.delay = 6
            entrar = driver.find_element("xpath", '//*[@id="id_s"]').is_displayed()
            while entrar:
                time.sleep(1)
                entrar = driver.find_element("xpath", '//*[@id="id_s"]').is_displayed()
            time.sleep(3)

            driver.get(
                "https://www.bing.com/msrewards/api/v1/enroll?publ=BINGIP&crea=ML1ML5&pn=BINGTRIAL5TO250P201808&partnerId=BrowserExtensions&pred=true&sessionId=337EAFB7F24C6B6B347ABD28F3586A96")
            self.delay = 20
            self.bingantibug('//*[@id="id_n"]', driver)
            self.delay = 25

            driver.get("https://rewards.bing.com/optout")
            self.bingantibug('//*[@id="opt-out-page"]/div[4]/div[5]/form/button', driver)
            cookies = driver.get_cookies()
            elemento = driver.find_element("name", '__RequestVerificationToken')
            valor = elemento.get_attribute('value')
            headers = {
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            }

            payload = {
                "__RequestVerificationToken": valor
            }

            cookies_requests = {cookie['name']: cookie['value'] for cookie in cookies}
            response = requests.post("https://rewards.bing.com/optout", headers=headers, cookies=cookies_requests, data=payload)
            while response.status_code != 200:
                print("Não desbugou direito, tentando dnv")
                response = requests.post("https://rewards.bing.com/optout", headers=headers, cookies=cookies_requests, data=payload)

            time.sleep(3)
            self.delay = 25
            driver.get(
                "https://account.xbox.com/pt-br/accountcreation?returnUrl=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&ru=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&rtc=1&csrf=3VhQvhdMuj732EgcoWdImeMRZtPOvCd4I3KCMOf43kD0IYXFqOhyr1VpL60wRIIjzzNB6RpmOc4YJcvfLkVCwo16OyA1&wa=wsignin1.0")
            url = driver.current_url
            if url == "https://www.xbox.com/pt-BR/":
                return
            while not url.__contains__("accountcreation"):
                driver.get("https://account.xbox.com/pt-br/accountcreation?returnUrl=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&ru=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&rtc=1&csrf=3VhQvhdMuj732EgcoWdImeMRZtPOvCd4I3KCMOf43kD0IYXFqOhyr1VpL60wRIIjzzNB6RpmOc4YJcvfLkVCwo16OyA1&wa=wsignin1.0")
                url = driver.current_url
            self.bingantibug('//*[@id="Accept"]', driver)
            driver.find_element('xpath', '//*[@id="Accept"]').click()
            time.sleep(4)
            mostra = driver.find_elements('xpath', '//*[@id="undefined"]/div[2]/div/button')
            while mostra:
                driver.get(
                    "https://account.xbox.com/pt-br/accountcreation?returnUrl=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&ru=https%3a%2f%2fwww.xbox.com%2fpt-BR%2f&rtc=1&csrf=3VhQvhdMuj732EgcoWdImeMRZtPOvCd4I3KCMOf43kD0IYXFqOhyr1VpL60wRIIjzzNB6RpmOc4YJcvfLkVCwo16OyA1&wa=wsignin1.0")
                self.bingantibug('//*[@id="Accept"]', driver)
                driver.find_element('xpath', '//*[@id="Accept"]').click()
                time.sleep(4)
                mostra = driver.find_elements('xpath', '//*[@id="undefined"]/div[2]/div/button')
            url = driver.current_url
            while url != "https://www.xbox.com/pt-BR/":
                try:
                    driver.find_element('xpath', '//*[@id="Accept"]').click()
                except:
                    pass
                url = driver.current_url
            driver.close()
            self.contas.append(email + ";" + senha)
        except:
            pass


    def manager(self, bot=False):
        threads = []
        for e, s in zip(self.emails, self.senhas):
            t = threading.Thread(target=self.logar, args=(e, s))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        import os
        if os.path.isfile('IA/accs.txt'):
            modo_abertura = 'a'
        else:
            modo_abertura = 'w'
        if not bot:
            with open(f"IA/accs.txt", modo_abertura) as c:
                for v in self.contas:
                    c.write(v + '\n')
        else:
            with open(f"IA/usuariostxt/{os.getlogin()}.txt", modo_abertura) as c:
                for v in self.contas:
                    c.write(v + '\n')
        for v in self.contas:
            if self.canal != "1116093603199057961":
                v = f"{str(v)}"
            else:
                v = str(v).split(";")
                v = f"""{os.getlogin()}:{v[0]}
{v[1]}"""
            mensagem = Discord(self.token, self.canal, v)
            mensagem.enviar()


class Discord:
    def __init__(self, token, canal, conta):
        self.token = token
        self.canal = canal
        self.conta = conta

    def enviar(self):
        py = {
            'content': self.conta
        }

        header = {
            'authorization': self.token
        }

        r.post("https://discord.com/api/v9/channels/" + self.canal + "/messages",
                    data=py, headers=header, verify=False)


class contas:
    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.item = None
        self.emails = None
        self.senhas = None

    def gerar(self):
        email = []
        aitem = []
        senha = []
        dtb = "https://contas2-b9481-default-rtdb.firebaseio.com/"

        itens = []
        contas = requests.get(dtb + "Contas/.json", verify=False).json()
        for i in contas:
            itens.append(i)
        for _ in range(int(self.quantidade)):
            item = random.choice(itens)
            itemjson = contas[item]
            conta = [itemjson[i] for i in itemjson]
            contafinal = conta[0]
            contasplit = str(contafinal).split(":")
            aitem.append(item)
            email.append(contasplit[0])
            senha.append(contasplit[1])

        self.item = aitem
        self.emails = email
        self.senhas = senha


class Desbug:
    def __init__(self, quantidade, canal):
        self.quantidade = quantidade
        self.canal = canal

    def main(self, *bot):
        dtb = "https://contas2-b9481-default-rtdb.firebaseio.com/"
        acc = contas(self.quantidade)
        acc.gerar()

        Login = login(acc.emails, acc.senhas, self.canal)

        if bot:
            Login.manager(bot[0])
        else:
            Login.manager()


        for i in acc.item:
            requests.delete(dtb + "Contas/" + i + "/.json", verify=False)
        return Login.contas
