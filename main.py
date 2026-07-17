print("🤖 سلام! من چت‌بات تو هستم.")
print("رابنویس exit برای خروج")

while True:
    user_message = input("👤 شما: ")

    if user_message.lower() == "exit":
        print("🤖 خداحافظ!")
        break

    print("🤖 گفتی:", user_message)