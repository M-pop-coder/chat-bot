from responses import responses
from memory import show_history
from ui import welcome
from chatbot import get_answer

welcome()


history = []

while True:
    user_message = input("👤 شما: ").strip().lower()

    # EIXIT LOOP
    if user_message == "exit":
        print("🤖 خداحافظ!")
        break
    elif user_message == "خداحافظ":
        print("🤖سلام من رو به مادرت ابلاغ کن")
        break

    # PRINT HISTORY
    if user_message == "history":
        show_history(history)
        continue

    answer = get_answer(user_message, responses)

    if answer:
        print("🤖", answer)
    else:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)

    history.append({"role": "user", "content": user_message})
