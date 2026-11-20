const fs = require('fs');

const en = JSON.parse(fs.readFileSync('public/data/en.json', 'utf8'));
const as = JSON.parse(fs.readFileSync('public/data/as.json', 'utf8'));
const mai = JSON.parse(fs.readFileSync('public/data/mai.json', 'utf8'));

// 1. Update 14-Year texts in story
en.story.sectionTitle = "Our 14-Year Journey";
en.story.sectionSubtitle = "From high school sweethearts in 2012 to tying the knot in 2026";

as.story.sectionTitle = "আমাৰ ১৪ বছৰীয়া প্ৰেমৰ যাত্ৰা";
as.story.sectionSubtitle = "২০১২ চনৰ স্কুলীয়া দিনৰ পৰা ২০২৬ চনৰ শুভ বিবাহলৈ";

mai.story.sectionTitle = "हमर १४ वर्षक प्रेम यात्रा";
mai.story.sectionSubtitle = "२०१२ क विद्यालय प्रांगण सँ २०२६ क पावन विवाह वेदी धरि";

// 2. Chapters data (15 chronological chapters)
const chaptersEn = [
  {
    year: "2012",
    title: "First Outing, First Sparks",
    subtitle: "School Trip to Manesar",
    desc: "Where it all began. Amidst high school chatter and adventurous day outings in Manesar, two lives crossed paths and an enduring spark was ignited.",
    image: "assets/photos/story_2012.jpeg"
  },
  {
    year: "2013",
    title: "Bus Rides & Shared Notes",
    subtitle: "Another High School Adventure",
    desc: "Passing notes across school bus seats, endless inside jokes, and realizing that every school trip was only memorable because we were together.",
    image: "assets/photos/story_2013.jpg"
  },
  {
    year: "2014",
    title: "Farewell Smiles & Sweet Beginnings",
    subtitle: "At a Restaurant After School Farewell",
    desc: "Dressed in formal farewell blazers and sarees, sitting at a local restaurant laughing over memories, silently promising that school ending was only our prologue.",
    image: "assets/photos/story_2014.jpeg"
  },
  {
    year: "2015",
    title: "Dhaak Beats & Festivity",
    subtitle: "Durga Puja Celebrations",
    desc: "Under the festive glow of pandal lights, fragrant incense, and rhythmic dhaak beats, celebrating the divine warmth of autumn together.",
    image: "assets/photos/story_2015.jpeg"
  },
  {
    year: "2016",
    title: "Above the Clouds in Triund",
    subtitle: "First Mountain Trek Together",
    desc: "Conquering rocky trails, cold mountain winds, and reaching the majestic green ridge of Triund together—our very first mountain adventure.",
    image: "assets/photos/story_2016.jpeg"
  },
  {
    year: "2017",
    title: "Chopsticks & Korean Flavors",
    subtitle: "First Dinner at a Korean Restaurant",
    desc: "Experimenting with sizzling barbecue and chopsticks, laughing through clumsy bites, and discovering our shared love for diverse culinary journeys.",
    image: "assets/photos/story_2017.jpeg"
  },
  {
    year: "2018",
    title: "Quiet Walks & Warm Companionship",
    subtitle: "Precious Outings & Timeless Bonds",
    desc: "Stepping out for spontaneous peaceful walks, sharing dreams and everyday stories, and finding comfort in simply having each other nearby.",
    image: "assets/photos/story_2018.jpeg"
  },
  {
    year: "2019",
    title: "The Misty Parvati Valley",
    subtitle: "Trek to Kheerganga",
    desc: "Winding pine trails, rushing river gorges, and soothing hot springs beneath a sky full of stars in the heart of Himachal.",
    image: "assets/photos/story_2019.jpg"
  },
  {
    year: "2020",
    title: "Unstoppable Laughter",
    subtitle: "First Live Standup Comedy Show",
    desc: "Tears of pure laughter, front-row comedy, and sharing the sheer happiness that makes every ordinary week feel extraordinary.",
    image: "assets/photos/story_2020.jpg"
  },
  {
    year: "2021",
    title: "The Moon Lake of Spiti",
    subtitle: "Expedition to Chandratal",
    desc: "Surrounded by barren Himalayan peaks and crystal turquoise waters at 14,000 feet, feeling that our love could weather any terrain.",
    image: "assets/photos/story_2021.jpg"
  },
  {
    year: "2022",
    title: "Colors of Eternal Joy",
    subtitle: "Festive Rang & Gulal",
    desc: "Drenched in crimson, gold, and joy. Celebrating Holi with hearts as vibrant as the festive gulal in the air.",
    image: "assets/photos/story_2022.jpg"
  },
  {
    year: "2023",
    title: "Dressed to Slay Together",
    subtitle: "Celebrations at a Wedding",
    desc: "All dolled up in ethnic finery, lighting up the celebration, and exchanging knowing smiles when friends asked: 'When is yours?'",
    image: "assets/photos/story_2023.jpg"
  },
  {
    year: "2024",
    title: "Another Wedding, Waiting for Ours",
    subtitle: "Dreaming of the Mandap",
    desc: "Celebrating love with loved ones, sharing secret glances across the wedding canopy, knowing with every heartbeat that our turn was coming next.",
    image: "assets/photos/story_2024.jpg"
  },
  {
    year: "2025",
    title: "Rokafied & Blessed",
    subtitle: "Official Family Sealing of Forever",
    desc: "Phulam Gamosas, Maithili Paag, golden envelopes, and blessed smiles. The moment both families officially proclaimed: It's #pooshu time!",
    image: "assets/photos/story_2025.jpeg"
  },
  {
    year: "2026",
    title: "#pooshu Forever: The Wedding",
    subtitle: "December 2, 2026 • Sacred Vows",
    desc: "Fourteen unforgettable years of laughter, growth, and companionship culminating at the sacred wedding mandap. Our forever starts today.",
    image: "assets/photos/story_2026.jpg"
  }
];

