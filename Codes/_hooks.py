
def check_admin(client_id: int) -> bool:
    from HypeHashes import admin as idz
    for p in _ba.get_foreground_host_session().sessionplayers:
        if p.inputdevice.client_id == client_id:
            if p.get_v1_account_id() in idz:
                return True
                print(dir(p))
                print(dir(p[0]))
            else:
                return False

def cmds(inp:str,clid:int):
    chtmsg = _ba.chatmessage
    scrmsg = _ba.screenmessage
    
    if inp in ["/check", "/c"]:
        scrmsg("Commands works sir!", color=(0.2,1,0.2),transient=True,clients=[clid])
    
    if c in ['/', '/help']:
                    
                    chatmsg("/help --> to see commands")
                    chatmsg("/kick PLAYER_ID Motive Ban-Time--> to kick Players")
                    chatmsg("/mods --> to see currenty mods")
                    chatmsg("/list --> to see players_id, pb-ids")
                    chatmsg("/refresh or /ref --> to reload the mods")
                    chatmsg("/end --> for end game")
                    chatmsg("/restart --> To restart the server")
                
                
                elif c in ['/ref', '/refresh']:
                    os.system("sudo rm -rf HypeServerStaff/ && gh repo clone thegamer002/HypeServerStaff && sudo cp HypeServerStaff/Codes/* ba_root/mods/ && sudo rm -rf HypeServerStaff/ && sudo rm -f ba_root/mods/HypeRefresh.py")

                    
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
                        chatmsg("use /kick ID MOTIVE BAN-TIME -> Optional")
                    
                    else:
                        motive = str(a[1])
                        os.system(f"echo {motive} >> kickLogs.txt")
                        chatmsg("Player Kicked")
                        
                        if len(a)==3:
                            _cmd.kick_server(int(a[0]), int(a[2]))
                        elif len(a)==2:
                            _cmd.kick_server(int(a[0]))
                            
                        
                elif c == '/end':
                    try:
                        _ba.get_foreground_host_activity().end_game()
                    except: chatmsg("Game Ended")
                    
                        
                elif c == '/restart':
                    _cmd.restart_server()
                    
                
                elif c == '/kicklog':
                    if a ==[]:
                        chatmsg("use view or delete")
                        
                    elif a[0] == 'view':
                        with open("kickLogs.txt", "r") as log:
                            kicklog = log.readlines()
                        
                        for line in kicklog:
                            chatmsg(line)
                            
                    elif a[0] == 'delete':
                        os.system("sudo rm -f kickLogs.txt")
    


def filter_chat_message(msg: str, client_id: int) -> str | None:
    
    if msg[0] == "/":
        if check_admin(client_id=client_id):
            print("admin just sent a command")
            cmds(inp=msg,clid=client_id)
            return None
        else:
            print("non-admin just sent a command")
    return msg