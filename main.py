import csv


while True:
    name = input("Name: ")
    if name.strip():
        break
    else:
        print()
        print("Name cannot be empty")
        print()

while True:
    try: 
        number = int(input("Number: "))
        if number:
            if len(str(number))==10:
                break

            elif len(str(number))>10 or len(str(number))<10:
                print("!!!Please enter a valid 10 digit numebr!!!")

    except:
       print
       print("!!!Number must be numeric!!!")
       print()     


relation = input("Relation: ")

note = input("Note: ")

with open('contact-details.csv','a',newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name,number,relation,note])

print("Details saved successfully")