#!/usr/bin/env python3
"""Build the PJN Dental social landing pages (static HTML) into this folder.

Run: python3 build.py   -> writes index.html + one folder per page.
Copy rules: "can/may/linked", never "causes" or "cures"; no prices; no success rates.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHONE = "(503) 649-1646"
TEL = "tel:+15036491646"
ADDR = "17535 SW Tualatin Valley Hwy, Beaverton, OR 97003"
MAPS = "https://maps.google.com/?q=PJN+Dental+17535+SW+Tualatin+Valley+Hwy+Beaverton+OR+97003"
IG = "https://www.instagram.com/drpascalnguyen/"
LOGO = "https://pjndental.com/wp-content/uploads/2026/06/PJN-logo-emblem.png"


def exam_url(campaign):
    return f"https://pjndental.com/new-patients/?utm_source=social&utm_medium=landing&utm_campaign={campaign}"


def page(slug, title, desc, body, campaign):
    depth = "../" if slug else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | PJN Dental, Beaverton OR</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | Dr. Pascal Nguyen, DMD, NMD">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{LOGO}">
<link rel="icon" href="{LOGO}">
<link rel="stylesheet" href="{depth}style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="{depth or './'}"><img src="{LOGO}" alt="PJN Dental logo">PJN Dental</a>
  <a class="call-sm" href="{TEL}">📞 {PHONE}</a>
</div></header>
{body}
<div class="band"><div class="wrap">
  <h2>Start with a new patient exam</h2>
  <p>Your first visit is unhurried. We listen to your story first, then look at your teeth, gums, bite, jaw joints, airway and overall health together, so the plan fits you.</p>
  <div class="ctas">
    <a class="btn btn-primary" href="{exam_url(campaign)}">Request a new patient exam</a>
    <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
    <a class="btn btn-ghost" href="{IG}">Message me on Instagram</a>
  </div>
</div></div>
<footer><div class="wrap">
  <p><strong>PJN Dental</strong> · Dr. Pascal Nguyen, DMD, NMD<br>
  <a href="{MAPS}">{ADDR}</a> · <a href="{TEL}">{PHONE}</a></p>
  <p class="note">This page is general education, not medical or dental advice, and it is not a diagnosis. Every mouth is different; your options depend on an in-person exam.</p>
  <p class="note"><a href="https://pjndental.com/">pjndental.com</a></p>
</div></footer>
</body>
</html>
"""


def hero(eyebrow, h1, lede, campaign):
    return f"""<div class="hero"><div class="wrap">
  <p class="eyebrow">{eyebrow}</p>
  <h1>{h1}</h1>
  <p class="lede">{lede}</p>
  <div class="ctas">
    <a class="btn btn-primary" href="{exam_url(campaign)}">Request a new patient exam</a>
    <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
  </div>
</div></div>"""


PAGES = {}

# ---------------------------------------------------------------- hub (link in bio)
PAGES[""] = ("Start here", "Dr. Pascal Nguyen, biological dentist in Beaverton, Oregon. Zirconia implants, safe amalgam removal, root canal second opinions and airway screening.", f"""
<div class="hero"><div class="wrap">
  <p class="eyebrow">Dr. Pascal Nguyen, DMD, NMD · Beaverton, Oregon</p>
  <h1>Whole-body dentistry, explained simply</h1>
  <p class="lede">Saw one of our videos? Start here.</p>
</div></div>
<div class="wrap links" style="padding-top:20px">
  <a class="btn btn-dark" href="{exam_url('hub')}">Request a new patient exam</a>
  <a class="btn btn-outline" href="{TEL}">Call {PHONE}</a>
  <h2 style="margin-top:28px">Popular topics</h2>
  <a class="btn btn-outline" href="zirconia-implants/">Zirconia (metal-free) implants</a>
  <a class="btn btn-outline" href="safe-amalgam-removal/">Safe silver (mercury) filling removal</a>
  <a class="btn btn-outline" href="root-canal-second-opinion/">Root canal second opinion</a>
  <a class="btn btn-outline" href="airway-self-screen/">Free airway &amp; sleep self-screen</a>
  <a class="btn btn-outline" href="exam/">What's in a new patient exam</a>
  <h2>Where we are</h2>
  <p><a href="{MAPS}">{ADDR}</a></p>
</div>
""", "hub")

