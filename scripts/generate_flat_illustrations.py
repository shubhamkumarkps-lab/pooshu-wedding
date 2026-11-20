import os

OUTPUT_DIR = 'illustrations_flat'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Hero Couple Flat Illustration (couple_pooshu_flat.svg)
couple_pooshu_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <defs>
    <linearGradient id="pastelSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFDF9"/>
      <stop offset="60%" stop-color="#FDF1F4"/>
      <stop offset="100%" stop-color="#F6E7EB"/>
    </linearGradient>
    <linearGradient id="goldFoil" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ECC880"/>
      <stop offset="45%" stop-color="#FDF4D4"/>
      <stop offset="80%" stop-color="#C8A253"/>
      <stop offset="100%" stop-color="#99732B"/>
    </linearGradient>
    <linearGradient id="paagGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D32F2F"/>
      <stop offset="60%" stop-color="#B71C1C"/>
      <stop offset="100%" stop-color="#7F0000"/>
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Base -->
  <rect width="600" height="500" rx="20" fill="url(#pastelSky)"/>

  <!-- Ornate Arch Halo in Background -->
  <path d="M 120,480 L 120,240 C 120,130 190,70 300,70 C 410,70 480,130 480,240 L 480,480 Z" 
        fill="#FAF3E8" stroke="url(#goldFoil)" stroke-width="2.5" opacity="0.85"/>
  <path d="M 140,480 L 140,245 C 140,148 200,90 300,90 C 400,90 460,148 460,245 L 460,480" 
        fill="none" stroke="#C8A253" stroke-width="1.2" stroke-dasharray="5, 4" opacity="0.6"/>

  <!-- Hanging Floral Garlands (Blush roses and Kopou orchids) -->
  <g id="floral-garland">
    <path d="M 120,160 Q 210,120 300,160 Q 390,120 480,160" stroke="#7BA896" stroke-width="3" fill="none"/>
    <circle cx="210" cy="138" r="9" fill="#F48FB1"/>
    <circle cx="210" cy="138" r="4" fill="#C2185B"/>
    <circle cx="390" cy="138" r="9" fill="#F48FB1"/>
    <circle cx="390" cy="138" r="4" fill="#C2185B"/>
    <circle cx="300" cy="160" r="11" fill="#F8BBD0"/>
    <circle cx="300" cy="160" r="5" fill="#D81B60"/>
    <!-- Foxtail Orchids hanging -->
    <path d="M 170,145 Q 165,180 160,205" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
    <circle cx="163" cy="170" r="5" fill="#E1BEE7"/>
    <circle cx="160" cy="188" r="4" fill="#CE93D8"/>
    <circle cx="158" cy="202" r="3" fill="#BA68C8"/>
    <path d="M 430,145 Q 435,180 440,205" stroke="#4CAF50" stroke-width="1.5" fill="none"/>
    <circle cx="437" cy="170" r="5" fill="#E1BEE7"/>
    <circle cx="440" cy="188" r="4" fill="#CE93D8"/>
    <circle cx="442" cy="202" r="3" fill="#BA68C8"/>
  </g>

  <!-- ================= GROOM (Shubham) ================= -->
  <g id="groom" transform="translate(225, 200)">
    <!-- Sherwani Torso -->
    <path d="M -50,110 L -40,300 L 40,300 L 50,110 Z" fill="#FDFBF9" stroke="#3D262A" stroke-width="1.5"/>
    <rect x="-42" y="110" width="84" height="190" fill="#FFFDF8"/>
    
    <!-- Zari Neck & Placket -->
    <rect x="-8" y="110" width="16" height="190" fill="url(#goldFoil)"/>
    <line x1="0" y1="110" x2="0" y2="300" stroke="#99732B" stroke-width="1.5"/>
    <circle cx="0" cy="130" r="2.5" fill="#C72C35"/>
    <circle cx="0" cy="155" r="2.5" fill="#C72C35"/>
    <circle cx="0" cy="180" r="2.5" fill="#C72C35"/>
    <circle cx="0" cy="205" r="2.5" fill="#C72C35"/>

    <!-- Gold Embroidered Dupatta Stole draped across shoulder -->
    <path d="M -45,110 Q -10,180 -30,300 L -48,300 L -50,120 Z" fill="#FCE4EC" stroke="#C8A253" stroke-width="1.2"/>
    <line x1="-36" y1="130" x2="-25" y2="290" stroke="#C8A253" stroke-width="2"/>

    <!-- Neck & Face -->
    <rect x="-14" y="80" width="28" height="35" rx="4" fill="#FFDFC4"/>
    <ellipse cx="0" cy="65" rx="34" ry="40" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.5"/>

    <!-- Facial Features -->
    <ellipse cx="-13" cy="62" rx="4" ry="4.5" fill="#2C2C2C"/>
    <ellipse cx="13" cy="62" rx="4" ry="4.5" fill="#2C2C2C"/>
    <circle cx="-11" cy="60" r="1.5" fill="#FFFFFF"/>
    <circle cx="15" cy="60" r="1.5" fill="#FFFFFF"/>
    <!-- Subtle Eyebrows -->
    <path d="M -20,52 Q -12,48 -5,52" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M 5,52 Q 12,48 20,52" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Warm Gentle Smile -->
    <path d="M -7,82 Q 0,89 7,82" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Rosy Cheek Blushes -->
    <ellipse cx="-20" cy="74" rx="7" ry="4" fill="#FF8FA3" opacity="0.6"/>
    <ellipse cx="20" cy="74" rx="7" ry="4" fill="#FF8FA3" opacity="0.6"/>

    <!-- Groom's Maithili Paag (Traditional Headgear) -->
    <!-- Paag Base -->
    <path d="M -38,42 C -42,10 -25,-18 0,-22 C 25,-18 42,10 38,42 C 18,48 -18,48 -38,42 Z" 
          fill="url(#paagGradient)" stroke="#5B0E12" stroke-width="2"/>
    <!-- Central Crest Fold -->
    <path d="M -22,-5 C -8,-28 8,-28 22,-5 C 8,-12 -8,-12 -22,-5 Z" fill="#FFE082" stroke="#B78103" stroke-width="1.5"/>
    <path d="M -34,32 C -15,40 15,40 34,32" stroke="#FFD54F" stroke-width="2.5" fill="none"/>
    <!-- Brooch / Kalangi with feather -->
    <circle cx="0" cy="10" r="7" fill="#C72C35" stroke="#FFD54F" stroke-width="2"/>
    <circle cx="0" cy="10" r="3" fill="#FFFFFF"/>
    <path d="M 0,-22 Q -8,-45 -18,-55 Q 6,-45 2,-24" fill="#FFF8E1" stroke="#FFA000" stroke-width="1.2"/>
  </g>

  <!-- ================= BRIDE (Pooja) ================= -->
  <g id="bride" transform="translate(375, 205)">
    <!-- Assamese Muga Silk Mekhela Chador Torso -->
    <path d="M -45,110 L -40,300 L 45,300 L 45,110 Z" fill="#FAF1E0" stroke="#3D262A" stroke-width="1.5"/>
    <rect x="-40" y="110" width="82" height="190" fill="#FAF1E0"/>

    <!-- Red Kingkhap Geometrical Border on Saree Drapes -->
    <path d="M -40,110 Q 0,180 35,300 L 45,300 L -30,110 Z" fill="#F5DFB8" stroke="#C72C35" stroke-width="1.5"/>
    <line x1="-25" y1="125" x2="35" y2="280" stroke="#C72C35" stroke-width="3" stroke-dasharray="4, 3"/>
    
    <!-- Gold Blouse & Chunni -->
    <path d="M -30,110 L 30,110 L 25,170 L -25,170 Z" fill="#E8B86D" stroke="#3D262A" stroke-width="1.2"/>

    <!-- Neck & Traditional Assamese Lokaparo / Dholbiri Necklace -->
    <rect x="-12" y="80" width="24" height="35" rx="4" fill="#FFDFC4"/>
    <ellipse cx="0" cy="115" rx="14" ry="7" fill="#C8A253"/>
    <circle cx="0" cy="117" r="3.5" fill="#C72C35"/>

    <!-- Face -->
    <ellipse cx="0" cy="65" rx="32" ry="38" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.5"/>

    <!-- Long Dark Hair flowing with Kopou Orchid Flowers -->
    <path d="M -35,50 C -40,10 -30,-5 0,-8 C 30,-5 40,10 35,50 C 44,70 42,120 38,150 C 30,100 24,80 20,70 C 0,55 -20,55 -35,50 Z" 
          fill="#212121"/>
    <!-- Left hair drape -->
    <path d="M -35,50 C -42,80 -38,125 -32,150 C -28,110 -28,80 -25,70 Z" fill="#212121"/>

    <!-- Foxtail Orchid Garland in Hair (Kopou Phool) -->
    <g transform="translate(26, 25)">
      <circle cx="0" cy="0" r="6" fill="#F48FB1"/>
      <circle cx="0" cy="0" r="2.5" fill="#880E4F"/>
      <circle cx="6" cy="10" r="5.5" fill="#F48FB1"/>
      <circle cx="6" cy="10" r="2" fill="#880E4F"/>
      <circle cx="8" cy="22" r="5" fill="#F48FB1"/>
      <circle cx="8" cy="22" r="2" fill="#880E4F"/>
    </g>

    <!-- Traditional Gold Jhumkas -->
    <circle cx="-32" cy="72" r="4.5" fill="url(#goldFoil)"/>
    <circle cx="32" cy="72" r="4.5" fill="url(#goldFoil)"/>

    <!-- Red Bindi on Forehead -->
    <circle cx="0" cy="48" r="3" fill="#C72C35"/>

    <!-- Facial Features -->
    <ellipse cx="-12" cy="62" rx="4" ry="4.5" fill="#2C2C2C"/>
    <ellipse cx="12" cy="62" rx="4" ry="4.5" fill="#2C2C2C"/>
    <circle cx="-10" cy="60" r="1.5" fill="#FFFFFF"/>
    <circle cx="14" cy="60" r="1.5" fill="#FFFFFF"/>
    <!-- Eyelashes -->
    <path d="M -16,56 Q -12,52 -8,56" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <path d="M 8,56 Q 12,52 16,56" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Sweet Smile -->
    <path d="M -6,82 Q 0,89 6,82" stroke="#2C2C2C" stroke-width="2" fill="none" stroke-linecap="round"/>
    <!-- Cheeks -->
    <ellipse cx="-18" cy="74" rx="7" ry="4" fill="#FF8FA3" opacity="0.6"/>
    <ellipse cx="18" cy="74" rx="7" ry="4" fill="#FF8FA3" opacity="0.6"/>
  </g>

  <!-- Hands Holding in Center -->
  <g id="holding-hands" transform="translate(300, 375)">
    <circle cx="-12" cy="0" r="12" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.2"/>
    <circle cx="12" cy="0" r="11" fill="#FFDFC4" stroke="#3D262A" stroke-width="1.2"/>
    <!-- Red Bridal Bangles (Chuda & Muthi) -->
    <ellipse cx="16" cy="-4" rx="3" ry="8" fill="#C72C35"/>
    <ellipse cx="20" cy="-5" rx="3" ry="8" fill="#FFD54F"/>
    <!-- Floating Gold Heart -->
    <path d="M 0,-15 C -8,-25 -22,-12 0,6 C 22,-12 8,-25 0,-15 Z" fill="#C72C35" stroke="#C8A253" stroke-width="1.5"/>
  </g>

  <!-- Bottom Script Banner -->
  <rect x="150" y="445" width="300" height="38" rx="19" fill="#FFFDFB" stroke="url(#goldFoil)" stroke-width="1.5"/>
  <text x="300" y="469" font-family="'Raleway', 'Cinzel Decorative', serif" font-size="14" font-weight="700" 
        fill="#3D262A" text-anchor="middle" letter-spacing="3">
    POOJA &amp; SHUBHAM • #POOSHU
  </text>
