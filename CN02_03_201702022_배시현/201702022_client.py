import socket

TCP_IP = '10.0.02.15'
TCP_PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP,TCP_PORT))

message = sock.recv(1024)
print(message.decode())

print('Please select 1 number from 1 to 10.')
mynum = input('Number : ')
sock.send(mynum.encode())
selectNum = sock.recv(1024)

print('you choice the number : ' + selectNum.decode() + '. Please wait.')
message = sock.recv(1024)
print(message.decode())

choice = input('multiply or add :')
sock.send(choice.encode())
message = sock.recv(1024)
print(message.decode())

sock.close()
