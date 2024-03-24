from telegram import Update
from PIL import Image,ImageFont,ImageDraw
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import re
from datetime import datetime, time
from hijri_converter import convert
import pytz

token = '1220511258:AAFsOzM6AFqvw67qy2joByJZVHsfzc2Yj8c'
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.effective_message.chat_id
    user = update.effective_user
    res = str(chat_id)
    await update.message.reply_html(rf"Assalomu alaykum va rahmatullohi va barakatuh {user.mention_html()}!")

    with open('obunachilar.txt', 'a') as f:
        f.write(" {}".format(res))
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("")
counter = 0
async def salok(context: ContextTypes.DEFAULT_TYPE) -> None:
    hijri_months = [
    "Muharram", "Safar", "Rabi'ul-avval", "Rabi'ul-akhir",
    "Jumada al-awwal", "Jumada al-akhir", "Rajab", "Sha'ban",
    "Ramazon", "Shavval", "Zul-Qi'dah", "Zul-Hijjah"
    ]
    hafta_kunlari = {
        'Monday': 'Dushanba',
        'Tuesday': 'Seshanba',
        'Wednesday': 'Chorshanba',
        'Thursday': 'Payshanba',
        'Friday': 'Juma',
        'Saturday': 'Shanba',
        'Sunday': 'Yakshanba'
    }
    
    oylar = {
        'January': 'Yanvar',
        'February': 'Fevral',
        'March': 'Mart',
        'April': 'Aprel',
        'May': 'May',
        'June': 'Iyun',
        'July': 'Iyul',
        'August': 'Avgust',
        'September': 'Sentabr',
        'October': 'Oktabr',
        'November': 'Noyabr',
        'December': 'Dekabr'
    }
    hozir = datetime.now()
    hafta = hafta_kunlari[hozir.strftime('%A')]
    son = '@Onhayat_kitoblar'
    sanoq = 0
    if hafta == 'Juma':
        sanoq += 1
        jumatext = 'Juma ayyomingiz muborak bo`lsin. Alloh bu kunda qiladigan ammalllaringini o`z dargohida qabul etsin\n🤲🤲🤲Omiyn! \n\n https://t.me/Onxayat_kitoblar'
        with open('jumatabrik/juma{}.jpg'.format(sanoq), 'rb') as photo:
            await context.bot.send_photo(son, photo=photo, caption=jumatext)
        if sanoq > 10:
            sanoq = 0
        return sanoq
        
    kun = hozir.day
    oy = oylar[hozir.strftime('%B')]
    yil = hozir.year
    global counter
    counter += 1
    gregorian_date = hozir
    hijri_date = convert.Gregorian(gregorian_date.year, gregorian_date.month, gregorian_date.day).to_hijri()
    salomlash = f"👋Assalomu alaykum va rahmatullohi va barakatuh \nKitob do`konimizning qadrli a`zolari \n📚📚📚Allox sizning bugungi kuningizni mutoalaga boy qilsin ..!!! \nOmiyn.\nBugun haftaning {hafta} kuni {kun}- {oy} {yil}-yil\nHijriy: {hijri_date.day} - {hijri_months[hijri_date.month - 1]} {hijri_date.year}-yil\n👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻👇🏻\nBizning rasmiy manzilimiz: https://t.me/Onxayat_kitoblar"
    with open('salom/salom{}.jpg'.format(counter), 'rb') as photo1:
        await context.bot.send_photo(son, photo=photo1, caption=salomlash)
    with open('namoz/namoz1.jpg', 'rb') as photo:
        await context.bot.send_photo(son, photo=photo, caption="✅Namoz vaqti \n\n 🤲🤲🤲 Namozni o`z vaqtida muxofaza qiluvchilarga jannat bo`lsin! \n 🕌🕌🕌O'nhayat masjidi namoz Vaqtlari \n\n https://t.me/Onxayat_kitoblar")
    with open("textlar/izoh{}.txt".format(counter), "r", encoding="utf-8") as file:
        line = file.readlines()
        izoh1= line[0].strip()
        izoh2= line[1].strip()
        izoh3= line[2].strip()
        izoh4= line[3].strip()
        izohtext = f"{izoh1}\n🖋🖋🖋{izoh2}\n\n📚📚📚{izoh4}\n\n👉{izoh3}\nBuyurtma qilish uchun https://t.me/Zakaz_murojatbot\n\nBizga qo`shiling va kitobxonlardan bo`ling https://t.me/Onxayat_kitoblar"
    with open('rasmlar/rasm{}.jpg'.format(counter), 'rb') as photo:
        await context.bot.send_photo(son, photo=photo, caption=izohtext)
    if counter > 29:
        counter = 0
    return counter
