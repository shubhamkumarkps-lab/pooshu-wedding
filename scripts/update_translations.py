import json

# EN
with open('public/data/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

en['nav'] = {
    'wedding': 'The Wedding',
    'bride': '🌸 Know the Bride',
    'groom': '🦚 Know the Groom',
    'story': 'Our Story',
    'events': 'Events',
    'rsvp': 'RSVP'
}
en['envelope']['instruction'] = 'Press & Hold to Unveil'
en['envelope']['blooming'] = 'Blooming...'
en['envelope']['unveiled'] = 'Unveiled!'
en['rsvp']['submitBtn'] = 'Confirm Your RSVP'

en['bridePage'] = {
    'badge': 'Assamese Heritage • The Bride',
    'title': 'Pooja Haloi',
    'subtitle': 'A journey of grace, warmth, cultural pride, and boundless dreams',
    'motto': '🌸 হেঁপাহৰ ৰঙীন সপোন (Dreams woven with pure devotion)',
    'heritageTitle': 'Cultural Roots & Assamese Traditions',
    'heritageText': 'Rooted in the timeless elegance of Assam, Pooja carries forward the warmth of Phulam Gamosa, the pride of Muga silk, and the auspicious fragrance of Kopou orchids. Her heritage shines through festive Rongali Bihu rhythms, the reverence of Brass Xorai, and heartfelt wedding customs including Joron and Biya Naam.',
    'storyTitle': 'The 12-Year Love Story (Her Perspective)',
    'storyText': 'What started across high school benches in 2014 was simple and effortless. Over 12 years of exams, college, career dreams, and quiet moments, Shubham became my anchor, my confidant, and my greatest source of joy. Every milestone felt lighter with him by my side.',
    'factsTitle': 'Passions, Quirks & Fun Facts',
    'facts': [
        {'icon': '✨', 'title': 'The Creative Heart', 'desc': 'An eye for aesthetic design, home warmth, and making every moment memorable.'},
        {'icon': '☕', 'title': 'Chai Over Everything', 'desc': 'Cannot start the morning without a steaming cup of handcrafted milk tea.'},
        {'icon': '🥘', 'title': 'Culinary Pride', 'desc': 'Loves authentic Assamese Maasor Tenga, Khar, and festive homemade Pithas.'},
        {'icon': '💛', 'title': 'Favorite Memory', 'desc': 'Shubham surprising her after long exam seasons with comfort food and endless laughter.'}
    ],
    'familyTitle': 'Family Honor & Blessings',
    'familyText': 'Beloved daughter of Dr. Ajit Kumar Haloi & Smt. Champa Haloi • Sister of Neha Haloi.',
    'blessing': 'May Lord Ganesha and the sacred soil of Kamrup bless their lifelong union with boundless joy and health.',
    'backBtn': '← Back to Wedding Invitation',
    'peerBtn': 'Explore Shubham\'s Story 🦚'
}

en['groomPage'] = {
    'badge': 'Maithili Heritage • The Groom',
    'title': 'Shubham Kumar Thakur',
    'subtitle': 'A mind driven by vision, a heart anchored in tradition and loyalty',
    'motto': '🦚 मिथिलाक पाग, विद्या ओ संस्कार (Honor, wisdom & sanctity)',
    'heritageTitle': 'Cultural Roots & Maithili Traditions',
    'heritageText': 'Carrying the legacy of Mithila—the land of Raja Janak and Sita—Shubham takes pride in the honor of the Paag, the cosmic harmony of Kohbar art, and sacred Vedic traditions. His cultural roots represent unwavering integrity, deep respect for elders, and the musical poetry of Maithili Vivah Geet.',
    'storyTitle': 'The 12-Year Love Story (His Perspective)',
    'storyText': 'The moment I saw Pooja in 2014, my world found its center. Through 12 transformative years—school farewells, engineering challenges, product milestones—her faith in me has been my guiding light. Choosing her forever is the easiest and greatest decision of my life.',
    'factsTitle': 'Passions, Quirks & Fun Facts',
    'facts': [
        {'icon': '💻', 'title': 'The Visionary Builder', 'desc': 'Passionate technologist and product creator who loves turning complex ideas into magic.'},
        {'icon': '🎵', 'title': 'Melody Explorer', 'desc': 'Deeply moved by traditional ghazals, regional wedding geet, and vintage melodies.'},
        {'icon': '🍲', 'title': 'Comfort Food', 'desc': 'Classic Maithili Machh-Bhaat and festive winter tilkuts.'},
        {'icon': '🌟', 'title': 'Favorite Trait in Pooja', 'desc': 'Her radiant smile that instantly dissolves stress and makes any house feel like home.'}
    ],
    'familyTitle': 'Family Honor & Blessings',
    'familyText': 'Beloved son of Shri Suman Thakur & Smt. Kiran Thakur • Brother of Shivam Thakur.',
    'blessing': 'May the divine blessings of Lord Shiva and Mata Parvati grant their journey everlasting companionship.',
    'backBtn': '← Back to Wedding Invitation',
    'peerBtn': 'Explore Pooja\'s Story 🌸'
}

with open('public/data/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)

# AS
with open('public/data/as.json', 'r', encoding='utf-8') as f:
    as_data = json.load(f)

as_data['nav'] = {
    'wedding': 'শুভ বিবাহ',
    'bride': '🌸 কইনাক জানক',
    'groom': '🦚 দৰাক জানক',
    'story': 'আমাৰ কাহিনী',
    'events': 'মাংগলিক কাৰ্যসূচী',
    'rsvp': 'উপস্থিতি নিশ্চিতকৰণ'
}
as_data['envelope']['instruction'] = 'খুলিবলৈ স্পৰ্শ কৰি ধৰি ৰাখক'
as_data['envelope']['blooming'] = 'পাহি মেলিছে...'
as_data['envelope']['unveiled'] = 'উন্মোচিত হ\'ল!'
as_data['rsvp']['submitBtn'] = 'উপস্থিতি নিশ্চিত কৰক'

as_data['bridePage'] = {
    'badge': 'অসমীয়া ঐতিহ্য • আমাৰ কইনা',
    'title': 'পূজা হালৈ',
    'subtitle': 'সৌন্দৰ্য্য, আত্মীয়তা, ঐতিহ্যৰ গৌৰৱ আৰু উজ্জ্বল সপোনৰ এক সুন্দৰ যাত্ৰা',
    'motto': '🌸 আইৰ আশীৰ্বাদ আৰু হেঁপাহৰ এনাজৰী',
    'heritageTitle': 'সাংস্কৃতিক শিপা আৰু অসমীয়া পৰম্পৰা',
    'heritageText': 'অসমৰ বুকুত জন্ম লৈ পূজাই লগত লৈ ফুৰে ফুলাম গামোচাৰ মৰম, মুগা ৰেচমৰ গৌৰৱ আৰু কপৌ ফুলৰ পৱিত্ৰ সুবাস। ৰঙালী বিহুৰ আনন্দ, কাঁহৰ শৰাইৰ সন্মান আৰু পৰম্পৰাগত বিয়া নামৰ মাংগলিক সুৰেৰে তেওঁৰ জীৱন সদায় সমৃদ্ধ।',
    'storyTitle': '১২ বছৰীয়া প্ৰেমৰ যাত্ৰা (পূজাৰ দৃষ্টিত)',
    'storyText': '২০১৪ চনৰ স্কুলৰ সেই চিনাকিটো আছিল অতি সহজ আৰু আপোন। যোৱা ১২ বছৰৰ পৰীক্ষা, কেৰিয়াৰ আৰু জীৱনৰ উত্থান-পতনৰ মাজত শুভম আছিল মোৰ আটাইতকৈ বিশ্বাসী সংগী।',
    'factsTitle': 'প্ৰিয় দিশ আৰু ব্যক্তিত্ব',
    'facts': [
        {'icon': '✨', 'title': 'সৃজনশীল মন', 'desc': 'সকলো পৰিৱেশ আনন্দময় আৰু নান্দনিক কৰি তোলাৰ সুন্দৰ ক্ষমতা।'},
        {'icon': '☕', 'title': 'চাহৰ প্ৰতি ভালপোৱা', 'desc': 'এমুঠি গৰম চাহ নহ\'লে পুৱাটো অসম্পূৰ্ণ।'},
        {'icon': '🥘', 'title': 'অসমীয়া খাদ্যৰ সোৱাদ', 'desc': 'মাছৰ টেঙা আৰু ঘৰুৱা পিঠা সদায় অতি প্ৰিয়।'},
        {'icon': '💛', 'title': 'শুভমৰ সৈতে প্ৰিয় স্মৃতি', 'desc': 'পৰীক্ষাৰ ব্যস্ততাৰ মাজতো শুভমৰ সেই নিৰৱ সমৰ্থন আৰু হাঁহি।'}
    ],
    'familyTitle': 'পৰিয়াল আৰু শুভাভিন্দন',
    'familyText': 'শ্ৰীমতী চম্পা হালৈ আৰু ড° অজিত কুমাৰ হালৈৰ স্নেহৰ কন্যা • নেহা হালৈৰ ভগ্নী।',
    'blessing': 'ভগৱান শ্ৰীগণেশ আৰু অসম মাতৃৰ আশীৰ্বাদেৰে তেওঁলোকৰ সংসাৰ সুখ আৰু শান্তিৰে ভৰি পৰক।',
    'backBtn': '← মূল নিমন্ত্ৰণলৈ উভতি যাওক',
    'peerBtn': 'শুভমৰ কাহিনী জানক 🦚'
}

as_data['groomPage'] = {
    'badge': 'মৈথিলী ঐতিহ্য • আমাৰ দৰা',
    'title': 'শুভম কুমাৰ ঠাকুৰ',
    'subtitle': 'দৃষ্টিশীল মন, পৰম্পৰা আৰু নিষ্ঠাৰ প্ৰতি নিৰন্তৰ সমৰ্পণ',
    'motto': '🦚 মিথিলাৰ পাগ আৰু চিৰন্তন সংস্কাৰ',
    'heritageTitle': 'সাংস্কৃতিক শিপা আৰু মৈথিলী ঐতিহ্য',
    'heritageText': 'ৰজা জনক আৰু সীতা মাতাৰ পৱিত্ৰ ভূমি মিথিলাৰ সন্তান শুভমে গৌৰৱেৰে বহন কৰে মিথিলা পাগৰ সন্মান, কোহবৰ কলাৰ পৱিত্ৰ প্ৰতীক আৰু বৈদিক পৰম্পৰাৰ নিষ্ঠা।',
    'storyTitle': '১২ বছৰীয়া প্ৰেমৰ যাত্ৰা (শুভমৰ দৃষ্টিত)',
    'storyText': '২০১৪ চনত পূজাক প্ৰথম দেখোঁতেই মই অনুভৱ কৰিছিলোঁ যে মোৰ জীৱনৰ পথ বিচাৰি পালোঁ। ১২ বছৰীয়া এই যাত্ৰাত পূজাৰ মৰম আৰু সাহসেই মোৰ পথ প্ৰদৰ্শক হৈ আহিছে।',
    'factsTitle': 'প্ৰিয় দিশ আৰু ব্যক্তিত্ব',
    'facts': [
        {'icon': '💻', 'title': 'নতুন সৃষ্টিৰ প্ৰয়াস', 'desc': 'প্ৰযুক্তি আৰু নতুন সৃষ্টিশীল ধাৰণাৰ প্ৰতি গভীৰ অনুৰাগ।'},
        {'icon': '🎵', 'title': 'সংগীতৰ প্ৰেম', 'desc': 'লোকগীত, গজল আৰু পৰম্পৰাগত সুৰৰ গভীৰ শ্ৰোতা।'},
        {'icon': '🍲', 'title': 'প্ৰিয় খাদ্য', 'desc': 'পৰম্পৰাগত মৈথিলী মাছ-ভাত আৰু তিলকুট।'},
        {'icon': '🌟', 'title': 'পূজাৰ শ্ৰেষ্ঠ গুণ', 'desc': 'পূজাৰ সৰল হাঁহিটোৱে যিকোনো কঠিন মুহূৰ্তকো সহজ কৰি তোলে।'}
    ],
    'familyTitle': 'পৰিয়াল আৰু শুভাভিন্দন',
    'familyText': 'শ্ৰীমতী কিৰণ ঠাকুৰ আৰু শ্ৰী সুমন ঠাকুৰৰ সুযোগ্য পুত্ৰ • শিৱম ঠাকুৰৰ ভাতৃ।',
    'blessing': 'মহাদেৱ আৰু মাতা পাৰ্বতীৰ কৃপাত দুয়োৰে দাম্পত্য জীৱন চিৰসুখী হওক।',
    'backBtn': '← মূল নিমন্ত্ৰণলৈ উভতি যাওক',
    'peerBtn': 'পূজাৰ কাহিনী জানক 🌸'
}

with open('public/data/as.json', 'w', encoding='utf-8') as f:
    json.dump(as_data, f, ensure_ascii=False, indent=2)

# MAI
with open('public/data/mai.json', 'r', encoding='utf-8') as f:
    mai = json.load(f)

mai['nav'] = {
    'wedding': 'शुभ विवाह',
    'bride': '🌸 कन्या परिचय',
    'groom': '🦚 वर परिचय',
    'story': 'हमर यात्रा',
    'events': 'मांगलिक कार्यक्रम',
    'rsvp': 'उपस्थिति स्वीकृति'
}
mai['envelope']['instruction'] = 'खोलबाक लेल दबा क\' राखू'
mai['envelope']['blooming'] = 'पुष्प विकसित भ\' रहल अछि...'
mai['envelope']['unveiled'] = 'प्रकट भेल!'
mai['rsvp']['submitBtn'] = 'उपस्थिति स्वीकृत करू'

mai['bridePage'] = {
    'badge': 'असमिया परंपरा • कन्या परिचय',
    'title': 'पूजा हालोई',
    'subtitle': 'सौंदर्य, आत्मीयता, सांस्कृतिक गौरव आ पावन स्वप्नक सुंदर संगम',
    'motto': '🌸 मातृस्नेह आ पवित्र संस्कारक संगम',
    'heritageTitle': 'सांस्कृतिक जड़ि आ असमिया परंपरा',
    'heritageText': 'असमक पावन भूमिक कन्या पूजाक व्यक्तित्व में फुलाम गामोचाक स्नेह, मूगा सिल्कक गौरव आ कपोऊ फूलक पवित्रता रचल-बसल अछि। बिहुक उमंग, पीतलक शराईक सम्मान आ पारंपरिक विवाह गीतिक मिठास हुनक पहचान अछि।',
    'storyTitle': '१२ वर्षक प्रेम यात्रा (पूजाक दृष्टि सँ)',
    'storyText': '२०१४ में विद्यालयक प्रांगण सँ शुरू भेल ई पहचान अति सरल आ निश्चल छल। १२ वर्षक प्रत्येक मोड़ पर शुभमक साथ हमरा निरंतर संबल आ असीम प्रसन्नता देलक।',
    'factsTitle': 'रुचि आ व्यक्तित्व',
    'facts': [
        {'icon': '✨', 'title': 'रचनात्मक स्वभाव', 'desc': 'प्रत्येक स्थान केँ अपन स्नेह आ कला सँ जीवंत बनायब हुनक स्वभाव अछि।'},
        {'icon': '☕', 'title': 'चाय सँ अनुराग', 'desc': 'सुप्रभात में गरम चाय बिना दिन अधूरा लगैत अछि।'},
        {'icon': '🥘', 'title': 'असमिया स्वाद', 'desc': 'पारंपरिक माछक झोर आ पीठा विशेष प्रिय अछि।'},
        {'icon': '💛', 'title': 'शुभमक संग स्मृति', 'desc': 'शुभमक धैर्य आ निश्चल प्रेम जे सदैव विश्वास बनौने राखलक।'}
    ],
    'familyTitle': 'कुल गौरव आ शुभाशीर्वाद',
    'familyText': 'श्रीमती चम्पा हालोई आ डॉ. अजीत कुमार हालोईक सुपुत्री • नेहा हालोईक बहिन।',
    'blessing': 'भगवान श्रीगणेशक कृपा सँ नव युगलक जीवन में सुख आ समृद्धिक निरंतर वास होअय।',
    'backBtn': '← मुख्य निमंत्रण पर वापस जाऊ',
    'peerBtn': 'शुभमक परिचय देखू 🦚'
}

groom_page_mai = {
    'badge': 'मैथिली परंपरा • वर परिचय',
    'title': 'शुभम कुमार ठाकुर',
    'subtitle': 'दूरदर्शी विचार, सनातन संस्कार आ अटूट निष्ठाक प्रतीक',
    'motto': '🦚 मिथिलाक पाग, मर्यादा आ विद्या',
    'heritageTitle': 'सांस्कृतिक जड़ि आ मैथिली परंपरा',
    'heritageText': 'राजा जनक आ जानकीक पावन भूमि मिथिलाक गौरव शुभम अपन पागक सम्मान, कोहबर कलाक पवित्र संदेश आ वैदिक मर्यादा केँ प्राणप्रण सँ धारण करैत छथि। पारंपरिक विवाह गीत आ कुलपरंपरा हुनक जीवनक आधार अछि।',
    'storyTitle': '१२ वर्षक प्रेम यात्रा (शुभमक दृष्टि सँ)',
    'storyText': '२०१४ में जब पहिल बेर पूजा केँ देखलहुँ, तखनहिं मन निश्चिंत भ\' गेल छल जे हमर संगी मिल गेल। १२ वर्षक ई यात्रा में पूजाक विश्वास हमर सर्वोपरि संबल रहल अछि।',
    'factsTitle': 'रुचि आ व्यक्तित्व',
    'facts': [
        {'icon': '💻', 'title': 'नव सृजन शिल्पी', 'desc': 'प्रौद्योगिकी आ नव-नव विचार केँ साकार करबाक प्रबल उत्साह।'},
        {'icon': '🎵', 'title': 'संगीत प्रेमी', 'desc': 'मैथिली पारंपरिक गीत, गजल आ शास्त्रीय सुरक अनुरागी।'},
        {'icon': '🍲', 'title': 'प्रिय भोजन', 'desc': 'पारंपरिक मिथिलाक माछ-भात आ मखानक खीर।'},
        {'icon': '🌟', 'title': 'पूजाक प्रिय गुण', 'desc': 'पूजाक निश्चल मुस्कान जे सब संताप केँ दूर क\' दैत अछि।'}
    ],
    'familyTitle': 'कुल गौरव आ शुभाशीर्वाद',
    'familyText': 'श्रीमती किरण ठाकुर आ श्री सुमन ठाकुरक सुपुत्र • शिवम ठाकुरक भाय।',
    'blessing': 'भगवान शिव आ माता जानकीक शुभाशीर्वाद सँ दुनू गोटेक जीवन सदा मंगलमय रहय।',
    'backBtn': '← मुख्य निमंत्रण पर वापस जाऊ',
    'peerBtn': 'पूजाक परिचय देखू 🌸'
}
mai['groomPage'] = groom_page_mai

with open('public/data/mai.json', 'w', encoding='utf-8') as f:
    json.dump(mai, f, ensure_ascii=False, indent=2)

print('Updated en.json, as.json, mai.json successfully!')
