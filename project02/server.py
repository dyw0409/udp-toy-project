#UDP
#socket() 소켓생성
#bind():ip주소,포트 할당
#TCP와 다르게 메시지와 정보(ip,포트)를 주고 받음
#recvfrom(): 데이터 받음
#sendto():주소포함 데이터 전송
#~.decode('utf-8')

#소켓생성시 tcp는  socket.SOCK_STREAM
#udp는 socket.SOCK_DGRAM

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 3000))
print("server start(클라이언트 기다리는 중)")

data, client_addr = s.recvfrom(1024)
filename = data.decode()
print("요청받은 파일명:" + filename)

try:
  with open(filename, 'rb') as f:
    while True:
      chunk = f.read(1024)  # 1024바이트씩 쪼개서 읽음
      if not chunk: break
      s.sendto(chunk, client_addr)

  s.sendto(b'', client_addr)
  print("파일 전송 완료")

except FileNotFoundError:
    s.sendto(b'404', client_addr)
    print("❌ 요청한 파일이 존재하지 않습니다.")

    

s.close()