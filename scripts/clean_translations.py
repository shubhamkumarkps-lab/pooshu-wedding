import json

# EN
with open('public/data/en.json', 'r', encoding='utf-8') as f:
    en = json.load(f)

en['nav']['wedding'] = 'The Wedding'
en['nav']['bride'] = 'Know the Bride'
en['nav']['groom'] = 'Know the Groom'
en['nav']['story'] = 'Our Story'
en['nav']['events'] = 'Events'
en['nav']['rsvp'] = 'RSVP'

en['bridePage']['peerBtn'] = "Explore Shubham's Story"
en['groomPage']['peerBtn'] = "Explore Pooja's Story"

en['audio']['maithiliBtn'] = 'Maithili Song'
en['audio']['assameseBtn'] = 'Assamese Song'

with open('public/data/en.json', 'w', encoding='utf-8') as f:
    json.dump(en, f, ensure_ascii=False, indent=2)

# AS
with open('public/data/as.json', 'r', encoding='utf-8') as f:
    as_data = json.load(f)

as_data['nav']['wedding'] = 'শুভ বিবাহ'
as_data['nav']['bride'] = 'কইনাক জানক'
as_data['nav']['groom'] = 'দৰাক জানক'
as_data['nav']['story'] = 'আমাৰ কাহিনী'
as_data['nav']['events'] = 'কাৰ্যসূচী'
as_data['nav']['rsvp'] = 'উপস্থিতি'

as_data['bridePage']['peerBtn'] = 'শুভমৰ কাহিনী জানক'
as_data['groomPage']['peerBtn'] = 'পূজাৰ কাহিনী জানক'

as_data['audio']['maithiliBtn'] = 'মৈথিলী গান'
as_data['audio']['assameseBtn'] = 'অসমীয়া গান'

with open('public/data/as.json', 'w', encoding='utf-8') as f:
    json.dump(as_data, f, ensure_ascii=False, indent=2)

# MAI
with open('public/data/mai.json', 'r', encoding='utf-8') as f:
    mai = json.load(f)

mai['nav']['wedding'] = 'शुभ विवाह'
mai['nav']['bride'] = 'कन्या परिचय'
mai['nav']['groom'] = 'वर परिचय'
mai['nav']['story'] = 'हमर यात्रा'
mai['nav']['events'] = 'कार्यक्रम'
mai['nav']['rsvp'] = 'स्वीकृति'

mai['bridePage']['peerBtn'] = 'शुभमक परिचय देखू'
mai['groomPage']['peerBtn'] = 'पूजाक परिचय देखू'

mai['audio']['maithiliBtn'] = 'मैथिली गीत'
mai['audio']['assameseBtn'] = 'असमिया गीत'

with open('public/data/mai.json', 'w', encoding='utf-8') as f:
    json.dump(mai, f, ensure_ascii=False, indent=2)

print('Cleaned button emojis from all 3 JSON files!')