</svg>'''

# 2. Assamese Brass Xorai with Kopou Orchids (assamese_xorai_kopou.svg)
assamese_xorai_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="brassGold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF2B2"/>
      <stop offset="35%" stop-color="#E5C158"/>
      <stop offset="70%" stop-color="#C29731"/>
      <stop offset="100%" stop-color="#8C6614"/>
    </linearGradient>
    <linearGradient id="orchidGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F8BBD0"/>
      <stop offset="50%" stop-color="#E91E63"/>
      <stop offset="100%" stop-color="#880E4F"/>
    </linearGradient>
  </defs>

  <rect width="500" height="500" rx="20" fill="#FAF7F2"/>
  <circle cx="250" cy="250" r="210" fill="#FFFDFB" stroke="#E0D5C1" stroke-width="2"/>

  <!-- Phulam Gamosa Cloth Beneath -->
  <g id="gamosa-cloth" transform="translate(100, 260)">
    <path d="M 0,60 L 300,60 L 320,180 L -20,180 Z" fill="#FFFFFF" stroke="#C72C35" stroke-width="2"/>
    <!-- Red woven geometric rows -->
    <line x1="-15" y1="80" x2="315" y2="80" stroke="#C72C35" stroke-width="3"/>
    <line x1="-18" y1="92" x2="318" y2="92" stroke="#C72C35" stroke-width="2"/>
    <path d="M 0,115 L 20,95 L 40,115 L 60,95 L 80,115 L 100,95 L 120,115 L 140,95 L 160,115 L 180,95 L 200,115 L 220,95 L 240,115 L 260,95 L 280,115 L 300,95" stroke="#C72C35" stroke-width="3.5" fill="none"/>
    <line x1="-20" y1="165" x2="320" y2="165" stroke="#C72C35" stroke-width="4"/>
  </g>

  <!-- Brass Xorai (Standing Vessel) -->
  <g id="xorai-vessel" transform="translate(250, 150)">
    <!-- Base Plate -->
    <ellipse cx="0" cy="200" rx="80" ry="22" fill="url(#brassGold)" stroke="#5D4037" stroke-width="2"/>
    <ellipse cx="0" cy="195" rx="68" ry="16" fill="#FFF9C4"/>
    <!-- Curved Fluted Pedestal Stem -->
    <path d="M -16,195 C -12,140 -25,90 -18,60 L 18,60 C 25,90 12,140 16,195 Z" fill="url(#brassGold)" stroke="#5D4037" stroke-width="2"/>
    <ellipse cx="0" cy="120" rx="28" ry="8" fill="url(#brassGold)" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Shallow Bowl Dish -->
    <ellipse cx="0" cy="55" rx="110" ry="30" fill="url(#brassGold)" stroke="#5D4037" stroke-width="2"/>
    <ellipse cx="0" cy="50" rx="98" ry="24" fill="#FFF59D"/>

    <!-- Tamul-Paan Offering (Betel Leaves & Areca Nuts) -->
    <path d="M -40,42 C -20,20 20,20 40,42 C 20,62 -20,62 -40,42 Z" fill="#43A047" stroke="#2E7D32" stroke-width="1.5"/>
    <circle cx="-12" cy="42" r="9" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>
    <circle cx="12" cy="40" r="9" fill="#8D6E63" stroke="#4E342E" stroke-width="1.5"/>

    <!-- Tiered Conical Lid of Xorai -->
    <path d="M -75,45 C -60,0 0,-60 0,-60 C 0,-60 60,0 75,45 Z" fill="url(#brassGold)" stroke="#5D4037" stroke-width="2"/>
    <ellipse cx="0" cy="45" rx="75" ry="16" fill="url(#brassGold)" stroke="#5D4037" stroke-width="1.5"/>
    <!-- Finial Crown Needle -->
    <polygon points="0,-95 -7,-60 7,-60" fill="url(#brassGold)" stroke="#5D4037" stroke-width="1.5"/>
    <circle cx="0" cy="-96" r="6" fill="#FFD54F" stroke="#5D4037" stroke-width="1.5"/>
  </g>

  <!-- Cascading Kopou Phool (Foxtail Orchid Sprays on Sides) -->
  <g id="kopou-left" transform="translate(100, 120)">
    <path d="M 0,0 Q 30,80 15,160 Q 5,200 15,240" stroke="#388E3C" stroke-width="3" fill="none"/>
    <!-- Delicate Pink Orchid Florets -->
    <g fill="#F48FB1" stroke="#AD1457" stroke-width="1">
      <circle cx="8" cy="30" r="9"/>
      <circle cx="22" cy="55" r="10"/>
      <circle cx="12" cy="85" r="11"/>
      <circle cx="24" cy="115" r="11"/>
      <circle cx="15" cy="145" r="10"/>
      <circle cx="22" cy="175" r="9"/>
      <circle cx="14" cy="205" r="8"/>
      <circle cx="16" cy="230" r="6"/>
    </g>
    <!-- Dark Magenta Orchid Lips -->
    <g fill="#880E4F">
      <circle cx="8" cy="31" r="3"/>
      <circle cx="22" cy="56" r="3.5"/>
      <circle cx="12" cy="86" r="3.5"/>
      <circle cx="24" cy="116" r="3.5"/>
      <circle cx="15" cy="146" r="3"/>
      <circle cx="22" cy="176" r="2.5"/>
    </g>
  </g>

  <g id="kopou-right" transform="translate(400, 120) scale(-1, 1)">
    <path d="M 0,0 Q 30,80 15,160 Q 5,200 15,240" stroke="#388E3C" stroke-width="3" fill="none"/>
    <g fill="#F48FB1" stroke="#AD1457" stroke-width="1">
      <circle cx="8" cy="30" r="9"/>
      <circle cx="22" cy="55" r="10"/>
      <circle cx="12" cy="85" r="11"/>
      <circle cx="24" cy="115" r="11"/>
      <circle cx="15" cy="145" r="10"/>
      <circle cx="22" cy="175" r="9"/>
      <circle cx="14" cy="205" r="8"/>
      <circle cx="16" cy="230" r="6"/>
    </g>
    <g fill="#880E4F">
      <circle cx="8" cy="31" r="3"/>
      <circle cx="22" cy="56" r="3.5"/>
      <circle cx="12" cy="86" r="3.5"/>
      <circle cx="24" cy="116" r="3.5"/>
      <circle cx="15" cy="146" r="3"/>
      <circle cx="22" cy="176" r="2.5"/>
    </g>
  </g>

  <!-- Title Banner -->
  <text x="250" y="475" font-family="'Raleway', sans-serif" font-size="14" font-weight="700" 
        fill="#6E4750" text-anchor="middle" letter-spacing="3">
    ASSAMESE XORAI &amp; KOPOU PHOOL
  </text>
</svg>'''

