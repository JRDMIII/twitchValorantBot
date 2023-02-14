import socket
import sys
import threading
import os

#this is the constructor method for the chat class
class chat_application():

    # Defining the width and the height of the window
    WIDTH = 600
    HEIGHT = 600
    def __init__(self):
        super().__init__()

        print("Starting to recieve")
        self.start_receiver()

    def start_receiver(self):
        print("Starting receiver")
        self.name = "Laptop"
        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    print("Welp")
            except Exception as e:
                # an error will be printed on the command line or console if there's an error
                print("An error occurred!")
                print(e)
                client.close()
                break

if __name__ == "__main__":
    PORT = 5000
    SERVER_IP = "10.36.19.158"
    ADDRESS = (SERVER_IP, PORT)
    FORMAT = "utf-8"

    # this creates a new client socket and connects it to the server
    client = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
    client.connect(ADDRESS)
    connected = True
    print("Connected")


    chat_app = chat_application()




