# ba_meta require api 7

#odules
from ba.internal import get_chat_messages as gchatmsg, chatmessage as chatmsg
from ba import _hooks
import ba
import _ba
import os


#Main Code
class _cmd():


    def _home():
        
        messages = gchatmsg()
        if len(messages)>1:
            lchatmsg = messages[len(messages)-1]
            
            c = lchatmsg.split(' ')[1]
            
            if c.startswith('/'):
                return _cmd.commands()
            else:
                pass


    def commands():
        
        session = _ba.get_foreground_host_session().sessionplayers
        
        messages = gchatmsg()
        if len(messages)>1:
            lchatmsg = messages[len(messages)-1]

            c = lchatmsg.split(' ')[1]
            a = lchatmsg.split(' ')[2:]
            playername = lchatmsg.split(':')[0]
            
            if playername in ['\ue063VinesCraft']:
                if c in ['/', '/help']:
                    
                    chatmsg("/help --> to see commands")
                    chatmsg("/kick PLAYER_ID --> to kick Players")
                    chatmsg("/mods --> to see currenty mods")
                    chatmsg("/list --> to see players_id, pb-ids")
                    chatmsg("/refresh or /ref --> to reload the mods")
                    chatmsg("/end --> for end game")
                
                
                elif c in ['/ref', '/refresh']:
                    chatmsg("Server Refreshing Mods!, Enter In one minute.")
                    os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && sudo cp HypeServerStaff/Codes/* ba_root/mods/HypeAdminCmds.py && sudo rm -rf HypeServerStaff/")
                    chatmsg("_____________Upload Complete______________")
                    
                    
                elif c == '/mods':
                    os.system("sudo ls ba_root/mods/ > cmd.txt ")
                    with open("cmd.txt", "r") as cmd:
                        command = cmd.readlines()
                    for lin in command: 
                        mods = lin.split(".py")[0]
                        chatmsg(mods)
                    
                    chatmsg("===Archives or Mods===")
                    
                    
                elif c in ['/l', '/list']:
                    
                    if session == []:
                        chatmsg("Players Not Found")
                        
                    else:
                        chatmsg("== Name == IDs ==")
                        for player in session:
                            chatmsg(f"{player.getname(True, True)[0:9]} ----> {player.id}")
                            
                        
                        chatmsg("== For kick only ==")
                        
                        for player in session:
                            chatmsg(f"{player.getname(True, True)[0:9]} ----> {player.inputdevice.client_id}")
                        
                            
                        chatmsg("==== PB-IDs =====")
                        
                        for player in session:
                            chatmsg(f"{player.getname(True, True)[0:9]} ----> {player.get_v1_account_id()}")
                        chatmsg("=================")
                        
                elif c in ['/kick', '/k']:
                    if a == []:
                        chatmsg("use /kick ID MOTIVE")
                        
                    else:
                        os.system(f"echo {a[1]} >> kickLogs.txt")
                        chatmsg(f"{session[a[0]].getname(True, True)} Kicked")
                        _ba.disconnect_client(int(a[0]))
                        
                elif c == '/end':
                    ba.screenmessage("Game ending", (0,1,0))
                    _ba.get_foreground_host_session().end_game()
                    
                    
                else:
                    chatmsg("Command Error")



def readCmd():
    ba.timer(0.5, _cmd._home, True)
    #ba.timer(5.0, _cmd.testingserver, False)
    
# ba_meta export plugin

class cmds(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    readCmd()   