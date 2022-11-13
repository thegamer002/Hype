# ba_meta require api 7

from ba.internal import get_chat_messages as gmsg, chatmessage as msg
import ba
import _ba
import os



class _cmd():
    
    def _home():
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/' or ';'):
                return _cmd.commands()
            else:
                pass
            
            
            
            
    def commands():
        
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
                
            if c == '/pwd':
                os.system("pwd > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f" Server Path Is : {f.read()}")
            
            
            if c in ['/ref', '/refresh']:
                msg("Server Refreshing Mods!, Enter In one minute.")
                os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && cp HypeServerStaff/Codes/* /home/ubuntu/coutinho/tests/BombSquad_Server_Linux_x86_64_1.7.13/dist/ba_root/mods/ && sudo rm -rf HypeServerStaff/")
                os.system("ls /home/ubuntu/coutinho/tests/BombSquad_Server_Linux_x86_64_1.7.13/dist/ba_root/mods/ > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f"Directories : {f.read()}")
                
                
    
def readCmd():
    ba.timer(0.5, _cmd._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   