const chaptersAs = [
  {
    year: "২০১২",
    title: "প্ৰথম যাত্ৰা, প্ৰথম চিনাকি",
    subtitle: "মানেছাৰলৈ স্কুলীয়া ভ্ৰমণ",
    desc: "মানেছাৰৰ স্কুলীয়া ভ্ৰমণৰ হাঁহি-ধেমালিৰ মাজতে দুয়োৰে মাজত আৰম্ভ হৈছিল এটি আজীৱন স্মৃতিৰ পাতনি।",
    image: "assets/photos/story_2012.jpeg"
  },
  {
    year: "২০১৩",
    title: "আকৌ এটি স্কুলীয়া ভ্ৰমণ",
    subtitle: "বাসৰ খিৰিকী আৰু নীৰৱ কথা",
    desc: "স্কুল বাছৰ খিৰিকীৰ কাষত বহি ভাগ-বটোৱাৰা কৰা গান আৰু কথা—প্ৰতিটো ভ্ৰমণ মাথোঁ ইজনে সিজনৰ উপস্থিতিতেই বিশেষ হৈ পৰিছিল।",
    image: "assets/photos/story_2013.jpg"
  },
  {
    year: "২০১৪",
    title: "স্কুলৰ বিদায়বেলাৰ স্মৃতি",
    subtitle: "বিদায় অনুষ্ঠানৰ পিছত ৰেস্তোৰাঁত",
    desc: "বিদায়ৰ পোছাক পিন্ধি স্কুলৰ স্মৃতি সুঁৱৰি ৰেস্তোৰাঁত কটোৱা সময়—স্কুল সমাপ্ত হ'লেও আমাৰ বন্ধুত্ব সদায় একেদৰেই থাকিব বুলি কৰা মৌন শপত।",
    image: "assets/photos/story_2014.jpeg"
  },
  {
    year: "২০১৫",
    title: "শাৰদীয় দুৰ্গাপূজাৰ আনন্দ",
    subtitle: "ঢাকৰ মাত আৰু পোহৰৰ উৎসৱ",
    desc: "মণ্ডপৰ আলোকসজ্জা আৰু ঢাকৰ ধ্বনিৰ মাজত শাৰদীয় দুৰ্গোৎসৱৰ পৱিত্ৰ আনন্দ দুয়ো একেলগে উপভোগ কৰাৰ ক্ষণ।",
    image: "assets/photos/story_2015.jpeg"
  },
  {
    year: "২০১৬",
    title: "পাহাৰৰ বুকুত প্ৰথম পদচিহ্ন",
    subtitle: "ত্ৰিয়ুণ্ডলৈ প্ৰথম পাহাৰীয়া ভ্ৰমণ",
    desc: "শীতল পাহাৰী বতাহ আৰু ওখোৰা-মোখোৰা বাট অতিক্ৰম কৰি ত্ৰিয়ুণ্ডৰ সেউজ শৃংগত ভৰি দিয়াৰ অপূৰ্ব ৰোমাঞ্চ।",
    image: "assets/photos/story_2016.jpeg"
  },
  {
    year: "২০১৭",
    title: "কোৰিয়ান সোৱাদ আৰু চপষ্টিক",
    subtitle: "কোৰিয়ান ৰেস্তোৰাঁত প্ৰথম সান্ধ্যভোজ",
    desc: "চপষ্টিক চলোৱাৰ হাঁহি-ধেমালিৰ মাজত নতুন সোৱাদৰ সন্ধান আৰু দুয়োৰে আড্ডাৰে ভৰা এটি সুন্দৰ সন্ধিয়া।",
    image: "assets/photos/story_2017.jpeg"
  },
  {
    year: "২০১৮",
    title: "শান্ত খোজ আৰু অন্তৰংগ কথা",
    subtitle: "ব্যস্ততাৰ মাজত সান্ধ্যভ্ৰমণ",
    desc: "ব্যস্ত দিনবোৰৰ মাজত নীৰৱ খোজ কঢ়া, সপোন ভগাই লোৱা আৰু দুয়ো কাষত থকাৰ আশ্বাসেৰে আগবাঢ়ি যোৱা।",
    image: "assets/photos/story_2018.jpeg"
  },
  {
    year: "২০১৯",
    title: "পাৰ্বতী উপত্যকাৰ মায়াময় সৌন্দৰ্য",
    subtitle: "খীৰগঙ্গালৈ পাহাৰীয়া ট্ৰেক",
    desc: "সৰল গছৰ ছাঁ, পাহাৰীয়া নদীৰ কলকল ধ্বনি আৰু আকাশভৰা তৰাৰ তলত খীৰগঙ্গাৰ পাহাৰ বগোৱাৰ যাত্ৰা।",
    image: "assets/photos/story_2019.jpg"
  },
  {
    year: "২০২০",
    title: "প্ৰাণখোলা হাঁহিৰ সন্ধিয়া",
    subtitle: "প্ৰথম লাইভ ষ্টেণ্ডআপ কমেডী শ্ব'",
    desc: "প্ৰথমবাৰ লাইভ ষ্টেণ্ডআপ শ্ব' উপভোগ কৰি প্ৰাণখুলি হাঁহি আনন্দৰ সাগৰত বুৰ যোৱা এটি মনপৰশা সন্ধিয়া।",
    image: "assets/photos/story_2020.jpg"
  },
  {
    year: "২০২১",
    title: "স্পিতিৰ চন্দ্ৰতাল হ্ৰদৰ পাৰত",
    subtitle: "১৪,০০০ ফুট উচ্চতাত নীল জলৰাশি",
    desc: "হিমালয়ৰ আকাশচুম্বী পাহাৰ আৰু নীলাভ পানীৰ চন্দ্ৰতালৰ কাষত চিৰন্তন প্ৰেমৰ গভীৰ অনুভৱ।",
    image: "assets/photos/story_2021.jpg"
  },
  {
    year: "২০২২",
    title: "ফাকুৱাৰ ৰঙীণ আনন্দ",
    subtitle: "হেঁপাহৰ ৰং আৰু ফাকু",
    desc: "ৰঙৰ উৎসৱ ফাকুৱাত ৰঙীন হৈ পৰা দুখন মন—মৰমৰ ৰঙেৰে জীৱনৰ কেনভাছ সজাই তোলাৰ ক্ষণ।",
    image: "assets/photos/story_2022.jpg"
  },
  {
    year: "২০২৩",
    title: "বিবাহ অনুষ্ঠানত ৰাজকীয় সাজত",
    subtitle: "বন্ধুৰ বিয়াত একেলগে উপস্থিত",
    desc: "পৰম্পৰাগত সাজ-পোছাকত বিয়াৰ আনন্দ ভাগ কৰি থকাৰ মাজতে সকলোৱে সুধিছিল: 'তোমালোকৰ বিয়াখন কেতিয়া?'",
    image: "assets/photos/story_2023.jpg"
  },
  {
    year: "২০২৪",
    title: "আকৌ এখন বিয়া, আমাৰ অপেক্ষাত",
    subtitle: "বিয়াৰ মণ্ডপ আৰু আমাৰ সপোন",
    desc: "আনৰ বিয়াত শুভাশিস জনোৱাৰ সময়ত দুয়োৰে চকুৱে চকুৱে কথা হৈছিল—খুব সোনকালেই আমাৰ নিজৰ দিনটো আহিব।",
    image: "assets/photos/story_2024.jpg"
  },
  {
    year: "২০২৫",
    title: "পৰিয়ালৰ আশীৰ্বাদ: ৰোকা সম্পন্ন",
    subtitle: "ফুলাম গামোচা আৰু মৈথিলী পাগৰ বন্ধন",
    desc: "দুয়োখন পৰিয়ালৰ সান্নিধ্যত ৰোকা অনুষ্ঠান সম্পন্ন হ'ল—ফুলাম গামোচা আৰু মৈথিলী পাগেৰে এটি নতুন অধ্যায়ৰ শুভাৰম্ভ।",
    image: "assets/photos/story_2025.jpeg"
  },
  {
    year: "২০২৬",
    title: "#pooshu চিৰদিনৰ বাবে: পৱিত্ৰ বিবাহ",
    subtitle: "০২ ডিচেম্বৰ, ২০২৬ • চিৰন্তন শপত",
    desc: "১৪ বছৰীয়া প্ৰেম, বিশ্বাস আৰু বন্ধুত্বৰ মহামিলন—পৱিত্ৰ বিবাহ মণ্ডপত আমাৰ নতুন যাত্ৰাৰ আৰম্ভণি।",
    image: "assets/photos/story_2026.jpg"
  }
];

