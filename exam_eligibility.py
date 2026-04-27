medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()
if medical_cause == 'Y':
    print("Allowed to attend the exam.")
else:
    atten = float(input("Enter your attendance percentage: "))
    if atten >= 75:
        print("Allowed")
    else:
        print("Not allowed")