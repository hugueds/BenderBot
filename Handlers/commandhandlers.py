import core
from features import generateOffense
from features import timeHelper


def callback_minute(context):
    if timeHelper.get_actual_time() >= 0 and timeHelper.get_actual_time() <= 7:
        return
    if not core.bender_bot.mute:
        chat_id = context.job.context
        context.bot.send_message(chat_id=chat_id,
                                 text=generateOffense.generateOffense())


def start(update, context):
    if not core.bender_bot.offenseOn and not (0 <= timeHelper.get_actual_time() <= 7):
        core.bender_bot.offenseOn = True
        context.job_queue.run_repeating(callback_minute, interval=3600, first=1,
                                        context=update.message.chat_id)
    else:
        if not (timeHelper.get_actual_time() >= 0 and timeHelper.get_actual_time() <= 7):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Seu degenerado! Alguém já deu start em mim! " +
                                          "Se você quer tanto assim que eu te humilhe, espere a sua vez!")


def repo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Nossos repositórios\n\n" +
                                  "Grupo-OpenCV-BR -> https://github.com/Grupo-OpenCV-BR\n\n" +
                                  "Tutoriais e Dicas -> https://github.com/Grupo-OpenCV-BR/tutoriais-tecnologia \n\n" +
                                  "Imagens Médicas -> https://github.com/Grupo-OpenCV-BR/imagens-medicas\n\n" +
                                  "Prova e testes -> https://github.com/Grupo-OpenCV-BR/imagens-medicas \n\n" +
                                  "CookBook -> https://github.com/Grupo-OpenCV-BR/cookbook \n\n" +
                                  "Claro , o repositório mais importante -> https://github.com/Grupo-OpenCV-BR/BenderBot \n\n" +
                                  "A contribuição é aberta, só mandar a PR que a @natalia_py e o @andreemidio1 aprovam\n\n " +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@natalia_py, @andreemidio1 , @TioPerneta e @hugueds \n\n\n\n" +
                                  "# E vão estudar bando de baderneiros !!")


def vagas(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Vagas de Visão Computacional \n\n" +
                                  "Visão Computacional -> https://www.linkedin.com/jobs/search/?f_WRA=true&geoId=106057199&keywords=Vis%C3%A3o%20computacional&location=Brasil&position=1&pageNum=0\n\n" +
                                  "A Até conseguirmos criar uma plataforma de visualização dessas vagas aqui no grupo, iremos usar o link acima.\n\n " +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@natalia_py, @andreemidio1 , @TioPerneta e @hugueds \n\n" +
                                  "Parem de vacilação e corram atrás, se você não for, você é um bundão !! \n\n")



def mute_(update, context):
    # blackListManager.free_members()
    # member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "mute")

    # if member_in_blacklist:
    #     return
    # else:
    #     blackListManager.add_member(update.message.from_user.first_name, "mute")
    
    if core.bender_bot.mute:
        pass
    else:
        core.bender_bot.mute = True
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                            text= "Ok... Ok... Estou calando a boca!")


def unmute(update, context):
    if not core.bender_bot.mute:
        pass
    else:       
        core.bender_bot.mute = False
        context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text= "I'm back, bitches! Mordam a minha bunda de metal!")


def help(update, context):
    # blackListManager.free_members()
    # member_in_blacklist = blackListManager.is_member_in_blacklist(update.message.from_user.first_name, "help")
    #
    # if member_in_blacklist:
    #     return
    # else:
    #     blackListManager.add_member(update.message.from_user.first_name, "help")
    #
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="LISTA DE COMANDOS:\n" +
                                  "/start -> Comando para que eu envie xingamentos a cada 1h\n" +
                                  "/repo -> Comando para acessar nossos repositórios\n" +
                                  "/vagas -> Comando para mostrar vagas de CV \n" +
                                  "/mute_ -> Comando para eu calar a minha boca\n" +
                                  "/unmute -> Comando para que eu volte a xingar vocês\n" +
                                  "/help -> Comando que exibe esta lista de comandos\n\n" +
                                  "ATENÇÃO\n" +
                                  "Se eu ficar xingando de madrugada, basta usar o comando /mute_\n" +
                                  "Se eu apresentar mal funcionamento, fale com os idiotas que cuidam da minha manutenção:\n" +
                                  "@natalia_py, @andreemidio1, @TioPerneta e @hugueds \n\n" +
                                  "E tenho dito! Truuuuucccoooooooooooo Marreco !")
