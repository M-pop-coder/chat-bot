from responses import responses
from ui import welcome
from chatbot import ChatBot
from normalize import normalizer

bot = ChatBot()


welcome()



while True:
    user_message = normalizer(input("👤 شما: "))

    # EIXIT LOOP
    if user_message == "exit":
        print("🤖 خداحافظ!")
        break
    elif user_message == "خداحافظ":
        print("🤖سلام من رو به مادرت ابلاغ کن")
        break

    # PRINT HISTORY
    if user_message == "history":
        bot.show_history()
        continue
    else:
        # APPEND HISTORY (USER)
        # برای اینکه خود کلمه ی history ذخیره نشود
        bot.add_user_message(user_message)

    answer = bot.get_answer(user_message, responses)

    if answer:
        print("🤖", answer)
    else:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)

    # APPEND HISTORY (BOT)
    bot.add_assistant_message(answer)
    bot.save_history()

