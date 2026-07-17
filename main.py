responses = {
    "سلام": "سلام! خوش اومدی",
    "خوبی": "من عالی‌ام، ممنون.",
    "اسمت چیه": "من یک چت‌ بات پایتونی هستم.",
    "کمک": "چه کمکی از دستم برمیاد؟",
    "ممنون": "خواهش می‌کنم ❤️"
}


print("🤖 سلام! من چت‌ بات تو هستم.")
print("رابنویس exit برای خروج\n")

while True:
    user_message = input("👤 شما: ")

    # EIXIT LOOP
    if user_message.lower().strip() == "exit":
        print("🤖 خداحافظ!")
        break
    elif user_message.strip() == "خداحافظ":
        print("سلام من رو به مادرت ابلاغ کن")
        break

    found = False

    for i in responses:
        if i in user_message:
            print(responses[i])
            found = True
            break
        
    if not found:
        print("این را هنوز بلد نیستم")
