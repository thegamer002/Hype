# meta-scanner will skip this file if this number doesn&#x27;t match theirs.
# To learn more, see https://ballistica.net/wiki/meta-tag-system
# ba_meta require api 7

import ba
import _ba 
from _ba import chatmessage as msg


class _cmd():
    
    teams = [&#x27;brazil&#x27;, &#x27;latam&#x27;, &#x27;egypt&#x27;, &#x27;algeria&#x27;, &#x27;turkey&#x27;, &#x27;russia&#x27;, &#x27;italy&#x27;]
    def _home():
        messages = get_chat_messages()
        if len(messages)&gt;1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(&#x27; &#x27;)[1]
            if c.startswith(&#x27;/&#x27;):
                return _cmd.commands()
            else:
                pass
                
            
            
    def commands():
        messages = get_chat_messages()
        if len(messages)&gt;1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(&#x27; &#x27;)[1]
            a = lmsg.split(&#x27; &#x27;)[2:]
            
            if c == &#x27;/&#x27;:
                msg(&quot;Use /teams brazil,argentina to change teams and /timer to 10 minutes on screen&quot;)
            
        
        
# ba.timer(0.05, _update, repeat=True)      
def readCmd():
    msg(f&#x27;God Commands&#x27;)
    ba.timer(0.5, _cmd._home, True)
# Tell the app about our Plugin.


# ba_meta export plugin

class TimerCmd(ba.Plugin):
    &quot;&quot;&quot;My awesome plugin.&quot;&quot;&quot;
    ba.internal.set_party_icon_always_visible(True)
    readCmd()
