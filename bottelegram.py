import telebot


API_KEY = "your api-key here"

bot = telebot.TeleBot(API_KEY)  

@bot.message_handler(commands=["opcao1"])
def opcao1(menssagem):
    bot.send_message(menssagem.chat.id, 'Acesse meu perfil do GitHub: https://github.com/BetoSytherine')
 

@bot.message_handler(commands=["opcao2"])
def opcao2(menssagem):
    
     bot.send_message(menssagem.chat.id, 'Por ser apenas um teste não adicioantei uita opções por enquanto!')




@bot.message_handler(commands=["opcao3"])
def opcao3(menssagem):
    
    bot.send_message(menssagem.chat.id, 'Abraçõ cara tamo junto!!')





def verificar(menssagem):
    return True


@bot.message_handler(func=verificar)
def responder(menssagem):

    texto = """Seguinte meu parceiro, to sem brincadeira ja é?
Escolhe alguma dessas opções ae, sem risadinha jae, se não o tapao vai cumer rapa:
               
               /opcao1 - Acessar GitHub
               /opcao2 - ...
               /opcao3 - Mandar um abraço!
               
               Qualquer outra merda aeu vou repetir esta poha de texto"""

    bot.reply_to(menssagem, texto)




bot.polling()
