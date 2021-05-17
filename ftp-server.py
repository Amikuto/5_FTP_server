import socket
import os
import utils
import logging

'''
pwd - показывает название рабочей директории
ls - показывает содержимое текущей директории
cat <filename> - отправляет содержимое файла
'''

os.chdir('docs')


def process(req):
    req_list = req.split(" ")
    req = req_list[0]
    if req == 'pwd':
        return utils.current_dir()
    elif req == 'ls':
        return utils.files_in_curr_directory()
    elif req == 'cat':
        return utils.show_text(req_list[-1])
    elif req == 'mkdir':
        return utils.create_folder(req_list[-1])
    elif req == 'rmdir':
        return utils.delete_folder(req_list[-1])
    elif req == 'touch':
        return utils.create_file(req_list[-1])
    elif req == 'rmfile':
        return utils.remove_file(req_list[-1])
    elif req == 'mv':
        return utils.rename_file(req_list[-2], req_list[-1])
    elif req == 'copy':
        return utils
    elif req == 'disconnect':
        pass
    return 'bad request'


PORT = 6666

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
print("Прослушиваем порт", PORT)

while True:
    conn, addr = sock.accept()
    
    request = conn.recv(1024).decode()
    
    response = process(request)
    conn.send(response.encode())

conn.close()