sanoq1 = 0
sanoq2 = 0
async def salok1(context: ContextTypes.DEFAULT_TYPE) -> None:
    son = '@Onhayat_kitoblar'
    global sanoq1
    global sanoq2
    sanoq1 += 1
    sanoq2 += 1
    with open("hikmat/yozuv{}.txt".format(sanoq2), "r", encoding="utf-8") as file:
        yozuv = file.read()
    with open('hikmat/hikmat{}.jpg'.format(sanoq1), 'rb') as hikmat:
        yozuv1 = f"{yozuv}\nBuyurtma uchun https://t.me/Zakaz_murojatbot\n\nBizga qo`shiling va kitobxonlardan bo`ling https://t.me/Onxayat_kitoblar"
        await context.bot.send_photo(son, photo=hikmat, caption=yozuv1)
    if sanoq1 > 13:
        sanoq1 = 0
        return sanoq1

    if sanoq2 > 200:
        sanoq2 = 0
        return sanoq2
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    salom = update.message.text 
    kir = {
        'salom':'Assalomu alaykum',
        'Salom':'Assalomu alaykum',
        'Assalomu alaykum ' : 'Va aleykum assalom',
        'Va aleykum assalom ' : 'Ahvollaringzi qanday',
        'va aleykum assalom va rahmatullohi va barakatuh':'Ahvollaringiz yaxshimi',
        'Va aleykum assalom va rahmatullohi va barakatuh':'Ahvollaringiz yaxshimi',
        'Ishlaringiz yahshimi':'Ha yaxshi qanday zakazingiz bor',
        'ishlaringiz yahshimi':'Ha yaxshi qanday zakazingiz bor',
        'ishlaringiz yaxshimi':'Ha yaxshi qanday zakazingiz bor',
        'Ishlaringiz yaxshimi':'Ha yaxshi qanday zakazingiz bor',
        'Qanday kitbolar bor':'Hozircha qiziqarli kitoblar bor',
        'Qanday qiziqarli kitoblar bor':'Kitoblarni nomini imloviy hatolarsiz yozing Biz u haqida habar beramiz',
        'Jannat ziynati':'',
        'Umra va haj':'25000',
        'umra va haj':'25000',
        'haj va umra':'25000',
        'Umra':'15000 minglik va 25 minglari bor',
        'Islomda salomatlik':'Islomda salomatlikning narxi 25000 so`m',
        'islomda salomatlik':'Islomda salomatlikning narxi 25000 so`m',
        'bu botni kim yaratgan ':'Bu bot @Abdullox109 dasturini yozgan',
        'bu bot kimniki':'Bu bot @Abdullox109 dasturini yozgan',
        'botni hojayini kim':'Ahmatillo',
        'kitoblarni qayerdan olasizlar':'O`zimi',
        'Zakaz':'zakaz qilish uchun chetdagi knopkalardan birini bosing',
        'Ibodati islomiya':'yumshoq muqovali 30 ming qattiq muqovali 40 ming',
        'ibodati islomiya':'yumshoq muqovali 30 ming qattiq muqovali 40 ming',
        'bot kim tomonidan yaratilgan':'@qadr_user tomonidan ',
        'salom':'Assalomu alaykum',
        'Salom':'Assalomu alaykum',
        'Assalomu alaykum ' : 'Va aleykum assalom',
        'Va aleykum assalom ' : 'Ahvollaringzi qanday' ,
        'Yaxshi ' : 'Qanday yordam bera olaman' ,
        'qalaysiz':'yahshiman',
        'nima gaplar':'tinchlik',
        'nima gap':'tinchlik',
        'qachon ko`rishamiz':'Bu borada bir nima deyishim qiyin',
        'qayerda ishlayapsiz':'men hozir kitob do`konida ishlayapman',
        'hozir nima bilan bandsiz':'hozir malum bir faoliyat turi bilan shug`ullanayapman',
        'nima qilayapsiz':'siz bilan yozishayapman',
        'sizga qo`shilmoqchiman':'menga qo`shilish qadr kanalimga obuna boling va shu botga ortfoliolaringi tashlab qoying',
        'nima qilayapsan':'Bekorchilik',
        'qanday ish bu':'ma`lum ishni qoyillatmagandan keyin shuni qiladida',
        'kimsan':'Ahmatilloning shaxsiy botiman menga yuborgan habarlaringiz Ahmatilloga alohida ko`rinadi va u kuzatib boradi',
        'Yahshi korgan qizing bormi':'Ha bolgan oldin lekin hozircha yoq',
        'I love you':'Men bunday ahmoqoa malumotlarni yoqtirmayman',
        'Atom':'Atom bu kichik zarracha bo`lib undan butun borliq yaralgan va u ma`lum qismlarga bolinadi elektron proton va nesytronlarga',
        'Neytron':'Neytron bu yadroning ichida oylashgan yadroning bir bolagi bo`lib uning massasi bir buton olmish ikki o`n ustida yigirma yettiga teng',
        'Axmoq':'Bunday nomaqbul so`z ishlatmang',
        'qayerda yashaysan':'shaxsiy malumotlarni aytish taqiqlanadi',
        'Nima gap':'tinchlik nima gap bolsin bizga xizmat yoqmi',
        'Markaz qalay ketayapti':'o`quv markazi hozircha yashi ketayapti lekin ozgina muammolar bor',
        'nima ish qilayapsiz':'men hozir kitob do`konida ishlayapman',
        'sizni qanday toposam boladi':'meni faqat yakshanba kunlari topishingiz mumkin',
        'dunyo':'dunyo huddi hojatxonaga',
        'meni yoqtirasanmi':'men musilmon bo`lgan barcha odamlarni yoqtiraman',
        'akkauntizni bera olasizmi':'ha @Ahmatillo mening akkauntim',
        'akkauntingizni bera olasizmi':'ha @Ahmatillo mening akkauntim',
        'akkauntingni bera olasanmi':'ha @Ahmatillo mening akkauntim',
        'hozirgacha qanday ish qilgansiz':'@qadr_user ga qoshiling korasiz',
        'hozirgacha qanday ish qilgansan':'@qadr_user ga qoshiling korasiz',
        'tuhskunlikka tushib qoldim nima qilay':'agar siz tushkunlikka tushgan bolsangiz buni eng yaxshi yechimi bu Allohga istig`for aytish va shukr keltirish',
        'Tuya':'Bu maxsus buyruq bo`lib buni yozmang',
        'nima qila olasan':'hech nima',
        'ha unda nega javob yozayapsan':'yozgim keldi yozaman',
        'ahvollaring yahshimi':'yahshi xozircha',
        'kun tartibing qanday':'Aratalab turib yuzni yuvamiz uyog`i tavakkal',
        'ko`tarildingmi':'yog`aaaa',
        'adashayapsan':'bu ish bo`lishi mumkin',
        'Chatgpt nima':'bu suniy intellekt bolib u odamlarga yordam beradi',
        'mol':'sokinmang',
        'qo`y':'sokinmang',
        'qotoq':'sokinmang',
        'yaramas':'sokinmang',
        'jinni':'sokinmang',
        'axmoq':'sokinmang',
        'am':'sokinmang',
        'musir':'sokinmang',
        'tuya':'sokinmang',
        'it':'sokinmang',
        'mushuk':'sokinmang',
        'kuygan':'sokinmang',
        'tuxum':'sokinmang',
        'tuxumbosh':'sokinmang',
        'yebergan':'sokinmang',
        'Yi`g`ilishga boramizmi':'ha boramiz hozir ishdaman',
        'nima ish qilyapsan':'hozir muhim ishlar bilan bandman qanday ishligini bot bo`lganim uchun bilmayman',


        




    }
    text1 = salom
    text2 = kir.get(text1, 'Bu buyruq botga kiritilmagaligi uchun sizga ma`lumot bera olmaymiz iltimos boshqa gaplardan yozing kamchiliklarni to`g`irlashga harakat qilamiz') 
    await update.message.reply_text(text2)
