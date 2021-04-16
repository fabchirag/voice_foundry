def convert():
    print("Please enter the phone number in format of: '1-800-###-####'")
    phone = input("Enter your phone number: ")
    print("phonenumber:", phone)
    try:
        if len(phone) == 14:
            print(f"Length: {len(phone)}, Number accepted: ", phone)
        table_entry = {"phonenumber": phone}
        sample = vanitynumber.all_wordifications(phone, 5)
        print(sample)
    except ValueError:
        print(f"Length: {len(phone)}, Only 14 are allowed..")

convert()