import os
import csv
import re
from flask import Flask, render_template, request, jsonify
from markupsafe import Markup


rkup

# ڕێڕەوا تەمام یا فۆڵدەرێ templates دیار بکە
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)



app = Flask(__name__)

# CSV File storage for Patimat scholarship applicants
CSV_FILE = 'students.csv'

def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Student Name', 'Guardian', 'Phone', 'Email', 'Program', 'Grade', 'Reason'])
        writer.writerow(data)

# ---------------------------------------------------------------------------
# Minimal inline icon set (hand-drawn, lucide-inspired) so the page has no
# external icon dependency. Each entry is the inner <svg> markup.
# ---------------------------------------------------------------------------

ICONS = {
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "login": '<path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"/><path d="M10 17l5-5-5-5"/><path d="M15 12H3"/>',
    "sparkles": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2 2M16 16l2 2M18 6l-2 2"/><circle cx="12" cy="12" r="2"/>',
    "graduation-cap": '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12.5V17c0 1.5 3 3 6 3s6-1.5 6-3v-4.5"/>',
    "arrow-left": '<path d="M19 12H5M12 19l-7-7 7-7"/>',
    "lightbulb": '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.3h6c0-1 .4-1.8 1-2.3A7 7 0 0 0 12 2Z"/>',
    "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09Z"/><path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 19 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2Z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
    "baby": '<path d="M9 12h.01M15 12h.01"/><path d="M8 17c1 1 2.5 1.5 4 1.5s3-.5 4-1.5"/><circle cx="12" cy="12" r="9"/>',
    "school": '<path d="m4 6 8-4 8 4-8 4-8-4Z"/><path d="M18 10v6H6v-6"/><path d="M12 10v9M2 10l10-5 10 5"/>',
    "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="10" y="10" width="4" height="4"/><path d="M9 2v2M15 2v2M9 20v2M15 20v2M2 9h2M2 15h2M20 9h2M20 15h2"/>',
    "heart-pulse": '<path d="M19 14c1.5-1.5 3-3.5 3-5.9A4.6 4.6 0 0 0 17.5 3.5c-1.3 0-2.5.5-3.5 1.5-1-1-2.2-1.5-3.5-1.5A4.6 4.6 0 0 0 6 8.1"/><path d="M3.5 12h5l1.5-2.5 2 5 1.5-2.5h6.5"/><path d="M4 14c1.5 3 4.6 6 8 8 3.4-2 6.5-5 8-8"/>',
    "salad": '<path d="M7 21h10"/><path d="M12 21a8 8 0 0 0 8-8H4a8 8 0 0 0 8 8Z"/><path d="M12 13V4a2 2 0 0 1 4 0M7 13c0-2 1-4 2-4"/>',
    "shield-check": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "check-circle": '<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>',
    "loader": '<path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .3 2 .6 2.9a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.2-1.2a2 2 0 0 1 2.1-.5c.9.3 1.9.5 2.9.6a2 2 0 0 1 1.8 2.1Z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
    "map-pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    # -- added for the sidebar / footer / chat widget -----------------------
    "home": '<path d="m3 11 9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M9 20v-6h6v6"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    "layers": '<path d="m12 2 9 5-9 5-9-5 9-5Z"/><path d="m3 12 9 5 9-5"/><path d="m3 17 9 5 9-5"/>',
    "images": '<rect x="3" y="5" width="14" height="14" rx="2"/><circle cx="8" cy="10" r="1.5"/><path d="m4 17 4-4 3 3 4-5 4 4"/>',
    "user-plus": '<circle cx="9" cy="8" r="4"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6"/><path d="M19 8v6M22 11h-6"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 4 6 4 9s-1.5 6.4-4 9c-2.5-2.6-4-6-4-9s1.5-6.4 4-9Z"/>',
    "send": '<path d="m22 2-9.5 20-3-8-8-3Z"/><path d="M22 2 10.5 13.5"/>',
    "bot": '<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 2v4"/><circle cx="9" cy="14" r="1.2"/><circle cx="15" cy="14" r="1.2"/><path d="M8 20v2M16 20v2"/>',
    "youtube": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="m10 9 5 3-5 3Z" fill="currentColor" stroke="none"/>',
    "tiktok": '<path d="M15 3v10.2a3.3 3.3 0 1 1-2.4-3.2"/><path d="M15 3a5.2 5.2 0 0 0 5 5"/>',
    "snapchat": '<path d="M12 3c2.6 0 4.4 2 4.4 4.6 0 1.3-.1 2.3.2 3.1.5.2 1.1.1 1.6-.1.3-.1.8 0 .8.5 0 .6-.9.9-1.6 1.2-.2.1-.3.4-.1.8.3.7 1.1 1.5 2.3 1.8.3.1.3.6-.1.8-.5.3-1.2.4-1.7.6-.1.3-.2.6-.4.8-.3.3-.8.2-1.4.3-.5.1-.8.5-1.7.9-.9.4-2 .3-2.3.3s-1.4.1-2.3-.3c-.9-.4-1.2-.8-1.7-.9-.6-.1-1.1 0-1.4-.3-.2-.2-.3-.5-.4-.8-.5-.2-1.2-.3-1.7-.6-.4-.2-.4-.7-.1-.8 1.2-.3 2-1.1 2.3-1.8.2-.4.1-.7-.1-.8-.7-.3-1.6-.6-1.6-1.2 0-.5.5-.6.8-.5.5.2 1.1.3 1.6.1.3-.8.2-1.8.2-3.1C7.6 5 9.4 3 12 3Z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>',
}


