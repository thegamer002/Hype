# ba_meta require api 7

import ba
from ba import GameActivity
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
            
            if c == '/help':
                msg("Use /teams or /timer")
            
            elif c == '/timer':
                if a==[]:
                    #try:
                    setup_standard_time_limit(10.0)
                    msg("Timer added ")
                   #except:
                     #   msg('Timer Error')
                    
 
#class GameActivity(Activity[PlayerType, TeamType]):
 #   def setup_standard_time_limit(self, duration): 
     #   self._Time = int(duration)
     
    def setup_standard_time_limit(self, duration: float) -> None:
        """
        Create a standard game time-limit given the provided
        duration in seconds.
        This will be displayed at the top of the screen.
        If the time-limit expires, end_game() will be called.
        """
        from ba._nodeactor import NodeActor

        if duration <= 0.0:
            return
        self._standard_time_limit_time = int(duration)
        self._standard_time_limit_timer = _ba.Timer(
            1.0, WeakCall(self._standard_time_limit_tick), repeat=True
        )
        self._standard_time_limit_text = NodeActor(
            _ba.newnode(
                'text',
                attrs={
                    'v_attach': 'top',
                    'h_attach': 'center',
                    'h_align': 'left',
                    'color': (1.0, 1.0, 1.0, 0.5),
                    'position': (-25, -30),
                    'flatness': 1.0,
                    'scale': 0.9,
                },
            )
        )
        self._standard_time_limit_text_input = NodeActor(
            _ba.newnode(
                'timedisplay', attrs={'time2': duration * 1000, 'timemin': 0}
            )
        )
        self.globalsnode.connectattr(
            'time', self._standard_time_limit_text_input.node, 'time1'
        )
        assert self._standard_time_limit_text_input.node
        assert self._standard_time_limit_text.node
        self._standard_time_limit_text_input.node.connectattr(
            'output', self._standard_time_limit_text.node, 'text'
        )  



def readCmd():
    ba.timer(0.5, _cmd._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()