import socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('192.168.5.128', 3000)
filename = 'test2.jpg'
#파일명을 보냄
c.sendto(filename.encode(), server_addr)

with open("0526" + filename, 'wb') as f:
    while True:
        data, addr = c.recvfrom(1024)
        if not data == b'__END__':
            break
        f.write(data)

print("파일 받기 완료")
c.close()
