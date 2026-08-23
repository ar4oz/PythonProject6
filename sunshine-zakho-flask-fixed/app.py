import os
import csv
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify
from markupsafe import Markup

app = Flask(__name__)

CSV_FILE = 'students.csv'


def save_to_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Student Name', 'Guardian', 'Phone', 'Email', 'Program', 'Grade', 'Reason'])
        writer.writerow(data)


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

NAV = [
    {"label": "سەرەکی", "href": "#hero", "key": "nav.home"},
    {
        "label": "خزمەتگوزارییەکانمان",
        "href": "#programs",
        "key": "nav.programs",
        "children": [
            {"label": "سکۆلارشیپی خوێندن", "href": "#programs", "hint": "ڕووسیا، ئەڵمانیا، سوید",
             "key": "nav.programs.kg"},
            {"label": "ڤیزای پزیشکی و چارەسەری", "href": "#about", "hint": "هیندستان، ئەڵمانیا، ئێران",
             "key": "nav.programs.school"},
            {"label": "ڤیزای گشتی و ئەوروپا", "href": "#about", "hint": "شەنگن و کۆنفرانس", "key": "nav.programs.tech"},
        ],
    },
    {"label": "سکۆلارشیپی ڕووسیا", "href": "#russia", "key": "nav.russia"},
    {"label": "خزمەتگوزارییەکان بۆ خوێندکار", "href": "#student-services", "key": "nav.student_services"},
    {"label": "وێنەکان", "href": "#gallery", "key": "nav.gallery"},
    {"label": "پەیوەندی", "href": "#contact", "key": "nav.contact"},
]

SIDEBAR_LINKS = [
    {"icon": "home", "href": "#hero", "label": "سەرەکی", "key": "sidebar.home"},
    {"icon": "grid", "href": "#programs", "label": "خزمەتگوزارییەکانمان", "key": "sidebar.programs"},
    {"icon": "layers", "href": "#russia", "label": "سکۆلارشیپی ڕووسیا 100%", "key": "sidebar.russia"},
    {"icon": "images", "href": "#student-services", "label": "تایبەتمەندی بۆ خوێندکار", "key": "sidebar.services"},
    {"icon": "images", "href": "#gallery", "label": "وێنەکان", "key": "sidebar.gallery"},
    {"icon": "user-plus", "href": "#scholarship", "label": "تۆمارکردنی ناو", "key": "sidebar.register"},
    {"icon": "login", "href": "#contact", "label": "پەیوەندیکردن", "key": "sidebar.login"},
]

LANGUAGES = [
    {"code": "ku", "label": "کوردی (سۆرانی)", "short": "CKB", "flag": "ku"},
    {"code": "en", "label": "English", "short": "EN", "flag": "us"},
    {"code": "ar", "label": "العربية", "short": "AR", "flag": "iq"},
]

HERO_STATS = [
    {"value": "100%", "label": "گرەنتی وەرگرتن", "key": "hero.stat.students"},
    {"value": "+140", "label": "وڵاتی باوەرپێکراو", "key": "hero.stat.teachers"},
    {"value": "VIP", "label": "خزمەتگوزاری متمانەپێکراو", "key": "hero.stat.standards"},
]

ROTATING_WORDS = ["خوێندن", "چارەسەری پزیشکی", "ڤیزای شەنگن",  "سکۆلارشیپ", "هەلی کار"]

VALUES = [
    {
        "icon": "graduation-cap",
        "title": "١. سکۆلارشیپ و خوێندن لە دەرەوە",
        "text": "بە دەستەبەری 100%، دەرفەتی خوێندن لە ڕووسیا (کورسیر خۆڕایی + مووچە)، ئەڵمانیا، سوید (Lund University)، مالیزیا و فڕۆکەوانی مەدەنی لە یۆنان و ڕووسیا.",
        "tags": ["ڕووسیا", "ئەڵمانیا", "سوید", "مالیزیا", "فڕۆکەوانی"],
        "key": "values.0",
    },
    {
        "icon": "heart-pulse",
        "title": "٢. ڤیزای پزیشکی و چارەسەری",
        "text": "پرۆسێسێکی خێرا بۆ ڤیزای نەخۆش بەرەو هیندستان، ئێران، ئوردن، تورکیا، ئەڵمانیا و ئەوروپا. چاودێری شێرپەنجە و چاو لە باشترین نەخۆشخانەکانی ڕووسیا.",
        "tags": ["ڤیزای نەخۆش", "فیۆدۆرۆڤ", "وەرگێڕی تایبەت", "پادکێجی VIP"],
        "key": "values.1",
    },
    {
        "icon": "sparkles",
        "title": "٣. ڤیزای گشتی و ئەوروپا (Schengen)",
        "text": "دابینکردنی ڤیزای شەنگن بێ پارەی پێشەکی، ڤیزای کۆنفرانسە نێودەوڵەتییەکان، ڤیزای بازرگانی، خێزانی و دەستەبەرکردنی هەلی کار لە ئەڵمانیا.",
        "tags": ["شەنگن بێ پێشەکی", "کۆنفرانس", "هەلی کار ئەڵمانیا"],
        "key": "values.2",
    },
]

