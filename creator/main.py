from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

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

cred = credentials.Certificate("firebase-adminsdk.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
resume_ref = db.collection("resume")

existing = resume_ref.where("email", "==", email).stream()
for doc in existing:
    print(f"User with email {email} already exists.")
    exit()


if inp := input("Are you sure you want to add this user? (y/n) ").lower() != "y":
    exit()

print(f"Adding user {name}...")

resume_ref.add(
    {
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
)
