
import os



class processes:

    path = '>'


    '''
    errors_amount = 0

    def error(self, msg, type):

        self.errors_amount = 1
        errors = ['Bad command', 'Item or container not found']

        print("E: " + type + " error: " + msg if type(msg) == 'str' else errors[msg] if msg >= self.errors_amount else "Unknown error")
    '''
    def save(self, data, itempath):
        with open(itempath, 'w+') as f:
            try:
                f.write(data)
            except:
                processes.error(1, "fatal")
            finally:
                f.close()
    
    def load(self, itempath):
        with open(itempath, 'r+') as f:
            try:
                f.read()
            except:
                processes.error(1, "fatal")
            finally:
                f.close()

'''
class exec_cmd:

    def __init__(self):
        print("'exec_cmd': MODULE ACTIVATED.")
    
    def exec(self, cmd):
        if type(cmd) == 'int':
            pass
        else:
            if 'cd' in cmd:
                cmd = cmd.replace('cd ', '')
                os.chdir(cmd.replace('>', '/'))
            elif cmd == 'ls':
                os.listdir(path)

'''