def icon(name: str, cls: str = "icon") -> Markup:
    body = ICONS.get(name, "")
    return Markup(
        f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>'
    )


app.jinja_env.globals["icon"] = icon

# ---------------------------------------------------------------------------
# Site content (kept in Python so it's easy to edit without touching HTML)
# ---------------------------------------------------------------------------

NAV = [
    {"label": "سەرەکی", "href": "#hero", "key": "nav.home"},
    {
        "label": "دەربارە",
        "href": "#about",
        "key": "nav.about",
        "children": [
            {"label": "چیرۆکا مە", "href": "#about", "hint": "ناسینا پاتیمات", "key": "nav.about.story"},
            {"label": "بەهایێن مە", "href": "#values", "hint": "نرخ و پرەنسیپ", "key": "nav.about.values"},
            {"label": "ستافێ پێشکەفتی", "href": "#values", "hint": "ڕاوێژکارێن شارەزا", "key": "nav.about.staff"},
        ],
    },
    {
        "label": "پرۆگرام",
        "href": "#programs",
        "key": "nav.programs",
        "children": [
            {"label": "بەکالۆریۆس", "href": "#programs", "hint": "خوێندنا زانکۆیێ", "key": "nav.programs.kg"},
            {"label": "ماستەر و دکتۆرا", "href": "#programs", "hint": "خوێندنا باڵا", "key": "nav.programs.school"},
            {"label": "کۆرسێن زمانان", "href": "#programs", "hint": "ئینگلیزی و ئایەلتس", "key": "nav.programs.tech"},
        ],
    },
    {"label": "بورس", "href": "#scholarship", "key": "nav.scholarship"},
    {"label": "پەیوەندی", "href": "#contact", "key": "nav.contact"},
]

# Quick-links for the sliding overlay sidebar (Images 2 & 3)
SIDEBAR_LINKS = [
    {"icon": "home", "href": "#hero", "label": "دەستپێک", "key": "sidebar.home"},
    {"icon": "grid", "href": "#programs", "label": "زانکۆ و بەرنامە", "key": "sidebar.programs"},
    {"icon": "layers", "href": "#scholarship", "label": "دەرفەتێن سکۆلەرشیپێ", "key": "sidebar.scholarships"},
    {"icon": "images", "href": "#gallery", "label": "چالاکی و سەرکەوتن", "key": "sidebar.staff"},
    {"icon": "user-plus", "href": "#scholarship", "label": "تۆمارکرن", "key": "sidebar.register"},
    {"icon": "login", "href": "#login", "label": "چوونە ژوور", "key": "sidebar.login"},
]