# 3. Maithili Peacocks with Sacred Lotus (maithili_peacock_lotus.svg)
maithili_peacock_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <linearGradient id="mithilaSky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FDFBF9"/>
      <stop offset="100%" stop-color="#F9EFEB"/>
    </linearGradient>
    <linearGradient id="peacockBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1B6B76"/>
      <stop offset="100%" stop-color="#0E4249"/>
    </linearGradient>
  </defs>

  <rect width="500" height="500" rx="20" fill="url(#mithilaSky)"/>

  <!-- Ornate Madhubani Double Border -->
  <rect x="20" y="20" width="460" height="460" rx="14" fill="none" stroke="#C8A253" stroke-width="2"/>
  <rect x="28" y="28" width="444" height="444" rx="10" fill="none" stroke="#C72C35" stroke-width="1.5" stroke-dasharray="6, 4"/>

  <!-- Central Auspicious Kohbar Lotus Mandala -->
  <g transform="translate(250, 310)">
    <!-- Base Leaf Pool -->
    <ellipse cx="0" cy="50" rx="110" ry="24" fill="#E8F5E9" stroke="#388E3C" stroke-width="2"/>
    <!-- Outer Lotus Petals -->
    <path d="M 0,20 C -45,0 -70,-50 0,-95 C 70,-50 45,0 0,20 Z" fill="#FCE4EC" stroke="#C72C35" stroke-width="2"/>
    <path d="M -15,20 C -60,-10 -90,-45 -45,-75 C -15,-55 0,-20 -15,20 Z" fill="#F8BBD0" stroke="#C72C35" stroke-width="1.5"/>
    <path d="M 15,20 C 60,-10 90,-45 45,-75 C 15,-55 0,-20 15,20 Z" fill="#F8BBD0" stroke="#C72C35" stroke-width="1.5"/>
    <!-- Center Pod -->
    <ellipse cx="0" cy="-20" rx="20" ry="30" fill="#FFF176" stroke="#F57F17" stroke-width="2"/>
    <circle cx="0" cy="-30" r="4" fill="#C72C35"/>
    <circle cx="-6" cy="-18" r="3" fill="#C72C35"/>
    <circle cx="6" cy="-18" r="3" fill="#C72C35"/>
  </g>

  <!-- Left Dancing Madhubani Peacock -->
  <g transform="translate(140, 240)">
    <!-- Long Plumed Fan -->
    <path d="M -20,20 C -70,60 -115,40 -125,-10 C -130,-50 -90,-80 -45,-70 C -15,-65 0,-30 -20,20 Z" 
          fill="#E0F2F1" stroke="#1B6B76" stroke-width="2"/>
    <!-- Feather Eyes (Ocelli) -->
    <g transform="translate(-85, -20)">
      <ellipse cx="0" cy="0" rx="16" ry="11" fill="url(#peacockBlue)"/>
      <ellipse cx="0" cy="0" rx="9" ry="6" fill="#FFD54F"/>
      <circle cx="0" cy="0" r="3.5" fill="#C72C35"/>
    </g>
    <g transform="translate(-50, -45)">
      <ellipse cx="0" cy="0" rx="14" ry="9" fill="url(#peacockBlue)"/>
      <ellipse cx="0" cy="0" rx="8" ry="5" fill="#FFD54F"/>
      <circle cx="0" cy="0" r="3" fill="#C72C35"/>
    </g>

    <!-- Graceful Slender Neck & Body -->
    <path d="M 0,25 C -15,15 -25,-15 -10,-45 C 2,-65 24,-70 28,-90 C 30,-100 24,-110 32,-116 C 40,-122 52,-114 48,-100 C 44,-85 35,-70 38,-45 C 40,-20 28,12 10,28 Z" 
          fill="url(#peacockBlue)" stroke="#0E4249" stroke-width="2"/>

    <!-- Crown Crest Feathers -->
    <path d="M 38,-120 Q 44,-136 54,-134 M 36,-120 Q 34,-140 38,-142 M 34,-118 Q 26,-132 20,-133" 
          stroke="#C8A253" stroke-width="2" fill="none"/>
    <circle cx="54" cy="-134" r="3.5" fill="#C72C35"/>
    <circle cx="38" cy="-142" r="3.5" fill="#FFD54F"/>
    <circle cx="20" cy="-133" r="3.5" fill="#C72C35"/>

    <!-- Head & Beak -->
    <polygon points="48,-110 64,-107 48,-103" fill="#FFD54F" stroke="#3D262A" stroke-width="1.2"/>
    <circle cx="38" cy="-110" r="3" fill="#FFFFFF"/>
    <circle cx="39" cy="-110" r="1.5" fill="#2C2C2C"/>

    <!-- Wing with Fine Hatching Lines -->
    <path d="M 12,-30 C -8,-5 -5,22 15,28 C 26,30 30,12 25,-12 Z" fill="#FFF9C4" stroke="#3D262A" stroke-width="1.5"/>
    <line x1="6" y1="-12" x2="20" y2="-2" stroke="#C72C35" stroke-width="1.2"/>
    <line x1="5" y1="-2" x2="22" y2="10" stroke="#C72C35" stroke-width="1.2"/>
    <line x1="6" y1="10" x2="19" y2="20" stroke="#C72C35" stroke-width="1.2"/>
  </g>

  <!-- Right Dancing Madhubani Peacock (Mirrored) -->
  <g transform="translate(360, 240) scale(-1, 1)">
    <path d="M -20,20 C -70,60 -115,40 -125,-10 C -130,-50 -90,-80 -45,-70 C -15,-65 0,-30 -20,20 Z" 
          fill="#E0F2F1" stroke="#1B6B76" stroke-width="2"/>
    <g transform="translate(-85, -20)">
      <ellipse cx="0" cy="0" rx="16" ry="11" fill="url(#peacockBlue)"/>
      <ellipse cx="0" cy="0" rx="9" ry="6" fill="#FFD54F"/>
      <circle cx="0" cy="0" r="3.5" fill="#C72C35"/>
    </g>
    <g transform="translate(-50, -45)">
      <ellipse cx="0" cy="0" rx="14" ry="9" fill="url(#peacockBlue)"/>
      <ellipse cx="0" cy="0" rx="8" ry="5" fill="#FFD54F"/>
      <circle cx="0" cy="0" r="3" fill="#C72C35"/>
    </g>

    <path d="M 0,25 C -15,15 -25,-15 -10,-45 C 2,-65 24,-70 28,-90 C 30,-100 24,-110 32,-116 C 40,-122 52,-114 48,-100 C 44,-85 35,-70 38,-45 C 40,-20 28,12 10,28 Z" 
          fill="url(#peacockBlue)" stroke="#0E4249" stroke-width="2"/>

    <path d="M 38,-120 Q 44,-136 54,-134 M 36,-120 Q 34,-140 38,-142 M 34,-118 Q 26,-132 20,-133" 
          stroke="#C8A253" stroke-width="2" fill="none"/>
    <circle cx="54" cy="-134" r="3.5" fill="#C72C35"/>
    <circle cx="38" cy="-142" r="3.5" fill="#FFD54F"/>
    <circle cx="20" cy="-133" r="3.5" fill="#C72C35"/>

    <polygon points="48,-110 64,-107 48,-103" fill="#FFD54F" stroke="#3D262A" stroke-width="1.2"/>
    <circle cx="38" cy="-110" r="3" fill="#FFFFFF"/>
    <circle cx="39" cy="-110" r="1.5" fill="#2C2C2C"/>

    <path d="M 12,-30 C -8,-5 -5,22 15,28 C 26,30 30,12 25,-12 Z" fill="#FFF9C4" stroke="#3D262A" stroke-width="1.5"/>
    <line x1="6" y1="-12" x2="20" y2="-2" stroke="#C72C35" stroke-width="1.2"/>
    <line x1="5" y1="-2" x2="22" y2="10" stroke="#C72C35" stroke-width="1.2"/>
    <line x1="6" y1="10" x2="19" y2="20" stroke="#C72C35" stroke-width="1.2"/>
  </g>

  <!-- Traditional Top Tree of Life Branches -->
  <path d="M 160,80 Q 250,50 340,80" stroke="#7BA896" stroke-width="3" fill="none"/>
  <circle cx="210" cy="65" r="5" fill="#F48FB1"/>
  <circle cx="250" cy="55" r="6" fill="#C72C35"/>
  <circle cx="290" cy="65" r="5" fill="#F48FB1"/>

  <text x="250" y="455" font-family="'Raleway', sans-serif" font-size="14" font-weight="700" 
        fill="#3D262A" text-anchor="middle" letter-spacing="3">
    MITHILA KOHBAR &amp; PEACOCKS
  </text>
