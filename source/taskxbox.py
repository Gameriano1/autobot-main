import requests
import urllib3
import time
import re
import glob
from sys import stdout
import threading


class Xbox:
    def ativar(xuid: str, auth, ide):

        urllib3.disable_warnings()

        payload = {
            "titles": [{"expiration": 600, "id": ide, "state": "active", "sandbox": "RETAIL"}]
        }

        headers = {
            'Accept-Encoding': 'gzip, deflate',
            'x-xbl-contract-version': '3',
            'Authorization': auth,
            'Cache-Control': 'no-cache'
        }

        response = requests.post(f"https://presence-heartbeat.xboxlive.com/users/xuid({xuid})/devices/current",
                                 json=payload,
                                 headers=headers, verify=False)
        if response.status_code != 200:
            p = 16
            while response.status_code != 200:
                stdout.write(
                    "\r" + "Um Erro foi Encontrado, Esperando " + str(p) + " segundos e tentando executar novamente")
                stdout.flush()
                time.sleep(p)
                response = requests.post(f"https://presence-heartbeat.xboxlive.com/users/xuid({xuid})/devices/current",
                                         json=payload,
                                         headers=headers, verify=False)

    def conquistar(xuid, auth, ide, scid, idi):

        urllib3.disable_warnings()

        payloadconquistar = {
            "action": "progressUpdate", "serviceConfigId": scid, "titleId": ide,
            "userId": xuid, "achievements": [{"id": idi, "percentComplete": 100}]}

        headersconquistar = {
            'Accept-Encoding': 'gzip, deflate',
            'x-xbl-contract-version': '2',
            'Cache-Control': 'no-cache',
            'User-Agent': 'XboxServicesAPI/2021.04.20210610.3 c',
            'accept': 'application/json',
            'accept-language': 'en-GB',
            'Content-Type': 'text/plain; charset=utf-8',
            'Authorization': auth,
            'Host': 'achievements.xboxlive.com',
            'Connection': None,
        }

        responsi = requests.post(
            f"https://achievements.xboxlive.com/users/xuid(" + xuid + ")/achievements/" + scid + "/update?",
            json=payloadconquistar, headers=headersconquistar, verify=False)
        if responsi.status_code == 200 or responsi.status_code == 304:
            pass
        elif responsi.status_code == 429:
            while responsi.status_code == 429:
                stdout.write(
                    "\r" + "Um Erro foi Encontrado, Esperando " + "5" + " segundos e tentando executar novamente")
                stdout.flush()
                time.sleep(5)
                responsi = requests.post(
                    f"https://achievements.xboxlive.com/users/xuid(" + xuid + ")/achievements/" + scid + "/update?",
                    json=payloadconquistar, headers=headersconquistar, verify=False)
        else:
            pass

    def conquista(xuid, auth, authrewards):

        urllib3.disable_warnings()

        headersconquista = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': 'IT',
            'X-Rewards-Language': 'it-IT',
            'Authorization': authrewards,
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
        }

        ids = [1870475503, 2030093255]
        scids = ["00000000-0000-0000-0000-00006f7d30ef", "00000000-0000-0000-0000-00007900c3c7"]

        t1s = []
        for gameid, scid in zip(ids, scids):
            t = threading.Thread(target=Xbox.ativar, args=(xuid, auth, gameid))
            t1s.append(t)

        for t1 in t1s:
            t1.start()
            t1.join()

        conquista = ["", ""]
        nume = 1
        for gameid, scid in zip(ids, scids):
            while conquista[0] != "pcchild4_playe":
                status = requests.get("https://prod.rewardsplatform.microsoft.com/dapi/me?channel=xboxapp&options=6", headers=headersconquista, verify=False).json()
                itens = [tasks for tasks in status['response']["counters"] if tasks.__contains__("RewardsOnboarding")]
                conquista = [tasks.replace("ENUS_xboxapp_punchcard_RewardsOnboarding_", "") for tasks in itens if tasks.__contains__("ENUS_xboxapp_punchcard_RewardsOnboarding_")]
                conquista.sort()
                t = threading.Thread(target=Xbox.conquistar, args=(xuid, auth, gameid, scid, nume))
                t.start()
                t.join()
                nume += 1
                if not len(conquista):
                    conquista = ["",""]
                if nume >= 10:
                    break

def checkpesquisa(authenticate):
    headersfarm = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': "IT",
            'X-Rewards-Language': 'it-IT',
            'Authorization': f'{authenticate}',
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
    }

    status = requests.get("https://prod.rewardsplatform.microsoft.com/dapi/me?channel=xboxapp&options=6",
                              headers=headersfarm, verify=False).json()
    return status['response']['balance']

