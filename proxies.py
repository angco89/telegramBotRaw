import requests

server = 'http://192.168.0.157'
linkProxy = server + '/v2/proxy_list?page=1&limit=20&sort=%2Bid'
#getProxy tạm thời khai báo proxy chứ ko get từ API về để lấy proxy
def getProxy():
    r = requests.get(linkProxy)

    if r.status_code != 200:
        print('Proxy không tồn tại')

    dataJson = r.json()['data']
    proxy = ''
    for idx, item in enumerate(dataJson):
        if 'extra_info' not in item:
            print(f'Vị trí {idx + 1} không có proxy')
        else:
            proxy = item['system'] + ':' + str(item['proxy_port'])
            break
    return proxy

def renew(linkProxy):
    linkRenew = server + ':' + '10000/reset?proxy=' + linkProxy
    print(linkRenew)
    r = requests.get(linkRenew)
    return