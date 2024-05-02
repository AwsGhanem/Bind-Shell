# Bind-Shell Using Python

**The Bind shell is a type of shells that opens a socket and binds itself to it, as simple as that.**

- In terms of Hacking, bind shell is opened by the attacker himself and he's the one who initiates the connection.

#

### To apply as much as beneficial modules, we used (threading, argparse) beside sockets which is the most important one.


# Diagram of the whole experiment
![image](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/342fd9f7-3179-4290-b9c3-405255fa49b7)



- () Numbers represent connection establishment
- <> Numbers represent the communitcation process between client and server
- We are using a default port to listen to and the same port for the client
- The socket will look like [127.0.0.1:DEFAULTport]
- All of the functions are described within the code comments
#

**Help Manual** 
- `-h` to view the flags
- `-l` to start the server-shell
- `-c` to conntect to the server-shell (`-c IP-address`)

# Running the Script and Viewing the traffic 
> [!WARNING]
> **The whole communication is done as plain-text, this means it's vulnerable to some kind of attacks (MITM,sniffing,etc...).**

1) **Connecting to the Server-shell**
- ![Screenshot 2024-05-02 215613](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/ca9a5db7-9d7e-4542-8fd6-2f9b6dd67778)

2) **Performing a command**
- ![image](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/9841515e-f025-4a15-ba84-1507124eabe8)

3) **The executed command will be logged to the server**
- ![image](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/3894b015-ed79-48f3-8793-ebff8f4076eb)

4) **The traffic on Wireshark is all on plain-text because no encryption is used**

- ![image](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/62871f00-b49c-4669-8200-1b45dfa288e0)