</svg>'''

# 4. Assamese Jaapi & Gamosa (assamese_jaapi_gamosa.svg)
assamese_jaapi_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="jaapiBamboo" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="60%" stop-color="#FFD54F"/>
      <stop offset="100%" stop-color="#FFA000"/>
    </radialGradient>
  </defs>

  <rect width="500" height="500" rx="20" fill="#FDFBF9"/>
  <circle cx="250" cy="230" r="170" fill="url(#jaapiBamboo)" stroke="#6D4C41" stroke-width="4"/>

  <!-- Concentric Bamboo Rings -->
  <circle cx="250" cy="230" r="140" fill="none" stroke="#8D6E63" stroke-width="2"/>
  <circle cx="250" cy="230" r="105" fill="none" stroke="#8D6E63" stroke-width="2"/>
  <circle cx="250" cy="230" r="70" fill="none" stroke="#8D6E63" stroke-width="2"/>
  <circle cx="250" cy="230" r="35" fill="none" stroke="#8D6E63" stroke-width="2"/>

  <!-- Conical Center Boss (Jaapi Crown) -->
  <circle cx="250" cy="230" r="22" fill="#D32F2F" stroke="#6D4C41" stroke-width="2"/>
  <circle cx="250" cy="230" r="10" fill="#FFEB3B"/>

  <!-- Red & Green Velvet Ornament Triangular Patches (Traditional Jaapi Decor) -->
  <g id="jaapi-patches">
    <!-- 8 Symmetrical Red Velvet Points -->
    <polygon points="250,95 240,125 260,125" fill="#C72C35"/>
    <polygon points="250,365 240,335 260,335" fill="#C72C35"/>
    <polygon points="115,230 145,220 145,240" fill="#C72C35"/>
    <polygon points="385,230 355,220 355,240" fill="#C72C35"/>
    <polygon points="155,135 175,150 160,165" fill="#2E7D32"/>
    <polygon points="345,135 325,150 340,165" fill="#2E7D32"/>
    <polygon points="155,325 175,310 160,295" fill="#2E7D32"/>
    <polygon points="345,325 325,310 340,295" fill="#2E7D32"/>
  </g>

  <!-- Woven Phulam Gamosa Scarf draped underneath -->
  <g transform="translate(50, 390)">
    <rect x="0" y="0" width="400" height="60" fill="#FFFFFF" stroke="#C72C35" stroke-width="2"/>
    <line x1="20" y1="0" x2="20" y2="60" stroke="#C72C35" stroke-width="4"/>
    <line x1="380" y1="0" x2="380" y2="60" stroke="#C72C35" stroke-width="4"/>
    <path d="M 50,30 L 70,10 L 90,30 L 110,10 L 130,30 L 150,10 L 170,30 L 190,10 L 210,30 L 230,10 L 250,30 L 270,10 L 290,30 L 310,10 L 330,30 L 350,10" 
          stroke="#C72C35" stroke-width="3" fill="none"/>
  </g>

  <text x="250" y="480" font-family="'Raleway', sans-serif" font-size="14" font-weight="700" 
        fill="#3D262A" text-anchor="middle" letter-spacing="3">
    ASSAMESE JAAPI &amp; PHULAM GAMOSA
  </text>
</svg>'''

