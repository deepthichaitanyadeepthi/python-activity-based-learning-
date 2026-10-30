

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))


consultation = float(input("Enter consultation charge: "))
diagnostic = float(input("Enter diagnostic charge: "))
treatment = float(input("Enter treatment charge: "))


if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
   
    total = consultation + diagnostic + treatment

   
    if total >= 10000:
        discount = total * 0.10
    elif total >= 5000:
        discount = total * 0.05
    else:
        discount = 0

    
    final_bill = total - discount

    print("\n===== BILL DETAILS =====")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charge:", consultation)
    print("Diagnostic Charge:", diagnostic)
    print("Treatment Charge:", treatment)
    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final_bill)

   
    paid = float(input("\nEnter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:
        balance = final_bill - paid

       
        if balance == 0:
            print("Patient Classification: Fully Paid")
        elif paid > 0:
            print("Patient Classification: Partially Paid")
        else:
            print("Patient Classification: Unpaid")

        print("Amount Paid:", paid)
        print("Balance Amount:", balance)

print("\nThank you!")