const chaptersMai = [
  {
    year: "२०१२",
    title: "पहिल भ्रमण, पहिल सान्निध्य",
    subtitle: "मानेसरक विद्यालय यात्रा",
    desc: "मानेसरक विद्यालय यात्रा में संग-संग बितेने क्षण, जतय सँ दूटा मनक बीच एक अटूट स्नेहक आरंभ भेल।",
    image: "assets/photos/story_2012.jpeg"
  },
  {
    year: "२०१३",
    title: "विद्यालयक पुनः एकटा यात्रा",
    subtitle: "बसक खिड़की आ मधुर संवाद",
    desc: "स्कूल बसक यात्रा, मंद हास्य आ एक-दोसरक संग समय बितयबाक ओ बालसुलभ आनंद जे जीवन भरिक लेल अमर भ' गेल।",
    image: "assets/photos/story_2013.jpg"
  },
  {
    year: "२०१४",
    title: "विद्यालय विदाई आ संकल्प",
    subtitle: "विदाई समारोहक उपरांत रेस्टोरेंट में",
    desc: "विद्यालय विदाईक परिधान में रेस्टोरेंट में बैसि कय कयल गेल हास-परिहास आ जीवन पथ पर संग चलबाक मौन प्रतिज्ञा।",
    image: "assets/photos/story_2014.jpeg"
  },
  {
    year: "२०१५",
    title: "दुर्गा पूजाक पावन उल्लास",
    subtitle: "ढाकक नाद आ दीपमालिका",
    desc: "माँ दुर्गाक पूजा पंडालक दिव्य आभा, ढाकक नाद आ शरद ऋतुक पावन उल्लास में संगहि बीतल क्षण।",
    image: "assets/photos/story_2015.jpeg"
  },
  {
    year: "२०१६",
    title: "पहाड़क शिखरक स्पर्श: त्रियुंड",
    subtitle: "प्रथम पर्वतीय ट्रैकिंग",
    desc: "शीतल पर्वतीय समीर आ पथरीली राह केँ पार कय त्रियुंडक हरित शिखरक ऊंचाई पर संगहि विजय पावब।",
    image: "assets/photos/story_2016.jpeg"
  },
  {
    year: "२०१७",
    title: "कोरियन स्वाद आ चॉपस्टिक्स",
    subtitle: "कोरियन रेस्टोरेंट में प्रथम रात्रिभोज",
    desc: "चॉपस्टिक्स सँ भोजन करबाक मीठ अभ्यास, हास-परिहास आ नवीन स्वादक संग एक अविस्मरणीय सांध्यवेला।",
    image: "assets/photos/story_2017.jpeg"
  },
  {
    year: "२०१८",
    title: "शांत भ्रमण आ अटूट साथ",
    subtitle: "जीवनक डगर पर संगहि यात्रा",
    desc: "व्यस्त जीवनक बीच छोट-छोट पदयात्रा, भविष्यक स्वप्न आ एक-दोसरक उपस्थिति सँ भेटल अपार शांति।",
    image: "assets/photos/story_2018.jpeg"
  },
  {
    year: "२०१९",
    title: "खीरगंगाक विहंगम घाटी",
    subtitle: "हिमाचलक पावन पर्वत यात्रा",
    desc: "देवदारुक वन, निर्मल नदक कल-कल नाद आ नक्षत्रलोकक छाँह में खीरगंगाक पावन ट्रैकिंग।",
    image: "assets/photos/story_2019.jpg"
  },
  {
    year: "२०२०",
    title: "हृदयस्पर्शी हास्यक सांध्यवेला",
    subtitle: "प्रथम लाइव स्टैंडअप कॉमेडी शो",
    desc: "सामने बैसि कय लाइव हास्य प्रहसनक आनंद लेब, नयन सँ आनंदक अश्रुपात आ अवर्णनीय प्रसन्नता।",
    image: "assets/photos/story_2020.jpg"
  },
  {
    year: "२०२१",
    title: "स्पीतिक चंद्रताल सरोवर",
    subtitle: "१४,००० फीट ऊंचाई पर पावन नीलिमा",
    desc: "हिमालयक तुंग शिखरक बीच चंद्रतालक नील जलराशिक साक्षी में प्रेम आ विश्वासक नव शिखर।",
    image: "assets/photos/story_2021.jpg"
  },
  {
    year: "२०२२",
    title: "होलीक पावन रंगोत्सव",
    subtitle: "गुलाल आ प्रीतिक रंग",
    desc: "हर्षोल्लासक संग अबीर-गुलाल सँ रंगायल मन आ एक-दोसरक प्रति अगाध प्रेमक पावन उत्सव।",
    image: "assets/photos/story_2022.jpg"
  },
  {
    year: "२०२३",
    title: "विवाह समारोह में संगहि शोभा",
    subtitle: "मित्रक विवाहोत्सव में उपस्थिति",
    desc: "पारंपरिक भव्य परिधान में विवाहोत्सव में दीपशिखा सदृश चमकैत, आ मित्रगणक प्रश्न: 'अहाँ दुनूक पावन लग्न कहिया?'",
    image: "assets/photos/story_2023.jpg"
  },
  {
    year: "२०२४",
    title: "पुनः एकटा विवाह, हमर प्रतीक्षा",
    subtitle: "विवाह वेदी आ पावन स्वप्न",
    desc: "आनक विवाह में सम्मिलित होइत मनहिं मन अपन पावन वेदीक स्वप्न संजोयब, जे आब हमर पावन परिणयक समय अछि।",
    image: "assets/photos/story_2024.jpg"
  },
  {
    year: "२०२५",
    title: "रोका संस्कार आ शुभाशीर्वाद",
    subtitle: "मिथिलाक पाग आ गामोछाक संगम",
    desc: "दुनू परिवारक आत्मीय उपस्थिति में रोकाक पावन रस्म सम्पन्न, पाग-गामोछा सँ सजल हमर परिणयक आधिकारिक उद्घोष।",
    image: "assets/photos/story_2025.jpeg"
  },
  {
    year: "२०२६",
    title: "#pooshu सदा-सदाक लेल: पावन परिणय",
    subtitle: "०२ दिसम्बर, २०२६ • सप्तपदी आ पावन वचन",
    desc: "१४ वर्षक साधना, प्रेम आ विश्वासक पावन परिणति। विवाह वेदी पर अग्नि केँ साक्षी मानि आजीवन संग रहबाक संकल्प।",
    image: "assets/photos/story_2026.jpg"
  }
];