class Farm:
    def TaskXbox(o, authenticate, country, abreviados, mscv, cookies):

        if authenticate is None:
            raise Exception('Coloque um authenticate valido')

        headersfarm = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': abreviados,
            'X-Rewards-Language': 'it-IT',
            'MS-CV': mscv,
            'Authorization': f'{authenticate}',
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
        }

        cookie = {
            'Cookie': cookies
        }

        urllib3.disable_warnings()

        payloadfarm = {
            "id": "", "timestamp": "", "type": 80, "amount": 1, "country": f"{abreviados}", "retry_in_background": 'true',
            "attributes": {"offerid": f"{country}{o}"}
        }

        tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities', json=payloadfarm,
                               headers=headersfarm, cookies=cookie, verify=False)
        while tentar.status_code != 200:
            stdout.write(f"\rOcorreu um Erro 💀 , pais: {abreviados}")
            tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities',
                                   json=payloadfarm,
                                   headers=headersfarm, cookies=cookie, verify=False)
            if tentar.status_code == 200:
                stdout.write("\rErro Resolvido 🔥")

    def checkpesquisa(authenticate):
        headersfarm = {
                'Cache-Control': 'no-cache',
                'Accept': 'application/json',
                'Accept-Encoding': 'gzip, deflate',
                'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
                'X-Rewards-Country': "IT",
                'X-Rewards-Language': 'it-IT',
                'Authorization': f'{authenticate}',
                'Connection': 'Keep-Alive',
                'Host': 'prod.rewardsplatform.microsoft.com',
        }

        status = requests.get("https://prod.rewardsplatform.microsoft.com/dapi/me?channel=xboxapp&options=6",
                                  headers=headersfarm, verify=False).json()
        return status['response']['balance']


    def RewardsRun(auths, mscv, cook, countries, cc):

        headersfarm = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': "IT",
            'X-Rewards-Language': 'it-IT',
            'MS-CV': mscv,
            'Authorization': f'{auths}',
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
        }

        cookie = {
            'Cookie': cook
        }

        urllib3.disable_warnings()

        while True:
            threads = []
            taskscompletar = ["pcchild1_dset", "pcchild3_shope", "pcchild5_gpquest", "pcchild6_redeem", "pcchild7_app"]
            status = requests.get("https://prod.rewardsplatform.microsoft.com/dapi/me?channel=xboxapp&options=6", headers=headersfarm, cookies=cookie, verify=False).json()
            itens = [tasks for tasks in status['response']["counters"] if tasks.__contains__("RewardsOnboarding")]
            taskspais = [tasks.replace(f"{countries}_xboxapp_punchcard_RewardsOnboarding_", "") for tasks in itens if tasks.__contains__(countries)]
            try:
                taskspais.remove("pcparent")
                taskspais.remove("pcchild2_searche")
            except:
                pass
            elementos_exclusivos = list(set(taskscompletar) - set(taskspais))
            if not len(elementos_exclusivos):
                break
            for o in elementos_exclusivos:
                o = "_xboxapp_punchcard_RewardsOnboarding_" + o
                t = threading.Thread(target=Farm.TaskXbox, args=(o, auths, countries, cc, mscv, cook))
                threads.append(t)
                t.start()
            o = "_Welcome_Tour_XboxApp_Offer"
            t = threading.Thread(target=Farm.TaskXbox,args=(o,auths,countries,cc,mscv,cook))
            threads.append(t)
            t.start()
            for t in threads:
                t.join()


    def singletask(task, auth, mscv, cookie):
        o = "_xboxapp_punchcard_RewardsOnboarding_" + task

        headersfarm = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': "IT",
            'X-Rewards-Language': 'it-IT',
            'MS-CV': mscv,
            'Authorization': f'{auth}',
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
        }

        cookies = {
            'Cookie': cookie
        }

        urllib3.disable_warnings()

        payloadfarm = {
            "id": "", "timestamp": "", "type": 80, "amount": 1, "country": f"IT", "retry_in_background": 'true',
            "attributes": {"offerid": f"ITIT{o}"}
        }

        tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities', json=payloadfarm,
                               headers=headersfarm, cookies=cookies, verify=False)
        while tentar.status_code != 200:
            stdout.write(f"\rOcorreu um Erro 💀 , pais: IT")
            tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities',
                                   json=payloadfarm,
                                   headers=headersfarm, cookies=cookies, verify=False)
            if tentar.status_code == 200:
                stdout.write("\rErro Resolvido 🔥")

    def singlexbox(task, auth, mscv, cookie):
        if task == "pcchild1":
            o = "_xboxapp_" + task + "_xboxactivity_achievementpc_MayTopFive2023"
        else:
            o = "_xboxapp_" + task + "_urlreward_achievementpc_MayTopFive2023"

        headersfarm = {
            'Cache-Control': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate',
            'X-Rewards-AppId': 'RewardsAppOnXbox v1.1.1.0',
            'X-Rewards-Country': "IT",
            'X-Rewards-Language': 'it-IT',
            'MS-CV': mscv,
            'Authorization': f'{auth}',
            'Connection': 'Keep-Alive',
            'Host': 'prod.rewardsplatform.microsoft.com',
        }

        cookies = {
            'Cookie': cookie
        }
        urllib3.disable_warnings()

        payloadfarm = {
            "id": "", "timestamp": "", "type": 80, "amount": 1, "country": f"IT", "retry_in_background": 'true',
            "attributes": {"offerid": f"ENUS{o}"}
        }

        tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities', json=payloadfarm,
                               headers=headersfarm, cookies=cookies, verify=False)
        while tentar.status_code != 200:
            stdout.write(f"\rOcorreu um Erro 💀 , pais: IT")
            tentar = requests.post('https://prod.rewardsplatform.microsoft.com/dapi/me/activities',
                                   json=payloadfarm,
                                   headers=headersfarm, cookies=cookies, verify=False)
            if tentar.status_code == 200:
                stdout.write("\rErro Resolvido 🔥")

