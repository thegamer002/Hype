# ba_meta require api 7

from _ba import chatmessage as msg
import ba
import _ba


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
            
            if c in ['/help', '/', '/h']:
                msg("Use /teams or /timer")
            
            elif c == '/timer':
                msg("Timer added with sucess")
                _ba.getactivity().setup_standard_time_limit(6)
                pass
                    
    
def readCmd():
    ba.timer(0.15, _cmd._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   