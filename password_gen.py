import random

use_for = input("What do you want to use the password for? ")
duljina = int(input("How long should the password be? "))
pw = "0123456789qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM,.-+!#$%&/()=?*"

random_s = [random.choice(pw) for i in range(duljina)]
random_pw = "".join(random_s)

file = open("Random_password.txt", "a")
file.write("\n" + random_pw + "   This password is used for -> " + use_for)
file.close()
