from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from utils import to_title_case

### SET DATA HERE ###
### REQUIRED DATA ###
name = "John Doe"
email = "test@gmail.com"
hall = "RP"
department = "CSE"
graduationYear = 2024
bio = """
A long bio here.
"""
LsTaken = [
    {
        "title": "Test 123",
        "items": [
            "failed to enter college",
            "failed to enter school",
        ],
    },
    {
        "title": "Test 456",
        "items": [
            "failed to enter college",
        ],
    },
]
BrightSide = [
    {
        "title": "Test 123",
        "items": [
            "failed to enter college",
            "failed to enter school",
        ],
    },
    {
        "title": "Test 456",
        "items": [
            "failed to enter college",
        ],
    },
]
### OPTIONAL DATA ###
linkedin = None
facebook = None
instagram = None
website = None
displayEmail = None
image = None
noContextImage = None
### DO NOT MODIFY BELOW CODE ###

for section in LsTaken:
    section["title"] = to_title_case(section["title"])

for section in BrightSide:
    section["title"] = to_title_case(section["title"])

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

data = {
    "name": name,
    "email": email,
    "hall": hall,
    "department": department,
    "graduationYear": graduationYear,
    "linkedin": linkedin,
    "facebook": facebook,
    "instagram": instagram,
    "website": website,
    "displayEmail": displayEmail,
    "bio": bio,
    "image": image,
    "noContextImage": noContextImage,
    "LsTaken": LsTaken,
    "BrightSide": BrightSide,
    "createdAt": datetime.now(),
}

db = firestore.client()
resume_ref = db.collection("resume")

existing = resume_ref.where("email", "==", email).stream()
for doc in existing:
    print(f"User with email {email} already exists.")
    print(f"User ID: {doc.id}")
    if inp := input("Are you sure you want to add this user? (y/n) ").lower() != "y":
        exit()
    else:
        doc_ref = resume_ref.document(doc.id)
        doc_ref.update(data)
        print(f"Updated user {name} with ID {doc.id}")
        exit()


if inp := input("Are you sure you want to add this user? (y/n) ").lower() != "y":
    exit()

print(f"Adding user {name}...")

doc = resume_ref.add(data)
print(doc[1].id)
