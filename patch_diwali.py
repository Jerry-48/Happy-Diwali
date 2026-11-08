#!/usr/bin/env python3
"""
Jerry's original Diwali HTML ne ek pan feature add karya vagar sudharse:
  1) Hindi/Devanagari -> Gujarati (Hind Vadodara font)
  2) Footer: "Made with ❤️ by Sujal" + social icons
Usage:  python patch_diwali.py index.html      ->  index_final.html
"""
import re, sys, pathlib

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
s = src.read_text(encoding="utf-8")

def rep(old, new, label=""):
    global s
    if old in s:
        s = s.replace(old, new)
    else:
        print("NOT FOUND:", label or old[:50])

# ---------- 1) Fonts: Hindi fonts -> Hind Vadodara ----------
rep("Rozha+One&family=Tiro+Devanagari+Hindi:ital@0;1", "Hind+Vadodara:wght@400;600;700", "font link")
rep("'Rozha One', 'Tiro Devanagari Hindi', serif", "'Hind Vadodara', sans-serif", "font-hindi")
rep("'Tiro Devanagari Hindi', serif", "'Hind Vadodara', sans-serif", "font-devanagari")

# ---------- 1) Text: Hindi -> Gujarati ----------
T = [
 ("॥ शुभ दीपावली ॥ Authentic Heritage Diwali Celebration", "🪔 શુભ દિવાળી · Diwali Celebration"),
 ("<span> शुभ </span>", "<span> શુભ </span>"),
 ("<span> लाभ </span>", "<span> લાભ </span>"),
 ("॥ श्री गणेशाय नमः ॥", "॥ શ્રી ગણેશાય નમઃ ॥"),
 ("द्वार खोलें • Pull Silk Cord to Enter", "દ્વાર ખોલો • Pull Silk Cord to Enter"),
 ("॥ श्री महालक्ष्म्यै नमः • शुभ दीपावली ॥", "॥ શ્રી મહાલક્ષ્મ્યૈ નમઃ • શુભ દિવાળી ॥"),
 ("स्नेह निमंत्रण • Festive Patrika", "સ્નેહ નિમંત્રણ • Festive Patrika"),
 ("अपना शुभ नाम लिखें • Enter your name...", "તમારું નામ લખો • Enter your name..."),
 ("कृपया अपना शुभ नाम दर्ज करें • Please enter", "કૃપા કરીને તમારું નામ લખો • Please enter"),
 ("दीप प्रज्वलित करें • Light the Diyas", "દીવા પ્રગટાવો • Light the Diyas"),
 ("॥ दीपज्योतिः परब्रह्म दीपज्योतिर्जनार्दनः ॥", "॥ દીપજ્યોતિઃ પરબ્રહ્મ દીપજ્યોતિર્જનાર્દનઃ ॥"),
 ("॥ दीपोत्सव की हार्दिक शुभकामनाएं ॥", "॥ દીપોત્સવની હાર્દિક શુભેચ્છાઓ ॥"),
 ("— सुख, शांति एवं समृद्धि • Ghar Ki Diwali —", "— સુખ, શાંતિ અને સમૃદ્ધિ • Ghar Ki Diwali —"),
 ("अगला आशीर्वाद • Next Wish", "આગળનો આશીર્વાદ • Next Wish"),
 ("अनार व चकरी • Anar & Chakri", "અનાર અને ચકરી • Anar & Chakri"),
 ("संदेश कॉपी • Copy Patrika", "સંદેશ કૉપી • Copy Patrika"),
 ("नाद • Sound On", "નાદ • Sound On"),
 ("मौन • Muted", "મૌન • Muted"),
 ("॥ शुभं करोति कल्याणं आरोग्यं धनसंपदा ॥", "॥ શુભં કરોતિ કલ્યાણં આરોગ્યં ધનસંપદા ॥"),
 ("॥ तमसो मा ज्योतिर्गमय ॥", "॥ તમસો મા જ્યોતિર્ગમય ॥"),
 ("॥ महालक्ष्मी नमस्तुभ्यं नमस्तुभ्यं सुरेश्वरी ॥", "॥ મહાલક્ષ્મી નમસ્તુભ્યં નમસ્તુભ્યં સુરેશ્વરી ॥"),
 ("॥ दीपोत्सवः सर्वसुखप्रदायकः ॥", "॥ દીપોત્સવઃ સર્વસુખપ્રદાયકઃ ॥"),
 ("॥ सर्वे भवन्तु सुखिनः सर्वे सन्तु निरामयाः ॥", "॥ સર્વે ભવન્તુ સુખિનઃ સર્વે સન્તુ નિરામયાઃ ॥"),
 ("सुख, शांति एवं समृद्धि • Ghar Ki Diwali", "સુખ, શાંતિ અને સમૃદ્ધિ • Ghar Ki Diwali"),
 ("अंधकार से प्रकाश की ओर • Eternal Radiance", "અંધકારમાંથી પ્રકાશ તરફ • Eternal Radiance"),
 ("शुभ लाभ • Blessings of Prosperity", "શુભ લાભ • Blessings of Prosperity"),
 ("मंगलमय दीपावली • Joy & Togetherness", "મંગલમય દિવાળી • Joy & Togetherness"),
 ("आरोग्यं धनसंपदा • Health & Fortune", "આરોગ્યં ધનસંપદા • Health & Fortune"),
 ("अतिथि (Dear Friend)", "મિત્ર (Dear Friend)"),
 (" शुभ दीपावली! All 5 Sacred", "શુભ દિવાળી! All 5 Sacred"),
 ("संदेश कॉपी हो गया!", "સંદેશ કૉપી થઈ ગયો!"),
 ("शुभ दीपावली • Shubh Deepavali", "શુભ દિવાળી • Shubh Deepavali"),
]
for old, new in T:
    rep(old, new)

