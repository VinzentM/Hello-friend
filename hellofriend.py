"""
hellofriend.py
Author: <Vinzent Moesch>
Credit: <list sources used, if any>

Assignment:

Write and submit an interactive Python program that asks for the user's name and age, 
then prints how much older Python is than the user (based on a simple comparison of 
birth year). Python's first public release occurred in 1991. Something like this:

Please tell me your name: Guido
Please tell me your age: 16
Hello, Guido. Python is 8 years older than you are!

Note that the text: "Guido" and "16" are entered by the user running the program. 
The final line ("Hello...") is generated dynamically when you run the program, based 
on the name and age that the user enters.
"""

s1=input("Please tell me your name: ")
s2=int(input("Please tell me your age: "))
s3="Hello, {1}. Python is {0} years older than you"
s4="Hello, {1}. Python is {0} years younger than you"
s5="Hello, {0}. Python is as old as you"
a=25
if int(s2)<int(a):
    print(s3.format(int(a-int(s2)),str(s1)))
if int(s2)>int(a):
    print(s4.format(int(int(s2)-a),str(s1)))
if int(s2)==int(a):
    print(s5.format(str(s1)))
