import requests
import simplejson
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def translate_api_one(data):
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate'
    data = {"from":"zh","to":"en",'client_id':'8GxPnyhY5UVIT1W9ufbsA7vS','q':data}
    a = requests.post(url,params=data)
    b = simplejson.loads(a.text)
    result =  b['trans_result'][0]['dst']
    print result
    return result

def translate_api_two(data):
    url = 'http://openapi.baidu.com/public/2.0/bmt/translate'
    data = {"from":"zh","to":"en",'client_id':'p4TtioEBkPG38yI9QF8cnBLA','q':data}
    a = requests.post(url,params=data)
    b = simplejson.loads(a.text)
    result =  b['trans_result'][0]['dst']
    print result
    return result

def loadDataName(namepath):
    namefiles=open(namepath)
    raw = namefiles.readlines()
    namefiles.close()
    name = []
    for i in range(len(raw)):
        name.append(raw[i].strip('\n'))
    return name

def loadDataSet(filepath):
    files = open(filepath)
    raw = files.readlines()
    files.close()
    data = []
    for i in range(len(raw)):
        data.append(raw[i].strip('\n'))
    return data



namepath = '/root/last/dataset'
name = loadDataName(namepath)
filepath = []
savefilepath = []
for i in range(len(name)):
    filepath.append('/root/last/'+name[i])
    savefilepath.append('/root/tmp_eng_data/'+name[i])

for i in range(len(name)):
    print filepath[i]
    data = loadDataSet(filepath[i])
    for j in range(2,len(data)):
        translate = translate_api_two(data[j])
        save = open(savefilepath[i],'a+')
        save.write(translate)
        save.write('\n')
        save.close()
        