# ---------- 2) Footer ----------
CSS = """
/* ===== Footer: Made with love by Sujal ===== */
#site-footer{position:fixed;left:0;right:0;bottom:0;z-index:45;padding:8px 10px 10px;text-align:center;background:linear-gradient(transparent,rgba(18,4,2,.92) 55%);pointer-events:none}
#site-footer p{color:#f6e095;font-weight:700;font-size:1rem;text-shadow:0 0 14px rgba(255,170,40,.6)}
#site-footer .soc{display:flex;gap:10px;justify-content:center;margin-top:6px;pointer-events:auto}
#site-footer .soc a{width:38px;height:38px;border-radius:50%;display:grid;place-items:center;color:#f6e095;border:1.5px solid #d4a843;background:rgba(43,10,5,.9);transition:all .25s}
#site-footer .soc a:hover{transform:translateY(-4px) scale(1.1);background:#f6e095;color:#2e0903;box-shadow:0 0 18px rgba(255,200,80,.8)}
#site-footer svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
"""
HTML = """
    <footer id="site-footer">
        <p>Made with ❤️ by Sujal</p>
        <div class="soc" id="soc"></div>
    </footer>

"""
JS = """
        /* ===== Footer links: khali link = icon hide ===== */
        const LINKS = {
            GitHub: "https://github.com/Jerry-48",
            Telegram: "",
            LinkedIn: "https://www.linkedin.com/in/kalena-sujalkumar-06299b377/",
            Portfolio: "",
            WhatsApp: ""
        };
        const ICON = {
            GitHub: '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>',
            Telegram: '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4 20-7z"/>',
            LinkedIn: '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 2a2 2 0 1 1 0 4 2 2 0 0 1 0-4z"/>',
            Portfolio: '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
            WhatsApp: '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>'
        };
        document.getElementById('soc').innerHTML = Object.keys(LINKS).filter(k => LINKS[k]).map(k =>
            `<a href="${LINKS[k]}" target="_blank" rel="noopener" aria-label="${k}" title="${k}"><svg viewBox="0 0 24 24">${ICON[k]}</svg></a>`).join('');

"""
rep("</style>", CSS + "    </style>", "</style>")
rep('<div id="toast-box"', HTML.lstrip("\n") + '    <div id="toast-box"', "toast-box")
rep("window.onload = function () {", JS + "        window.onload = function () {", "window.onload")
# footer thi niche na content na dabay + link click par burst na thay
rep("pt-16 pb-6", "pt-16 pb-24", "main padding")
rep("!e.target.closest('button')) {", "!e.target.closest('button') && !e.target.closest('a')) {", "pointerdown")

out = src.with_name(src.stem + "_final.html")
out.write_text(s, encoding="utf-8")
left = sorted(set(re.findall(r"[^\n]*[\u0900-\u097F][^\n]*", s)))
print("Saved:", out)
print("Baki rahela Hindi lines:", len(left))
for l in left:
    print("  ", l.strip()[:90])