import os

os.makedirs('public/assets/illustrations', exist_ok=True)

illustrations = [
    ('story_01_school_2014.svg', '2014', 'First Bell, First Glance', 'High School Classroom', '#FFE8EC', '#FFB6C1',
     '''
     <rect x="60" y="60" width="280" height="90" rx="6" fill="#2E4F4F" stroke="#0E2929" stroke-width="3"/>
     <text x="200" y="110" font-family="sans-serif" font-size="16" fill="#FFFFFF" text-anchor="middle" opacity="0.9">Classroom 10-A • 2014</text>
     <rect x="50" y="210" width="130" height="85" rx="6" fill="#C89F77"/>
     <rect x="220" y="210" width="130" height="85" rx="6" fill="#C89F77"/>
     <g transform="translate(115, 150)">
       <rect x="-15" y="35" width="30" height="55" rx="8" fill="#FFFFFF" stroke="#3D262A" stroke-width="1.5"/>
       <polygon points="-4,35 4,35 0,55" fill="#C72C35"/>
       <circle cx="0" cy="15" r="18" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.5"/>
       <path d="M-18,12 C-18,-8 18,-8 18,12 C10,0 -10,0 -18,12 Z" fill="#2C2C2C"/>
       <circle cx="-6" cy="15" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="15" r="2" fill="#2C2C2C"/>
       <path d="M-3,22 Q0,25 3,22" stroke="#2C2C2C" stroke-width="1" fill="none"/>
       <ellipse cx="-10" cy="18" rx="3.5" ry="2" fill="#FF8FA3" opacity="0.7"/>
       <ellipse cx="10" cy="18" rx="3.5" ry="2" fill="#FF8FA3" opacity="0.7"/>
     </g>
     <g transform="translate(285, 150)">
       <rect x="-15" y="35" width="30" height="55" rx="8" fill="#FFFFFF" stroke="#3D262A" stroke-width="1.5"/>
       <polygon points="-4,35 4,35 0,55" fill="#C72C35"/>
       <circle cx="0" cy="15" r="18" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.5"/>
       <path d="M-20,15 C-20,-10 20,-10 20,15 C10,5 -10,5 -20,15 Z" fill="#3E2723"/>
       <ellipse cx="-20" cy="12" rx="5" ry="10" fill="#3E2723"/>
       <ellipse cx="20" cy="12" rx="5" ry="10" fill="#3E2723"/>
       <circle cx="-6" cy="15" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="15" r="2" fill="#2C2C2C"/>
       <path d="M-3,22 Q0,26 3,22" stroke="#2C2C2C" stroke-width="1" fill="none"/>
       <ellipse cx="-10" cy="18" rx="3.5" ry="2" fill="#FF8FA3" opacity="0.7"/>
       <ellipse cx="10" cy="18" rx="3.5" ry="2" fill="#FF8FA3" opacity="0.7"/>
     </g>
     <path d="M190,170 Q200,160 210,170 Q200,185 190,170 Z" fill="#E91E63"/>
     '''),
    
    ('story_02_library_2015.svg', '2015', 'Whispers in the Library', 'Secret Notes in Physics Books', '#FFF3E0', '#FFE0B2',
     '''
     <rect x="40" y="50" width="75" height="240" rx="4" fill="#8D6E63" stroke="#5D4037" stroke-width="2"/>
     <rect x="285" y="50" width="75" height="240" rx="4" fill="#8D6E63" stroke="#5D4037" stroke-width="2"/>
     <rect x="45" y="65" width="65" height="15" fill="#E57373"/>
     <rect x="45" y="85" width="65" height="20" fill="#81C784"/>
     <rect x="45" y="110" width="65" height="16" fill="#64B5F6"/>
     <rect x="290" y="65" width="65" height="18" fill="#BA68C8"/>
     <rect x="290" y="88" width="65" height="16" fill="#4DB6AC"/>
     <ellipse cx="200" cy="260" rx="80" ry="25" fill="#D7CCC8"/>
     <g transform="translate(170, 180)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-18,-4 C-18,-20 18,-20 18,-4 Z" fill="#2C2C2C"/>
       <circle cx="-5" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="5" cy="0" r="2" fill="#2C2C2C"/>
     </g>
     <g transform="translate(230, 180)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-18,-4 C-18,-20 18,-20 18,-4 Z" fill="#3E2723"/>
       <circle cx="-5" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="5" cy="0" r="2" fill="#2C2C2C"/>
     </g>
     <rect x="188" y="210" width="24" height="16" rx="2" fill="#FFFFFF" stroke="#C8A253" stroke-width="1"/>
     <path d="M196,218 C194,215 198,213 200,216 C202,213 206,215 204,218 L200,222 Z" fill="#C72C35"/>
     '''),

    ('story_03_farewell_2016.svg', '2016', 'School Farewell & Promises', 'End of School, Beginning of Us', '#F3E5F5', '#E1BEE7',
     '''
     <circle cx="80" cy="80" r="6" fill="#FFD54F"/>
     <circle cx="320" cy="90" r="8" fill="#80CBC4"/>
     <circle cx="150" cy="60" r="5" fill="#F48FB1"/>
     <circle cx="260" cy="70" r="7" fill="#90CAF9"/>
     <g transform="translate(160, 160)">
       <rect x="-18" y="30" width="36" height="80" rx="6" fill="#1A237E"/>
       <polygon points="-4,30 4,30 0,60" fill="#FFD54F"/>
       <circle cx="0" cy="0" r="22" fill="#FFDFC4"/>
       <path d="M-22,-5 C-22,-25 22,-25 22,-5 Z" fill="#2C2C2C"/>
       <circle cx="-7" cy="0" r="2.5" fill="#2C2C2C"/>
       <circle cx="7" cy="0" r="2.5" fill="#2C2C2C"/>
       <path d="M-4,10 Q0,14 4,10" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
     </g>
     <g transform="translate(240, 160)">
       <path d="M-18,30 L18,30 L25,110 L-25,110 Z" fill="#F06292"/>
       <path d="M-18,30 L10,65 L5,110 L-20,110 Z" fill="#AD1457"/>
       <circle cx="0" cy="0" r="22" fill="#FFDFC4"/>
       <path d="M-22,-5 C-22,-25 22,-25 22,-5 Z" fill="#3E2723"/>
       <circle cx="-23" cy="6" r="3" fill="#FFD54F"/>
       <circle cx="23" cy="6" r="3" fill="#FFD54F"/>
       <circle cx="-7" cy="0" r="2.5" fill="#2C2C2C"/>
       <circle cx="7" cy="0" r="2.5" fill="#2C2C2C"/>
       <path d="M-4,10 Q0,15 4,10" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
     </g>
     <ellipse cx="200" cy="200" rx="10" ry="7" fill="#FFDFC4"/>
     <path d="M195,190 Q200,185 205,190 Q200,205 195,190 Z" fill="#E91E63"/>
     '''),

    ('story_04_metro_2017.svg', '2017', 'Shared Earphones & Metro Rides', 'Delhi Metro Yellow Line', '#E8F5E9', '#C8E6C9',
     '''
     <rect x="40" y="60" width="320" height="130" rx="12" fill="#E0F7FA" stroke="#78909C" stroke-width="2.5"/>
     <rect x="30" y="200" width="340" height="90" rx="8" fill="#B0BEC5"/>
     <rect x="40" y="50" width="320" height="10" fill="#FBC02D"/>
     <g transform="translate(160, 150)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#2C2C2C"/>
       <circle cx="-6" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2" fill="#2C2C2C"/>
       <rect x="-15" y="20" width="30" height="55" rx="6" fill="#3F51B5"/>
     </g>
     <g transform="translate(235, 150)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#3E2723"/>
       <circle cx="-6" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2" fill="#2C2C2C"/>
       <rect x="-15" y="20" width="30" height="55" rx="6" fill="#EC407A"/>
     </g>
     <path d="M145,155 Q195,210 250,155" stroke="#FFFFFF" stroke-width="2.5" fill="none"/>
     <rect x="188" y="220" width="24" height="40" rx="4" fill="#263238"/>
     <text x="200" y="105" font-family="sans-serif" font-size="16" fill="#C2185B" text-anchor="middle">♫</text>
     '''),

    ('story_05_cultures_2018.svg', '2018', 'Assam & Mithila Flavors', 'Pitha, Thekua & Traditions', '#FFF8E1', '#FFECB3',
     '''
     <ellipse cx="200" cy="235" rx="130" ry="45" fill="#FFFDE7" stroke="#C8A253" stroke-width="2"/>
     <rect x="110" y="220" width="180" height="28" fill="#FFFFFF" stroke="#C72C35" stroke-width="1.5"/>
     <line x1="120" y1="220" x2="120" y2="248" stroke="#C72C35" stroke-width="2"/>
     <line x1="280" y1="220" x2="280" y2="248" stroke="#C72C35" stroke-width="2"/>
     <ellipse cx="160" cy="235" rx="22" ry="10" fill="#FFCC80"/>
     <ellipse cx="240" cy="235" rx="22" ry="10" fill="#FFE082"/>
     <g transform="translate(145, 130)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#2C2C2C"/>
       <circle cx="-6" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2" fill="#2C2C2C"/>
       <path d="M-3,8 Q0,12 3,8" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
     </g>
     <g transform="translate(255, 130)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#3E2723"/>
       <circle cx="-6" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2" fill="#2C2C2C"/>
       <path d="M-3,8 Q0,12 3,8" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
       <circle cx="20" cy="-6" r="4.5" fill="#F48FB1"/>
     </g>
     <text x="160" y="205" font-size="12" fill="#8D6E63" text-anchor="middle">Til Pitha</text>
     <text x="240" y="205" font-size="12" fill="#8D6E63" text-anchor="middle">Thekua</text>
     '''),

    ('story_06_monsoon_2019.svg', '2019', 'Monsoon Rain & Masala Chai', 'Under One Shared Umbrella', '#E1F5FE', '#B3E5FC',
     '''
     <g stroke="#81D4FA" stroke-width="2" stroke-linecap="round">
       <line x1="60" y1="40" x2="50" y2="65"/>
       <line x1="120" y1="50" x2="110" y2="75"/>
       <line x1="280" y1="45" x2="270" y2="70"/>
       <line x1="340" y1="60" x2="330" y2="85"/>
     </g>
     <path d="M90,130 C90,40 310,40 310,130 Z" fill="#F8BBD0" stroke="#EC407A" stroke-width="3"/>
     <line x1="200" y1="40" x2="200" y2="220" stroke="#8D6E63" stroke-width="4"/>
     <path d="M200,220 C200,230 185,230 185,220" stroke="#8D6E63" stroke-width="4" fill="none"/>
     <g transform="translate(165, 170)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#2C2C2C"/>
       <circle cx="-6" cy="0" r="2.5" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2.5" fill="#2C2C2C"/>
       <rect x="-14" y="20" width="28" height="65" rx="6" fill="#5C6BC0"/>
     </g>
     <g transform="translate(235, 170)">
       <circle cx="0" cy="0" r="20" fill="#FFDFC4"/>
       <path d="M-20,-5 C-20,-22 20,-22 20,-5 Z" fill="#3E2723"/>
       <circle cx="-6" cy="0" r="2.5" fill="#2C2C2C"/>
       <circle cx="6" cy="0" r="2.5" fill="#2C2C2C"/>
       <rect x="-14" y="20" width="28" height="65" rx="6" fill="#AB47BC"/>
     </g>
     <g transform="translate(200, 235)">
       <polygon points="-10,0 -7,14 7,14 10,0" fill="#BCAAA4"/>
       <path d="M-4,-3 Q0,-8 4,-3" stroke="#B0BEC5" stroke-width="1.5" fill="none"/>
     </g>
     '''),

    ('story_07_videocalls_2021.svg', '2021', 'Late Night Video Calls', 'Across Miles, Never Apart', '#EDE7F6', '#D1C4E9',
     '''
     <rect x="50" y="70" width="135" height="160" rx="8" fill="#FFFFFF" stroke="#9575CD" stroke-width="2.5"/>
     <rect x="215" y="70" width="135" height="160" rx="8" fill="#FFFFFF" stroke="#9575CD" stroke-width="2.5"/>
     <rect x="60" y="80" width="115" height="115" rx="6" fill="#263238"/>
     <rect x="225" y="80" width="115" height="115" rx="6" fill="#263238"/>
     <g transform="translate(118, 140)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-18,-5 C-18,-20 18,-20 18,-5 Z" fill="#2C2C2C"/>
       <circle cx="-5" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="5" cy="0" r="2" fill="#2C2C2C"/>
       <path d="M-3,7 Q0,11 3,7" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
     </g>
     <g transform="translate(282, 140)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-18,-5 C-18,-20 18,-20 18,-5 Z" fill="#3E2723"/>
       <circle cx="-5" cy="0" r="2" fill="#2C2C2C"/>
       <circle cx="5" cy="0" r="2" fill="#2C2C2C"/>
       <path d="M-3,7 Q0,11 3,7" stroke="#2C2C2C" stroke-width="1.5" fill="none"/>
     </g>
     <g fill="#E91E63">
       <circle cx="200" cy="120" r="5"/>
       <circle cx="200" cy="148" r="8"/>
       <circle cx="200" cy="175" r="5"/>
     </g>
     <text x="200" y="260" font-size="12" font-family="sans-serif" fill="#5E35B1" text-anchor="middle">Distance Means So Little</text>
     '''),

    ('story_08_varanasi_2023.svg', '2023', 'The Ghats of Varanasi', 'Rowing at Sunrise in Royal Blue Saree', '#E0F7FA', '#80DEEA',
     '''
     <rect x="40" y="50" width="320" height="120" fill="#FFE0B2" rx="8"/>
     <polygon points="80,120 90,80 100,120" fill="#D7CCC8"/>
     <polygon points="120,120 135,70 150,120" fill="#BCAAA4"/>
     <polygon points="280,120 295,75 310,120" fill="#D7CCC8"/>
     <path d="M40,160 Q120,150 200,160 T360,160 L360,290 L40,290 Z" fill="#4DD0E1" opacity="0.8"/>
     <path d="M80,230 C120,260 280,260 320,230 L310,205 C270,220 130,220 90,205 Z" fill="#8D6E63" stroke="#4E342E" stroke-width="2"/>
     <g transform="translate(200, 165)">
       <circle cx="0" cy="-15" r="18" fill="#FFDFC4"/>
       <path d="M-18,-20 C-18,-35 18,-35 18,-20 C22,5 15,15 12,25 C-5,10 -15,5 -18,-20 Z" fill="#212121"/>
       <circle cx="-16" cy="-12" r="2.5" fill="#FFD54F"/>
       <circle cx="16" cy="-12" r="2.5" fill="#FFD54F"/>
       <circle cx="0" cy="-18" r="1.5" fill="#C62828"/>
       <path d="M-18,2 C-10,35 10,35 18,2 L14,48 L-14,48 Z" fill="#1565C0"/>
       <path d="M-14,8 L10,30 L8,48 L-12,24 Z" fill="#FFD54F"/>
       <line x1="-45" y1="40" x2="20" y2="15" stroke="#D7CCC8" stroke-width="4"/>
     </g>
     <ellipse cx="110" cy="265" rx="12" ry="6" fill="#F48FB1"/>
     <ellipse cx="290" cy="270" rx="14" ry="7" fill="#F48FB1"/>
     '''),

    ('story_09_families_2024.svg', '2024', 'When Two Families Became One', 'Gamosa Meets Paag', '#FBE9E7', '#FFCCBC',
     '''
     <rect x="40" y="50" width="320" height="230" rx="10" fill="#FFF8E1" stroke="#FFB74D" stroke-width="2"/>
     <path d="M50,85 Q200,60 350,85" stroke="#C72C35" stroke-width="3" fill="none"/>
     <circle cx="100" cy="80" r="5" fill="#FFEB3B"/>
     <circle cx="200" cy="72" r="7" fill="#E91E63"/>
     <circle cx="300" cy="80" r="5" fill="#FFEB3B"/>
     <g transform="translate(120, 160)">
       <circle cx="0" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M-17,-8 C-17,-22 17,-22 17,-8 Z" fill="#D32F2F"/>
       <rect x="-13" y="17" width="26" height="55" rx="6" fill="#FFE082"/>
     </g>
     <g transform="translate(200, 145)">
       <circle cx="-15" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M-32,-8 C-32,-24 0,-24 0,-8 Z" fill="#2C2C2C"/>
       <circle cx="15" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M0,-8 C0,-24 32,-24 32,-8 Z" fill="#3E2723"/>
       <ellipse cx="0" cy="22" rx="26" ry="10" fill="#FFFFFF" stroke="#C72C35" stroke-width="1.5"/>
     </g>
     <g transform="translate(280, 160)">
       <circle cx="0" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M-17,-8 C-17,-22 17,-22 17,-8 Z" fill="#4E342E"/>
       <rect x="-13" y="17" width="26" height="55" rx="6" fill="#FFCDD2"/>
     </g>
     <text x="200" y="250" font-size="12" font-family="sans-serif" font-weight="bold" fill="#C72C35" text-anchor="middle">Thakur &amp; Haloi Parivar</text>
     '''),

    ('story_10_proposal_2025.svg', '2025', 'The Proposal Under The Stars', 'Fairy Lights, A Ring & Forever', '#ECEFF1', '#CFD8DC',
     '''
     <rect x="40" y="50" width="320" height="230" rx="10" fill="#1A237E"/>
     <circle cx="80" cy="75" r="1.5" fill="#FFFFFF"/>
     <circle cx="120" cy="65" r="2" fill="#FFE082"/>
     <circle cx="280" cy="70" r="2" fill="#FFFFFF"/>
     <circle cx="320" cy="90" r="1.5" fill="#FFE082"/>
     <path d="M40,85 Q120,120 200,95 Q280,120 360,85" stroke="#FFE082" stroke-width="1.5" fill="none"/>
     <circle cx="100" cy="105" r="3.5" fill="#FFF59D"/>
     <circle cx="160" cy="105" r="3.5" fill="#FFF59D"/>
     <circle cx="240" cy="105" r="3.5" fill="#FFF59D"/>
     <circle cx="300" cy="105" r="3.5" fill="#FFF59D"/>
     <g transform="translate(150, 170)">
       <circle cx="0" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M-17,-5 C-17,-20 17,-20 17,-5 Z" fill="#2C2C2C"/>
       <polygon points="-12,17 12,17 18,55 -5,55" fill="#283593"/>
       <rect x="16" y="25" width="14" height="10" rx="2" fill="#B71C1C"/>
       <circle cx="23" cy="22" r="3" fill="#E0F7FA" stroke="#FFD54F" stroke-width="1"/>
     </g>
     <g transform="translate(250, 150)">
       <circle cx="0" cy="0" r="17" fill="#FFDFC4"/>
       <path d="M-17,-5 C-17,-22 17,-22 17,-5 Z" fill="#3E2723"/>
       <circle cx="-5" cy="2" r="2" fill="#2C2C2C"/>
       <circle cx="5" cy="2" r="2" fill="#2C2C2C"/>
       <ellipse cx="-9" cy="6" rx="3.5" ry="2" fill="#FF8FA3"/>
       <ellipse cx="9" cy="6" rx="3.5" ry="2" fill="#FF8FA3"/>
       <path d="M-14,17 L14,17 L22,85 L-22,85 Z" fill="#F8BBD0"/>
     </g>
     <path d="M172,192 L182,192 M177,187 L177,197" stroke="#FFD54F" stroke-width="2"/>
     <text x="200" y="260" font-size="13" font-weight="bold" fill="#FFD54F" text-anchor="middle">She Said YES! 💍</text>
     '''),

    ('story_11_wedding_2026.svg', '2026', '#pooshu Forever', 'The Sacred Mandap & Eternal Vows', '#FCE4EC', '#F8BBD0',
     '''
     <rect x="60" y="60" width="18" height="210" fill="#C8A253" rx="3"/>
     <rect x="322" y="60" width="18" height="210" fill="#C8A253" rx="3"/>
     <path d="M60,80 Q200,45 340,80" stroke="#C72C35" stroke-width="5" fill="none"/>
     <circle cx="120" cy="70" r="5" fill="#FFB300"/>
     <circle cx="200" cy="62" r="7" fill="#E91E63"/>
     <circle cx="280" cy="70" r="5" fill="#FFB300"/>
     <polygon points="185,250 215,250 210,268 190,268" fill="#B0BEC5" stroke="#78909C" stroke-width="1.5"/>
     <path d="M195,250 Q200,230 205,250 Q200,240 195,250 Z" fill="#FF5722"/>
     <g transform="translate(150, 150)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-17,-7 C-17,-28 17,-28 17,-7 Z" fill="#C62828" stroke="#FFD54F" stroke-width="1.5"/>
       <circle cx="0" cy="-16" r="2.5" fill="#FFD54F"/>
       <rect x="-15" y="18" width="30" height="70" rx="5" fill="#FFF8E1" stroke="#C8A253" stroke-width="1.2"/>
       <path d="M-13,18 Q0,40 13,18 L15,75 L7,75 L-5,32 L-13,75 Z" fill="#F8BBD0"/>
       <path d="M-13,24 Q0,50 13,24" stroke="#C72C35" stroke-width="2.5" fill="none"/>
     </g>
     <g transform="translate(250, 150)">
       <circle cx="0" cy="0" r="18" fill="#FFDFC4"/>
       <path d="M-18,-5 C-18,-24 18,-24 18,-5 Z" fill="#2C2C2C"/>
       <ellipse cx="20" cy="-2" rx="5" ry="10" fill="#F48FB1"/>
       <path d="M-16,18 L16,18 L24,88 L-24,88 Z" fill="#F5E6CC" stroke="#C8A253" stroke-width="1.2"/>
       <line x1="-20" y1="80" x2="20" y2="80" stroke="#C72C35" stroke-width="2.5"/>
       <path d="M-13,24 Q0,50 13,24" stroke="#C72C35" stroke-width="2.5" fill="none"/>
     </g>
     <path d="M162,198 Q200,218 238,198" stroke="#E91E63" stroke-width="2" fill="none"/>
     <text x="200" y="280" font-family="serif" font-size="13" font-weight="bold" fill="#C72C35" text-anchor="middle">December 02, 2026</text>
     ''')
]

for filename, year, title, subtitle, bg1, bg2, content in illustrations:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 320" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad_{year}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg1}"/>
      <stop offset="100%" stop-color="{bg2}"/>
    </linearGradient>
  </defs>
  <rect width="400" height="320" rx="16" fill="url(#bgGrad_{year})"/>
  <rect x="12" y="12" width="376" height="296" rx="12" fill="none" stroke="#C8A253" stroke-width="1.5" stroke-dasharray="6, 4" opacity="0.6"/>
  <rect x="25" y="22" width="65" height="26" rx="13" fill="#FFFFFF" stroke="#C8A253" stroke-width="1"/>
  <text x="57" y="39" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700" fill="#3D262A" text-anchor="middle">{year}</text>
  {content}
</svg>'''
    filepath = os.path.join('public/assets/illustrations', filename)
    with open(filepath, 'w') as f:
        f.write(svg)
    print(f'Created {filepath}')
