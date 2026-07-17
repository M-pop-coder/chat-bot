print("🤖 سلام! من چت‌بات تو هستم.")
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

    if user_message == "کمک":
        print("چه کمکی از دستم برمیاد؟")
    if user_message == "ممنون":
        print("متشکرم.برای خدمت گذاری آماده ام")
    else:
        print("🤖 گفتی:", user_message)
