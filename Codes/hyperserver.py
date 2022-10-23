# Tell the app which of its api versions we are written for. The app's
# meta-scanner will skip this file if this number doesn't match theirs.
# To learn more, see https://ballistica.net/wiki/meta-tag-system
# ba_meta require api 7

import ba
import _ba 
from _ba import chatmessage as msg


class _cmd():
    
    teams = ['brazil', 'latam', 'egypt', 'algeria', 'turkey', 'russia', 'italy']
    def _home():
        messages = get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/'):
                return _cmd.commands()
            else:
                pass
                
            
            
    def commands():
        messages = get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
            
            if c == '/':
                msg("Use /teams brazil,argentina to change teams and /timer to 10 minutes on screen")
            
        
        
# ba.timer(0.05, _update, repeat=True)      
def readCmd():
    msg(f'God Commands')
    ba.timer(0.5, _cmd._home, True)
# Tell the app about our Plugin.


# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()
