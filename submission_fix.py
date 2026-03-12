# Product recommendation chatbot that provides recommendations for a laptop or phone

# User input

def ask_user(question, valid_options):
    max_retries = 0
    while max_retries <= 3:
        print(question)
        answer = input("Your answer: ").strip().lower()

        # Error #1: Empty input
        if answer == "":
            print("You didn't type anything. Please enter a value and try again.\n")
            print("\033[31m" + f"You have {3 - max_retries} attempts left." + "\033[0m")
            max_retries +=1

        # Error #2: Invalid input
        elif answer not in valid_options:
            print(f"That is not a valid option. Please choose from one of the following options: {valid_options}\n")
            print("\033[31m" + f"You have {3 - max_retries} attempts left." + "\033[0m")
            max_retries +=1
        
        else:
            return answer
    
    print("\033[31m" + "Too many invalid attempts. Exiting the chatbot." + "\033[0m")
    exit()

# Laptop flow

def laptop_flow():
    print("Understood. Let me ask you a few questions first.")

    os = ask_user(
        "What operating system do you prefer?\n  1) Windows\n  2) macOS",
        ["windows", "macos", "1", "2"]
    )

    budget = ask_user(
        "What is your budget?\n  1) low (under $800)\n  2) high (over $800)",
        ["low", "high", "1", "2"]
    )

    use_case = ask_user(
        "What will you mainly use it for?\n  1) student\n  2) work\n  3) personal",
        ["student", "work", "personal", "1", "2", "3"]
    )

    # Map number inputs to words
    if os == "1": os = "windows"
    if os == "2": os = "macos"
    if budget == "1": budget = "low"
    if budget == "2": budget = "high"
    if use_case == "1": use_case = "student"
    if use_case == "2": use_case = "work"
    if use_case == "3": use_case = "personal"

    # Windows recommendations
    if os == "Windows":
        if budget == "low":
            if use_case == "student":
                print("I recommend the Acer Aspire 5.")
            elif use_case == "work":
                print("I recommend the Lenovo IdeaPad 3.")
            else:
                print("I recommend the HP Pavilion 15.")
        else:
            if use_case == "student":
                print("I recommend the Dell XPS 13.")
            elif use_case == "work":
                print("I recommend the Microsoft Surface Pro.")
            elif use_case == "personal":
                print("I recommend the ASUS ROG Zephyrus.")

    # macOS recommendations
    else:
        if budget == "low":
            if use_case == "student":
                print("I recommend the MacBook Neo (A18 Pro).")
            elif use_case == "work":
                print("I recommend the MacBook Pro (M1). You can get this used.")
            else:
                print("I recommend the MacBook Air (M1). You can get this used.")
        else:
            if use_case == "student":
                print("I recommend the MacBook Air (M5, 13 inch).")
            elif use_case == "work":
                print("I recommend the MacBook Pro (M5 Max, 16 inch).")
            else:
                print("I recommend the MacBook Pro (M5, 14 inch).")


# Phone flow

def phone_flow():
    print("Understood. Let me ask you a few questions first.")

    os = ask_user(
        "Do you prefer Android or iPhone?\n  1) Android\n  2) iPhone",
        ["android", "iphone", "1", "2"]
    )
    
    budget = ask_user(
        "What is your budget?\n  1) low (under $500)\n  2) high (over $500)",
        ["low", "high", "1", "2"]
    )

    feature = ask_user(
        "\nWhat feature matters most to you?\n  1) camera\n  2) battery\n  3) performance",
        ["camera", "battery", "performance", "1", "2", "3"]
    )

    # Map number inputs to words
    if os == "1": os = "Android"
    if os == "2": os = "iPhone"
    if budget == "1": budget = "low"
    if budget == "2": budget = "high"
    if feature == "1": feature = "camera"
    if feature == "2": feature = "battery"
    if feature == "3": feature = "performance"

    # Android recommendations
    if os == "Android":
        if budget == "low":
            if feature == "camera":
                print("I recommend the Google Pixel 8a.")
            elif feature == "battery":
                print ("I recommend the OnePlus 12R.")
            else:
                print("I recommend the Samsung Galaxy A35.")
        else:
            if feature == "camera":
                print("I recommend the Google Pixel 10.")
            elif feature == "battery":
                print("I recommend the OnePlus 15.")
            else:
                print("I recommend the Samsung Galaxy S25 Ultra.")

    # iPhone recommendations
    else:
        if budget == "low":
            if feature == "camera":
                print("I recommend the iPhone 15 Pro. You would need to find this at a reseller.")
            elif feature == "battery":
                print("I recommend the iPhone 15 Plus. You would need to find this at a reseller.")
            else:
                print("I recommend the iPhone 15 Pro Max. You would need to find this at a reseller.")
        else:
            if feature == "camera":
                print("I recommend the iPhone 17 Pro.")
            elif feature == "battery":
                print("I recommend the iPhone 17 Pro Max.")
            else:
                print("I recommend the iPhone 17e.")


# Main code

print("Hello! Welcome to the chatbot. Let me help you find a device.\n"
)

product = ask_user(
    "What type of product are you looking for today?\n 1) laptop\n  2) phone",
    ["laptop", "phone", "1", "2"]
)


# Map number inputs
if product == "1": product = "laptop"
if product == "2": product = "phone"

if product == "laptop":
    laptop_flow()
elif product == "phone":
    phone_flow()
    
print("Thank you for using our chatbot. We hope you have a great day!")
exit()
