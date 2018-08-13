from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, asyncio, json, threading, codecs, sys, os, re, urllib, requests, wikipedia, html5lib, timeit, pafy, youtube_dl

line = LINE("")
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))


cl = line
oepoll = OEPoll(cl)
mid = cl.profile.mid
Bots = [cl]
RASuper = ["u0237b0ec326fc36a91743df4a1ad2591","ube1a66baeac2eca0dbf4f88808273b21","u46a01dcbd2f0a7619a365af18d337f12","ub121ee804555b797edb570fe364ada13","ua58d0ae01e030c10ca98944472e7c1d7","ud1d6400274da6a0a0b630332d4da50b7","u4da22f6d8d4c8d82dfd63e10c0215dba"]
RAStaff = ["u0237b0ec326fc36a91743df4a1ad2591"]
RAFa = RASuper + RAStaff
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot) 

def bot(op):
    try:
        if op.type == 5:
            if Setmain["autoadd"] == True:
                cl.sendMessageWithMention(op.param1, op.param1,"Hai","\nsalam kenal ya\n\n{}".format(str(Setmain["RAmessage"])))
                

        if op.type == 13:
            if mid in op.param3:
              if op.param2 in RASuper:                    
                if Setmain["autojoin"] == True:                 
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 13:
            if op.param3 in Setmain["blacklist"]:
                cl.cancelGroupInvitation(op.param1,[op.param3])
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass                
        if op.type == 17:
            if op.param2 in Setmain["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass              
        if op.type == 19:
           if op.param3 in RASuper:
              cl.inviteIntoGroup(op.param1,RASuper)            
              cl.kickoutFromGroup(op.param1,[op.param2])
              Setmain["blacklist"][op.param2] = True
           else:
               pass 
        if op.type == 55:
          if mid in op.param1:
            if op.param2 in Setmain["blacklist"]:
                cl.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass               
        if op.type == 46:
            if op.param2 in mid:
                cl.removeAllMessages() 
        if op.type == 19:
            if mid in op.param3:
               Setmain["blacklist"][op.param2] = True
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = sender
                elif msg.toType == 2:
                    to = receiver
                    
                if msg.contentType == 13:
                    if Setmain["autoscan"] == True:
                        msg.contentType = 0
                        cl.sendText(msg.to,msg.contentMetadata["mid"])
                        
                elif msg.contentType == 0:
                    if Setmain["autoread"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:
                        
            #---------------------- Start Command ------------------------#
                        
                        if text.lower() == "menu":
                          if msg._from in RASuper:                        
                              md = " 🔎² 🔎² αя вσтѕ 🔎² \n\n"
                              md += "🔎² .cek「@」\n"
                              md += "🔎² .gid\n"
                              md += "🔎² .yid\n"
                              md += "🔎² .pengaturan\n"
                              md += "🔎² .restart\n"
                              md += "🔎² .removechat\n"
                              md += "🔎² .cekmid 「on/off」\n"
                              md += "🔎² .autoread 「on/off」\n"
                              md += "🔎² menu1\n"
                              cl.sendText(msg.to, md)
                            
                        if text.lower() == "menu1":
                          if msg._from in RASuper:                        
                              md = " 🔎² 🔎² αя вσтѕ 🔎²  \n\n"
                              md += "🔎² .protect on/off\n"
                              md += "🔎² .qr on/of\n"
                              md += "🔎² .invite on/off\n"
                              md += "🔎² .larangan on/off\n"                            
                              md += "🔎² .hai\n"
                              md += "🔎² .respon\n"                            
                              md += "🔎² .spbot\n"
                              md += "🔎² .clearban\n"
                              md += "🔎² .pulang\n"                                
                              md += "🔎² .listbl\n"                                
                              cl.sendText(msg.to, md)                            
                            
                        elif text.lower() == ".set":
                            if msg._from in RASuper:
                                ginfo = cl.getGroup(msg.to)                               
                                md = "\n\npengaturan di group\n " +str(ginfo.name) + "\n\n"
                                if Setmain["autoscan"] == True: md+="✅  cekmid\n"
                                else: md+="❎ cekmid\n"
                                if Setmain["autoread"] == True: md+="✅ autoread\n"
                                else: md+="❎ autoread\n"
                                if Setmain["protect"] == True: md+="✅ protect\n"
                                else: md+="❎ protect\n"
                                if Setmain["protectqr"] == True: md+="✅ qr\n"
                                else: md+="❎ qr\n"
                                if Setmain["protectguest"] == True: md+="✅ invite\n"
                                else: md+="❎ invite\n"
                                if Setmain["autojoin"] == True: md+="✅ autojoin\n"
                                else: md+="❎ autojoin\n" 
                                if Setmain["larangan"] == True: md+="✅ larangan\n"
                                else: md+="❎ larangan\n"                                     
                                cl.sendText(msg.to, md)
                                
            #---------------------- On/Off Command -------------------# 
            
                        elif text.lower() == ".autoread on":
                            if msg._from in RASuper:
                                if Setmain["autoread"] == False:
                                    Setmain["autoread"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".autoread off":
                            if msg._from in RASuper:
                                if Setmain["autoread"] == True:
                                    Setmain["autoread"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Autoread dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")
                        elif text.lower() == ".join on":
                            if msg._from in RASuper:
                                if Setmain["autojoin"] == False:
                                    Setmain["autojoin"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","already on")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".join off":
                            if msg._from in RASuper:
                                if Setmain["autojoin"] == True:
                                    Setmain["autojoin"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","already off")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","sudah off")                                    
                                    
                                    
                
            
                        elif text.lower() == ".qr on":
                            if msg._from in RASuper:
                                if Setmain["protectqr"] == False:
                                    Setmain["protectqr"] = True
                                    cl.sendMessageWithMention(msg.to,msg._from,"","protect Qr diaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                   
                        elif text.lower() == ".cekmid on":
                            if msg._from in RASuper:
                                if Setmain["autoscan"] == False:
                                    Setmain["autoscan"] = True
                                    ginfo = cl.getGroup(msg.to)
                                    msgs = "cekmid diaktifkan\nDi Group  " +str(ginfo.name)
                                    cl.sendText(msg.to, msgs)                                    
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah aktif")
                                    
                        elif text.lower() == ".cekmid off":
                            if msg._from in RASuper:
                                if Setmain["autoscan"] == True:
                                    Setmain["autoscan"] = False
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Cekmid dinonaktifkan")
                                else:
                                    cl.sendMessageWithMention(msg.to,msg._from,"","Sudah off")            
                            
            #---------------- Fungsi Command ------------------#
                        
                                                                       
                        elif ".cek" in text.lower():
                            if msg._from in RASuper:                    
                                key = eval(msg.contentMetadata["MENTION"])
                                keys = key["MENTIONEES"][0]["M"]
                                ra = cl.getContact(keys)
                                try:
                                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/{}".format(str(ra.pictureStatus)))
                                    cl.sendMessageWithMention(msg.to,ra.mid,"[Nama]\n","\n\n[Bio]\n{}".format(str(ra.statusMessage)))
                                except:
                                    pass
                            
                        elif text.lower() == ".gid":
                            if msg._from in RASuper:                            
                                cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                                cl.sendText(msg.to,msg.to)
                            
                        elif text.lower() == ".yid":
                            if msg._from in RASuper:                            
                                cl.sendMessageWithMention(msg.to, msg._from,"","\nMemproses..")
                                cl.sendText(msg.to,msg._from)
                        
                        elif text.lower() == "bot":
                            if msg._from in RASuper:                            
                                cl.sendText(msg.to, "opo bos")
                            
                        elif text.lower() == "spedo":
                            if msg._from in RASuper:                            
                                start = time.time()
                                cl.sendText(msg.to, "wait..")
                                elapsed_time = time.time() - start
                                cl.sendText(msg.to, "%s " % (elapsed_time))
                          
                        elif text.lower() == "restart":
                            if msg._from in RASuper:
                                cl.sendText(msg.to,"wait....")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)
                                
                        elif text.lower() == "hapuschat":
                            if msg._from in RASuper:
                                try:
                                    cl.removeAllMessages(op.param2)
                                    cl.sendText(msg.to, "chat di bersihkan")
                                except:
                                    pass        
                                                    
                        elif text.lower() == "bye":
                            if msg._from in RASuper:
                                ra = cl.getGroup(msg.to)
                                #cl.sendMessageWithMention(msg.to,ra.creator.mid,"Maaf pemilik group","\naku keluar dulu ya..")
                                cl.leaveGroup(msg.to)
                        elif text.lower() =="clearban":
                            if msg._from in RASuper:                                
                                Setmain["blacklist"] = {}
                                cl.sendText(msg.to, "resik kabeh")                                 

                        elif text.lower() == ".listgroup":
                            if msg._from in RASuper:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendText(msg.to,"╔══[ ℓιsт gяσυρ ]\n║\n"+ma+"║\n╚══[ тσтαℓ「"+str(len(gid))+"」gяσυρ ]")                                
                                
                        elif text.lower() == ".listbl":
                            if msg._from in RASuper:
                                if Setmain["blacklist"] == {}:
                                    cl.sendText(msg.to, "blacklist kosong bro")
                                else:
                                    no = 0
                                    hasil = "\n"
                                    for a in cl.getContacts(Setmain["blacklist"]):
                                        no += 1
                                        hasil += "\n" + str(no) + ". " + str(a.displayName)
                                    hasil += "\n\ntotal {} kotoran".format(str(len(cl.getContacts(Setmain["blacklist"]))))
                                    cl.sendText(msg.to,hasil)

                                    
                        elif ".hai" in text.lower():
                            if msg._from in RASuper:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Bots:
                                        pass
                                    else:
                                        try:
                                            #cl.sendMessageWithMention(msg.to,target,"Maaf","aku kick")
                                            klist = [cl]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                        except:
                                            pass                                                              
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in RASuper:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["autojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        
                                    else:    
                                        cl.sendMessageWithMention(msg.to,msg._from,"Maaf","\naktifkan auotojoin dulu")

    except Exception as error:
        print (error)
        
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
