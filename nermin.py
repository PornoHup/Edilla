# Bu repo aykhan_s tərəfindən 29.11.2022 tarixində yığılıb
# Bu repodan icazəsiz hər hansı kodu sətri məlumatı kopyalıyıb
# Öz adına çıxaran peysərdi
# Bu yazıları silmədən işlədin

# t.me/RoBotlarimTg | YouTube: RoBotlarimTg |
# t.me/aykhan_s | insta: aykhan026 | 
# GitHub: aykhan026


from komekci.aykhan import Nermin
import base64
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim,riyad,sura,reksane,yeraz,maqa,fatya,nezrin
from mesajlar.bot import yeni_user, start, info, oyun, zer, bol, ftop, btop, carx, ox
from telethon import events, Button
import random


# Yeni istifadəçi mesajı
@Nermin.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")
#start
        
nermin_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@Nermin.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}")
  
#info

@Nermin.on(events.NewMessage(pattern='(?i)/info+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(info)}")

 #oyunlar   
    
@Nermin.on(events.NewMessage(pattern='(?i)/oyunlar+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(oyun)}")
 

@Nermin.on(events.NewMessage(pattern='(?i)/zer+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(zer)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/ox+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ox)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/carx+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(carx)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/ftop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ftop)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/btop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(btop)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/boling+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(bol)}")
 




@Nermin.on(events.NewMessage(pattern='(?i)selam+'))
@Nermin.on(events.NewMessage(pattern='(?i)merhaba+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@Nermin.on(events.NewMessage(pattern='(?i)nasılsın+'))
@Nermin.on(events.NewMessage(pattern='(?i)nasılsınız+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@Nermin.on(events.NewMessage(pattern='(?i)teşekkür+'))
@Nermin.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@Nermin.on(events.NewMessage(pattern='(?i)gitdim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gidiyorum+'))
@Nermin.on(events.NewMessage(pattern='(?i)bb+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@Nermin.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@Nermin.on(events.NewMessage(pattern='(?i)@Thagiyev+'))
@Nermin.on(events.NewMessage(pattern='(?i)@mmzd_13+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Hashimova_1+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Mmmmdli+'))
@Nermin.on(events.NewMessage(pattern='(?i)@aghayefffa+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Sonnqruz+'))
@Nermin.on(events.NewMessage(pattern='(?i)@YerazzAbii+'))
@Nermin.on(events.NewMessage(pattern='(?i)@h3senovha+'))
@Nermin.on(events.NewMessage(pattern='(?i)@fliz190+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Sorgoz_putin+'))
@Nermin.on(events.NewMessage(pattern='(?i)riyad+'))
@Nermin.on(events.NewMessage(pattern='(?i)yeraz+'))
@Nermin.on(events.NewMessage(pattern='(?i)reksane+'))
@Nermin.on(events.NewMessage(pattern='(?i)fatya+'))
@Nermin.on(events.NewMessage(pattern='(?i)nezrin+'))
@Nermin.on(events.NewMessage(pattern='(?i)@thagiyev+'))
@Nermin.on(events.NewMessage(pattern='(?i)sura+'))
@Nermin.on(events.NewMessage(pattern='(?i)maqa+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(thagiyev)}")

@Nermin.on(events.NewMessage(pattern='(?i)ban+'))
@Nermin.on(events.NewMessage(pattern='(?i)kick+'))
@Nermin.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)🙄+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji1)}")

@Nermin.on(events.NewMessage(pattern='(?i)😂+'))
@Nermin.on(events.NewMessage(pattern='(?i)🤣+'))
@Nermin.on(events.NewMessage(pattern='(?i)😅+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji2)}")

@Nermin.on(events.NewMessage(pattern='(?i)federasyon+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(fed)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)neden+'))
@Nermin.on(events.NewMessage(pattern='(?i)niye+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(niye)}")

    
@Nermin.on(events.NewMessage(pattern='(?i)ne+'))
@Nermin.on(events.NewMessage(pattern='(?i)nasıl+'))
@Nermin.on(events.NewMessage(pattern='(?i)what+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ne)}")
   
@Nermin.on(events.NewMessage(pattern='(?i)hey+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hay)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)mal+'))
@Nermin.on(events.NewMessage(pattern='(?i)maal+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(mal)}")
    
    
@Nermin.on(events.NewMessage(pattern='(?i)canım+'))
@Nermin.on(events.NewMessage(pattern='(?i)can+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(can)}")
    
    
@Nermin.on(events.NewMessage(pattern='(?i)kuzum+'))
@Nermin.on(events.NewMessage(pattern='(?i)canım+'))
@Nermin.on(events.NewMessage(pattern='(?i)❤+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(balam)}")
   
@Nermin.on(events.NewMessage(pattern='(?i)hoş+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(xos)}")
     
@Nermin.on(events.NewMessage(pattern='(?i)nereye+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hara)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)gel+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gel)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)gördüm+'))
@Nermin.on(events.NewMessage(pattern='(?i)gördünmü+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gordum)}")
         
@Nermin.on(events.NewMessage(pattern='(?i)tema+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(taım)}")

        
        
        
        
nermin_run = nermin_start.decode("utf8")
print(">> Chat bot uğurla işləyir ♿ <<")
print(f"{nermin_run}")
Nermin.run_until_disconnected()
