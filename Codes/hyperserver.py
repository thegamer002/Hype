# ba_meta require api 7

import ba
import _ba 
from _ba import chatmessage as msg


class _cmd():
    
    def _home():
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/'):
                return _cmd.commands()
            else:
                pass
                
            
            
    def commands():
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
            
            if c == '/':
                msg("Use /teams /n /timer")
            
        

def readCmd():
    msg(f'God Commands')
    ba.timer(5.0, _cmd._home, True)

    # ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()
   
