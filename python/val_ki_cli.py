''' CLI - Validation

    This command line app will validate a single include.
    Input: Path to an include file.
    Output: Displays validation.

    Matt Briggs V1.0.1: 9.1.2020
'''

import cmd
import val_ki_functions as VAL
import mod_utilities as MU

APPVERSION = "Validation CLI Version 1.0.0.20200901\n"
SCHEMAS = r"C:\git\mb\azs-modular-poc\Model\schemas"

class TagTerminal(cmd.Cmd):
    """Accepts commands via the normal interactive prompt or on the command line."""

    prompt = "> "

    def do_check(self, line):
        '''The main logic of the utility.'''
        
        try:
            module_body = MU.get_textfromMD(line)
            split_path = line.split("\\")[-1].split("-")
            module_slug = "{}-{}".format(split_path[0],split_path[1])
            body_parse = VAL.parse_module(module_body)
            schema_path = VAL.get_schemas(SCHEMAS)
            validation = VAL.validate_module_ki(schema_path[module_slug], body_parse )
            print(validation)

            print("Done")
            return
        except Exception as e:
            print ("There was some trouble.\nError code: {}".format(e))
            return

    def do_help(self, line):
        '''Type help to get help for the application.'''
        print("Type `check` <path to include>")
        return False

    def do_quit(self, line):
        '''Type quit to exit the application.'''
        return True

    def do_exit(self, line):
        '''Type exit to exit the application.'''
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    TagTerminal().cmdloop(APPVERSION)