# 5. Maithili Kohbar Heart Fish (maithili_kohbar_fish.svg)
maithili_fish_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="500" height="500" rx="20" fill="#FAF5EE"/>
  <rect x="25" y="25" width="450" height="450" rx="14" fill="#FFFDFB" stroke="#C8A253" stroke-width="2"/>

  <!-- Twin Kohbar Fish Intertwined Forming Hearts (Symbol of Love & Fertility) -->
  <g transform="translate(250, 230)">
    <!-- Top Heart formed by fish bodies -->
    <path d="M 0,-40 C -70,-130 -140,-20 0,90 C 140,-20 70,-130 0,-40 Z" 
          fill="#FFF0F2" stroke="#C72C35" stroke-width="3"/>
    
    <!-- Left Fish -->
    <path d="M -10,-40 C -80,-80 -110,0 -40,65 C -20,40 -15,0 -10,-40 Z" fill="#FFE082" stroke="#3D262A" stroke-width="2"/>
    <circle cx="-60" cy="-25" r="4" fill="#3D262A"/>
    <!-- Scales -->
    <path d="M -45,-15 Q -55,0 -40,15 M -60,0 Q -70,15 -55,30" stroke="#C72C35" stroke-width="2" fill="none"/>
    <polygon points="-40,65 -65,85 -55,60" fill="#D32F2F"/>

    <!-- Right Fish -->
    <path d="M 10,-40 C 80,-80 110,0 40,65 C 20,40 15,0 10,-40 Z" fill="#FFE082" stroke="#3D262A" stroke-width="2"/>
    <circle cx="60" cy="-25" r="4" fill="#3D262A"/>
    <!-- Scales -->
    <path d="M 45,-15 Q 55,0 40,15 M 60,0 Q 70,15 55,30" stroke="#C72C35" stroke-width="2" fill="none"/>
    <polygon points="40,65 65,85 55,60" fill="#D32F2F"/>

    <!-- Center Blooming Lotus -->
    <circle cx="0" cy="15" r="8" fill="#C72C35"/>
    <path d="M 0,15 C -20,0 -30,-20 0,-35 C 30,-20 20,0 0,15 Z" fill="#F48FB1" stroke="#AD1457" stroke-width="1.5"/>
  </g>

  <text x="250" y="440" font-family="'Raleway', sans-serif" font-size="14" font-weight="700" 
        fill="#3D262A" text-anchor="middle" letter-spacing="3">
    MITHILA KOHBAR HEART-FISH
  </text>
</svg>'''

# Save the new cultural flat illustrations
with open(os.path.join(OUTPUT_DIR, 'couple_pooshu_flat.svg'), 'w') as f:
    f.write(couple_pooshu_svg)

with open(os.path.join(OUTPUT_DIR, 'assamese_xorai_kopou.svg'), 'w') as f:
    f.write(assamese_xorai_svg)

with open(os.path.join(OUTPUT_DIR, 'maithili_peacock_lotus.svg'), 'w') as f:
    f.write(maithili_peacock_svg)

with open(os.path.join(OUTPUT_DIR, 'assamese_jaapi_gamosa.svg'), 'w') as f:
    f.write(assamese_jaapi_svg)

with open(os.path.join(OUTPUT_DIR, 'maithili_kohbar_fish.svg'), 'w') as f:
    f.write(maithili_fish_svg)

print('Cultural flat illustrations generated in illustrations_flat/')