async def rek(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('obunachilar.txt', 'r') as f:
        text = f.read()
        tes = text.split()
        sel = set(tes)
    for sat in (sel):
        son = int(sat)
    with open('rek/rek.txt', 'r') as q:
        rasmtext = q.read()
    with open('rek/rasm1.jpg', 'rb') as photo:
        await context.bot.send_photo(son, photo=photo, caption=rasmtext)
async def obuna(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('obunachilar.txt', 'r') as f:
        text = f.read()
        tes = text.split()
        sel = set(tes)
        son = len(sel)
        yoz = "Bizning obunachilarimiz soni {} ta. Daturdagi kamchiliklar sabab bir oz adashish bo`lishi mumkin".format(son)
        await update.message.reply_text(yoz)
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    salom = update.message.text
    user = update.message.from_user
    qisqa =user.first_name
    qisqa1 =user.username
    qisqa2 =user.id
    id = 1278419094
    await context.bot.send_message(id, text=salom)
    await context.bot.send_message(id, text=qisqa)
    await context.bot.send_message(id, text=f"@{qisqa1}")
    await context.bot.send_message(id, text=qisqa2)
async def namoz_vaqti(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    salom = update.message.text
    image_path = 'namoz/namoz.jpg'
    rasm = Image.open(image_path)
    chiz = ImageDraw.Draw(rasm)
    tex   = re.search(r'<(.*?)>', salom.splitlines()[0]).group(1)
    texts = re.search(r'<(.*?)>', salom.splitlines()[1]).group(1)
    text1 = re.search(r'<(.*?)>', salom.splitlines()[2]).group(1)
    text2 = re.search(r'<(.*?)>', salom.splitlines()[3]).group(1)
    text3 = re.search(r'<(.*?)>', salom.splitlines()[4]).group(1)
    font = ImageFont.truetype( r"D:/ptbot/Telegram-bot/takr/Bilanger.ttf", 80)
    font1 = ImageFont.truetype(r"D:/ptbot/Telegram-bot/takr/Bilanger.ttf", 80)
    font2 = ImageFont.truetype( "D:/ptbot/Telegram-bot/takr/Bilanger.ttf", 80)
    font3 = ImageFont.truetype( "D:/ptbot/Telegram-bot/takr/Bilanger.ttf", 80)
    font4 = ImageFont.truetype( "D:/ptbot/Telegram-bot/takr/Bilanger.ttf", 80)
    chiz.text((880,330), tex,  fill ="#3C6650", font=font,)
    chiz.text((880,480), texts, fill ="#3C6650", font=font1)
    chiz.text((880,630), text1, fill ="#3C6650", font=font2)
    chiz.text((880,780), text2, fill ="#3C6650", font=font3)
    chiz.text((880,930), text3, fill ="#3C6650", font=font4)
    rasm.save("namoz/namoz1.jpg")
    await update.message.reply_photo( photo=open('namoz/namoz1.jpg', 'rb'), parse_mode='HTML')


def main() -> None:
    application = Application.builder().token(token).build()
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    target_time1 = tashkent_tz.localize(datetime.combine(datetime.today(), time(hour=8, minute=0)))
    target_time2 = tashkent_tz.localize(datetime.combine(datetime.today(), time(hour=5, minute=0)))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("namoz", namoz_vaqti))
    application.add_handler(CommandHandler("reklama2002", rek))
    application.add_handler(CommandHandler("obunachilar", obuna))
    application.add_handler(CommandHandler("buyurtma", buy))
    application.add_handler(CommandHandler("yordam", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    jon = application.job_queue
    jon.run_daily(salok, target_time1)
    jon.run_daily(salok1, target_time2)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    
if __name__ == "__main__":
    main()
