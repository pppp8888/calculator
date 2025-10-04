def show_menu():
    print("\n🧮 เครื่องคิดเลข")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")


while True:
    show_menu()
    choice = input("กรุณาเลือกเมนู (1-5): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("ป้อนเลขที่ 1: "))
            num2 = float(input("ป้อนเลขที่ 2: "))
        except ValueError:
            print("⚠️ กรุณาใส่ตัวเลขให้ถูกต้อง")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"ผลลัพธ์: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"ผลลัพธ์: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"ผลลัพธ์: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("❌ หารด้วย 0 ไม่ได้")
            else:
                result = num1 / num2
                print(f"ผลลัพธ์: {num1} / {num2} = {result}")


    else:
        print("⚠️ กรุณาเลือกเมนูระหว่าง 1 ถึง 5 เท่านั้น")
