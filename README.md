# Mahakal Salutary Consultancy Hub — Website 

A branded Streamlit landing page for three service verticals under one Mahakal Salutary identity:
- Skill Development (Pan India; suggested age group 18–40)
- Real Estate (Nagpur, Maharashtra; rent, sale and purchase)
- Admission Counselling (college/course guidance; suggested age group 17–25)

The contact person for the displayed phone number and address is **Mona Deshmukh**.

## Enquiry buttons

Each service card has its own enquiry button. It opens WhatsApp in a new tab with a pre-filled message for that service, addressed to the business contact number. The property enquiry button therefore opens a property-specific WhatsApp message rather than a blank page.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt` to the repository root.
3. Open Streamlit Community Cloud and deploy the repository.
4. Select `app.py` as the app's main file.

## Before publishing

- Confirm the spelling and legal presentation of the business name.
- Confirm the exact address format and phone number.
- Confirm that Mona Deshmukh is the correct public-facing contact person.
- Replace the service descriptions with the business's precise offerings.
- Add a privacy policy and terms if you later collect personal/customer information.
- The WhatsApp buttons open pre-filled enquiry messages; this version does not store customer enquiries.
