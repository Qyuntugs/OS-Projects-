import random
import time
people = {
    "person_A":{"Name": random.choice(["Adl","Ril","Osl"]),
    "Age": random.choice([14,15,16]),
    "Gender": random.choice(["Male","Female"])
    },
    "person_B":{"Name": random.choice(["Adl","Ril","Osl"]),
    "Age": random.choice([14,15,16]),
    "Gender": random.choice(["Male","Female"])
    },
    "person_C":{"Name": random.choice(["Adl","Ril","Osl"]),
    "Age": random.choice([14,15,16]),
    "Gender": random.choice(["Male","Female"])
    }
}
print("Input No to end Navigation.")
while True:
    Navigation = input("Start Navigation?: ")
    if Navigation.lower() == "no":
        print("...")
        time.sleep(1)
        print("Finished.")
        break
    elif Navigation.lower() == "yes":
        Navigation_person = input("which person?, person_A/B/C?: ")
        if Navigation_person.lower() == "no":
            print("...")
            time.sleep(1)
            print("Finished.")
            break
        person = people[Navigation_person]
        Navigation_info = input("which info? Name? Age? Gender?: ")
        if Navigation_info == "Name":
            print(person[Navigation_info])
        elif Navigation_info == "Age":
            print(person[Navigation_info])
        elif Navigation_info == "Gender":
            print(person[Navigation_info])
        elif Navigation_info.lower() == "no":
            print("...")
            time.sleep(1)
            print("Finished.")
            break
        Navigation_end = input("Navigation Finished. More?: ")
        if Navigation_end.lower() == "no":
            print("...")
            time.sleep(1)
            print("Finished.")
            break