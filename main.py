import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

unique_contacts = []

for contact in contacts_list:
    full_name = ' '.join(contact[:3]).split()
    new_contact = []
    lastname = full_name[0]
    firstname = full_name[1]
    if len(full_name) == 3:
        surname = full_name[2]
    else:
        surname = ''
    work = contact[3]
    position = contact[4]
    phone = contact[5]
    email = contact[6]
    phone = ''.join((phone.replace('-', '')).split())
    if 'доб.' not in phone:
        pattern = r"(\+7|8)\(?(\d{3})\)?(\d{3})(\d{2})(\d{2})"
        phone = re.sub(pattern, r"+7(\2)\3-\4-\5", phone)
    else:
        pattern = r"(\+7|8)\(?(\d{3})\)?(\d{3})(\d{2})(\d{2})\s*\(?\s*доб.\s*(\d+)\)?"
        phone = re.sub(pattern, r"+7(\2)\3-\4-\5 доб.\6", phone)
    new_contact = (lastname, firstname, surname, work, position, phone, email)
    unique_contacts.append(new_contact)

for idx, contact in enumerate(unique_contacts):
    contact = list(contact)
    for x in range(idx + 1, len(unique_contacts)):
        if contact[0] == unique_contacts[x][0] and contact[1] == unique_contacts[x][1]:
            new_contact = []
            for y in range(len(contact)):
                if contact[y] == '':
                    new_contact.append(unique_contacts[x][y])
                else:
                    new_contact.append(contact[y])
            unique_contacts[idx] = new_contact
            del unique_contacts[x]
            break



with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    for contact_info in unique_contacts:
        datawriter.writerow(contact_info)