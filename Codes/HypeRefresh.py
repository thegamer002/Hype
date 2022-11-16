# ba_meta require api 7

from ba.internal import get_chat_messages as gmsg, chatmessage as msg
import ba.internal as bs
import ba
import _ba
import os
import HypeTagsHashes as htgs




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
    
    def PermissionCheck(self, ClientID):
        session = _ba.get_foreground_host_session().sessionplayers
        admins = []
        for player in session:
            if player.inputdevice.get_v1_account_id() == ClientID:
                admins = player.get_v1_account_id()
        if admins in htgs.Admin:
            return True
        else: 
            return _cmd.PermissionCheck
            
            
    def commands(self, ClientID):
        messages = gmsg()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
        
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
        
            if c in ['/help', '/']:
                msg("___________________________________")
                msg("|/pwd - To show current Path       |")
                msg("|/ref, /refresh - To mods          |")
                msg("|/mods - To see mods in directory  |")
                msg("|/list, /l - To see players id     |")
                msg("|/help - To see commands           |")
            
            elif c == '/pwd':
                os.system("pwd > cmd.txt")
                f = open("cmd.txt", "r")
                msg(f" Server Path Is : {f.read()}")
            
            
            elif c in ['/ref', '/refresh']:
                msg("Server Refreshing Mods!, Enter In one minute.")
                os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && sudo cp HypeServerStaff/Codes/* ba_root/mods/ && sudo rm -rf HypeServerStaff/")
                msg("_____________Upload Complete______________")
                
            elif c == '/mods':
                os.system("sudo ls ba_root/mods/ > cmd.txt")
                msg("Archives or Mods")
                with open("cmd.txt", "r") as cmd:
                    command = cmd.readlines()
                for lin in command: 
                    msg(lin)
            
            elif c in ['/l', '/list']:
                session = _ba.get_foreground_host_session().sessionplayers
                msg("_________________________________________________")
                msg("|         •NAME•        |          •IDs•        |")
                msg("|_______________________|_______________________|")
                for player in session:
                    msg(f"|{player.getname(True, True)} ---> {player.id} or {player.inputdevice.client_id}")
                msg("|_______________________________________________|")
         
        
                
                
    
def readCmd():
    ba.timer(0.5, _cmd._home, True)
    #ba.timer(5.0, _cmd.testingserver, False)
    
# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   