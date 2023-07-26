# WAHEGURU JI
import termios
import tty
import sys
import colorama
from colorama import Fore, Style

colorama.init()

description_colour = Fore.CYAN
command_colour = Fore.GREEN
error_colour = Fore.RED + Style.DIM
curr_style = Fore.YELLOW
prev_char = ''


def gpt_description(text):
    return (description_colour + text)


def gpt_command(text):
    output = (command_colour + text)
    return output


def error(text):
    return (error_colour + text + Style.RESET_ALL)


def user_input():
    global description_colour, command_colour, error_colour, curr_style, prev_char
    command = ""
    sys.stdout.write('$ ')
    sys.stdout.flush()
    # print(prev_char)
    while True:
        character = getch()
        if not ((character >= 'a' and character <= 'z') or character == '|' or character == '-' or character == ' '):
            break
        else:
            if (prev_char == ' '):
                if (character == '|'):
                    curr_style = Fore.MAGENTA
                elif (character == '-'):
                    curr_style = Fore.BLUE
                else:
                    curr_style = Fore.WHITE

            sys.stdout.write(curr_style + character)
            sys.stdout.flush()
            command += character
            prev_char = character
    print()
    return command


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


if (__name__ == '__main__'):
    # user_input()
    stringg = input()
    output = gpt_command(stringg)
    print(output)