PROGRAMS = [
    {
        "icon": "school",
        "title": "بەشە پزیشکییەکان",
        "age": "بەکالۆریۆس، ماجستێر، دکتۆرا",
        "text": "پزیشکیی گشتی، پزیشکیی ددان، دەرمانسازی، پزیشکیی ڤێتێرنەری، پەرستاری، چارەسەری سروشتی، و زانستە تەندروستییەکان.",
        "key": "programs.0",
    },
    {
        "icon": "cpu",
        "title": "بەشە ئەندازیارییەکان",
        "age": "سەرجەم بەشەکان",
        "text": "ئەندازیاریی نەوت و غاز، ئەندازیاریی میکانیک، ئەندازیاریی کارەبا، زانستی زانیاری و ئەندازیاریی کۆمپیوتەر.",
        "key": "programs.1",
    },
    {
        "icon": "rocket",
        "title": "زانستی، مرۆیی و کارگێڕی",
        "age": "دەرچووانی پۆلی 12 و خوێندنی باڵا",
        "text": "کیمیا، فیزیا، یاسا، کارگێڕیی کار، ئابووری، ڕاگەیاندن، وەرزش، هونەر و کۆرسی زمانی ڕووسی بێبەرامبەر.",
        "key": "programs.2",
    },
]

CARE = [
    {
        "icon": "shield-check",
        "title": "پێشوازیکردن و نیشتەجێکردن",
        "text": "پێشوازیکردنی خوێندکار لە فڕۆکەخانە و دابینکردنی شوێنی مانەوە (بەشە ناوخۆیی/خانوو) لە نزیکترین شوێنی کەمپەس.",
        "key": "care.0",
    },
    {
        "icon": "lightbulb",
        "title": "ڕاپەڕاندنی تەواوی مامەڵەکان",
        "text": "جێبەجێکردنی مامەڵە یاساییەکان، وەرگێڕانی بەڵگەنامەکان، پشکنینی تەندروستی و بیمەی تەندروستی.",
        "key": "care.1",
    },
    {
        "icon": "rocket",
        "title": "یاوەری تا یەکەم ڕۆژ و هەلی کار",
        "text": "نوێنەرەکانمان لەگەڵ خوێندکار دەمێننەوە تا یەکەم ڕۆژی دەوامی فەرمی و هاوکاری لە دۆزینەوەی هەلی کار.",
        "key": "care.2",
    },
]

SCHOLARSHIP_PERKS = [
    {"text": "خوێندنی بێبەرامبەر: کرێی خوێندن بۆ تەواوی ساڵەکان لەلایەن زانکۆوە دەدرێت", "key": "scholarship.perk.0"},
    {"text": "مووچەی مانگانە: دابینکردنی 45 - 50 دۆلار وەک دەرماڵەی مانگانە", "key": "scholarship.perk.1"},
    {"text": "بەبێ مەرجی تەمەن و کۆنمرە (معدل) بۆ دەرچووانی پۆلی 12", "key": "scholarship.perk.2"},
]

PROGRAM_OPTIONS = ["پزیشکی گشتی / ددان / دەرمانسازی", "ئەندازیاری (نەوت، کۆمپیوتەر...)", "ماجستێر / دکتۆرا",
                   "فڕۆکەوانی مەدەنی", "ڤیزای پزیشکی و چارەسەری" , "بەشەکانی تر "]
GRADE_OPTIONS = [
    "دەرچووی پۆلی 12 (زانستی)",
    "دەرچووی پۆلی 12 (وێژەیی)",
    "بڕوانامەی بەکالۆریۆس",
    "بڕوانامەی ماجستێر",
    "نەخۆش / داواکاری ڤیزای پزیشکی",
]