# ---------------------------------------------------------------- zirconia
PAGES["zirconia-implants"] = ("Zirconia Implants", "Metal-free zirconia dental implants in Beaverton, OR with Dr. Pascal Nguyen, DMD, NMD. Honest answers on zirconia vs titanium, fractures, cost and candidacy.", hero(
    "Metal-free tooth replacement", "Zirconia implants: metal-free, and honest about who they fit",
    "Zirconia is a white ceramic implant for people who want to replace a tooth without metal. It's a great option for many patients, and not the right one for everyone. Here's how we decide.", "zirconia") + """
<div class="wrap">
<h2>Why patients ask for zirconia</h2>
<ul class="check">
  <li><strong>Metal-free.</strong> A good fit if you prefer to avoid metal in your body, or have a known or suspected metal sensitivity.</li>
  <li><strong>Naturally white.</strong> No grey shadow showing through thin gums.</li>
  <li><strong>Doesn't corrode.</strong> Zirconia is a ceramic, so it doesn't rust or corrode the way metals can.</li>
  <li><strong>Gum-friendly surface.</strong> Studies suggest plaque may collect less on zirconia than on titanium. Your home care still matters most.</li>
</ul>

<h2>Zirconia vs. titanium, honestly</h2>
<div class="tablewrap"><table>
<tr><th></th><th>Zirconia</th><th>Titanium</th></tr>
<tr><td>Material</td><td>White ceramic, metal-free</td><td>Metal alloy</td></tr>
<tr><td>Track record</td><td>Newer; good short- to mid-term results for single teeth</td><td>Decades of long-term data</td></tr>
<tr><td>Best for</td><td>Single teeth and short bridges in well-selected cases</td><td>Almost every situation, including full-arch</td></tr>
<tr><td>Looks</td><td>White, natural at the gumline</td><td>Can show grey through thin gums</td></tr>
</table></div>
<p>We place both. If titanium is the better choice for you, we'll tell you.</p>

<h2>Questions we hear every day</h2>
<details><summary>Don't zirconia implants break?</summary><p>Early generations had more fracture problems. Today's designs are much stronger, and research on current implants for single teeth shows results comparable to titanium. Fractures are still possible, which is why careful case selection matters: we look at your bite, any grinding or clenching, and how much bone you have before recommending one.</p></details>
<details><summary>How much does a zirconia implant cost?</summary><p>It depends on your case: one tooth or several, whether you need bone grafting or an extraction first, and the type of crown. We give you an exact, written estimate at your consultation, before any treatment starts.</p></details>
<details><summary>Am I a good candidate?</summary><p>Often yes if you're replacing one or a few teeth, have enough healthy bone, and don't have heavy grinding. We confirm with a 3D (CBCT) scan, a bite analysis and a full exam.</p></details>
<details><summary>What happens at the first visit?</summary><p>We start by listening: your health history, your goals and any concerns about materials. Then we take a 3D scan and check your bone, gums and bite. You leave knowing your options, including whether zirconia makes sense for you.</p></details>
<details><summary>Can you test which materials suit me?</summary><p>Yes. We offer biocompatibility testing for patients who want extra information before choosing dental materials.</p></details>
</div>
""", "zirconia")

