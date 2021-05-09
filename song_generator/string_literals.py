'''
# string_literals.py
# William Ponton
# 5.8.21
# Collection of the string literals used in the program
'''

# string literals
# welcome()
WELCOME = '\nWelcome to the Song Generator!'
CREATIVE = '\nThe goal of this tool is to help you be more creative....\n...by adding some limitations to your process....\n'


# case_1
CASE_1 = '\nFirst, we will use the Song() class to make a new Song object.\nI\'ll hardcode the values into the constructor - this is one way to setup a new object.\n'

# case_2
CASE_2 = '\nSecond, we can use the class method \'get_random_parameters\' in the Song() class to randomize mySong, the object we instantiated by hardcoding.\n'

# case_3
CASE_3 = '\nFinally, we can convert a dictionary into a Song() object by using another method outside of the song class.  This method uses the values of the dictionary in the constructor when instantiating the object.\nYou can also see that the input dictionary results in a Song() object in the call to type.'

# goodbye
GOODBYE = 'Goodbye~!'

# test_output
def test_output():
  test = "Hello world ~ from string_literals.py"
  return print(test)

# Welcome
def welcome():
  welcome_message = WELCOME + CREATIVE
  return print(welcome_message)

# Case 1
def case_1():
  case_1_message = CASE_1
  return print(case_1_message)

# Case 2
def case_2():
  case_2_message = CASE_2
  return print(case_2_message)

# Case 3
def case_3():
  case_3_message = CASE_3
  return print(case_3_message)

# buh bye
def goodbye():
  goodbye = GOODBYE
  return print(goodbye)