LANGUAGES = [
    {"code": "ku", "label": "بادینی", "short": "KU", "flag": "ku"},
    {"code": "en", "label": "English", "short": "EN", "flag": "us"},
    {"code": "ar", "label": "العربية", "short": "AR", "flag": "iq"},
]

HERO_STATS = [
    {"value": "+١٢٠٠", "label": "قوتابییێن وەرگیراو", "key": "hero.stat.students"},
    {"value": "+٤٠", "label": "زانکۆییێن جیهانی", "key": "hero.stat.teachers"},
    {"value": "١٠٠٪", "label": "باوەرپێکراو", "key": "hero.stat.standards"},
]

ROTATING_WORDS = ["پاتیمات", "زیرەک", "باوەرپێکراو", "نێودەولەتی"]

VALUES = [
    {
        "icon": "lightbulb",
        "title": "ڕاوێژکاریا زانستی",
        "text": "ڕێنیشاندانا دروست بۆ هەڵبژارتنا بەش و زانکۆییێن نێودەولەتی ب شێوازەکێ فەرمی.",
        "tags": ["نووخوازی", "پێشکەفتن", "داهێنان"],
        "key": "values.0",
    },
    {
        "icon": "rocket",
        "title": "ستافێ پێشکەفتی",
        "text": "تیمەکێ شارەزا د بوارێ دابینکرنا بورسا خواندنێ و وەرگرتنا ڤیزایێ دا.",
        "tags": ["تەکنۆلۆژیا", "گەشەپێدان", "پاشەرۆژ"],
        "key": "values.1",
    },
    {
        "icon": "sparkles",
        "title": "حەماسەت بۆ سەرکەفتنێ",
        "text": "ئەم قوتابیان ئامادە دکەین دا ببنە سەرکردە و داهێنەرێن پاشەرۆژێ د جیهانێ دا.",
        "tags": ["لێهاتوویی", "پێشەنگ", "داهێنەر"],
        "key": "values.2",
    },
]

PROGRAMS = [
    {
        "icon": "baby",
        "title": "بەکالۆریۆس",
        "age": "خوێندنا سەرەتایی یا زانکۆیێ",
        "text": "دابینکرنا سکۆلەرشیپ و وەرگرتنا فەرمی د باشترین زانکۆییێن جیهانێ دا ب بەشێن هەمەرەنگ.",
        "key": "programs.0",
    },
    {
        "icon": "school",
        "title": "ماستەر و دکتۆرا",
        "age": "خوێندنا باڵا",
        "text": "دەرفەتێن ناوازە بۆ قوتابییێن خوێندنا باڵا دگەل داشکاندن و بورسا تایبەت.",
        "key": "programs.1",
    },
    {
        "icon": "cpu",
        "title": "کۆرسێن زمانان",
        "age": "ئامادەکارییا ئایەلتس و تۆفل",
        "text": "ئەم قوتابیان ئامادە دکەین بۆ بەدەستئینانا بڕوانامەیێن نێودەولەتی یێن زمانێ ئینگلیزی.",
        "key": "programs.2",
    },
]