en.story.chapters = chaptersEn;
as.story.chapters = chaptersAs;
mai.story.chapters = chaptersMai;

// 3. Remove Dietary Preferences from RSVP (Item 6)
delete en.rsvp.dietary;
delete en.rsvp.dietaryVeg;
delete en.rsvp.dietaryNonVeg;
delete en.rsvp.dietaryJain;

delete as.rsvp.dietary;
delete as.rsvp.dietaryVeg;
delete as.rsvp.dietaryNonVeg;
delete as.rsvp.dietaryJain;

delete mai.rsvp.dietary;
delete mai.rsvp.dietaryVeg;
delete mai.rsvp.dietaryNonVeg;
delete mai.rsvp.dietaryJain;

// 4. Update Groom caption (Item 7)
en.groomPage.subtitle = "A mind driven by vision, a heart & anchored in tradition & Love";
as.groomPage.subtitle = "দৃষ্টিশীল মন, পৰম্পৰা আৰু প্ৰেমৰ প্ৰতি নিৰন্তৰ সমৰ্পণ";
mai.groomPage.subtitle = "दूरदर्शी विचार, सनातन परंपरा आ प्रेम प्रति समर्पित हृदय";

// 5. Update 14-Year texts in Bride & Groom pages
en.bridePage.storyTitle = "The 14-Year Love Story (Her Perspective)";
en.bridePage.storyText = "What started across high school benches in 2012 was simple and effortless. Over 14 years of exams, college, career dreams, and quiet moments, Shubham became my anchor, my confidant, and my greatest source of joy. Every milestone felt lighter with him by my side.";

