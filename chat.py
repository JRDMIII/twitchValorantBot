import socket
import sys
import threading
import customtkinter as ct
import os

ct.set_appearance_mode("System")
ct.set_default_color_theme("dark-blue")

#this is the constructor method for the chat class
class chat_application(ct.CTk):

    # Defining the width and the height of the window
    WIDTH = 600
    HEIGHT = 600
    def __init__(self):
        super().__init__()

        self.geometry(f'{chat_application.WIDTH}x{chat_application.HEIGHT}')
        self.resizable(False, False)
        self.title("Consultation Chat")
        self.protocol("WM_DELETE_WINDOW", self.close)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=5)
        self.grid_columnconfigure(3, weight=0)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=15)
        self.grid_rowconfigure(2, weight=10)

        self.start_receiver()

    def start_receiver(self):
        print("Starting receiver")
        self.name = "Laptop"
        self.chat_screen(self.name)

        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def chat_screen(self, name):

        self.labelHead = ct.CTkLabel(self,
                                     text=name)
        self.labelHead.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")

        self.text_console = ct.CTkTextbox(self,
                                          width=550,
                                          height=470,
                                          corner_radius=5,
                                          state="disabled",
                                          font=("Nunito", -32))
        self.text_console.grid(row=1, column=1, columnspan=3, pady=10, padx=5)

        #this is an entry box where the user can type their message
        self.message_entry_box= ct.CTkEntry(self,
                                          width=550,
                                          height=60,
                                          corner_radius=5)
        self.message_entry_box.grid(row=2, column=1, columnspan=3, pady=5, padx=5)

        #this is a button to send the message
        self.send_msg_button = ct.CTkButton(self,
                                            text="Send",
                                            corner_radius=5,
                                            width=40,
                                            height=65,
                                            command=lambda: self.sendButtonFunc(self.message_entry_box.get()))
        self.send_msg_button.grid(row=2, column=3, pady=10, padx=20)

        self.text_console.configure(cursor="arrow")

        #create a scroll bar

        self.scrollbar= ct.CTkScrollbar(master=self,
                                        height=550,
                                        width=20,
                                        command=self.text_console.yview)
        self.scrollbar.grid(row=1, column=4, pady=10, padx=20)

        self.text_console.configure(yscrollcommand=self.scrollbar.set)



    def sendButtonFunc(self, msg):
        self.text_console.configure(state="disabled")
        self.msg = msg
        self.message_entry_box.delete(0, "end")
        send = threading.Thread(target=self.send_message)
        send.start()

    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                # if the messages from the server is NAME send the client's name
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    # insert messages to text box
                    self.text_console.configure(state="normal")
                    self.text_console.insert("end",
                                         message + "\n\n")

                    self.text_console.configure(state="disabled")
            except Exception as e:
                # an error will be printed on the command line or console if there's an error
                print("An error occurred!")
                print(e)
                client.close()
                break

    def send_message(self):
        self.text_console.configure(state="disabled")
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

    def close(self, event=0):
        self.destroy()

if __name__ == "__main__":
    PORT = 5000
    SERVER_IP = "192.168.1.141"
    ADDRESS = (SERVER_IP, PORT)
    FORMAT = "utf-8"

    connected = False
    while not connected:
        try:
            # this creates a new client socket and connects it to the server
            client = socket.socket(socket.AF_INET,
                                   socket.SOCK_STREAM)
            client.connect(ADDRESS)
            connected = True
            print("Connected")
        except:
            client = threading.Thread(target=os.startfile("client.py"))
            client.start()

    chat_app = chat_application()
    chat_app.mainloop()




