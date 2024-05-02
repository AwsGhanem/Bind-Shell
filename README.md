# Bind-Shell Using Python

**The Bind shell is a type of shells that opens a socket and binds itself to it, simple as that.**

- In terms of Hacking, bind shell is opened by the attacker himself and he's the one who initiates the connection.

#

### To apply as much as beneficial modules, we used (threading, argparse) beside sockets which is the most important one.


# Diagram of the whole experiment

![image](https://github.com/AwsGhanem/Bind-Shell/assets/123994471/c786b480-26aa-438f-b09b-b592ab2d0915)

- () Numbers represent connection establishment
- <> Numbers represent the communitcation process between client and server
- We are using a default port to listen to and the same port for the client
- The socket will look like [127.0.0.1:DEFAULTport]
- All of the functions are described within the code comments
#

## Help Manual 
- `-h` to view the flags
- `-l` to start the server-shell
- `-c` to conntect to the server-shell (`-c IP-address`)
  

