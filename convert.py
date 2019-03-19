import csv
import pprint


ADD_TO_NOTES = object()
CONVERT_BIRTHDAY = object()


MAP = {
    "Vorname": "First Name",
    "Weitere Vornamen": ADD_TO_NOTES,
    "Nachname": "Last Name",
    "Suffix": ADD_TO_NOTES,
    "Firma": "Organization",
    "Abteilung": "Department",
    "Position": "Job Title",
    "Straße geschäftlich": "Work Address",
    "Ort geschäftlich": "Work City",
    "Region geschäftlich": "Work State",
    "Postleitzahl geschäftlich": "Work ZipCode",
    "Land/Region geschäftlich": "Work Country",
    "Straße privat": "Home Address",
    "Ort privat": "Home City",
    "Postleitzahl privat": "Home ZipCode",
    "Land/Region privat": "Home Country",
    "Weitere Straße": None,
    "Weiterer Ort": None,
    "Weitere Postleitzahl": None,
    "E-Mail-Adresse": "Primary Email",
    "Telefon Assistent": ADD_TO_NOTES,
    "Fax geschäftlich": "Fax Number",
    "Telefon geschäftlich": "Work Phone",
    "Telefon geschäftlich 2": ADD_TO_NOTES,
    "Telefon Firma": ADD_TO_NOTES,
    "Fax privat": ADD_TO_NOTES,
    "Telefon privat": "Home Phone",
    "Telefon privat 2": ADD_TO_NOTES,
    "Mobiltelefon": "Mobile Number",
    "Weiteres Fax": ADD_TO_NOTES,
    "Weiteres Telefon": ADD_TO_NOTES,
    "Mobiltelefon 2": ADD_TO_NOTES,
    "Büro": ADD_TO_NOTES,
    "Geburtstag": CONVERT_BIRTHDAY,
    "Initialen": ADD_TO_NOTES,
    "Kategorien": ADD_TO_NOTES,
    "Kinder": ADD_TO_NOTES,
    "Notizen": "Notes",
    "Partner": ADD_TO_NOTES,
    "Webseite": "Web Page 1",
}


new_data = []

with open("outlook.csv", encoding="cp1252", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_row = {}
        additional_notes = {}
        for key, value in row.items():
            if not value:
                continue
            if key not in MAP:
                continue
            transform = MAP[key]
            if isinstance(transform, str):
                new_key = transform
                new_row[new_key] = value
            elif transform is ADD_TO_NOTES:
                additional_notes[key] = value
            elif transform is CONVERT_BIRTHDAY:
                if value == "0.0.00":
                    continue
                day, month, year = value.split(".")
                new_row["Birth Year"] = year
                new_row["Birth Month"] = month
                new_row["Birth Day"] = day
                print(row)

        notes = new_row.setdefault("Notes", "")
        notes += "\n" + "\n".join(
            f"{key}: {value}" for key, value in additional_notes.items() if value
        )
        notes = notes.strip()
        new_row["Notes"] = notes
        new_row["Display Name"] = " ".join(
            filter(None, [new_row.get("First Name"), new_row.get("Last Name")])
        )
        new_data.append(new_row)


with open("thunderbird.csv", "w", encoding="utf-8", newline="") as csvfile:
    fieldnames = [
        "First Name",
        "Last Name",
        "Display Name",
        "Nickname",
        "Primary Email",
        "Secondary Email",
        "Screen Name",
        "Work Phone",
        "Home Phone",
        "Fax Number",
        "Pager Number",
        "Mobile Number",
        "Home Address",
        "Home Address2",
        "Home City",
        "Home State",
        "Home ZipCode",
        "Home Country",
        "Work Address",
        "Work Address2",
        "Work City",
        "Work State",
        "Work ZipCode",
        "Work Country",
        "Job Title",
        "Department",
        "Organization",
        "Web Page 1",
        "Web Page 2",
        "Birth Year",
        "Birth Month",
        "Birth Day",
        "Custom 1",
        "Custom 2",
        "Custom 3",
        "Custom 4",
        "Notes",
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_data:
        writer.writerow(row)
