(function () {
  'use strict';

  /* =====================================================================
     TRANSLATIONS DICTIONARY
     Includes all navigation, sections, and the new Gallery filter buttons.
     ===================================================================== */
  var TRANSLATIONS = {
    ku: {
      'brand.title': 'کۆمپانیای پاتیمات', 'brand.sub': 'patimat-company.com',
      'nav.home': 'سەرەکی', 'nav.programs': 'خزمەتگوزارییەکانمان', 'nav.russia': 'سکۆلەرشیپی هەموو وەلاتەکان  ',
      'nav.student_services': 'خزمەتگوزارییەکان بۆ خوێندکار', 'nav.gallery': 'وێنەکان', 'nav.contact': 'پەیوەندی',
      'nav.programs.kg': 'سکۆلارشیپی خوێندن', 'nav.programs.school': 'ڤیزای پزیشکی و چارەسەری', 'nav.programs.tech': 'ڤیزای گشتی و ئەوروپا',
      'header.login': 'ئێستا پەیوەندی بکە',
      'sidebar.eyebrow': 'کۆمپانیای پاتیمات', 'sidebar.welcome.title': 'بەخێربێن',
      'sidebar.welcome.text': 'دەروازەیەک بۆ بەدەستهێنانی سکۆلارشیپی خوێندن و ڤیزای پزیشکی و گەشتیاری بە خزمەتگوزاریی VIP.',
      'sidebar.home': 'سەرەکی', 'sidebar.programs': 'خزمەتگوزارییەکانمان', 'sidebar.russia': 'سکۆڵەرشیپی هەموو وڵاتەکان',
      'sidebar.services': 'تایبەتمەندی بۆ خوێندکار', 'sidebar.gallery': 'گەلەریی وێنەکان', 'sidebar.register': 'تۆمارکردنی ناو', 'sidebar.login': 'پەیوەندیکردن',
      'hero.pill': 'پاتیمات — پێشەنگ لە سکۆلارشیپ و ڤیزای پزیشکی',
      'hero.title.pre': 'داهاتووت لەگەڵ پاتیمات مسۆگەر بکە؛', 'hero.title.post': 'لە باشترین وڵاتانی جیهاندا',
      'hero.lead': 'کۆمپانیای پاتیمات دەروازەیەکە بۆ بەدەستهێنانی سکۆلارشیپی خوێندن (بەکالۆریۆس، ماجستێر، دکتۆرا) لە باشترین زانکۆکانی جیهان بەبێ مەرجی تەمەن و کۆنمرە. هەروەها پێشەنگین لە دابینکردنی ڤیزای پزیشکی و گەشتیاری بە خزمەتگوزاریی VIP و متمانەپێکراو.',
      'hero.cta1': 'ئێستا پەیوەندی بکە', 'hero.cta2': 'بینینی خزمەتگوزارییەکان',
      'hero.card.title': 'کومپانیای پاتیمات',
      'hero.card.text': 'کۆمپانیای پاتیمات؛ بۆ پێشکەشکردنی سەرجەم خزمەتگوزارییەکان، ٢٤ کاتژمێر لە خزمەتتاندایە.',
      'hero.card.badge': 'پێشەنگی بێ هاوتا',
      'hero.stat.students': 'گرەنتی وەرگرتن', 'hero.stat.teachers': 'وڵاتی باوەرپێکراو', 'hero.stat.standards': 'خزمەتگوزاری متمانەپێکراو',
      'values.eyebrow': 'بەشی دووەم', 'values.title': 'خزمەتگوزارییەکانمان (Our Services)',
      'values.lead': 'بە دەستەبەری 100% گرەنتی، باشترین دەرفەتەکانی خوێندن و چارەسەری پزیشکی لە سەرتاسەری جیهان پێشکەش دەکەین.',
      'values.0.title': '١. سکۆلارشیپ و خوێندن لە دەرەوە', 'values.1.title': '٢. ڤیزای پزیشکی و چارەسەری', 'values.2.title': '٣. ڤیزای گشتی و ئەوروپا (Schengen)',
      'programs.eyebrow': 'بەشی سێیەم', 'programs.title': 'سکۆلەرشیپ  (Scholarship 100%)',
      'programs.lead': 'ئێمە لە کۆمپانیای پاتیمات دڵنیایی (١٠٠٪) دەدەین لە وەرگرتن و بانگهێشتنامە بۆ خوێندن لە هەموو وەڵاتەکان بەم تایبەتمەندییانە:',
      'programs.0.age': 'بەکالۆریۆس، ماجستێر، دکتۆرا', 'programs.0.title': 'بەشە پزیشکییەکان',
      'programs.1.age': 'سەرجەم بەشەکان', 'programs.1.title': 'بەشە ئەندازیارییەکان',
      'programs.2.age': 'دەرچووانی پۆلی 12 و خوێندنی باڵا', 'programs.2.title': 'زانستی، مرۆیی و کارگێڕی',
      'about.eyebrow': 'بەشی چوارەم', 'about.title': 'ئەو خزمەتگوزارییانەی پێشکەشی خوێندکاری دەکەین',
      'about.lead': 'لە پاتیمات، تەنها بانگهێشتنامە وەرناگرین، بەڵکو هەنگاو بە هەنگاو لەگەڵتین لە فڕۆکەخانەوە تا دەستپێکردنی دەوامی فەرمی:',
      'about.badge.label': 'خزمەتگوزاری یاوەریی تەواو',
      'care.0.title': 'پێشوازیکردن و نیشتەجێکردن', 'care.1.title': 'ڕاپەڕاندنی تەواوی مامەڵەکان', 'care.2.title': 'یاوەری تا یەکەم ڕۆژ و هەلی کار',
      'scholarship.pill': 'بەڵگەنامە داواکراوەکان', 'scholarship.title': 'خۆت تۆمار بکه بۆ سکۆلارشیپ',
      'scholarship.lead': 'بەڵگەنامە داواکراوەکان بۆ پێشکەشکردن: 1. سکانکردنی سەرجەم پەڕەکانی پاسپۆرت. 2. سکانکردنی بڕوانامەی دەرچوون بە وەرگێڕدراوی ئینگلیزی. 3. وێنەی کەسی (3 لە 4).',
      'scholarship.perk.0': 'خوێندنی بێبەرامبەر: کرێی خوێندن بۆ تەواوی ساڵەکان لەلایەن زانکۆوە دەدرێت',
      'scholarship.perk.1': 'مووچەی مانگانە: دابینکردنی 45 - 50 دۆلار وەک دەرماڵەی مانگانە',
      'scholarship.perk.2': 'بەبێ مەرجی تەمەن و کۆنمرە (معدل) بۆ دەرچووانی پۆلی 12',
      'form.studentName': 'ناوی سیانی خوێندکار', 'form.studentName.placeholder': 'ناو و پاشناو',
      'form.guardian': 'ناوی سەرپەرشتیار', 'form.guardian.placeholder': 'ناوی باوک / دایک',
      'form.phone': 'ژمارەی تەلەفۆن (واتسئەپ/ڤایبەر)', 'form.email': 'ئیمەیڵ',
      'form.program': 'بەشی داواکراو', 'form.grade': 'ئاستی خوێندنی ئێستا',
      'form.reason': 'کورتەیەک دەربارەی داواکارییەکەت', 'form.reason.placeholder': 'بنوسە کام وڵات یان خزمەتگوزاریت دەوێت...',
      'form.select': 'هەڵبژێرە...', 'form.submit': 'ناردنی داواکاری', 'form.sending': 'جاری ناردن...',
      'form.success.title': 'داواکارییەکەت وەرگیرا!', 'form.success.reset': 'داواکارییەکی نوێ',
      'form.error.required': 'تکایە سەرجەم خانە پێویستەکان پڕبکەرەوە.', 'form.error.generic': 'هەڵەیەک ڕوویدا. تکایە دووبارە هەوڵبدەرەوە.',
      'form.success.text': 'سوپاس{name}. تیمەکەی پاتیمات بە زووترین کات پەیوەندیت پێوە دەکەن.',
      'gallery.eyebrow': 'وێنەکان', 'gallery.title': 'سەرکەوتنەکانی پاتیمات لە جیهاندا',
      'filter.all': 'هەمووی', 'filter.russia': 'ڕووسیا', 'filter.germany': 'ئەڵمانیا', 'filter.sweden': 'سوید',
      'filter.uk_europe': 'بەریتانیا و ئەوروپا', 'filter.aviation': 'فڕۆکەوانی',
      'footer.cta.title': 'داهاتووت لەگەڵ پاتیمات مسۆگەر بکە',
      'footer.cta.text': 'پەیوەندیمان پێوە بکەن بۆ ڕاوێژکاریی بێبەرامبەر و وەرگرتنی زانیاریی زیاتر لە ڕێگەی تەلەفۆن، واتسئەپ، یان ڤایبەر.',
      'footer.cta.btn1': 'تۆمارکردنی ناو', 'footer.cta.btn2': '0750 888 3214',
      'footer.brand': 'کۆمپانیای پاتیمات',
      'footer.about': 'کۆمپانیای پاتیمات — پێشەنگ لە بەدەستهێنانی سکۆلارشیپی خوێندن لە باشترین زانکۆکانی جیهان و دابینکردنی ڤیزای پزیشکی و گەشتیاری.',
      'footer.rights': '© کۆمپانیای پاتیمات (patimat-company.com). سەرجەم مافەکان پارێزراون.',
      'contact.phone1.label': 'ژمارەی تەلەفۆنی سەرەکی', 'contact.phone2.label': 'ژمارەی تەلەفۆنی دووەم',
      'contact.email.label': 'ئیمەیڵ / وێبسایت', 'contact.hours.label': 'کاتی کارکردن', 'contact.address.label': 'ناونیشانی ئۆفیس',
      'map.eyebrow': 'ناونیشانی سەرەکی (ئۆفیس)', 'map.title': 'هەولێر، گەڕەکی مامۆستایان، شەقامی ١٥٠ مەتری، نزیک نافوورە، خانووی ژمارە ١٨', 'map.pin': 'ئۆفیسی هەولێر',
      'chatbot.title': 'یاریدەدەری زیرەکی پاتیمات', 'chatbot.subtitle': 'سۆرانی · English · العربية',
      'chatbot.placeholder': 'پرسیارەکەت بنووسە...',
      'chatbot.quick.fees': 'سکۆلارشیپی ڕووسیا', 'chatbot.quick.register': 'ڤیزای پزیشکی', 'chatbot.quick.location': 'ناونیشانی ئۆفیس', 'chatbot.quick.contact': 'پەیوەندی',
    },
    en: {
      'brand.title': 'Patimat Company', 'brand.sub': 'patimat-company.com',
      'nav.home': 'Home', 'nav.programs': 'Our Services', 'nav.russia': 'Global Scholarships', 'nav.student_services': 'Student Services',
      'nav.gallery': 'Gallery', 'nav.contact': 'Contact',
      'nav.programs.kg': 'Study Abroad', 'nav.programs.school': 'Medical Visas', 'nav.programs.tech': 'Schengen & Visas',
      'header.login': 'Contact Us Now',
      'sidebar.eyebrow': 'Patimat Company', 'sidebar.welcome.title': 'Welcome',
      'sidebar.welcome.text': 'Your gateway to securing study scholarships and medical/tourist visas with VIP service.',
      'sidebar.home': 'Home', 'sidebar.programs': 'Our Services', 'sidebar.russia': 'Russian Scholarship 100%',
      'sidebar.services': 'Student Perks', 'sidebar.gallery': 'Photo Gallery', 'sidebar.register': 'Register Now', 'sidebar.login': 'Contact Us',
      'hero.pill': 'Patimat — Leader in Scholarships & Medical Visas',
      'hero.title.pre': 'Secure your future with Patimat;', 'hero.title.post': 'In the world’s best countries',
      'hero.lead': 'Patimat Company is a gateway to securing study scholarships (Bachelor, Master, PhD) in top global universities with no age or GPA limits.',
      'hero.cta1': 'Contact Us Now', 'hero.cta2': 'View Services',
      'hero.card.title': 'Patimat Company',
      'hero.card.text': 'Patimat Company; at your service 24/7 to provide all services.',
      'hero.card.badge': 'Unmatched Leadership',
      'hero.stat.students': 'Guaranteed Admission', 'hero.stat.teachers': 'Approved Countries', 'hero.stat.standards': 'VIP Service',
      'values.eyebrow': 'Section Two', 'values.title': 'Our Services',
      'values.lead': 'With 100% guarantee, we provide top education and medical travel opportunities worldwide.',
      'values.0.title': '1. Study Abroad & Scholarships', 'values.1.title': '2. Medical & Treatment Visas', 'values.2.title': '3. Schengen & General Visas',
      'programs.eyebrow': 'Section Three', 'programs.title': 'Russian Scholarship 100%',
      'programs.lead': 'We offer 100% guaranteed admission and invitations for studying in Russia with these benefits:',
      'programs.0.age': 'Bachelor, Master, PhD', 'programs.0.title': 'Medical Specialties',
      'programs.1.age': 'All Engineering Branches', 'programs.1.title': 'Engineering Specialties',
      'programs.2.age': 'High School & Higher Education Graduates', 'programs.2.title': 'Sciences, Humanities & Management',
      'about.eyebrow': 'Section Four', 'about.title': 'Services Provided to Students',
      'about.lead': 'At Patimat, we do not just get invitations; we walk with you step by step from the airport to day one:',
      'about.badge.label': 'Full Companion Service',
      'care.0.title': 'Airport Reception & Housing', 'care.1.title': 'Legal & Translation Processing', 'care.2.title': 'Day-One Support & Job Assistance',
      'scholarship.pill': 'Required Documents', 'scholarship.title': 'Register for Scholarship',
      'scholarship.lead': 'Required Documents: 1. Full Passport Scan. 2. Translated Graduation Certificate. 3. Personal Photo (3x4).',
      'scholarship.perk.0': 'Free Tuition: Paid entirely by the university for all years',
      'scholarship.perk.1': 'Monthly Stipend: $45 - $50 provided monthly',
      'scholarship.perk.2': 'No Age or Minimum GPA requirements',
      'form.studentName': 'Full Student Name', 'form.studentName.placeholder': 'First and last name',
      'form.guardian': 'Guardian Name', 'form.guardian.placeholder': 'Parent / guardian name',
      'form.phone': 'Phone Number (WhatsApp/Viber)', 'form.email': 'Email',
      'form.program': 'Requested Specialty', 'form.grade': 'Current Academic Level',
      'form.reason': 'Brief details about your request', 'form.reason.placeholder': 'Specify country or service...',
      'form.select': 'Select...', 'form.submit': 'Send Application', 'form.sending': 'Sending...',
      'form.success.title': 'Application Received!', 'form.success.reset': 'New Application',
      'form.error.required': 'Please fill in all required fields.', 'form.error.generic': 'Something went wrong. Please try again.',
      'form.success.text': 'Thank you{name}. Patimat team will contact you shortly.',
      'gallery.eyebrow': 'Photo Gallery', 'gallery.title': 'Student Success Stories worldwide',
      'filter.all': 'All', 'filter.russia': 'Russia', 'filter.germany': 'Germany', 'filter.sweden': 'Sweden',
      'filter.uk_europe': 'UK & Europe', 'filter.aviation': 'Aviation',
      'footer.cta.title': 'Secure Your Future with Patimat',
      'footer.cta.text': 'Contact us for free consultation via phone, WhatsApp, or Viber.',
      'footer.cta.btn1': 'Register Now', 'footer.cta.btn2': '0750 888 3214',
      'footer.brand': 'Patimat Company',
      'footer.about': 'Patimat Company — Leader in study scholarships and medical/tourist visas worldwide.',
      'footer.rights': '© Patimat Company (patimat-company.com). All rights reserved.',
      'contact.phone1.label': 'Main Phone Number', 'contact.phone2.label': 'Secondary Phone Number',
      'contact.email.label': 'Email / Website', 'contact.hours.label': 'Working Hours', 'contact.address.label': 'Office Address',
      'map.eyebrow': 'Main Office Address', 'map.title': 'Erbil, Mamostayan Qr, 150m Street, near Fountain, House 18', 'map.pin': 'Erbil Office',
      'chatbot.title': 'Patimat AI Assistant', 'chatbot.subtitle': 'Soraní · English · Arabic',
      'chatbot.placeholder': 'Type your question...',
      'chatbot.quick.fees': 'Russian Scholarship', 'chatbot.quick.register': 'Medical Visas', 'chatbot.quick.location': 'Office Address', 'chatbot.quick.contact': 'Contact Us',
    },
    ar: {
      'brand.title': 'شركة پاتیمات', 'brand.sub': 'patimat-company.com',
      'nav.home': 'الرئيسية', 'nav.programs': 'خدماتنا', 'nav.russia': 'منح دراسية لكافة الدول', 'nav.student_services': 'خدمات الطلاب',
      'nav.gallery': 'معرض الصور', 'nav.contact': 'تواصل معنا',
      'nav.programs.kg': 'الدراسة في الخارج', 'nav.programs.school': 'التأشيرات الطبية', 'nav.programs.tech': 'شنغن والتأشيرات',
      'header.login': 'اتصل بنا الآن',
      'sidebar.eyebrow': 'شركة پاتیمات', 'sidebar.welcome.title': 'أهلاً بك',
      'sidebar.welcome.text': 'بوابتك للحصول على المنح الدراسية والتأشيرات العلاجية بخدمات VIP.',
      'sidebar.home': 'الرئيسية', 'sidebar.programs': 'خدماتنا', 'sidebar.russia': 'منحة روسيا 100%',
      'sidebar.services': 'مزايا الطلاب', 'sidebar.gallery': 'معرض الصور', 'sidebar.register': 'تسجيل الاسم', 'sidebar.login': 'تواصل معنا',
      'hero.pill': 'پاتیمات — الرائدة في المنح والتأشيرات الطبية',
      'hero.title.pre': 'اضمن مستقبلك مع پاتیمات؛', 'hero.title.post': 'في أفضل دول العالم',
      'hero.lead': 'شركة پاتیمات بوابة للحصول على منح دراسية (بكالوريوس، ماجستير، دكتوراه) في أفضل جامعات العالم بدون شروط العمر أو المعدل.',
      'hero.cta1': 'اتصل بنا الآن', 'hero.cta2': 'عرض الخدمات',
      'hero.card.title': 'شركة پاتیمات',
      'hero.card.text': 'شركة پاتیمات؛ لتقديم كافة الخدمات، نحن في خدمتكم على مدار 24 ساعة.',
      'hero.card.badge': 'ريادة لا مثيل لها',
      'hero.stat.students': 'قبول مضمون', 'hero.stat.teachers': 'دول معتمدة', 'hero.stat.standards': 'خدمة VIP',
      'values.eyebrow': 'القسم الثاني', 'values.title': 'خدماتنا (Our Services)',
      'values.lead': 'بضمان 100%، نقدم أفضل فرص الدراسة والعلاج الطبي حول العالم.',
      'values.0.title': '١. المنح والدراسة في الخارج', 'values.1.title': '٢. التأشيرات العلاجية والطبية', 'values.2.title': '٣. تأشيرات شنغن والعامة',
      'programs.eyebrow': 'القسم الثالث', 'programs.title': 'منحة روسيا (Russian Scholarship 100%)',
      'programs.lead': 'نضمن القبول والدعوة الدراسية في روسيا 100% بالمزايا التالية:',
      'programs.0.age': 'بكالوريوس، ماجستير، دكتوراه', 'programs.0.title': 'التخصصات الطبية',
      'programs.1.age': 'كافة الفروع الهندسية', 'programs.1.title': 'التخصصات الهندسية',
      'programs.2.age': 'خريجي السادس والدراسات العليا', 'programs.2.title': 'العلوم، الإنسانيات والإدارة',
      'about.eyebrow': 'القسم الرابع', 'about.title': 'الخدمات المقدمة للطالب',
      'about.lead': 'في پاتیمات، لا نكتفي بالموافقة بل نرافقك خطوة بخطوة من المطار وحتى اليوم الدراسي الأول:',
      'about.badge.label': 'خدمة مرافقة شاملة',
      'care.0.title': 'الاستقبال والسكن', 'care.1.title': 'إنجاز كافة المعاملات والترجمة', 'care.2.title': 'المرافقة والمساعدة في العمل',
      'scholarship.pill': 'المستمسكات المطلوبة', 'scholarship.title': 'سجل الآن للمنحة',
      'scholarship.lead': 'المستندات المطلوبة: 1. مسح ضوئي لجميع صفحات الجواز. 2. وثيقة التخرج مترجمة. 3. صورة شخصية (3x4).',
      'scholarship.perk.0': 'دراسة مجانية: أجور الدراسة مدفوعة بالكامل من الجامعة',
      'scholarship.perk.1': 'راتب شهري: توفير 45 - 50 دولار كمنحة شهرية',
      'scholarship.perk.2': 'بدون شروط العمر أو المعدل لخريجي السادس',
      'form.studentName': 'اسم الطالب الثلاثي', 'form.studentName.placeholder': 'الاسم الكامل',
      'form.guardian': 'اسم ولي الأمر', 'form.guardian.placeholder': 'اسم الأب / الأم',
      'form.phone': 'رقم الهاتف (واتساب/فايلر)', 'form.email': 'البريد الإلكتروني',
      'form.program': 'التخصص المطلوب', 'form.grade': 'المستوى الدراسي الحالي',
      'form.reason': 'تفاصيل مختصرة عن طلبك', 'form.reason.placeholder': 'اكتب الدولة أو الخدمة المطلوبة...',
      'form.select': 'اختر...', 'form.submit': 'إرسال الطلب', 'form.sending': 'جاري الإرسال...',
      'form.success.title': 'تم استلام طلبك!', 'form.success.reset': 'طلب جديد',
      'form.error.required': 'يرجى ملء جميع الحقول المطلوبة.', 'form.error.generic': 'حدث خطأ ما. يرجى المحاولة مرة أخرى.',
      'form.success.text': 'شكراً لك{name}. سيتواصل معك فريق پاتیمات بأسرع وقت.',
      'gallery.eyebrow': 'معرض الصور', 'gallery.title': 'قصص نجاح الطلاب مع پاتیمات',
      'filter.all': 'الكل', 'filter.russia': 'روسيا', 'filter.germany': 'ألمانيا', 'filter.sweden': 'السويد',
      'filter.uk_europe': 'المملكة المتحدة وأوروبا', 'filter.aviation': 'الطيران',
      'footer.cta.title': 'اضمن مستقبلك مع پاتیمات',
      'footer.cta.text': 'تواصل معنا للحصول على استشارة مجانية عبر الهاتف، الواتساب، أو الفايبر.',
      'footer.cta.btn1': 'تسجيل الاسم', 'footer.cta.btn2': '0750 888 3214',
      'footer.brand': 'شركة پاتیمات',
      'footer.about': 'شركة پاتیمات — الرائدة في المنح الدراسية والتأشيرات الطبية حول العالم.',
      'footer.rights': '© شركة پاتیمات (patimat-company.com). جميع الحقوق محفوظة.',
      'contact.phone1.label': 'رقم الهاتف الرئيسي', 'contact.phone2.label': 'رقم الهاتف الثاني',
      'contact.email.label': 'البريد / الموقع', 'contact.hours.label': 'أوقات العمل', 'contact.address.label': 'عنوان المكتب',
      'map.eyebrow': 'عنوان المكتب الرئيسي', 'map.title': 'أربيل، حي المعلمين، شارع 150م، قرب النافورة، منزل رقم 18', 'map.pin': 'مكتب أربيل',
      'chatbot.title': 'مساعد پاتیمات الذكي', 'chatbot.subtitle': 'سوراني · English · العربية',
      'chatbot.placeholder': 'اكتب سؤالك...',
      'chatbot.quick.fees': 'منحة روسيا', 'chatbot.quick.register': 'التأشيرات الطبية', 'chatbot.quick.location': 'عنوان المكتب', 'chatbot.quick.contact': 'تواصل معنا',
    },
  };

  var DIR = { ku: 'rtl', en: 'ltr', ar: 'rtl' };
  var currentLang = 'ku';

  try {
    var saved = window.localStorage.getItem('patimat-lang');
    if (saved && TRANSLATIONS[saved]) {
        currentLang = saved;
    }
  } catch (e) {
      console.warn('Storage unavailable');
  }

  function t(key) {
    var dict = TRANSLATIONS[currentLang] || TRANSLATIONS.ku;
    return (key in dict) ? dict[key] : (TRANSLATIONS.ku[key] || '');
  }

  function applyTranslations() {
    document.documentElement.setAttribute('lang', currentLang);
    document.documentElement.setAttribute('dir', DIR[currentLang]);

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      var value = t(key);
      if (value) {
          el.textContent = value;
      }
    });

    document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
      var key = el.getAttribute('data-i18n-placeholder');
      var value = t(key);
      if (value) {
          el.setAttribute('placeholder', value);
      }
    });

    var codeEl = document.querySelector('[data-code-current]');
    if (codeEl) {
        codeEl.textContent = currentLang === 'ku' ? 'CKB' : currentLang.toUpperCase();
    }

    var flagCurrent = document.querySelector('[data-flag-current]');
    var activeOption = document.querySelector('.lang-option[data-lang="' + currentLang + '"]');

    if (flagCurrent && activeOption) {
      flagCurrent.innerHTML = activeOption.querySelector('.lang-flag').innerHTML;
    }

    document.querySelectorAll('.lang-option').forEach(function (opt) {
      opt.classList.toggle('active', opt.getAttribute('data-lang') === currentLang);
    });
  }

  function setLang(lang) {
    if (!TRANSLATIONS[lang] || lang === currentLang) {
        return;
    }
    currentLang = lang;
    try {
        window.localStorage.setItem('patimat-lang', lang);
    } catch (e) {
        console.warn('Failed to set storage');
    }
    applyTranslations();
    resetChat();
  }

  var header = document.getElementById('site-header');
  function onScroll() {
    if (window.scrollY > 24) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
  }

  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  var langSwitcher = document.getElementById('lang-switcher');
  var langTrigger = document.getElementById('lang-trigger');

  if (langTrigger) {
    langTrigger.addEventListener('click', function (e) {
      e.stopPropagation();
      langSwitcher.classList.toggle('open');
    });
  }

  document.querySelectorAll('.lang-option').forEach(function (opt) {
    opt.addEventListener('click', function () {
      setLang(opt.getAttribute('data-lang'));
      langSwitcher.classList.remove('open');
    });
  });

  document.addEventListener('click', function (e) {
    if (langSwitcher && !e.target.closest('.lang-switcher')) {
      langSwitcher.classList.remove('open');
    }
  });

  var sidebar = document.getElementById('app-sidebar');
  var scrim = document.getElementById('sidebar-scrim');
  var sidebarToggle = document.getElementById('mobile-toggle');
  var sidebarClose = document.getElementById('sidebar-close');

  function openSidebar() {
    sidebar.classList.add('open');
    scrim.classList.add('open');
    sidebar.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    scrim.classList.remove('open');
    sidebar.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  if (sidebarToggle) {
      sidebarToggle.addEventListener('click', openSidebar);
  }

  if (sidebarClose) {
      sidebarClose.addEventListener('click', closeSidebar);
  }

  if (scrim) {
      scrim.addEventListener('click', closeSidebar);
  }

  if (sidebar) {
      sidebar.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', closeSidebar);
      });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeSidebar();
    }
  });

  document.querySelectorAll('.nav-dropdown-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var dropdown = btn.closest('.nav-dropdown');
      var isOpen = dropdown.classList.contains('open');
      document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
        d.classList.remove('open');
      });
      if (!isOpen) {
          dropdown.classList.add('open');
      }
    });
  });

  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown.open').forEach(function (d) {
        d.classList.remove('open');
      });
    }
  });

  var rotateEl = document.getElementById('rotate-word');
  if (rotateEl && window.ROTATING_WORDS && window.ROTATING_WORDS.length) {
    var words = window.ROTATING_WORDS;
    var index = 0;
    setInterval(function () {
      index = (index + 1) % words.length;
      rotateEl.textContent = words[index];
      rotateEl.classList.remove('rotate-word');
      void rotateEl.offsetWidth;
      rotateEl.classList.add('rotate-word');
    }, 2200);
  }

  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    revealEls.forEach(function (el) {
        observer.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
        el.classList.add('is-visible');
    });
  }

  /* =====================================================================
     Gallery Logic & Lightbox (Filter Images and Expand)
     ===================================================================== */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var galleryItems = document.querySelectorAll('.gallery-item');

  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      // Remove active class from all buttons
      filterBtns.forEach(function (b) {
          b.classList.remove('active');
      });
      // Add active class to clicked button
      btn.classList.add('active');

      var filterValue = btn.getAttribute('data-filter');

      // Filter logic
      galleryItems.forEach(function (item) {
        var category = item.getAttribute('data-category');
        if (filterValue === 'all' || category === filterValue) {
          item.classList.remove('hide');
        } else {
          item.classList.add('hide');
        }
      });
    });
  });

  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightbox-img');
  var lightboxClose = document.getElementById('lightbox-close');

  // Open Lightbox on click
  galleryItems.forEach(function (item) {
    item.addEventListener('click', function () {
      var img = item.querySelector('img');
      if (img && lightbox && lightboxImg) {
        lightboxImg.src = img.src;
        lightbox.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  // Close Lightbox
  if (lightboxClose && lightbox) {
    lightboxClose.addEventListener('click', function () {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
      setTimeout(function() {
          lightboxImg.src = "";
      }, 300);
    });

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox || e.target.classList.contains('lightbox-content-wrapper')) {
        lightbox.classList.remove('open');
        document.body.style.overflow = '';
        setTimeout(function() {
            lightboxImg.src = "";
        }, 300);
      }
    });
  }


  /* =====================================================================
     Scholarship Form
     ===================================================================== */
  var form = document.getElementById('scholarship-form');
  var successPanel = document.getElementById('scholarship-success');
  var successText = document.getElementById('success-text');
  var submitBtn = document.getElementById('submit-btn');
  var submitLabel = document.getElementById('submit-label');
  var submitIcon = document.getElementById('submit-icon');
  var resetBtn = document.getElementById('reset-form');

  var SUBMIT_ICON_DEFAULT = submitIcon ? submitIcon.innerHTML : '';
  var SPIN_SVG =
    '<svg class="icon icon-spin-loader" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
    '<path d="M12 2v4M12 18v4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M2 12h4M18 12h4M4.9 19.1l2.8-2.8M16.3 7.7l2.8-2.8"/></svg>';

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (submitBtn.disabled) return;

      submitBtn.disabled = true;
      submitLabel.textContent = t('form.sending');
      submitIcon.innerHTML = SPIN_SVG;

      var payload = {
        studentName: form.studentName.value,
        guardian: form.guardian.value,
        phone: form.phone.value,
        email: form.email.value,
        program: form.program.value,
        grade: form.grade.value,
        reason: form.reason.value,
      };

      fetch('/api/scholarship', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
        .then(function (res) {
          return res.json().then(function (data) {
            return { ok: res.ok, data: data };
          });
        })
        .then(function (result) {
          submitBtn.disabled = false;
          submitLabel.textContent = t('form.submit');
          submitIcon.innerHTML = SUBMIT_ICON_DEFAULT;

          if (result.ok && result.data.ok) {
            var name = result.data.studentName;
            var namePart = name ? ' ' + name : '';
            successText.textContent = t('form.success.text').replace('{name}', namePart);
            form.hidden = true;
            successPanel.hidden = false;
            successPanel.classList.add('visible');
          } else {
            alert(t('form.error.required'));
          }
        })
        .catch(function () {
          submitBtn.disabled = false;
          submitLabel.textContent = t('form.submit');
          submitIcon.innerHTML = SUBMIT_ICON_DEFAULT;
          alert(t('form.error.generic'));
        });
    });
  }

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      form.reset();
      form.hidden = false;
      successPanel.hidden = true;
      successPanel.classList.remove('visible');
    });
  }

  /* =====================================================================
     Chatbot Configuration
     ===================================================================== */
  var chatToggle = document.getElementById('chat-toggle');
  var chatPanel = document.getElementById('chat-panel');
  var chatClose = document.getElementById('chat-close');
  var chatMessages = document.getElementById('chat-messages');
  var chatForm = document.getElementById('chat-form');
  var chatInput = document.getElementById('chat-input');
  var chatQuick = document.getElementById('chat-quick');
  var chatStarted = false;

  function addBubble(text, who) {
    var bubble = document.createElement('div');
    bubble.className = 'chat-bubble ' + (who === 'user' ? 'chat-bubble-user' : 'chat-bubble-bot');
    bubble.textContent = text;
    chatMessages.appendChild(bubble);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function resetChat() {
    if (!chatStarted) return;
    chatMessages.innerHTML = '';
    greetChat();
  }

  function greetChat() {
    fetch('/api/chat/greeting?lang=' + encodeURIComponent(currentLang))
      .then(function (res) {
          return res.json();
      })
      .then(function (data) {
        if (data && data.ok) {
            addBubble(data.reply, 'bot');
        }
      })
      .catch(function () {
          console.warn('Chat error');
      });
  }

  function sendMessage(message) {
    if (!message) return;
    addBubble(message, 'user');
    fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: message, lang: currentLang }),
    })
      .then(function (res) {
          return res.json();
      })
      .then(function (data) {
        if (data && data.ok) {
            addBubble(data.reply, 'bot');
        }
        else {
            addBubble(t('form.error.generic'), 'bot');
        }
      })
      .catch(function () {
          addBubble(t('form.error.generic'), 'bot');
      });
  }

  if (chatToggle) {
    chatToggle.addEventListener('click', function () {
      var isHidden = chatPanel.hasAttribute('hidden');
      if (isHidden) {
        chatPanel.removeAttribute('hidden');
        if (!chatStarted) {
          chatStarted = true;
          greetChat();
        }
      } else {
        chatPanel.setAttribute('hidden', '');
      }
    });
  }

  if (chatClose) {
    chatClose.addEventListener('click', function () {
      chatPanel.setAttribute('hidden', '');
    });
  }

  if (chatForm) {
    chatForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var message = chatInput.value.trim();
      if (!message) return;
      sendMessage(message);
      chatInput.value = '';
    });
  }

  if (chatQuick) {
    chatQuick.addEventListener('click', function (e) {
      var btn = e.target.closest('.chat-quick-btn');
      if (btn) {
          sendMessage(btn.textContent);
      }
    });
  }

  /* Finally, apply translations on load */
  applyTranslations();

})();