CONTACTS = [
    {"icon": "phone", "label": "ژمارەی تەلەفۆنی سەرەکی", "value": "0750 888 3214", "key": "contact.phone1"},
    {"icon": "phone", "label": "ژمارەی تەلەفۆنی دووەم", "value": "0772 886 5151", "key": "contact.phone2"},
    {"icon": "mail", "label": "ئیمەیڵ / وێبسایت", "value": "patimat-company.com", "key": "contact.email"},
    {"icon": "clock", "label": "کاتی کارکردن", "value": "شەممە – پێنجشەممە", "key": "contact.hours"},
    {"icon": "map-pin", "label": "ناونیشانی ئۆفیس",
     "value": "هەولێر، گەڕەکی مامۆستایان، شەقامی 150 مەتری، نزیک نافوورە، خانووی ژمارە 18", "key": "contact.address"},
]

SOCIALS = [
    {"kind": "image", "icon": "facebook.svg", "label": "فەیسبووک", "href": "https://www.facebook.com/share/1DBJdn47X8/"},
    {"kind": "image", "icon": "instagram.svg", "label": "ئینستاگرام", "href": "https://www.instagram.com/patimat.iq?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="},
    {"kind": "svg", "icon": "youtube", "label": "یوتیوب", "href": "https://youtube.com"},
    {"kind": "svg", "icon": "tiktok", "label": "تیکتۆک", "href": "https://www.tiktok.com/@patimatcompany?is_from_webapp=1&sender_device=pc"},
    {"kind": "svg", "icon": "snapchat", "label": "سنابچات", "href": "https://snapchat.com"},
]

