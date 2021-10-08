import socket
import select
import os

def main(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen()
    readable = [server_socket]

    while True:
        try:
            input_ready, write_ready, except_ready = select.select(readable, [], [])
            for ir in input_ready:
                if ir  == server_socket:
                    csocket, addr = server_socket.accept()
                    input_ready.append(csocket)
                    print("from {}".format(addr))
                else:
                    data = ir.recv(1024)
                    if data:
                        response = "HTTP/1.1 200 OK\r\n"
                        ir.send(response.encode('utf-8'))
                    else:
                        ir.close()
                        input_ready.remove(ir)
        except Exception as err:
            print("EXCEPTION !!!", err)

            

if __name__ == "__main__":
    port = 8892
    main(port)
