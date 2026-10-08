# Génère version-graphique/index.html à partir de ../index.html
# (même contenu, même fonctionnement, direction artistique « mid-century graphique »).
# Relancer après chaque modification de index.html :  python3 version-graphique/_generateur.py
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'index.html'), encoding='utf-8').read()


def sub1(old, new, s, count=1):
    assert old in s, 'introuvable : ' + old[:60]
    return s.replace(old, new, count)


# Chemins (la page est un dossier plus bas)
s = src.replace('src="assets/', 'src="../assets/').replace('poster="assets/', 'poster="../assets/')
s = s.replace("'assets/videos/", "'../assets/videos/").replace('href="domaines/', 'href="../domaines/')
s = sub1('<title>Sarah Mostfa — Avocate au Barreau de Lyon</title>',
         '<title>Sarah Mostfa — Avocate au Barreau de Lyon (version graphique)</title>', s)

# Polices : une grotesque suisse + une mono « fiche technique »
s = sub1('&family=Inter:wght@300;400;500&display=swap',
         '&family=Inter:wght@300;400;500&family=Inter+Tight:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap', s)

# Haut de page : composition d'affiche
hero_start = s.index('<section class="hv hv-l vid is-active">')
hero_end = s.index('</section>', hero_start) + len('</section>')
HERO = '''<section class="hv hv-l vid is-active">
        <div class="mc-rule"></div>
        <div class="mc-block">
            <video class="depth" poster="../assets/videos/amphitheatre.jpg" muted loop playsinline autoplay preload="auto" aria-hidden="true">
                <source src="../assets/videos/amphitheatre.mp4" type="video/mp4">
                <source src="../assets/videos/amphitheatre.webm" type="video/webm">
            </video>
            <div class="mc-dots"></div>
            <span class="mc-fig">Fig. 1 — L'amphithéâtre</span>
        </div>
        <div class="mc-sun"></div>
        <div class="center">
            <p class="mc-eyebrow rise" style="--d:200ms"><span>Avocate</span><span>Barreau de Lyon</span></p>
            <h1 class="name name-c">
                <span class="mask"><span style="--d:300ms">Sarah</span></span>
                <span class="mask"><span style="--d:420ms"><em>Mostfa</em><span class="dot">.</span></span></span>
            </h1>
            <div class="mc-stripe rise" style="--d:650ms"><i></i><i></i><i></i></div>
            <div class="mc-cols rise" style="--d:800ms">
                <p><b>Avocate au Barreau de Lyon</b>Assure la défense de vos intérêts devant les juridictions civiles et commerciales.</p>
                <p><b>Domaines</b>Contentieux civil<br>Contentieux commercial<br>Conseil juridique</p>
                <p><b>Cabinet</b>14 rue de la Charité<br>69002 Lyon</p>
            </div>
        </div>
        <div class="mc-year rise" style="--d:900ms"><small>Serment</small>/24</div>
        <div class="cue-abs"><div class="cue rise" style="--d:1100ms"><span>Découvrir</span><i></i></div></div>
    </section>'''
s = s[:hero_start] + HERO + s[hero_end:]

# Publications : couvertures façon collection de poche
n = [0]
def cover(m):
    n[0] += 1
    return ('<div class="pub-cover"><span class="pc-top"><span>N°</span><span>Analyse</span></span>'
            '<span class="pc-num">%02d</span><span class="pc-cat"><span>%s</span><span>Lyon</span></span></div>\n                %s'
            % (n[0], m.group(1), m.group(0)))
s = re.sub(r'<div class="pub-meta"><span>([^<]+)</span>', cover, s)
assert n[0] == 3

# Lien de retour vers la version actuelle
s = sub1('<nav class="nav" id="nav">',
         '<a class="mc-badge" href="../index.html">Version graphique — essai <span>↗ version actuelle</span></a>\n<nav class="nav" id="nav">', s)

STYLE = open(os.path.join(HERE, '_style.css'), encoding='utf-8').read()
s = sub1('</head>', '<style>\n' + STYLE + '</style>\n</head>', s)

open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(s)
print('ok', len(s))