# ---------------------------------------------------------------- amalgam
PAGES["safe-amalgam-removal"] = ("Safe Silver Filling Removal", "Safe removal of silver (amalgam) fillings in Beaverton, OR using the SMART protocol. Dr. Pascal Nguyen, DMD, NMD.", hero(
    "Silver (amalgam) fillings", "Thinking about removing your silver fillings? Do it safely.",
    "Silver fillings are about 50% mercury. If you and your dentist decide to replace them, how they're removed matters as much as what replaces them.", "amalgam") + """
<div class="wrap">
<h2>What the FDA says</h2>
<p>In 2020 the FDA recommended that some people avoid getting <em>new</em> amalgam fillings when appropriate: pregnant or nursing women, women planning a pregnancy, children under 6, and people with kidney problems, neurological conditions or a known mercury sensitivity.</p>
<p>The FDA does <strong>not</strong> recommend removing healthy, intact fillings just because they're amalgam, since removal itself can release mercury vapor. So the decision is personal, made with your dentist, based on the condition of the fillings and your health.</p>

<h2>How we remove amalgam: the SMART protocol</h2>
<p>When removal is the right call, we follow the SMART protocol (Safe Mercury Amalgam Removal Technique), designed to reduce mercury exposure for you and our team:</p>
<ul class="check">
  <li>A protective dental dam to isolate the tooth</li>
  <li>High-volume suction right at the tooth to capture vapor and particles</li>
  <li>Removing the filling in larger chunks rather than grinding it away</li>
  <li>Fresh air supply and protective covering for you</li>
  <li>Room air filtration</li>
  <li>Replacement with metal-free materials, chosen with optional biocompatibility testing</li>
</ul>

<h2>Common questions</h2>
<details><summary>Should I remove all my fillings at once?</summary><p>Usually not. We plan removal in stages based on which fillings are failing, cracked or decayed, and on your health. We'll map it out together.</p></details>
<details><summary>What replaces the amalgam?</summary><p>Tooth-colored, metal-free materials. For larger fillings, that may be a ceramic inlay, onlay or crown so the tooth stays strong.</p></details>
<details><summary>Will removing my fillings fix my health problems?</summary><p>We can't promise that, and you should be wary of anyone who does. What we can do is remove failing fillings carefully, replace them with metal-free materials, and look at your oral health as part of your whole health.</p></details>
<details><summary>What does it cost?</summary><p>It depends on how many fillings, their size and what replaces them. You'll get a written estimate after your exam.</p></details>
</div>
""", "amalgam")

# ---------------------------------------------------------------- root canal
PAGES["root-canal-second-opinion"] = ("Root Canal Second Opinion", "Get a root canal second opinion from biological dentist Dr. Pascal Nguyen in Beaverton, OR. Keep, retreat or remove: a balanced look at your options.", hero(
    "Root canal second opinion", "Told you need a root canal, or worried about one you have?",
    "Not every root canal-treated tooth needs to come out, and not every one should stay. A second opinion looks at the whole picture before you decide.", "rootcanal") + """
<div class="wrap">
<h2>Your options, side by side</h2>
<div class="grid">
  <div class="card"><h3>Keep it</h3><p>Some teeth heal well and can be kept. Sometimes a retreatment or a referral to an endodontist is the best path.</p></div>
  <div class="card"><h3>Remove it carefully</h3><p>If a treated tooth shows ongoing infection or inflammation, careful removal with thorough cleaning of the site, ozone and PRF to support healing may be best.</p></div>
  <div class="card"><h3>Replace it</h3><p>After removal, options include a metal-free zirconia implant, a bridge or a partial, depending on your bone and bite.</p></div>
</div>

<h2>What we look at</h2>
<ul class="check">
  <li>A 3D (CBCT) scan, which shows infection and bone loss that flat 2D x-rays can miss</li>
  <li>Your symptoms, and how the tooth and gums look and feel</li>
  <li>Your overall health history: chronic inflammation or infection can be linked to oral health</li>
  <li>Your goals and how you feel about each option</li>
</ul>

<h2>Common questions</h2>
<details><summary>My root canal doesn't hurt. Could there still be a problem?</summary><p>Sometimes, yes. Infection around a treated tooth can be silent. A 3D scan is the best way to check.</p></details>
<details><summary>Do you just pull every root canal tooth?</summary><p>No. Our job is to give you a clear, balanced picture. Many patients leave keeping their tooth.</p></details>
<details><summary>Do I need my old x-rays?</summary><p>If you have them, bring or send them. They help us compare over time. We'll take our own 3D scan either way.</p></details>
</div>
""", "rootcanal")