as.bridePage.storyTitle = "১৪ বছৰীয়া প্ৰেমৰ যাত্ৰা (পূজাৰ দৃষ্টিত)";
as.bridePage.storyText = "২০১২ চনত স্কুলৰ ক্লাছৰুমত আৰম্ভ হোৱা চিনাকিটো অতি সহজ আৰু সুন্দৰ আছিল। ১৪ বছৰীয়া এই যাত্ৰাত পূজাৰ প্ৰতিটো সপোন আৰু সুখ-দুখৰ সংগী হৈ পৰিল শুভম।";

mai.bridePage.storyTitle = "१४ वर्षक प्रेम यात्रा (पूजाक दृष्टि सँ)";
mai.bridePage.storyText = "२०१२ में विद्यालयक प्रांगण सँ शुरू भेल ई यात्रा अति सहज छल। १४ वर्षक ई सुदीर्घ डगर पर शुभम हमर संबल, हमर सुख-दुखक साथी आ प्रेमक आधार बनल रहलाह।";

en.groomPage.storyTitle = "The 14-Year Love Story (His Perspective)";
en.groomPage.storyText = "The moment I saw Pooja in 2012, my world found its center. Through 14 transformative years—school farewells, engineering challenges, product milestones—her faith in me has been my guiding light. Choosing her forever is the easiest and greatest decision of my life.";

