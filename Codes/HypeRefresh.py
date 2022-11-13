# ba_meta require api 7

from ba.internal import chatmessage as msg
import ba
import _ba
import os



class _cmd():
    
    def _home():
        messages = msg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/' or ';'):
                return _cmd.commands()
            else:
                pass
            
            
            
            
    def commands():
        
        messages = _ba.get_chat_messages()
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
                os.system("export GH_TOKEN='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'")
                os.system("gh auth login --with-token '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')
                os.system("gh repo clone thegamer002/HypeServerStaff/")
                os.system("ls > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f"Directories : {f.read()}")
                
                
    
def readCmd():
    ba.timer(0.5, _cmd._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   