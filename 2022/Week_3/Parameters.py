from codecs import charmap_encode


char_name = input("what is your name:")
char_role = input("what chacter role are you?")

def my_function(the_name):
    print(f"Your name is {char_name}")
    print(f"Your charcter role is {char_role}")

my_function(char_name, char_role)
