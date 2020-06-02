Name: Jariwala Prayag
UTA ID: 1001719373
CSE - 5360 - 001
Assignment - 03 - Task1
______________________________________________

Used Language: python
______________________________________________

It works in two modes

1) One-move mode - The best possible move is given as a output by the system.

compilation

>python maxconnect4.py one-move input1.txt output1.txt 10

here, input1.txt is the initial state. 

output1.txt is the file where the state after playing the best possible move is stored.

last command line argument is a depth. Algorithm will analyze next "depth" moves of the game to give best possible move.

2) Interactive mode - an interactive game between computer and human

>python maxconnect4.py interactive input1.txt human-next 10

or

>python maxconnect4.py interactive input1.txt computer-next 10

here, input1.txt is the initial state.

human-next / computer-next determines whether huma or computer makes a next move

last command line argument is a depth. Algorithm will analyze next "depth" moves of the game to give best possible move.