CARE = [
    {
        "icon": "heart-pulse",
        "title": "پشتیڤانیا تەواو",
        "text": "یاوەرییا قوتابی ژ دەستپێکا تۆمارکرنێ هەتا گەهشتنا زانکۆیێ و دابینکرنا ئاکنجیبوونێ.",
        "key": "care.0",
    },
    {
        "icon": "salad",
        "title": "مەرجێن ئاسان",
        "text": "گرنگیەکا تایبەت ددەینە ئاسانکاری د بەڵگەنامە و وەرگرتنا بورسێن بەلاڕاست دا.",
        "key": "care.1",
    },
    {
        "icon": "shield-check",
        "title": "پاراستن و زامنی",
        "text": "دابینکرنا خزمەتگوزارییان ب شەفافییەت و پاراستنا مافێن قوتابیان ب تەمامی.",
        "key": "care.2",
    },
]

SCHOLARSHIP_PERKS = [
    {"text": "داشکاندن هەتا ٥٠٪ بۆ خەرجیێن خوێندنا زانکۆیێ", "key": "scholarship.perk.0"},
    {"text": "بورسا تایبەت بۆ قوتابیێن سەرکەفتی و لێهاتوو", "key": "scholarship.perk.1"},
    {"text": "رێکێن دراوی یێن هەسان و گونجای بۆ دانیشتبووان", "key": "scholarship.perk.2"},
]

PROGRAM_OPTIONS = ["بەکالۆریۆس", "ماستەر", "دکتۆرا", "کۆرسێ زمان"]
GRADE_OPTIONS = [
    "ئاستێ یەکێ (Unconditional)",
    "ئاستێ دووێ (Conditional)",
    "بڕوانامەیا ئامادەیی",
    "بڕوانامەیا بەکالۆریۆس",
    "بڕوانامەیا ماستەر",
    "دی",
]

CONTACTS = [
    {"icon": "phone", "label": "ژمارا مۆبایلێ (واتسئەپ)", "value": "+964 750 555 8848", "key": "contact.phone1"},
    {"icon": "phone", "label": "ژمارا پشتیڤانیێ", "value": "+964 750 666 8848", "key": "contact.phone2"},
    {"icon": "mail", "label": "ئیمەیل", "value": "info@patimat.iq", "key": "contact.email"},
    {"icon": "clock", "label": "کاتژمێرێن کارکرنێ", "value": "شەممە – پێنجشەممە، ٨:٠٠ – ١٦:٠٠", "key": "contact.hours"},
    {"icon": "map-pin", "label": "ناڤونیشان", "value": "کوردستان - دهۆک / زاخۆ", "key": "contact.address"},
]

SOCIALS = [
    {"kind": "image", "icon": "facebook.svg", "label": "فەیسبووک", "href": "https://facebook.com"},
    {"kind": "image", "icon": "instagram.svg", "label": "ئینستاگرام", "href": "https://instagram.com/patimat.iq"},
    {"kind": "svg", "icon": "youtube", "label": "یوتیوب", "href": "https://youtube.com"},
    {"kind": "svg", "icon": "tiktok", "label": "تیکتۆک", "href": "https://tiktok.com"},
    {"kind": "svg", "icon": "snapchat", "label": "سنابچات", "href": "https://snapchat.com"},
]

