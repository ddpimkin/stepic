import socket


def mysend(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError('broken')
        totalsent += sent


def myreceive(sock, msglen):
    msg =''
    while len(msg) < msglen:
        chunck = sock.recv(msglen-len(msg))
        if chunck == '':
            raise RuntimeError('broken')
        msg += chunck
    return msg


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 1234))
        s.listen(10)
        while True:
            conn, addr = s.accept()
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(data)
            conn.close()
    except:
        if s:
            s.close()