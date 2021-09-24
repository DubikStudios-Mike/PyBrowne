import socket
import platform
import subprocess
import os
import pbl
import bpx


on = False

pbl.path = 'Users>Guest>'
# os.chdir(os.path.dirname(pbl.path.replace('>', '/') if platform.system().lower() == 'linux' or platform.system().lower() == 'macos' else pbl.path if platform.system().lower() == 'browne' else pbl.path.replace('>', '/')))
home_dir = "/home/justmike/workspaces/PyBrowne-0.1.0/PyBrowne/" # if socket.gethostname() == 'justmike-Aspire-V5-552P' and platform.system().lower() == 'linux' else input('Please type in the full path for "PyBrowne-0.1.0". *INCLUDING "PyBrowne-0.1.0"'))
os.chdir(home_dir)


apps = ('---', '---', '---', '---', '---')

cache = ''


lic = ('lic')
# cmds = ('cmds', 'commands')
# hide = ('hide')
exc = ('exec')
hlp = ('help')
cd = ('cd')
ls = ('ls')  # , ('-a', '-d', '-i'))

commands = ('d', 'a', 'i', 'b', 'x', hlp, cd, ls, exc, lic)


error = ''


print("""

        [D]etails
        [Lic]ense
        [A]ccount
         [I]tems
        [B]rownet (not available)
          E[x]it

<---=--=-=-===-=-=--=--->
1 - """ + apps[1] +
"\n2 - " + apps[2] +
"\n3 - " + apps[3] +
"\n0 - Applications")

while True:
      print(error)

      command = input("\n " + pbl.path + " $ ")
      command = command.lower()
      error = ''

      '''if not command.lower() in commands:
            error = "E: BAD COMMAND."
      else:'''
            # pbl.exec_cmd.exec(command, command)
      
      if not command in commands:
            print("INVALID")
            pass

      elif command == 'exec':
            itemToRun = input('\nItem: ')
            command = input('\nType: ')
            cache = input('\nMode: ')
            bpx.run('/home/justmike/workspaces/PyBrowne-0.1.0/PyBrowne/Programs/' + str(itemToRun), command, cache)
      elif command == 'help':
           print(str(commands).replace("(", '').replace(")", '').replace("'", ''))
      elif command == 'x':
            exit()
      elif command == 'd':
           print("""
                  
        PyBrowne v0.1.0 (PROTO)

                 |
   Apex License (A) 2021 Dubik Studios  
                 |

Apex License Type: Free and Open-Source (FOS)

      Type 'lic' for license details.
                  
                  """ + open(home_dir + "Main/data.lock", 'r+').readlines()[0].replace('[', '').replace(']', ''))
      elif command == 'lic':
            print("""
              |    
Apex License (A) 2021 Dubik Studios
              |    
                  
Terms of service: 1. WE DO NOT COLLECT ANY DATA WITHOUT
THE USER'S CONSENT. THIS INCLUDES [USAGE (ONLINE OR OFFLINE),
SENT ITEMS] 2. WE ARE NOT RESPONSIBLE FOR MALICIOUS USAGE
OF PYBROWNE, BROWNE OR BROWNEOVER. Legal: ANY USAGE OF 'BROWNE'
AND PROCLAIMING IT AS YOUR LEGALLY OWNED BRAND IN APEX OR
UNDER THE APEX LICENSE IS ILLEGAL IN APEX AND UNDER THE APEXLIC
LAW. ACTION CAN AND WILL BE TAKEN AS SOON AS POSSIBLE. VISIT
'apexttp://aww.apexlic.law/legal' FOR MORE INFORMATION.
                  """)
      
      elif command == 'b':
            print("Unavailable at this time.")
      
      '''elif command == 'a':
            print("Name: " + open(home_dir + "Main/data.lock", 'r+').str(readline(1)).replace('@', " Pass: ").replace('[', '').replace(']', '').replace("'", ''))


            on = True
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            try:
                  s.connect(('redacted ip lol', 1234))
            except:
                  print("Unavailable at this time.")
                  on = False
            while on:
                  choice = input("\nWelcome to Brownet! What would you like to do?\n[S]end Data, [R]eceive Data, Brownet [A]pplications, [Q]uit").lower().strip()
                  if choice == 'r':
                        data_r = s.recv(4096)
                  elif choice == 'q':
                        on = False
                        break
'''
