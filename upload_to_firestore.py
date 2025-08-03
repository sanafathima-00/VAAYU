import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore
import json

# 🧪 Load .env variables
load_dotenv()
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

# 🔐 Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

# 📁 Load JSON data
with open("data/valid_aod_points.json", "r") as file:
    aod_entries = json.load(file)

# 🕒 Define metadata
timestamp = "2025-08-01T05:45:00Z"
source = "INSAT-3DR"
file_name = "3RIMG_01AUG2025_0545_L2G_AOD_V02R00"

# 📤 Upload to Firestore
collection = db.collection("aod_data")
uploaded = 0

for entry in aod_entries:
    doc = {
        "lat": entry["lat"],
        "lon": entry["lon"],
        "aod": entry["aod"],
        "timestamp": timestamp,
        "source": source,
        "file": file_name
    }
    collection.add(doc)
    uploaded += 1
    if uploaded % 1000 == 0:
        print(f"✅ Uploaded {uploaded}...")

print(f"\n🎉 Upload completed successfully! Total uploaded: {uploaded}")
