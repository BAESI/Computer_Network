import socket 
import random

TCP_IP = '10.0.02.15'
TCP_PORT = 5001
PLAYER_NUM = 0
victory = 'Congratulation. You won!'
defeat = 'Unfortunately, you hav been defeated.'

NUMLIST = [random.randint(1,100) for i in range(10)]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen()


conn1, addr1 = sock.accept()
PLAYER_NUM = PLAYER_NUM + 1
print('Connection address : ' + str(addr1))
conn2, addr2 = sock.accept()
PLAYER_NUM = PLAYER_NUM + 1 
print('Connection address : ' + str(addr2))
conn3, addr3 = sock.accept()
PLAYER_NUM = PLAYER_NUM + 1
print('Connection address : ' + str(addr3))

if PLAYER_NUM == 3: 
    message = 'Okay... All player have gathered. Start the game.'
    conn1.send(message.encode())
    conn2.send(message.encode())
    conn3.send(message.encode())

    data1 = conn1.recv(1024)
    num1 = NUMLIST[int(data1.decode())-1]
    conn1.send(str(num1).encode())

    data2 = conn2.recv(1024)
    num2 = NUMLIST[int(data2.decode())-1]
    conn2.send(str(num2).encode())

    data3 = conn3.recv(1024)
    num3 = NUMLIST[int(data3.decode())-1]
    conn3.send(str(num3).encode())
 
    randompoint1 = random.randint(-1,4)
    randompoint2 = random.randint(-1,4)
    randompoint3 = random.randint(-1,4)

    message = 'Do you want multiply or add...?'
    
    conn1.send(message.encode())
    choice1 = conn1.recv(1024).decode()

    conn2.send(message.encode())
    choice2 = conn2.recv(1024).decode()

    conn3.send(message.encode())
    choice3 = conn3.recv(1024).decode()

    if choice1 == 'add':
        final1 = num1 + randompoint1
    elif choice1 == 'multiply':
        final1 = num1 * randompoint1

    if choice2 == 'add':
        final2 = num2 + randompoint2
    elif choice2 == 'multiply':
        final2 = num2 * randompoint2

    if choice3 == 'add':
        final3 = num3 + randompoint3
    elif choice1 == 'multiply':
        final3 = num3 * randompoint3

    if final1 > final2 :
        if final1 > final3:
            conn1.send(victory.encode())
            conn2.send(defeat.encode())
            conn3.send(defeat.encode())
        elif final1 < final3:
            conn1.send(defeat.encode())
            conn2.send(defeat.encode())
            conn3.send(victory.encode())
    elif final1 < final2 :
        if final2 > final3 :
            conn1.send(defeat.encode())
            conn2.send(victory.encode())
            conn3.send(defeat.encode())
        elif final2 < final3 :
            conn1.send(defeat.encode())
            conn2.send(defeat.encode())
            conn3.send(victory.encode())

conn1.close()
conn2.close()
conn3.close()


    