as.groomPage.storyTitle = "১৪ বছৰীয়া প্ৰেমৰ যাত্ৰা (শুভমৰ দৃষ্টিত)";
as.groomPage.storyText = "২০১২ চনত পূজাক প্ৰথম দেখোঁতেই মই অনুভৱ কৰিছিলোঁ যে মোৰ জীৱনৰ পথ বিচাৰি পালোঁ। ১৪ বছৰীয়া এই যাত্ৰাত পূজাৰ মৰম আৰু সাহসেই মোৰ পথ প্ৰদৰ্শক হৈ আহিছে।";

mai.groomPage.storyTitle = "१४ वर्षक प्रेम यात्रा (शुभमक दृष्टि सँ)";
mai.groomPage.storyText = "२०१२ में जब पहिल बेर पूजा केँ देखलहुँ, तखनहिं मन निश्चिंत भ' गेल छल जे हमर संगी मिल गेल। १४ वर्षक ई यात्रा में पूजाक विश्वास हमर सर्वोपरि संबल रहल अछि।";

// 6. Update Audio track label for Assamese to Indradhanu (Item 9)
en.audio.assameseBtn = "Indradhanu (Assamese)";
as.audio.assameseBtn = "ইন্দ্ৰধনু (অসমীয়া)";
mai.audio.assameseBtn = "इंद्रधनु (असमिया)";

fs.writeFileSync('public/data/en.json', JSON.stringify(en, null, 2), 'utf8');
fs.writeFileSync('public/data/as.json', JSON.stringify(as, null, 2), 'utf8');
fs.writeFileSync('public/data/mai.json', JSON.stringify(mai, null, 2), 'utf8');

console.log('Successfully updated en.json, as.json, and mai.json with 15 chapters, removed dietary, updated groom caption to Tradition & Love, and 14-year journey texts!');
