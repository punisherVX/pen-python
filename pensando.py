#!/usr/bin/env python
# Copyright (c) 2020, Pensando Systems
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# Author(s): Ryan Tischer ryan@pensando.io
#            Edward Arcuri edward@pensando.io
#
#
import json
import requests

from urllib3.exceptions import InsecureRequestWarning



class PSM:
    '''This is the docstring for PSM class'''

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    def __init__(self, server='https://localhost', user='admin', password='Pensando0$', tenant='default'):
        self.server = server
        self.user = user
        self.password = password
        self.tenant = tenant
        self.session = requests.Session()
        self.__psmLogin()



    def __psmLogin(self):
        authData = json.dumps({"username": self.user,"password": self.password,"tenant": self.tenant}).encode("utf-8")
        print(f"{authData}")
        self.session.verify = False
        auth = self.session.post(f"{self.server}/v1/login",authData)
        print(f"{auth.json}")
        return self.session


    def __getWebCall(self, url, *payload):
        """
        docstring
        """
        # raise NotImplementedError
        data = {} if not payload else payload[0]

        try:
            print(f"Data is {data}")
            response = self.session.get(url, data=json.dumps(data))
        except requests.exceptions.Timeout as to:
            print(f'Network Timeout: {to}')
        except requests.exceptions.TooManyRedirects as tmr:
            print(f'Too Many Redirects: {tmr}')
        except requests.exceptions.ConnectionError as ce:
            print(f'Connection Error: {ce}')
        except requests.exceptions.RequestException as err:
            print(f'Something went wrong but not sure what')
            raise SystemExit(err)

        return response

    def __postWebCall(self, url, *payload):
        """
        docstring
        """
        # raise NotImplementedError
        data = {} if not payload else payload[0]

        try:
            print(f"Data is {data}")
            response = self.session.post(url, data=json.dumps(data))
        except requests.exceptions.Timeout as to:
            print(f'Network Timeout: {to}')
        except requests.exceptions.TooManyRedirects as tmr:
            print(f'Too Many Redirects: {tmr}')
        except requests.exceptions.ConnectionError as ce:
            print(f'Connection Error: {ce}')
        except requests.exceptions.RequestException as err:
            print(f'Something went wrong but not sure what')
            raise SystemExit(err)

        return response

    def getCluster(self):
        print(f"trying to get to {self.server}")
        url = f"{self.server}/configs/cluster/v1/cluster"
        return  self.__getWebCall(url).json()


    def getDSC(self,dsc='data'):
        print(f"trying to get to {self.server}")
        url = f"{self.server}/configs/cluster/v1/distributedservicecards"
        response = self.__getWebCall(url).json()

        if dsc == 'macs':
            # pull out mac address of DSCs
            numDSC = (response['list-meta']['total-count'])
            print(f"Call returned {numDSC} DSCs")
            dscList = []
            for dscs in range(numDSC):
                dscList.append((response['items'][dscs]['meta']['name']))
            return dscList
        else:
            pass

        return response


    def getFlowExportPolicy(self):
        print(f"trying to get to {self.server}")
        url = f"{self.server}/configs/monitoring/v1/flowExportPolicy"
        return  self.__getWebCall(url).json()


    def getWorkloads(self):
        print(f"trying to get to {self.server}")
        url = f"{self.server}/configs/workload/v1/workloads"
        return  self.__getWebCall(url).json()






if __name__ == "__main__":
   pass