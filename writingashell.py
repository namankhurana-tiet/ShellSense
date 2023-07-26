import subprocess
import os
import practice
import colourcoded_commands as cc
finalstatus = 0


def main():
    while True:
        print('$ ', end="")
        command = cc.user_input()
        if command == 'exit':
            break
        elif command == 'help':
            print('psh : a simple shell written in python')
        elif command.startswith('cd'):
            change_directory(command)
        else:
            execute_command(command)
        print()


def execute_command(command):

    try:
        if (command == ''):
            pass

        elif (command.startswith('///')):
            output = practice.main(-1, command)
            print(cc.gpt_command(output))

        elif (command.startswith('--reverse')):
            output = practice.main(-2, command)
            print(cc.description_colour(output))

        if "|" in command:
            # save for restoring later on
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            # first command takes commandut from stdin
            fdin = os.dup(s_in)

            # iterate over all the commands that are piped
            for cmd in command.split("|"):
                # fdin will be stdin if it's the first iteration
                # and the readable end of the pipe if not.
                os.dup2(fdin, 0)
                os.close(fdin)

                # restore stdout if this is the last command
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                # redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                subprocess.run(cmd.strip().split())
                finalstatus = status.returncode
                output = practice.main(finalstatus, command)
                print(cc.gpt_command(output))
                # error = "psh: command not found: {}".format(cmd.strip())
                # print(cc.error(error))

            # restore stdout and stdin
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)

        else:
            status = subprocess.run(command.split())
            finalstatus = status.returncode
            output = practice.main(finalstatus, command)
            finaloutput = cc.gpt_command(output)
            print(finaloutput)

    except Exception as e:
        # error = ("Exception occured : command not found : {}".format(
        #     command))
        # print(cc.error(error))
        # finalstatus = status.returncode
        print(e)
        output = practice.main(1, command)
        print(cc.gpt_command(output))


def change_directory(command):
    path = "/" + command.split("/")[0].split(" ")[0]
    '''convert to absolute path and change directory'''
    try:
        os.chdir(os.path.abspath(path))
    except Exception:
        print('cd: No such file or directory : {}'.format(path))


if '__main__' == __name__:
    main()

# Features added:
# empty command doesn't return any error now
# if get_command is None:
#     print("No OpenAI API key found. "
#           "Please set GRAND_AUTH_KEY/GRAND_AUTH_SECRET or OPENAI_API_KEY.")
#     sys.exit(1)
