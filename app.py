import streamlit as st
from urllib.parse import quote

# ---------------------------------------------------------
# Mahakal Salutary Consultancy Hub | Initial landing page
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mahakal Salutary Consultancy Hub",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BUSINESS_NAME = "MAHAKAL SALUTARY"
SUBTITLE = "CONSULTANCY HUB"
PHONE_DISPLAY = "+91 77769 26925"
PHONE_DIGITS = "917776926925"
ADDRESS = "31 A, Gurudatta Colony, Narendra Nagar, Nagpur, Maharashtra"
CONTACT_PERSON = "Mona Deshmukh"

# Replace these descriptions/contact prompts as the business offerings are finalized.
# Each enquiry link opens WhatsApp to Mona Deshmukh with a service-specific pre-filled message.
domains = [
    {
        "number": "01",
        "title": "Skill Development",
        "tag": "PAN INDIA",
        "description": (
            "Build practical skills and take the next step in your professional journey. "
            "Our skill-development offering is intended for learners and working individuals."
        ),
        "audience": "Suggested age group: 18–40 years",
        "cta": "Enquire about skill development",
        "message": "Hello, I would like to know more about Skill Development programmes.",
    },
    {
        "number": "02",
        "title": "Real Estate",
        "tag": "NAGPUR, MAHARASHTRA",
        "description": (
            "Explore assistance for property rent, sale and purchase in Nagpur. "
            "Property-related enquiries are welcome from all age groups."
        ),
        "audience": "Rent · Sale · Purchase",
        "cta": "Enquire about a property",
        "message": "Hello, I have a real-estate enquiry regarding rent, sale or purchase in Nagpur.",
    },
    {
        "number": "03",
        "title": "Admission Counselling",
        "tag": "COLLEGE & COURSE GUIDANCE",
        "description": (
            "Get guidance while exploring colleges and courses. The service is intended "
            "for students considering their higher-education options."
        ),
        "audience": "Suggested age group: 17–25 years",
        "cta": "Enquire about admissions",
        "message": "Hello, I would like information about college and course admission guidance.",
    },
]

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    :root {
      --navy: #14264b;
      --gold: #b49350;
      --ink: #273247;
      --muted: #697386;
      --paper: #fbfaf7;
      --line: #e9e3d7;
    }
    .stApp {
      background:
        radial-gradient(circle at 8% 0%, rgba(180,147,80,.09), transparent 28rem),
        var(--paper);
      color: var(--ink);
      font-family: 'DM Sans', sans-serif;
    }
    .block-container {max-width: 1180px; padding-top: 1.6rem; padding-bottom: 2rem;}
    #MainMenu, footer, header {visibility: hidden;}
    .brand {
      text-align:center; padding: 1.25rem 1rem 1.1rem;
      border: 1px solid var(--line); outline: 1px solid rgba(180,147,80,.35);
      outline-offset: -7px; background: rgba(255,255,255,.78);
      box-shadow: 0 12px 35px rgba(25,37,59,.06);
      margin-bottom: 2.2rem;
    }
    .brand-name {
      font-family:'Playfair Display',serif; color:var(--navy);
      font-size: clamp(2rem, 5vw, 3.45rem); letter-spacing:.035em;
      line-height:1.15; font-weight:600;
    }
    .brand-sub {
      color:var(--gold); letter-spacing:.34em; font-size:.88rem;
      margin-top:.35rem; font-weight:600;
    }
    .brand-rule {color:var(--gold); font-size:1.35rem; margin:.65rem 0 .45rem;}
    .brand-services {color:var(--navy); font-size:1rem; font-weight:500;}
    .eyebrow {
      color:var(--gold); font-weight:700; letter-spacing:.18em;
      text-transform:uppercase; font-size:.72rem; text-align:center;
      margin-bottom:.55rem;
    }
    .hero-title {
      font-family:'Playfair Display',serif; color:var(--navy);
      text-align:center; font-size:clamp(2rem,4vw,3rem);
      line-height:1.15; margin:0 auto .7rem; max-width:800px;
    }
    .hero-copy {
      color:var(--muted); text-align:center; max-width:690px;
      margin:0 auto 1.8rem; font-size:1.02rem; line-height:1.7;
    }
    .section-label {
      color:var(--navy); font-family:'Playfair Display',serif;
      font-size:1.55rem; font-weight:600; margin:1.4rem 0 .35rem;
    }
    .section-note {color:var(--muted); margin-bottom:1.1rem; font-size:.93rem;}
    .domain-card {
      height:100%; min-height:300px; padding:1.55rem 1.45rem 1.35rem;
      background:#fff; border:1px solid var(--line); border-radius:13px;
      box-shadow:0 9px 26px rgba(25,37,59,.055);
      transition:transform .2s ease, box-shadow .2s ease;
    }
    .domain-card:hover {
      transform:translateY(-4px); box-shadow:0 15px 32px rgba(25,37,59,.10);
      border-color:rgba(180,147,80,.55);
    }
    .card-number {color:var(--gold); font-size:.78rem; letter-spacing:.15em; font-weight:700;}
    .card-tag {
      display:inline-block; margin:.8rem 0 .55rem; padding:.28rem .58rem;
      border-radius:30px; background:#f5f1e8; color:#8b713c;
      font-size:.65rem; font-weight:700; letter-spacing:.09em;
    }
    .card-title {
      font-family:'Playfair Display',serif; color:var(--navy);
      font-size:1.48rem; line-height:1.2; margin:.1rem 0 .7rem;
    }
    .card-description {color:var(--muted); font-size:.91rem; line-height:1.65; min-height:88px;}
    .card-audience {
      color:var(--ink); font-size:.82rem; font-weight:600;
      border-top:1px solid #f0ece4; padding-top:.8rem; margin-top:.8rem;
    }
    .contact-panel {
      background:var(--navy); color:#fff; padding:1.55rem 1.7rem;
      border-radius:14px; margin-top:2.3rem;
    }
    .contact-heading {
      color:#fff; font-family:'Playfair Display',serif;
      font-size:1.55rem; margin-bottom:.35rem;
    }
    .contact-copy {color:#dce2ed; font-size:.9rem; line-height:1.6;}
    .contact-item {color:#fff; font-size:.9rem; line-height:1.8;}
    .footer {
      border-top:1px solid var(--line); margin-top:2rem; padding:1.2rem .2rem .3rem;
      color:var(--muted); font-size:.78rem; text-align:center;
    }
    .enquiry-button {
      display:block; width:100%; box-sizing:border-box; text-align:center;
      margin-top:.75rem; border-radius:8px; border:1px solid var(--gold);
      background:#fff; color:var(--navy) !important; font-weight:700;
      padding:.68rem .7rem; text-decoration:none !important;
      transition:all .2s ease; font-size:.9rem;
    }
    .enquiry-button:hover {
      background:var(--navy); color:#fff !important; border-color:var(--navy);
    }
    a {color:inherit;}
    @media (max-width: 700px) {
      .brand {padding:1.1rem .6rem;}
      .brand-sub {letter-spacing:.2em;}
      .brand-services {font-size:.82rem;}
      .domain-card {min-height:unset;}
      .card-description {min-height:unset;}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Brand header
st.markdown(
    f"""
    <div class="brand">
      <div class="brand-name">{BUSINESS_NAME}</div>
      <div class="brand-sub">{SUBTITLE}</div>
      <div class="brand-rule">────── ✥ ॐ ✥ ──────</div>
      <div class="brand-services">Skill Development&nbsp; | &nbsp;Real Estate&nbsp; | &nbsp;Admission Counselling</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">A single point of contact for three services</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Guidance for your next step.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-copy">Mahakal Salutary Consultancy Hub brings together skill development, '
    'real-estate assistance and college admission guidance. Choose a service below to get in touch.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">Explore our services</div>', unsafe_allow_html=True)
st.markdown('<div class="section-note">Select the area you need help with. Our team will connect with you directly.</div>', unsafe_allow_html=True)

cols = st.columns(3, gap="large")
for col, item in zip(cols, domains):
    with col:
        st.markdown(
            f"""
            <div class="domain-card">
              <div class="card-number">{item['number']} &nbsp; / &nbsp; SERVICE</div>
              <div class="card-tag">{item['tag']}</div>
              <div class="card-title">{item['title']}</div>
              <div class="card-description">{item['description']}</div>
              <div class="card-audience">{item['audience']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        wa_url = f"https://wa.me/{PHONE_DIGITS}?text={quote(item['message'])}"
        st.markdown(
            f'<a class="enquiry-button" href="{wa_url}" target="_blank" rel="noopener noreferrer">'
            f'{item["cta"]} &nbsp; ↗</a>',
            unsafe_allow_html=True,
        )

st.markdown(
    f"""
    <div class="contact-panel">
      <div class="contact-heading">Let's connect</div>
      <div class="contact-copy">Have a question or want to discuss your requirement? Reach out to us.</div>
      <div class="contact-item" style="margin-top:.75rem;">
        <strong>Contact person:</strong> {CONTACT_PERSON}<br>
        <strong>Phone / WhatsApp:</strong> {PHONE_DISPLAY}<br>
        <strong>Address:</strong> {ADDRESS}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1, 1])
with left:
    st.markdown(f"**Contact: {CONTACT_PERSON}**")
    st.markdown("**Call / WhatsApp**")
    st.markdown(f"[{PHONE_DISPLAY}](tel:+{PHONE_DIGITS})")
with right:
    st.markdown("**Find us**")
    map_query = quote("31 A Gurudatta Colony, Narendra Nagar, Nagpur, Maharashtra")
    st.markdown(f"[Open address in Google Maps](https://www.google.com/maps/search/?api=1&query={map_query})")

st.markdown(
    f'<div class="footer">© {2026} {BUSINESS_NAME.title()} {SUBTITLE.title()}. All rights reserved.<br>'
    'Skill Development · Real Estate · Admission Counselling</div>',
    unsafe_allow_html=True,
)