# ---------------------------------------------------------------- new patient exam guide (DM "EXAM")
EXAM_ITEMS = [
    ("We listen first", "Your health history, your symptoms, what you've already tried and your goals. You won't be rushed."),
    ("3D (CBCT) scan", "A 3D view of your teeth, jaws, sinuses and airway. It shows infection, bone loss and anatomy that flat x-rays can miss."),
    ("Digital x-rays and photos", "A detailed record of your teeth so we can track changes over time."),
    ("Oral cancer screening", "A careful check of your tongue, cheeks, throat and lymph nodes."),
    ("Gum health", "We measure your gums and check for bleeding and inflammation, which is linked to the rest of your health."),
    ("Decay and wear", "We look for cavities, cracks and worn enamel, and what's causing them."),
    ("Bite and jaw joints (TMJ)", "We check how your teeth meet, your jaw joints, your range of motion and tender muscles."),
    ("Digital scan of your bite", "A 3D scan that shows wear patterns and stress on your teeth from grinding or clenching."),
    ("Airway and posture", "We look for signs of mouth breathing, snoring and sleep-disordered breathing, and how head and neck posture relate to your airway."),
    ("Saliva and pH", "Saliva protects your teeth. We check its flow and acidity, which affect decay and enamel erosion."),
    ("Blood sugar (A1C)", "Blood sugar affects inflammation, gum health and healing."),
    ("Nitric oxide", "Gives insight into circulation, which matters for healing."),
    ("Heart rate variability (HRV)", "A look at nervous system balance and stress resilience."),
    ("Minerals", "We talk about the minerals your teeth, gums and bone rely on."),
    ("Meridian assessment", "A traditional tooth-organ chart we use as one extra perspective alongside the clinical exam."),
]

