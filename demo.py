# coding 'utf-8'
import json
import os

filePath = os.getcwd()
print filePath
data = {
    "configs": [
        {
            "server": "oc.dnswhy.top",
            "server_port": 8388,
            "password": "xdxd1098",
            "method": "aes-256-cfb",
            "remarks": "VPN",
            "auth": False
        },
        {
            "server": "USA.ISS.TF",
            "server_port": 23456,
            "password": "90777618",
            "method": "aes-256-cfb",
            "remarks": "",
            "auth": False
        }
    ],
    "strategy": "null",
    "index": 1,
    "global": False,
    "enabled": True,
    "shareOverLan": False,
    "isDefault": False,
    "localPort": 1080,
    "pacUrl": "null",
    "useOnlinePac": False,
    "availabilityStatistics": "true",
    "autoCheckUpdate": False,
    "logViewer": {
        "fontName": "Consolas",
        "fontSize": 8.25,
        "bgColor": "Black",
        "textColor": "White",
        "topMost": False,
        "wrapText": False,
        "toolbarShown": False,
        "width": 600,
        "height": 400,
        "top": 640,
        "left": 1320
    }
}

json_str = json.dumps(data)

def go():
    with open(filePath + '/gui-config.json','w') as f :
        f.write(json_str)
    #print json_str


go()
