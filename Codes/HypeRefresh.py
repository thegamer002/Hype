# ba_meta require api 7

#odules
from ba.internal import get_chat_messages as gmsg, chatmessage as msg
from ba import _hooks
import ba
import _ba
import os


#Main Code
class _cmd():


    def _home():
        
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            
            if c.startswith('/'):
                return _cmd.commands()
            else:
                pass


    def commands():
        
        session = _ba.get_foreground_host_session().sessionplayers
        
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]

            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
            
            
            msg(str(_hooks.filter_chat_message(msg, client_id)))
                
            if c == '/pwd':
                os.system("pwd > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f" Server Path Is : {f.read()}")
            
            
            elif c in ['/ref', '/refresh']:
                msg("Server Refreshing Mods!, Enter In one minute.")
                os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && sudo cp HypeServerStaff/Codes/* ba_root/mods/ && sudo rm -rf HypeServerStaff/")
                msg("_____________Upload Complete______________")
                
                
            elif c == '/mods':
                os.system("sudo ls ba_root/mods/ > cmd.txt ")
                
                
                with open("cmd.txt", "r") as cmd:
                    command = cmd.readlines()
                for lin in command: 
                    msg(lin)
                
                msg("===Archives or Mods===")
                
                
            elif c in ['/l', '/list']:
                
                if session == []:
                    
                    msg("Players Not Found")
                else:
                    msg("== Name ==|== IDs ==")
                    for player in session:
                        msg(f"{player.getname(True, True)[0:9]} ----> {player.id}")
                        
                    msg("")
                    msg("== For kick only ==")
                    
                    for player in session:
                        msg(f"{player.getname(True, True)[0:9]} ----> {player.inputdevice.client_id}")
                    msg("===============")
        
            elif c == '/restart':
                ba.quit()



def readCmd():
    ba.timer(0.5, _cmd._home, True)
    #ba.timer(5.0, _cmd.testingserver, False)
    
# ba_meta export plugin

class cmds(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   