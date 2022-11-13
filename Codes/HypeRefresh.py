# ba_meta require api 7

from _ba import chatmessage as msg
import ba
import _ba
import os 


class _use():
    
    def _home():
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/'):
                return _use.refresh()
            else:
                pass
            
            
            
            
    def refresh():
        
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
            
            if c == '/pwd':
                os.system("pwd > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f" Server Path Is : {f.read()}")
            
            
            if c in ['/ref', '/refresh]:
                msg("Server Refreshing Mods!, Enter In one minute.")
                os.system("git clone https://github.com/thegamer002/HypeServerStaff/")
                os.system("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")
                os.system("")
                os.system("ls -la > cmd.txt")
                msg(f"Directories : {f.read()}")
                
                
                
                
                
def refr():
    ba.timer(0.3, _use._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    refr()   