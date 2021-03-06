import os
import config_parse
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
}


def analysis_master():
    for root, dirs, files in os.walk(config_parse.get_path() + '/VideoProcess/input/'):
        for file in files:
            with open('./input/' + file, 'r') as master:
                while True:
                    line = master.readline()
                    if not line:
                        break
                    if line[0] == '#':
                        continue
                    else:
                        line = line[:len(line) - 1]
                        response = requests.get(url=line, headers=headers, allow_redirects=True)
                        with open(config_parse.get_path() + '/VideoProcess/m3u8/' + find_file_name(line), 'wb') as out:
                            out.write(line.encode())
                            out.write('\n'.encode())
                            out.write(response.content.decode('utf8').encode())
                            break
            print(file, 'master analysis completely!!!')


def find_file_name(url):
    while True:
        n = url.find('/')
        if n == -1:
            return url
        else:
            url = url[n + 1:]


def find_name(name):
    return name[:name.find('.')]


def find_domain(url):
    n = len(url) - 1
    while url[n] != '/':
        n = n - 1
    return url[:n]


def find_end(file_point):
    i = 0
    while True:
        line = file_point.readline()
        if not line:
            return int(i - 7) / 2
        else:
            i = i + 1


def analysis_m3u8():
    for root, dirs, files in os.walk(config_parse.get_path() + '/VideoProcess/m3u8'):
        for file in files:
            if not os.path.exists(config_parse.get_path() + '/VideoProcess/ts/' + find_name(file)):
                os.mkdir(config_parse.get_path() + '/VideoProcess/ts/' + find_name(file))
            with open(config_parse.get_path() + '/VideoProcess/m3u8/' + file, 'r') as m:
                total = find_end(m)
                i = 0
                m.seek(0, 0)
                base = find_domain(m.readline())
                while True:
                    line = m.readline()
                    if not line:
                        break
                    if line[0] == '#':
                        continue
                    else:
                        i = i + 1
                        line = line[:len(line) - 1]
                        response = requests.get(url=base + '/' + line)
                        print(line+' downloading:'+str(i)+'/'+str(total))
                        with open(config_parse.get_path() + '/VideoProcess/ts/' + find_name(file) + '/' + line,
                                  'wb') as w:
                            w.write(response.content)


def generate_video_list():
    for root, dirs, files in os.walk(config_parse.get_path() + '/VideoProcess/m3u8'):
        for file in files:
            with open(config_parse.get_path() + '/VideoProcess/m3u8/' + file, 'r') as r:
                domain_url = find_domain(remove_new_line(r.readline()))
                with open(config_parse.get_path() + '/VideoProcess/video_list/' + file, 'wb') as w:
                    while True:
                        line = r.readline()
                        if not line:
                            break
                        if line[0] == '#':
                            continue
                        else:
                            input = ("file '" + config_parse.get_path() + "/VideoProcess/ts/" + find_name(
                                file) + '/' + remove_new_line(line) + "'").encode()
                            w.write(input)
                            w.write('\n'.encode())
    print('Generate video list completely!!!')


def remove_new_line(input):
    return input[:len(input) - 1]


def url_to_master():
    with open('./url/url.txt', 'r') as urls:
        while True:
            url = urls.readline()
            if not url:
                break
            else:
                url = url[:len(url) - 1]
                response = requests.get(url=url, headers=headers)
                response_json = response.json()
                master_url = response_json['data']['videoPlayerProps']['refs']['m3uUrl']
                name = response_json['data']['videoPlayerProps']['id']
                master_response = requests.get(url=master_url, headers=headers)
                if master_response.status_code == 200:
                    print(master_url, '\nget master file successfully!')
                else:
                    print(master_url, 'get master file failed! http status code =', master_response.status_code)
                with open('./input/' + name + '_master.m3u8', 'wb') as master:
                    master.write(master_response.content)