# ==============================================================================
# SMART GALLERY: Organized by exact filenames from the user's screenshots
# ==============================================================================
GALLERY = [
    # Russia Images
    {"src": "russia.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia1.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia2.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia3.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia4.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia5.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia6.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia7.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia8.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia9.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia10.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia11.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "eussia12.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia13jpg.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia14.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia15.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia16.jpg", "category": "russia", "alt": "Russian Scholarship"},
    {"src": "russia17.jpg", "category": "russia", "alt": "Russian Scholarship"},

    # Germany Images
    {"src": "germani.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani1.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani2.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani3.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani4.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani5.jpg", "category": "germany", "alt": "Study in Germany"},
    {"src": "germani6.jpg", "category": "germany", "alt": "Study in Germany"},

    # Sweden Images
    {"src": "swed.jpg", "category": "sweden", "alt": "Study in Sweden"},
    {"src": "swed1.jpg", "category": "sweden", "alt": "Study in Sweden"},
    {"src": "swed2.jpg", "category": "sweden", "alt": "Study in Sweden"},
    {"src": "swed3.jpg", "category": "sweden", "alt": "Study in Sweden"},
    {"src": "swed4.jpg", "category": "sweden", "alt": "Study in Sweden"},

    # UK and Europe Images
    {"src": "uk.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "uk1.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "uk2.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "uk3.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "europa.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "europa1.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "europa3.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "europa4.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},
    {"src": "europa5.jpg", "category": "uk_europe", "alt": "Study in UK and Europe"},

    # Aviation Images
    {"src": "froka1.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka2.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka3.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka4.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka5.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka6.jpg", "category": "aviation", "alt": "Aviation Study"},
    {"src": "froka7jpg.jpg", "category": "aviation", "alt": "Aviation Study"},
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


# --- زانیاریێن ئیمەیڵێ فرێکەر و وەرگر ---
SENDER_EMAIL = "pesbadini81@gmail.com"  #  Gmail ta
SENDER_PASSWORD = "zkenymlgzyqanbds"  # پاسوۆردێ ئەپڵیکەیشنێ (App Password)
RECEIVER_EMAIL = "compatimat@gmail.com"  # aw emaile nama bo dchit

import traceback


def send_email_notification(data):
    try:
        subject = f"داواکارییەکی نوێ: {data['student_name']}"
        body = f"""
        سڵاو، داواکارییەکی نوێ گەیشت:

        👤 ناو: {data['student_name']}
        👨‍👩‍👦 سەرپەرشتیار: {data['guardian']}
        📞 تەلەفۆن: {data['phone']}
        📧 ئیمەیڵ: {data['email']}
        🎓 بەش: {data['program']}
        📚 ئاست: {data['grade']}
        📝 کورتە: {data['reason']}
        """

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        print("🔄 دەستکرا بە پەیوەندی بە سێرڤەری Gmail...")
        server = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ ئیمەیڵ بە سەرکەوتوویی نێردرا!")
        return True
    except Exception as e:
        print("❌ هەڵە ڕوویدا لە ناردنی ئیمەیڵ:")
        print(e)
        traceback.print_exc()
        return False

@app.route("/api/scholarship", methods=["POST"])
def scholarship():
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

    # پاشەکەوتکرن د فایلا CSV دا
    save_to_csv([student_name, guardian, phone, email, program, grade, reason])

    # فرێکرنا ئیمەیڵێ ڕاستەوخۆ
    send_email_notification({
        "student_name": student_name,
        "guardian": guardian,
        "phone": phone,
        "email": email,
        "program": program,
        "grade": grade,
        "reason": reason
    })

    return jsonify({"ok": True, "studentName": student_name})
FAQ = [
    {
        "keywords": ["russia", "ڕووسیا", "روسیا", "رووسیا", "سکۆلارشیپ", "منحة"],
        "answer": {
            "ku": "سکۆڵەرشیپی نێودەوڵەتی ١٠٠٪ گرەنتییە بەبێ مەرجی تەمەن و کۆنمرە. خوێندنی خۆڕایی، مووچەی مانگانە، نیشتەجێبوون و کۆرسی زمانی بێبەرامبەر لە باشترین زانکۆکانی جیهان لەخۆدەگرێت!",
            "en": "100% guaranteed global scholarships with no age or GPA requirements. Fully funded education, monthly stipend, free accommodation, and preparatory language course in top global universities!",
            "ar": "منح دراسية دولية مضمونة بنسبة 100% بدون شروط العمر والمعدل. تشمل الدراسة المجانية، الراتب الشهري، السكن، ودورة اللغة المجانية في أفضل جامعات العالم!",
        },
    },
    {
        "keywords": ["medical", "پزیشکی", "نەخۆش", "علاج", "فيزا"],
        "answer": {
            "ku": "پاتیمات ڤیزای پزیشکی بۆ هیندستان، ئێران، ئوردن، تورکیا، ئەڵمانیا و ئەوروپا دابین دەکات. چاودێری شێرپەنجە و چاو لە نەخۆشخانەکانی فیۆدۆرۆڤ و بلۆخین لە ڕووسیا ب دەست دەکەوێت.",
            "en": "We provide medical visas for India, Iran, Jordan, Turkey, Germany, and Europe with full translator and hospitalization packages.",
            "ar": "نوفر تأشيرات علاجية إلى الهند، إيران، الأردن، تركيا، ألمانيا وأوروبا مع خدمات المترجم ورعاية مرضى السرطان والعيون في روسيا.",
        },
    },
    {
        "keywords": ["address", "ئۆفیس", "هەولێر", "موقع", "ناونیشان"],
        "answer": {
            "ku": "ناونیشانی ئۆفیسی سەرەکی: هەولێر، گەڕەکی مامۆستایان، شەقامی 150 مەتری، نزیک نافوورە، خانووی ژمارە 18. تەلەفۆن: 07508883214 / 07728865151",
            "en": "Main Office Address: Erbil, Mamostayan Qr, 150m Street, near Fountain, House 18. Phone: 07508883214 / 07728865151",
            "ar": "عنوان المكتب الرئيسي: أربيل، حي المعلمين، شارع 150م، قرب النافورة، منزل رقم 18. هاتف: 07508883214 / 07728865151",
        },
    },
]

FALLBACK = {
    "ku": "سوپاس بۆ پرسیارەکەت. بۆ ڕاوێژکاری بێبەرامبەر پەیوەندی بە 07508883214 یان 07728865151 بکە، یان فۆرمەکە پڕبکەرەوە.",
    "en": "Thanks for reaching out! For free consultation please call 07508883214 or 07728865151 or fill out the form.",
    "ar": "شكراً لاتصالك! للحصول على استشارة مجانية يرجى الاتصال على 07508883214 أو 07728865151 أو ملء الاستمارة.",
}

GREETING = {
    "ku": "سڵاو! من یاریدەدەری زیرەکی کۆمپانیای پاتیماتم بۆ سکۆلارشیپ و ڤیزای پزیشکی. چۆن دەتوانم هاوکارت بم؟",
    "en": "Hello! I am Patimat AI assistant for scholarships and medical visas. How can I help you?",
    "ar": "مرحباً! أنا مساعد پاتیمات للمنح الدراسية والتأشيرات الطبية. كيف يمكنني مساعدتك؟",
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


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)