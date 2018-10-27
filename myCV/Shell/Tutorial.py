#!/usr/bin/python

# A Basic SimpleCV interactive shell tutorial

#load required libraries
from __future__ import print_function
from SimpleCV import *

from subprocess import call
from code import InteractiveInterpreter
import platform

lb = "\n" #linebreak
tb = "\t" #tab
tutorial_interpreter = InteractiveInterpreter(globals())
logo = None
img = None
clone = None
thumb = None
eroded = None
cropped = None

#Command to clear the shell screen
def shellclear():
    if platform.system() == "Windows":
        return
    call("clear")

def attempt(variable_name, desired_class):
    prompt_and_run()
    variable = globals().get(variable_name)

    if isinstance(variable,desired_class):
        if desired_class == Image:
            if variable.isEmpty():
                print(lb)
                print("Although you can create empty Images on MyCV, let's not")
                print("play with that now!")
                print(lb)
                return False

        return True

    return False

def prompt_and_run():

    command = input("SimpleCV:> ")
    tutorial_interpreter.runsource(command)
    return command

def request_show_command():
    while True:
        if prompt_and_run().endswith('.show()'):
            return

def end_tutorial():
    print(lb)
    print("Type 'quit' to leave the tutorials, or press Enter to move on!")
    command = input("SimpleCV:> ")
    return command.lower() == 'quit'

def end_of_tutorial():
    print(lb)
    print("This is the end of our tutorial!")
    print(lb)
    print("For more help, go to www.simplecv.org, and don't forget about the")
    print("help function!")
    print(lb)

def command_loop(command, desired_tuple):
    while True:
        print(command)
        print(lb)

        if attempt(desired_tuple[0], desired_tuple[1]):
            return

        print(lb)
        print("Oops! %s is still not %s" % (desired_tuple[0], str(desired_tuple[1])))

def tutorial_image():
    shellclear()
    print("SimpleCV Image tutorial")
    print("-----------------------")
    print(lb)
    print("Using images is simple in OpenCV.")
    print(lb)
    print("First thing we are going to do is load an image. Try it yourself:")
    print(lb)

    cmd = "logo = Image(\"simplecv\")"
    desired_tuple = ('logo', Image)
    command_loop(cmd, desired_tuple)

    print(lb)
    print("Correct! You just loaded SimpleCV logo into memory.")
    print("Let's try it to use one of your images. There are different ways to")
    print("do that. You can try, for example:")
    print(lb)
    print("img = Image(URL_TO_MY_PICTURE) or img = Image(PATH_TO_MY_PICTURE)")
    print(lb)
    cmd =  "Example: img = Image('http://simplecv.org/logo.jpg')"

    desired_tuple = ('img', Image)
    command_loop(cmd, desired_tuple)

    print(lb)
    print("Perfect! Now we want to see it:")
    print(lb)
    cmd = "img.show()"
    print(cmd)
    print(lb)

    request_show_command()

    print(lb)
    print("Alright! This was tutorial 1/6.")
    print("Next tutorial: Saving Images")
    if not end_tutorial():
        # tutorial_save()
        end_of_tutorial()
    return

# Other tutorials will go here

def magic_tutorial(self,arg):
    tutorials_dict = {'image': tutorial_image,
                      # 'save': tutorial_save,
                      # 'camera': tutorial_camera,
                      # 'manipulation': tutorial_manipulation,
                      # 'copy': tutorial_copy,
                      # 'features': tutorial_features
                      }


    if (arg == ""):
        shellclear()
        print("+--------------------------------+")
        print(" Welcome to the MyCV tutorial ")
        print("+--------------------------------+")
        print(lb)
        print("At anytime on the MyCV Interactive Shell you can type tutorial,")
        print("then press the tab key and it will autocomplete any tutorial that")
        print("is currently available.")
        print(lb)
        print("Let's start off with Loading and Saving images!")
        print(lb)
        print(lb)
        input("[Press enter to continue]")
        tutorial_image()
        end_of_tutorial()
        return
    else:
        if arg in tutorials_dict:
            tutorials_dict[arg]()
        else:
            print("%s is not a tutorial!" % arg)