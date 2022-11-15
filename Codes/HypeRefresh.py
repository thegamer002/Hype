# ba_meta require api 7

from ba.internal import get_chat_messages as gmsg, chatmessage as msg
import ba.internal as bs
import ba
import _ba
import os



class _cmd():
    def testingserver():
        msg("Server is in testing")
        
    def _home():
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/' or ';'):
                return _cmd.commands()
            else:
                pass
    
    def PermissionCheck()
        session = _ba.get_foreground_host_session().sessionplayers
        admins = []
        for player in session:
            if player.inputdevice.get_v1_account_id == admins
            
            
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
                os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && sudo cp HypeServerStaff/Codes/* ba_root/mods/ && sudo rm -rf HypeServerStaff/")
                msg("_____________Upload Complete______________")
                
            if c == '/mods':
                os.system("sudo ls ba_root/mods/ > cmd.txt")
                msg("Archives or Mods")
                with open("cmd.txt", "r") as cmd:
                    command = cmd.readlines()
                for lin in command: 
                    msg(lin)
            
            if c in ['/l', '/list']:
                session = _ba.get_foreground_host_session().sessionplayers
                msg("|--------•NAME•--------|----------•ID•----------|")
                for player in session:
                    msg(f"|{player.getname()} ---> {player.id} or {player.inputdevice.client_id}")
                msg("|-----------------------------------------------|")
                
                
                
    
def readCmd():
    ba.timer(0.5, _cmd._home, True)
    #ba.timer(5.0, _cmd.testingserver, False)
    
# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   