PAGES["exam"] = ("What's in a New Patient Exam", "What happens at a new patient exam with Dr. Pascal Nguyen, DMD, NMD in Beaverton, OR: an unhurried, whole-body look at your oral health.", hero(
    "Your first visit", "What's actually in a new patient exam with me",
    "Many patients tell me they've felt rushed and that nobody looked at the whole picture. My exam is different. I'm not in a hurry, and I want to hear your story first. Here's everything we look at, and why.", "exam") + """
<div class="wrap">
<h2>Everything we look at</h2>
""" + "\n".join(f'<div class="card"><h3>{i}. {t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(EXAM_ITEMS, 1)) + """
<h2>What you leave with</h2>
<ul class="check">
  <li>A clear explanation of what we found, in plain language</li>
  <li>Your options, including doing nothing, with the pros and cons of each</li>
  <li>A written plan and estimate before any treatment starts</li>
</ul>
<p class="note">Not every test is right for every patient. We'll tell you which ones make sense for you.</p>
<p>— Dr. Pascal Nguyen, DMD, NMD</p>
</div>
""", "exam")

# ---------------------------------------------------------------- airway self-screen
QUESTIONS = [
    "Do you snore, or has someone told you that you snore?",
    "Do you wake up tired even after 7 to 8 hours in bed?",
    "Has anyone noticed you stop breathing or gasp during sleep?",
    "Do you wake up with headaches or a dry mouth?",
    "Do you grind or clench your teeth, or have worn-down teeth?",
    "Do you breathe through your mouth during the day or at night?",
    "Do you have high blood pressure?",
    "Do you get up more than once a night to use the bathroom?",
    "Do you feel foggy, irritable or sleepy during the day?",
    "Do you use a CPAP but still feel tired, or struggle to use it?",
]
KID_QUESTIONS = [
    "Does your child sleep with their mouth open or snore?",
    "Is your child restless at night, or wet the bed past age 5?",
    "Does your child have trouble focusing or seem tired during the day?",
    "Does your child grind their teeth or have crowded teeth?",
]


def qlist(items, name):
    return "\n".join(f'<label class="q"><input type="checkbox" name="{name}"><span>{q}</span></label>' for q in items)


PAGES["airway-self-screen"] = ("Free Airway & Sleep Self-Screen", "A free 2-minute self-screen for snoring, sleep apnea signs and mouth breathing, for adults and kids. From Dr. Pascal Nguyen, DMD, NMD, Beaverton OR.", hero(
    "Free · 2 minutes · no sign-up", "Snoring isn't just noise. Take the 2-minute airway self-screen.",
    "Check the boxes that apply to you (or your child). This isn't a diagnosis. It helps you decide whether an airway evaluation is worth it.", "airway") + f"""
<div class="wrap">
<h2>For adults</h2>
{qlist(QUESTIONS, "a")}
<h2>For kids <span class="note">(optional)</span></h2>
{qlist(KID_QUESTIONS, "k")}
<p style="margin-top:22px"><button class="btn btn-dark" style="border:0;cursor:pointer" onclick="score()">See my result</button></p>
<div id="result" class="card" aria-live="polite">
  <p class="big" id="rtitle"></p>
  <p id="rbody"></p>
  <div class="ctas"><a class="btn btn-dark" href="{exam_url('airway')}">Request a new patient exam</a><a class="btn btn-outline" href="{TEL}">Call {PHONE}</a></div>
</div>

<h2>Why airway matters</h2>
<p>In obstructive sleep apnea, the airway narrows or collapses during sleep and breathing pauses. Oxygen drops, and the body wakes just enough to breathe, often many times a night without you remembering. Over time, untreated sleep apnea is linked to high blood pressure, heart disease and diabetes.</p>
<p>Dentists often spot the early signs first: worn teeth from grinding, a scalloped tongue, a narrow palate or mouth breathing.</p>
<h2>What we do</h2>
<ul class="check">
  <li>An airway screening as part of every new patient exam, including a 3D scan of the airway</li>
  <li>Help arranging a home sleep test. Only a sleep study can diagnose sleep apnea</li>
  <li>Oral appliance therapy for appropriate patients, coordinated with your physician</li>
  <li>For kids: airway-focused growth guidance, myofunctional therapy and tongue-tie evaluation</li>
</ul>
</div>
<script>
function score(){{
  var a=document.querySelectorAll('input[name=a]:checked').length;
  var k=document.querySelectorAll('input[name=k]:checked').length;
  var t,b;
  if(a>=5||k>=2){{t="Worth getting checked soon";b="You checked "+a+" adult and "+k+" child signs. Several signs together are a good reason to have an airway evaluation and talk about a sleep test.";}}
  else if(a>=2||k>=1){{t="Worth mentioning at your next visit";b="You checked "+a+" adult and "+k+" child signs. A few signs don't mean you have sleep apnea, but they're worth a closer look.";}}
  else{{t="Low on this screen";b="You checked "+a+" adult and "+k+" child signs. If you still feel tired or someone notices you snore or gasp at night, get checked anyway.";}}
  document.getElementById('rtitle').textContent=t;document.getElementById('rbody').textContent=b+" This screen is not a diagnosis.";
  var r=document.getElementById('result');r.style.display='block';r.scrollIntoView({{behavior:'smooth',block:'center'}});
}}
</script>
""", "airway")


for slug, (title, desc, body, campaign) in PAGES.items():
    out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page(slug, title, desc, body, campaign))
    print("wrote", out.relative_to(ROOT))
