import json
import os
from time import gmtime, strftime
import AutoUpdate
import requests
import customtkinter as tk
import threading
import glob
import cv2
from source import *
import re


class gui(tk.CTk):
    def __init__(self):
        def updater():
            try:
                AutoUpdate.set_url("https://raw.githubusercontent.com/Gameriano1/Testing/main/version.txt")
                vers = requests.get("https://contas2-b9481-default-rtdb.firebaseio.com/Informações/.json",
                                    verify=False).json()
                vers = vers["versao"]
                try:
                    with open("source/ver.txt", "r") as v:
                        x = v.readlines()
                        verss = [p.strip() for p in x]
                except:
                    with open("source/ver.txt", "w+") as v:
                        v.write("1")
                if str(vers) == verss[0]:
                    print("Programa Está Atualizado!")
                else:
                    AutoUpdate.set_download_link("https://raw.githubusercontent.com/Gameriano1/buts/main/taskxbox.py")
                    print("Baixando a versão mais recente do bot...")
                    AutoUpdate.download("source/taskxbox.py")
                    AutoUpdate.get_latest_version()
                    with open("source/ver.txt", "w+") as v:
                        v.write(str(vers))
            except:
                pass

        updater()
        self.usuario = str(os.getlogin())
        self.hora = str(strftime("%d-%m-%Y %H:%M:%S", gmtime()))

        self.data = {"Hora": self.hora, "Usuario": self.usuario}

        self.canal = None
        self.quantidade = None

        super().__init__()
        print("Rodando programa...")

        self.title("Desbugador")
        self.geometry("500x400")
        self.resizable(False, False)

        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        label = tk.CTkLabel(self, text="Bot's", font=("Arial", 75))
        label.place(x=175, y=50)

        desbugador_button = tk.CTkButton(self, text="Desbugador", width=300, height=50, command=self.desbugador)
        desbugador_button.place(x=110, y=168)

        farm_button = tk.CTkButton(self, text="Bot de Farmar", width=300, height=50, command=self.farm)
        farm_button.place(x=110, y=220)

        settings_button = tk.CTkButton(self, text="Configurações", command=self.open_settings, width=300, height=50)
        settings_button.place(x=110, y=272)

    def open_settings(self):
        self.withdraw()

        settings_window = tk.CTk()
        settings_window.title("Configurações")
        settings_window.geometry("300x300")
        settings_window.resizable(False, False)

        settings_window.update_idletasks()
        width = settings_window.winfo_width()
        height = settings_window.winfo_height()
        x = (settings_window.winfo_screenwidth() // 2) - (width // 2)
        y = (settings_window.winfo_screenheight() // 2) - (height // 2)
        settings_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        # Defina a janela de configurações como uma janela modal vinculada à janela principal
        def on_closing():
            # Habilita a janela principal novamente
            self.deiconify()
            settings_window.destroy()

        def save_settings():
            label = tk.CTkLabel(settings_window, text="Configuração Salva com Sucesso", fg_color="green",
                                font=("Arial", 10))
            label.place(x=70, y=250)
            if leo.get():
                self.canal = "1060654131406188624"
            elif rebas.get():
                self.canal = "1093693916169130034"
            elif sly.get():
                self.canal = "1064710269017804890"
            elif kok.get():
                self.canal = "1078376461280497746"
            elif mica.get():
                self.canal = "1105624471135604816"
            elif black.get():
                self.canal = "1060654201962778707"

        rebas = tk.BooleanVar()
        leo = tk.BooleanVar()
        sly = tk.BooleanVar()
        kok = tk.BooleanVar()
        mica = tk.BooleanVar()
        black = tk.BooleanVar()

        mcbutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Black", variable=black)
        mcbutton.place(x=65, y=30)

        mcbutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Micael", variable=mica)
        mcbutton.place(x=65, y=60)

        kokbutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Koki", variable=kok)
        kokbutton.place(x=65, y=90)

        rebasbutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Rebas", variable=rebas)
        rebasbutton.place(x=65, y=120)

        leobutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Leo", variable=leo)
        leobutton.place(x=65, y=150)

        slybutton = tk.CTkCheckBox(settings_window, text="Enviar Contas Como Sly", variable=sly)
        slybutton.place(x=65, y=180)

        save_button = tk.CTkButton(settings_window, text="Salvar", command=save_settings)
        save_button.place(x=75, y=210)

        # Configura a função a ser executada quando a janela for fechada
        settings_window.protocol("WM_DELETE_WINDOW", on_closing)

        settings_window.mainloop()

    def farm(self):
        self.withdraw()

        farmwindow = tk.CTk()
        farmwindow.title("Bot de Farm")
        farmwindow.geometry("400x350")
        farmwindow.resizable(False, False)

        farmwindow.update_idletasks()
        width = farmwindow.winfo_width()
        height = farmwindow.winfo_height()
        x = (farmwindow.winfo_screenwidth() // 2) - (width // 2)
        y = (farmwindow.winfo_screenheight() // 2) - (height // 2)
        farmwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        def on_closing():
            # Habilita a janela principal novamente
            self.deiconify()
            farmwindow.destroy()

        def processrewards():
            mscv = []
            auth = []
            cookies = []

            my_files = glob.glob('rewards\*.txt')
            if not len(my_files):
                raise Exception("Arquivos Faltando")
            for s in my_files:
                countries = ['ITIT', 'ENNZ', 'PTBR']
                cc = ['IT', 'NZ', 'BR']
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
                except:
                    os.remove(s)
                    raise Exception("Arquivo " + s + " é uma bosta e nois vai deletar ele kk")

        def xbox():
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
                    authorization = [linha.replace("authorization: ", "") for linha in x if linha.__contains__("Authorization: ") or linha.__contains__("authorization: ")]
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

        def principal():
            label = tk.CTkLabel(farmwindow, text="Rodando...", fg_color="red", font=("Arial", 10))
            label.place(x=130, y=280)
            rewardsthread = threading.Thread(target=processrewards)
            xboxthread = threading.Thread(target=xbox)
            rewardsthread.start()
            xboxthread.start()
            rewardsthread.join()
            xboxthread.join()
            label.configure(text="Concluido!", fg_color="green")

        def onlytasks():
            label = tk.CTkLabel(farmwindow, text="Rodando...", fg_color="red", font=("Arial", 10))
            label.place(x=130, y=280)
            rewardsthread = threading.Thread(target=processrewards)
            rewardsthread.start()
            rewardsthread.join()
            label.configure(text="Concluido, Tasks feitas!", fg_color="green")

        def deletetxt():
            label = tk.CTkLabel(farmwindow, text="Rodando...", fg_color="red", font=("Arial", 10))
            label.place(x=130, y=280)
            rewards = os.listdir("rewards")
            xbox = os.listdir("xbox")

            for arquivox in xbox:
                caminho_completox = os.path.join("xbox", arquivox)
                os.remove(caminho_completox)
            for arquivor in rewards:
                caminho_completor = os.path.join("rewards", arquivor)
                os.remove(caminho_completor)
            label.configure(text="Concluido, Txt Deletados!", fg_color="green")

        def visualizer():

            def showcookie(user):

                def getcookie():
                    auth = []
                    mscv = []
                    cookies = []
                    with open("rewards/" + user + ".txt", "r") as f:
                        x = f.readlines()
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

                    headers = {
                        'Cache-Control': 'no-cache',
                        'Accept': 'application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
                        'X-Rewards-Country': 'BR',
                        'X-Rewards-Language': 'pt-BR',
                        'MS-CV': mscv[0],
                        'Authorization': auth[0],
                        'Connection': 'Keep-Alive',
                        'Host': 'prod.rewardsplatform.microsoft.com',
                    }

                    cookies = {
                        'Cookie': cookies[0]
                    }

                    def fazertask(task):
                        Farm.singletask(task, auth[0], mscv[0], cookie)

                    def getstatus():
                        status = requests.get("https://prod.rewardsplatform.microsoft.com/dapi/me?channel=xboxapp&options=6", headers=headers, cookies=cookies, verify=False).json()
                        try:
                            itens = [tasks for tasks in status['response']["counters"] if
                                     tasks.__contains__("RewardsOnboarding")]
                            tasksitalia = [tasks.replace("ITIT_xboxapp_punchcard_RewardsOnboarding_", "") for tasks in itens if tasks.__contains__("ITIT")]
                            conquista = [tasks.replace("ENUS_xboxapp_punchcard_RewardsOnboarding_", "") for tasks in itens if tasks.__contains__("ENUS_xboxapp_punchcard_RewardsOnboarding_")]
                            tasksitalia.extend(conquista)

                            completo = [tasks for tasks in status['response']["counters"] if tasks.__contains__("xboxapp_pcchild")]

                            remocoes = ["ENUS_xboxapp_", "_xboxactivity_achievementpc_MayTopFive2023", "_urlreward_achievementpc_MayTopFive2023"]
                            conqxbox = [re.sub('|'.join(map(re.escape, remocoes)), '', task) for task in completo if not task.__contains__("pcparent_achievementpc_MayTopFive2023")]

                            conqxbox.sort()
                            tasksitalia.sort()
                            return tasksitalia, conqxbox
                        except Exception as e:
                            raise Exception(e)
                    def atualizartestotasks(*task, rewards=True):
                        if task:
                            if rewards:
                                fazertask(task[0])
                            else:
                                Farm.singlexbox(task[0], auth[0], mscv[0], cookie)
                        tasksitalia, conquista = getstatus()
                        for i in tasksitalia:
                            if i == "pcparent": continue
                            cv2.putText(imagem, "Concluido", (170, posicaorewards[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 255, 0), thickness=2)
                            cv2.imshow(user, imagem)
                        for i in conquista:
                            cv2.putText(conq, "Concluido", (320,posicaoxbox[i]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2)
                            cv2.imshow("conquista", conq)

                    def eventomousexbox(event, x, y, flags, param):
                        if event == cv2.EVENT_LBUTTONDOWN:
                            if 16 <= x <= 302 and 14 <= y <= 202:
                                atualizartestotasks("pcchild1", rewards=False)
                                print("Desbloqueie Clicado!")
                            if 16 <= x <= 301 and 228 <= y <= 418:
                                atualizartestotasks("pcchild2", rewards=False)
                                print("Reclamar Clicado!")

                    def eventomousetask(event, x, y, flags, param):
                        if event == cv2.EVENT_LBUTTONDOWN:
                            if 9 <= x <= 158 and 3 <= y <= 99:
                                atualizartestotasks("pcchild1_dset")
                                print("Nave clicada!")
                            elif 9 <= x <= 158 and 111 <= y <= 203:
                                atualizartestotasks("pcchild2_searche")
                                print("Bing clicado!")
                            elif 9 <= x <= 153 and 209 <= y <= 305:
                                atualizartestotasks("pcchild3_shope")
                                print("Loja clicada!")
                            elif 9 <= x <= 153 and 415 <= y <= 507:
                                atualizartestotasks("pcchild5_gpquest")
                                print("Gamepass clicado!")
                            elif 9 <= x <= 153 and 519 <= y <= 609:
                                atualizartestotasks("pcchild6_redeem")
                                print("Moeda clicada!")
                            elif 9 <= x <= 153 and 619 <= y <= 703:
                                atualizartestotasks("pcchild7_app")
                                print("Rewards clicado!")

                    tasksitalia, conquista = getstatus()
                    imagem = cv2.imread('source/rewards.png')
                    conq = cv2.imread("source/conquista.png")
                    posicaorewards = {"pcchild1_dset": 90, "pcchild2_searche": 180, "pcchild3_shope": 295,
                               "pcchild4_playe": 390, "pcchild5_gpquest": 495, "pcchild6_redeem": 580,
                               "pcchild7_app": 700}
                    posicaoxbox = {"pcchild1": 150, "pcchild2": 360}

                    for i in tasksitalia:
                        if i == "pcparent": continue
                        cv2.putText(imagem, "Concluido", (170,posicaorewards[i]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), thickness=2)
                    for i in conquista:
                        cv2.putText(conq, "Concluido", (320,posicaoxbox[i]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), thickness=2)
                    cv2.namedWindow(user)
                    cv2.imshow(user, imagem)
                    cv2.imshow("conquista", conq)
                    cv2.setMouseCallback(user, eventomousetask)
                    cv2.setMouseCallback("conquista", eventomousexbox)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

                return getcookie

            def executar_funcao_retorno(argumento):
                funcao = showcookie(argumento)
                thread = threading.Thread(target=funcao)
                thread.start()


            visual = tk.CTk()
            visual.title("Bot de Farm")
            visual.geometry("400x350")
            visual.resizable(False, False)

            visual.update_idletasks()
            width = visual.winfo_width()
            height = visual.winfo_height()
            x = (visual.winfo_screenwidth() // 2) - (width // 2)
            y = (visual.winfo_screenheight() // 2) - (height // 2)
            visual.geometry('{}x{}+{}+{}'.format(width, height, x, y))

            usuariostxt = os.listdir("rewards")
            usuarios = [usuario.replace(".txt", "") for usuario in usuariostxt]

            x = 150
            y = 15

            def botao_clicado(user):
                executar_funcao_retorno(user)

            for user in usuarios:
                button = tk.CTkButton(visual, text=user, width=100, height=30)

                button.configure(command=lambda user=user: botao_clicado(user))
                button.place(x=x, y=y)
                y += 40


            visual.mainloop()

        label = tk.CTkLabel(farmwindow, text="Bot De Farm", font=("Arial", 40))
        label.place(x=95, y=30)

        farmglobal = tk.CTkButton(farmwindow, text="Farmar Global", width=150, height=50, command=principal)
        farmglobal.place(x=130, y=100)

        farmtasks = tk.CTkButton(farmwindow, text="Farmar Tasks", width=150, height=50, command=onlytasks)
        farmtasks.place(x=130, y=160)

        deletartxt = tk.CTkButton(farmwindow, text="Deletar Txt's", width=150, height=50, command=deletetxt)
        deletartxt.place(x=130, y=220)

        visualizar = tk.CTkButton(farmwindow, text="Visualizar Tasks", width=150, height=50, command=visualizer)
        visualizar.place(x=130, y=280)

        farmwindow.protocol("WM_DELETE_WINDOW", on_closing)

        farmwindow.mainloop()

    def desbugador(self):
        self.withdraw()

        desbugwindow = tk.CTk()
        desbugwindow.title("Desbugador")
        desbugwindow.geometry("400x250")
        desbugwindow.resizable(False, False)

        desbugwindow.update_idletasks()
        width = desbugwindow.winfo_width()
        height = desbugwindow.winfo_height()
        x = (desbugwindow.winfo_screenwidth() // 2) - (width // 2)
        y = (desbugwindow.winfo_screenheight() // 2) - (height // 2)
        desbugwindow.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        def on_closing():
            # Habilita a janela principal novamente
            self.deiconify()
            desbugwindow.destroy()

        def desbugar():
            self.quantidade = caixa_texto.get()
            if self.canal is None:
                label = tk.CTkLabel(desbugwindow, text="Por favor selecione um usuario nas config", fg_color="red",
                                    font=("Arial", 10))
                label.place(x=100, y=170)
                return
            desbugador = Desbug(self.quantidade, self.canal)
            t = threading.Thread(target=desbugador.main)
            t.start()
            labelt = tk.CTkLabel(desbugwindow, text=f"Gerando {self.quantidade} contas com sucesso", fg_color="green",
                                 font=("Arial", 10))
            labelt.place(x=130, y=170)

        caixa_texto = tk.CTkEntry(desbugwindow, width=30)
        caixa_texto.place(x=140, y=120)

        label = tk.CTkLabel(desbugwindow, text="Desbugador", font=("Arial", 40))
        label.place(x=100, y=50)

        farm_button = tk.CTkButton(desbugwindow, text="Desbugar", width=50, height=30, command=desbugar)
        farm_button.place(x=185, y=118)

        desbugwindow.protocol("WM_DELETE_WINDOW", on_closing)

        desbugwindow.mainloop()


if __name__ == '__main__':
    root = gui()
    hour = str(strftime("%Y-%m-%d", gmtime()))
    requests.post(f"https://contas2-b9481-default-rtdb.firebaseio.com/Report/{hour}/.json", data=json.dumps(root.data),
                  verify=False)
    root.mainloop()
