def welcome():
    print("🤖 سلام! من چت‌بات تو هستم.")
    print("برای خروج exit را بنویس.\n")


def show_history(history):

    if not history:
        print("📜 هنوز تاریخچه‌ای وجود ندارد.")
        return

    print("\n📜 تاریخچه گفتگو:\n")

    for message in history:

        if message["role"] == "user":
            print(f"👤, {message["content"]}\n")

        else:
            print(f"🤖, {message["content"]}\n")


def get_answer(user_message, responses):

    for keyword, answer in responses.items():

        if keyword in user_message:
            return answer

    return None


responses = {
    "سلام": "سلام! خوش اومدی",
    "خوبی": "من عالی‌ام، ممنون.",
    "اسمت چیه": "من یک چت‌ بات پایتونی هستم.",
    "کمک": "چه کمکی از دستم برمیاد؟",
    "ممنون": "خواهش می‌کنم ❤️",
}


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
    else:
        history.append({"role": "user", "content": user_message})

    answer = get_answer(user_message, responses)

    if answer:
        print("🤖", answer)
        history.append({"role": "assistant", "content": answer})
        continue

    else:
        answer = "این را هنوز بلد نیستم"
        print("🤖", answer)
        history.append({"role": "assistant", "content": answer})