# Gallery grid — reuses images already shipped with the project
GALLERY = [
    {"src": "hero-classroom.png", "alt": "دیدارا زانکۆییان"},
    {"src": "about-school.png", "alt": "بینایا ناڤەندا پاتیمات"},
    {"src": "placeholder.svg", "alt": "کۆنفرانسێن خوێندنێ"},
    {"src": "placeholder-logo.svg", "alt": "چالاکیێن ستافێ پاتیمات"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        nav=NAV,
        sidebar_links=SIDEBAR_LINKS,
        languages=LANGUAGES,
        hero_stats=HERO_STATS,
        rotating_words=ROTATING_WORDS,
        values=VALUES,
        programs=PROGRAMS,
        care=CARE,
        scholarship_perks=SCHOLARSHIP_PERKS,
        program_options=PROGRAM_OPTIONS,
        grade_options=GRADE_OPTIONS,
        contacts=CONTACTS,
        socials=SOCIALS,
        gallery=GALLERY,
        year=2026,
    )


@app.route("/api/scholarship", methods=["POST"])
def scholarship():
    """Handle the scholarship application form submission."""
    data = request.get_json(silent=True) or request.form

    student_name = (data.get("studentName") or "").strip()
    guardian = (data.get("guardian") or "").strip()
    phone = (data.get("phone") or "").strip()
    email = (data.get("email") or "").strip()
    program = (data.get("program") or "").strip()
    grade = (data.get("grade") or "").strip()
    reason = (data.get("reason") or "").strip()

    missing = [
        field
        for field, value in (
            ("studentName", student_name),
            ("guardian", guardian),
            ("phone", phone),
            ("program", program),
            ("grade", grade),
        )
        if not value
    ]
    if missing:
        return jsonify({"ok": False, "error": "missing_fields", "fields": missing}), 400

    # In a real app this would be persisted to a database / sent via email.
    save_to_csv([student_name, guardian, phone, email, program, grade, reason])
    print(
        "New Patimat scholarship application:",
        {
            "studentName": student_name,
            "guardian": guardian,
            "phone": phone,
            "email": email,
            "program": program,
            "grade": grade,
            "reason": reason,
        },
    )

    return jsonify({"ok": True, "studentName": student_name})


# ---------------------------------------------------------------------------
# Scholarship Advisor — lightweight, rule-based FAQ assistant for Patimat.
#
# NOTE: This answers common questions from a small multilingual knowledge
# base by keyword matching. It's intentionally self-contained (no external
# AI API key required) so the app runs out of the box. To back it with a
# real language model instead, swap `answer_question()` for a call to the
# provider of your choice and pass the user's message + selected language
# through.
# ---------------------------------------------------------------------------

FAQ = [
    {
        "keywords": ["fee", "cost", "price", "tuition", "بورس", "داشکاندن", "خەرجی", "قیمة", "رسوم", "تكلفة", "منحة", "پاتیمات"],
        "answer": {
            "ku": "پاتیمات بورسێن هەتا ٥٠٪ داشکاندن بۆ زانکۆییێن جیهانی ددەت. فۆرمێ 'داخازیا بورسێ' تژی بکە دا تیمێ مە پەیوەندیێ ب تە بکەت.",
            "en": "Patimat offers up to 50% discount scholarships for international universities. Fill out the application form and our team will contact you.",
            "ar": "تقدم پاتیمات منحة دراسية بخصم يصل إلى 50% للجامعات الدولية. يرجى تعبئة نموذج الطلب وسيتواصل فريقنا معك.",
        },
    },
    {
        "keywords": ["register", "enroll", "apply", "admission", "تۆمار", "داخاز", "تسجيل", "التحاق", "قبول"],
        "answer": {
            "ku": "بۆ تۆمارکرنێ د سکۆلەرشیپێن پاتیمات دا، فۆرمێ 'داخازیا بورسا خواندنێ' تژی بکە یان ژ ڕێکا واتسئەپێ بگەهە مە.",
            "en": "To register for Patimat scholarships, fill out the application form or reach us directly via WhatsApp.",
            "ar": "للتسجيل في منح پاتیمات، يرجى تعبئة نموذج طلب المنحة أو التواصل معنا عبر الواتساب.",
        },
    },
    {
        "keywords": ["age", "grade", "kindergarten", "تەمەن", "پۆل", "عمر", "الصف", "جامعة", "زانکۆ"],
        "answer": {
            "ku": "پاتیمات دەرفەتێن خواندنێ بۆ ئاستێن بەکالۆریۆس، ماستەر، و دکتۆرا ل دەڤەرێ و دەرڤەی وڵاتی دابین دکەت.",
            "en": "Patimat offers study opportunities for Bachelor's, Master's, and PhD levels locally and abroad.",
            "ar": "تقدم پاتیمات فرص دراسية لمراحل البكالوريوس، الماجستير، والدكتوراه محلياً وفي الخارج.",
        },
    },
    {
        "keywords": ["location", "address", "where", "map", "شوین", "ناڤونیشان", "زاخۆ", "دهۆک", "موقع", "عنوان", "خريطة"],
        "answer": {
            "ku": "ئەم ل هەرێما کوردستانێ ین (دهۆک / زاخۆ). نەخشەیا شوینی ل بنی پەرەگەهێ هەیە، بۆ سەردانەکا ئاسان.",
            "en": "We are located in Kurdistan Region (Duhok / Zakho). Map is available at the bottom of the page.",
            "ar": "موقعنا في إقليم كردستان (دهوك / زاخو). ستجد الخريطة أسفل هذه الصفحة.",
        },
    },
    {
        "keywords": ["phone", "contact", "call", "email", "پەیوەندی", "ژمار", "ئیمەیل", "اتصال", "هاتف", "بريد"],
        "answer": {
            "ku": "دشێی پەیوەندیێ ب ناڤەندا پاتیمات بکی ژ ڕێکا +964 750 555 8848 یان info@patimat.iq.",
            "en": "You can reach Patimat Center at +964 750 555 8848 or info@patimat.iq.",
            "ar": "يمكنكم التواصل مع مركز پاتیمات عبر +964 750 555 8848 أو info@patimat.iq.",
        },
    },
    {
        "keywords": ["hour", "time", "open", "کاتژمێر", "کارکرن", "دوام", "ساعات"],
        "answer": {
            "ku": "کاتژمێرێن کارکرنێ یێن پاتیمات: شەممە – پێنجشەممە، ٨:٠٠ – ١٦:٠٠.",
            "en": "Patimat office hours: Saturday – Thursday, 8:00 AM – 4:00 PM.",
            "ar": "ساعات الدوام في پاتیمات: السبت – الخميس، من 8:00 صباحًا حتى 4:00 مساءً.",
        },
    },
]

FALLBACK = {
    "ku": "سوپاس بۆ پرسیارا تە. بۆ پێزانینێن تەمام د بوارێ سکۆلەرشیپان دا، پەیوەندیێ ب ناڤەندا پاتیمات بکە ژ ڕێکا +964 750 555 8848.",
    "en": "Thanks for your question! For detailed scholarship info, please contact Patimat Center at +964 750 555 8848.",
    "ar": "شكرًا لسؤالك! للحصول على تفاصيل المنح الدراسية، يرجى التواصل مع مركز پاتیمات عبر +964 750 555 8848.",
}

GREETING = {
    "ku": "سڵاڤ! ئەز یاریدەدەرێ ژیریا دەستکرد یێ پاتیماتم بۆ سکۆلەرشیپ و زانیاریان. چ پرسیار هەیە؟",
    "en": "Hi! I'm Patimat Scholarship Advisor. What would you like to know?",
    "ar": "مرحبًا! أنا مساعد المنح الدراسية في پاتیمات. بماذا أستطيع مساعدتك؟",
}


def answer_question(message: str, lang: str) -> str:
    text = message.lower()
    for entry in FAQ:
        if any(re.search(re.escape(kw.lower()), text) for kw in entry["keywords"]):
            return entry["answer"].get(lang, entry["answer"]["ku"])
    return FALLBACK.get(lang, FALLBACK["ku"])


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    lang = (data.get("lang") or "ku").strip()
    if lang not in ("ku", "en", "ar"):
        lang = "ku"

    if not message:
        return jsonify({"ok": False, "error": "empty_message"}), 400

    reply = answer_question(message, lang)
    return jsonify({"ok": True, "reply": reply})


@app.route("/api/chat/greeting")
def chat_greeting():
    lang = (request.args.get("lang") or "ku").strip()
    if lang not in ("ku", "en", "ar"):
        lang = "ku"
    return jsonify({"ok": True, "reply": GREETING.get(lang, GREETING["ku"])})


if __name__ == "__main__":
    app.run(debug=True)