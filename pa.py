# -*- coding:utf-8 -*-
import requests
import bs4
import chardet
import os
import json

jsonFileName = '/gui-config.json'  #生成json 配置文件的位置路径
filePath = os.getcwd()

jsonData = {
    "configs": [
        {
            "server": "oc.dnswhy.top",
            "server_port": 8388,
            "password": "xdxd1098",
            "method": "aes-256-cfb",
            "remarks": "VPN",
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



def demo():
    
    response = requests.get('http://www.ishadowsocks.org/')
    dom = bs4.BeautifulSoup(response.text,"html.parser")
    
    html = dom.select('div.col-lg-4')
    count = 0       #记录循环次数,超过3就跳出
    dataArray = []  #数据
    nameArray = ['server','server_port','password','method','remarks','auth']
    for d in html:
        count+=1
        if(count == 4):
            break;

        h4 = d.select('h4')
        data = {}
        for index,e in enumerate(h4):
            #print e.get_text()
            tempString = e.get_text()
            tempSplitString = tempString.split(':')
            stringLen = len(tempSplitString)
            print stringLen
            print index
            if (stringLen > 1):
                print tempSplitString[0]
                print tempSplitString[1]
                
                #if index < 5:
                data[nameArray[index]] = tempSplitString[1]
                #else :
                 #   data['auth'] = 'False'
                
            else:
                data['auth'] = 'False'
                print tempSplitString[0]
            
            print '///////////////////'

        #dataArray.append(data) #join json
        jsonData['configs'].append(data)
        print data

    
    #jsonData['configs'] = dataArray
    #jsonData['configs'].append(dataArray)

    json_str = json.dumps(jsonData, indent=4)

    print json_str  #生成字符串
    with open(filePath + jsonFileName,'w') as f :
        f.write(json_str)

if __name__ == "__main__":
    demo()

