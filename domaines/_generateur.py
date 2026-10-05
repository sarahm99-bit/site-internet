import os
import os
OUT=os.path.dirname(os.path.abspath(__file__))+'/'
V='../assets/videos/domaines/'
IDX='../index.html'

PAGES={
 'contentieux-civil': dict(
   num='01', title='Contentieux civil', design=1, h2='Faire valoir vos droits.',
   catch="Vous êtes une société ou un particulier impliqué dans un litige civil et souhaitez faire valoir vos droits.",
   intro="Un différend avec un bailleur, une assurance, un professionnel ou un voisin peut vite devenir lourd à porter. J'analyse votre situation, je recherche une issue amiable lorsqu'elle est possible et, à défaut, je défends vos intérêts devant les juridictions civiles.",
   video='civil-echecs-noir-blanc',
   items=["Actions en responsabilité civile","Cautionnements","Baux d'habitation et loyers impayés","Indemnisation par les assurances","Contentieux de la consommation","Litiges de la construction et malfaçons"]),
 'contentieux-commercial': dict(
   num='02', title='Contentieux commercial', design=1, h2='Défendre votre activité.',
   catch="Vous faites face à un différend dans le cadre de vos relations d'affaires.",
   intro="Un litige avec un partenaire, un concurrent ou un associé peut fragiliser votre activité. J'évalue les enjeux et les risques avec vous, puis je défends vos intérêts, par la négociation comme devant les juridictions commerciales.",
   video='commercial-echecs-bronze',
   items=["Inexécution, retard ou mauvaise exécution contractuelle","Responsabilité civile délictuelle","Concurrence déloyale et parasitisme","Rupture brutale de relations commerciales","Conflits entre associés","Contrefaçon","Recouvrement de créances"]),
 'conseil-juridique': dict(
   num='03', title='Conseil juridique', design=1, h2='Anticiper plutôt que subir.',
   catch="Vous souhaitez sécuriser vos relations d'affaires, protéger vos créations ou bénéficier d'un appui juridique régulier.",
   intro="Bien rédiger un contrat, protéger une création, disposer d'un appui juridique au quotidien : le conseil permet d'anticiper les difficultés plutôt que de les subir, et de prendre vos décisions en connaissance de cause.",
   video='conseil-echecs',
   groups=[("Rédaction contractuelle",["Négociation et renégociation de contrats","CGV","Contrats commerciaux","Contrats de prestations de service","Contrats fournisseurs","Accords de consortium","Protocoles d'accords transactionnels"]),
           ("Propriété intellectuelle",["Contrats de licence","Cessions de droits d'auteur","Accords de confidentialité et secret des affaires","Consultations sur les moyens de protection de vos créations et projets","Recherches d'antériorité de marques"]),
           ("Support juridique des entreprises",["Service juridique externalisé","Formations juridiques sur mesure pour vos équipes"])]),
}
ORDER=['contentieux-civil','contentieux-commercial','conseil-juridique']

HEAD='''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Sarah Mostfa, Avocate au Barreau de Lyon</title>
<meta name="description" content="{catch}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400;1,500;1,600&family=Instrument+Serif:ital@0;1&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
        --vert: #72785f; --vert-dark: #5a6049; --beige: #d6cdb8; --nacre: #f0ebe2; --noir: #1a1a1a; --blanc: #fdfcfa;
        --serif: 'Cormorant Garamond', serif; --display: 'Instrument Serif', serif; --sans: 'Inter', sans-serif;
        --ease: cubic-bezier(0.22, 1, 0.36, 1);
    }}
    body {{ font-family: var(--sans); background: var(--blanc); color: var(--noir); -webkit-font-smoothing: antialiased; }}
    a {{ color: inherit; text-decoration: none; }}

    .nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 100; display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; padding: 22px 5vw; transition: background-color 0.6s, padding 0.4s; }}
    .nav.scrolled {{ background: rgba(253, 252, 250, 0.97); padding: 14px 5vw; }}
    .logo {{ font-family: var(--serif); font-size: 1.6rem; font-weight: 600; letter-spacing: -0.04em; }}
    .logo em {{ font-style: italic; font-weight: 400; color: var(--vert); }}
    .tabs {{ display: flex; padding: 4px; background: #d9cfbc; border-radius: 100px; }}
    .tabs a {{ padding: 10px 22px; border-radius: 100px; font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; transition: background 0.3s, color 0.3s; }}
    .tabs a:hover, .tabs a.on {{ background: var(--noir); color: var(--blanc); }}
    .dd {{ position: relative; display: flex; }}
    .chev {{ display: inline-block; width: 6px; height: 6px; margin-left: 8px; border-right: 1px solid currentColor; border-bottom: 1px solid currentColor; transform: translateY(-2px) rotate(45deg); transition: transform 0.4s var(--ease); }}
    .dd.open .chev {{ transform: translateY(1px) rotate(-135deg); }}
    .dd-panel {{ position: absolute; top: calc(100% + 10px); left: 50%; translate: -50% 0; min-width: 270px; padding: 6px; background: #d9cfbc; border-radius: 22px; display: grid; gap: 2px; opacity: 0; transform: translateY(-8px); pointer-events: none; transition: opacity 0.35s var(--ease), transform 0.45s var(--ease); }}
    .dd-panel::before {{ content: ''; position: absolute; left: 0; right: 0; top: -12px; height: 12px; }}
    .dd.open .dd-panel {{ opacity: 1; transform: none; pointer-events: auto; }}
    .tabs .dd-panel a {{ display: flex; justify-content: space-between; align-items: center; padding: 12px 18px; border-radius: 100px; font-size: 0.74rem; letter-spacing: 0.06em; text-transform: uppercase; background: none; color: var(--noir); }}
    .tabs .dd-panel a small {{ font-size: 0.62rem; color: var(--vert-dark); }}
    .tabs .dd-panel a:hover, .tabs .dd-panel a.cur {{ background: var(--noir); color: var(--blanc); }}
    .tabs .dd-panel a:hover small, .tabs .dd-panel a.cur small {{ color: var(--beige); }}
    .cta-nav {{ justify-self: end; padding: 13px 24px; border-radius: 100px; background: var(--vert); color: var(--blanc); font-size: 0.72rem; letter-spacing: 0.08em; text-transform: uppercase; }}

    .crumb {{ font-size: 0.64rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--vert-dark); display: flex; gap: 10px; flex-wrap: wrap; }}
    .crumb a:hover {{ color: var(--noir); }}
    .crumb span {{ opacity: 0.5; }}
    h1 {{ font-family: var(--display); font-weight: 400; line-height: 1; letter-spacing: -0.02em; }}
    .catch {{ font-family: var(--serif); font-size: clamp(1.3rem, 1.8vw, 1.6rem); line-height: 1.4; }}
    .intro {{ font-size: 1rem; line-height: 1.9; color: #555; max-width: 34em; }}
    .tag {{ font-size: 0.6rem; letter-spacing: 0.22em; text-transform: uppercase; color: var(--vert); }}
    .btn {{ display: inline-flex; align-items: center; gap: 14px; padding: 16px 28px; border-radius: 100px; background: var(--vert); color: var(--blanc); font-size: 0.72rem; letter-spacing: 0.15em; text-transform: uppercase; transition: background 0.3s; }}
    .btn:hover {{ background: var(--vert-dark); }}
    .btn svg {{ transition: transform 0.4s var(--ease); }}
    .btn:hover svg {{ transform: translateX(4px); }}
    .list {{ list-style: none; }}
    .list li {{ position: relative; padding: 11px 0 11px 22px; font-size: 0.95rem; line-height: 1.55; color: #444; }}
    .list li::before {{ content: ''; position: absolute; left: 0; top: 22px; width: 10px; height: 1px; background: var(--vert); }}

    .reveal {{ opacity: 0; transform: translateY(24px); transition: opacity 1s var(--ease), transform 1s var(--ease); transition-delay: var(--d, 0ms); }}
    .reveal.in {{ opacity: 1; transform: none; }}
    .rise {{ display: block; overflow: hidden; padding-bottom: 0.1em; }}
    .rise > span {{ display: inline-block; animation: up 1.3s var(--ease) both; animation-delay: var(--d, 100ms); }}
    @keyframes up {{ from {{ transform: translateY(105%); }} to {{ transform: none; }} }}
    video, .vposter {{ display: block; width: 100%; height: 100%; object-fit: cover; }}

    /* Bloc d'appel au rendez-vous et autres domaines (communs) */
    .callout {{ background: var(--nacre); padding: 110px 5vw; text-align: center; }}
    .callout p.big {{ font-family: var(--display); font-size: clamp(2rem, 4vw, 3.2rem); line-height: 1.1; margin-bottom: 28px; }}
    .callout p.big em {{ color: var(--vert); }}
    .others {{ padding: 90px 5vw 100px; max-width: 1200px; margin: 0 auto; }}
    .others h2 {{ font-size: 0.66rem; letter-spacing: 0.22em; text-transform: uppercase; color: var(--vert-dark); font-weight: 500; margin-bottom: 26px; }}
    .others-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0 4vw; }}
    .others a {{ display: flex; justify-content: space-between; align-items: baseline; gap: 20px; padding: 26px 0; border-top: 1px solid rgba(26, 26, 26, 0.14); font-family: var(--display); font-size: clamp(1.6rem, 2.6vw, 2.2rem); transition: color 0.3s, padding 0.5s var(--ease); }}
    .others a:hover {{ color: var(--vert-dark); padding-left: 10px; }}
    .others a small {{ font-family: var(--sans); font-size: 0.7rem; letter-spacing: 0.12em; color: var(--vert); }}
    .footer {{ background: var(--noir); color: rgba(255, 255, 255, 0.55); padding: 34px 5vw; display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap; font-size: 0.75rem; }}
    .footer .logo {{ color: var(--blanc); font-size: 1.3rem; }}
{css}
    @media (max-width: 900px) {{
        .tabs {{ display: none; }}
        .cta-nav {{ grid-column: 3; }}
        .others-grid {{ grid-template-columns: 1fr; }}
{css_m}
    }}
    @media (prefers-reduced-motion: reduce) {{ *, *::before, *::after {{ animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }} }}
</style>
</head>
<body>
<nav class="nav" id="nav">
    <a href="{idx}" class="logo">S<em>M</em></a>
    <div class="tabs">
        <a href="{idx}#presentation">Présentation</a>
        <div class="dd"><a href="{idx}#domaines" class="on" aria-haspopup="true" aria-expanded="false">Domaines<i class="chev"></i></a>
            <div class="dd-panel" role="menu">{ddlinks}</div></div>
        <a href="{idx}#publications">Publications</a>
        <a href="{idx}#contact">Contact</a>
    </div>
    <a href="{idx}#contact" class="cta-nav">Rendez-vous</a>
</nav>
'''
ARROW='<svg width="16" height="10" viewBox="0 0 16 10" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M0 5h15M11 1l4 4-4 4"/></svg>'
def video(v):
    return f'''<video muted loop playsinline autoplay preload="auto" poster="{V}{v}.jpg" aria-hidden="true">
            <source src="{V}{v}.mp4" type="video/mp4">
            <source src="{V}{v}.webm" type="video/webm">
        </video>'''
def crumb(p):
    return f'<p class="crumb"><a href="{IDX}">Accueil</a><span>/</span><a href="{IDX}#domaines">Domaines</a><span>/</span>{p["title"]}</p>'
def items_html(p):
    if 'groups' in p:
        return '<div class="groups">'+''.join(f'<div class="group reveal" style="--d:{i*120}ms"><h3>{g}</h3><ul class="list">'+''.join(f'<li>{x}</li>' for x in xs)+'</ul></div>' for i,(g,xs) in enumerate(p['groups']))+'</div>'
    return '<ul class="list cols reveal">'+''.join(f'<li>{x}</li>' for x in p['items'])+'</ul>'
def tail(key):
    p=PAGES[key]
    others=''.join(f'<a href="{k}.html">{PAGES[k]["title"]}<small>{PAGES[k]["num"]} →</small></a>' for k in ORDER if k!=key)
    return f'''
<section class="callout">
    <p class="big reveal">Votre situation appelle <em>une stratégie sur mesure</em>.</p>
    <a href="{IDX}#contact" class="btn reveal" style="--d:120ms"><span>Prendre rendez-vous</span>{ARROW}</a>
</section>
<section class="others">
    <h2>Autres domaines d'intervention</h2>
    <div class="others-grid">{others}</div>
</section>
<footer class="footer"><a href="{IDX}" class="logo">S<em>M</em></a><span>Sarah Mostfa — Avocate au Barreau de Lyon · 14 rue de la Charité, 69002 Lyon</span></footer>

<script>
(function () {{
    var nav = document.getElementById('nav');
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function onScroll() {{ nav.classList.toggle('scrolled', window.scrollY > 40); }}
    window.addEventListener('scroll', onScroll, {{ passive: true }}); onScroll();
    document.querySelectorAll('.dd').forEach(function (dd) {{
        var a = dd.querySelector('a'), t;
        function set(on) {{ dd.classList.toggle('open', on); a.setAttribute('aria-expanded', on); }}
        dd.addEventListener('mouseenter', function () {{ clearTimeout(t); set(true); }});
        dd.addEventListener('mouseleave', function () {{ t = setTimeout(function () {{ set(false); }}, 220); }});
        dd.addEventListener('focusin', function () {{ set(true); }});
        dd.addEventListener('focusout', function (e) {{ if (!dd.contains(e.relatedTarget)) set(false); }});
        dd.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') {{ set(false); a.focus(); }} }});
    }});
    var io = new IntersectionObserver(function (en) {{ en.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ threshold: 0.15 }});
    document.querySelectorAll('.reveal').forEach(function (el) {{ io.observe(el); }});
    document.querySelectorAll('video').forEach(function (v) {{
        if (reduce) {{ v.removeAttribute('autoplay'); v.pause(); return; }}
        var pr = v.play(); if (pr && pr.catch) pr.catch(function () {{
            var go = function () {{ v.play(); window.removeEventListener('pointerdown', go); window.removeEventListener('scroll', go); }};
            window.addEventListener('pointerdown', go); window.addEventListener('scroll', go, {{ passive: true }});
        }});
    }});

}})();
</script>
</body>
</html>
'''

# ═════ Design 1 — Partage (vidéo verticale à droite) ═════
CSS1='''    .h1wrap { display: grid; grid-template-columns: 1fr 1fr; min-height: 100vh; min-height: 100svh; background: var(--nacre); }
    .h1-text { display: flex; flex-direction: column; justify-content: center; gap: 28px; padding: 140px 6vw 80px 7vw; }
    .h1-text h1 { font-size: clamp(3.4rem, 6.4vw, 6.2rem); }
    .h1-text .num { font-family: var(--serif); font-size: 1.4rem; color: var(--vert); }
    .h1-media { position: relative; overflow: hidden; }
    .h1-media::after { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(240, 235, 226, 0.25), transparent 30%); pointer-events: none; }
    .body1 { padding: 120px 7vw 110px; max-width: 1300px; margin: 0 auto; }
    .body1 .lead { display: grid; grid-template-columns: 1fr 1.4fr; gap: 6vw; margin-bottom: 80px; align-items: start; }
    .body1 .lead h2 { font-family: var(--display); font-weight: 400; font-size: clamp(2rem, 3.4vw, 2.8rem); line-height: 1.1; }
    .groups { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4vw; }
    .body1 .list.cols { columns: 2; column-gap: 5vw; border-top: 1px solid rgba(114, 120, 95, 0.3); padding-top: 14px; }
    .body1 .list.cols li { break-inside: avoid; }
    .group h3 { font-family: var(--display); font-weight: 400; font-size: 1.7rem; padding-bottom: 16px; margin-bottom: 6px; border-bottom: 1px solid rgba(114, 120, 95, 0.3); }
'''
CSS1M='''        .h1wrap { grid-template-columns: 1fr; }
        .h1-media { height: 60vh; order: -1; }
        .h1-text { padding: 50px 20px; }
        .body1 { padding: 80px 20px; }
        .body1 .lead, .groups { grid-template-columns: 1fr; }
        .body1 .list.cols { columns: 1; }
'''
def page1(key):
    p=PAGES[key]
    return f'''<header class="h1wrap">
    <div class="h1-text">
        {crumb(p)}
        <h1><span class="rise"><span>{p["title"]}</span></span></h1>
        <p class="catch reveal" style="--d:300ms">{p["catch"]}</p>
        <div class="reveal" style="--d:450ms"><a href="{IDX}#contact" class="btn"><span>Prendre rendez-vous</span>{ARROW}</a></div>
    </div>
    <div class="h1-media">{video(p["video"])}</div>
</header>
<main class="body1">
    <div class="lead">
        <h2 class="reveal">{p["h2"]}</h2>
        <p class="intro reveal" style="--d:120ms">{p["intro"]}</p>
    </div>
    {items_html(p)}
</main>'''

# ═════ Design 2 — Bandeau (vidéo pleine largeur) ═════
CSS2='''    .h2wrap { position: relative; height: 82vh; min-height: 560px; overflow: hidden; }
    .h2wrap .media { position: absolute; inset: 0; }
    .h2wrap .veil { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(240, 235, 226, 0.15) 0%, rgba(240, 235, 226, 0.45) 55%, rgba(240, 235, 226, 0.92) 100%); }
    .h2-text { position: absolute; left: 6vw; right: 6vw; bottom: 8vh; display: flex; flex-direction: column; gap: 22px; }
    .h2-text h1 { font-size: clamp(3.6rem, 8vw, 7.6rem); }
    .h2-text .catch { max-width: 30em; text-shadow: 0 0 24px rgba(240, 235, 226, 0.9); }
    .body2 { display: grid; grid-template-columns: 1fr 1.25fr; gap: 7vw; padding: 110px 6vw 120px; max-width: 1300px; margin: 0 auto; align-items: start; }
    .side2 { position: sticky; top: 120px; display: flex; flex-direction: column; gap: 30px; }
    .rows2 { list-style: none; border-top: 1px solid rgba(26, 26, 26, 0.14); }
    .rows2 li { display: flex; justify-content: space-between; align-items: baseline; gap: 20px; padding: 26px 0; border-bottom: 1px solid rgba(26, 26, 26, 0.14); font-family: var(--display); font-size: clamp(1.45rem, 2.2vw, 1.9rem); line-height: 1.2; transition: color 0.3s, padding 0.5s var(--ease); }
    .rows2 li:hover { color: var(--vert-dark); padding-left: 8px; }
    .rows2 li small { font-family: var(--sans); font-size: 0.66rem; letter-spacing: 0.15em; color: var(--vert); flex-shrink: 0; font-variant-numeric: tabular-nums; }
'''
CSS2M='''        .body2 { grid-template-columns: 1fr; padding: 70px 20px; }
        .side2 { position: relative; top: 0; }
        .h2-text { left: 20px; right: 20px; }
'''
def page2(key):
    p=PAGES[key]
    rows=''.join(f'<li class="reveal" style="--d:{i*70}ms">{x}<small>{i+1:02d}</small></li>' for i,x in enumerate(p['items']))
    return f'''<header class="h2wrap">
    <div class="media">{video(p["video"])}</div>
    <div class="veil"></div>
    <div class="h2-text">
        {crumb(p)}
        <h1><span class="rise"><span>{p["title"]}</span></span></h1>
        <p class="catch reveal" style="--d:300ms">{p["catch"]}</p>
    </div>
</header>
<main class="body2">
    <aside class="side2">
        <p class="tag reveal">Domaine {p["num"]}</p>
        <p class="intro reveal" style="--d:120ms">{p["intro"]}</p>
        <div class="reveal" style="--d:240ms"><a href="{IDX}#contact" class="btn"><span>Prendre rendez-vous</span>{ARROW}</a></div>
    </aside>
    <ul class="rows2">{rows}</ul>
</main>'''

# ═════ Design 3 — Fenêtre (vidéo encadrée en portrait) ═════
CSS3='''    .h3wrap { background: var(--nacre); padding: 150px 6vw 110px; }
    .h3-grid { max-width: 1300px; margin: 0 auto; display: grid; grid-template-columns: 1.15fr 0.85fr; gap: 6vw; align-items: center; }
    .h3-text { display: flex; flex-direction: column; gap: 28px; }
    .h3-text h1 { font-size: clamp(3.4rem, 6.8vw, 6.4rem); }
    .window { position: relative; aspect-ratio: 4 / 5; max-width: 100%; }
    .window .frame { position: absolute; inset: 0; overflow: hidden; }
    .window::before { content: ''; position: absolute; inset: -14px 14px 14px -14px; border: 1px solid rgba(114, 120, 95, 0.45); pointer-events: none; }
    .window figcaption { position: absolute; left: 0; bottom: -34px; font-size: 0.6rem; letter-spacing: 0.22em; text-transform: uppercase; color: var(--vert-dark); }
    .body3 { padding: 120px 6vw 110px; max-width: 1300px; margin: 0 auto; }
    .body3 .tag { margin-bottom: 30px; display: block; }
    .grid3 { list-style: none; display: grid; grid-template-columns: repeat(3, 1fr); gap: 0 4vw; }
    .grid3 li { border-top: 1px solid rgba(26, 26, 26, 0.14); padding: 24px 0 34px; }
    .grid3 li small { display: block; font-size: 0.64rem; letter-spacing: 0.16em; color: var(--vert); margin-bottom: 12px; font-variant-numeric: tabular-nums; }
    .grid3 li span { font-family: var(--display); font-size: 1.5rem; line-height: 1.2; }
'''
CSS3M='''        .h3-grid { grid-template-columns: 1fr; }
        .h3wrap { padding: 120px 20px 80px; }
        .body3 { padding: 80px 20px; }
        .grid3 { grid-template-columns: 1fr; }
'''
def page3(key):
    p=PAGES[key]
    cells=''.join(f'<li class="reveal" style="--d:{(i%3)*100}ms"><small>{i+1:02d}</small><span>{x}</span></li>' for i,x in enumerate(p['items']))
    return f'''<header class="h3wrap">
    <div class="h3-grid">
        <div class="h3-text">
            {crumb(p)}
            <h1><span class="rise"><span>{p["title"]}</span></span></h1>
            <p class="catch reveal" style="--d:300ms">{p["catch"]}</p>
            <p class="intro reveal" style="--d:420ms">{p["intro"]}</p>
            <div class="reveal" style="--d:540ms"><a href="{IDX}#contact" class="btn"><span>Prendre rendez-vous</span>{ARROW}</a></div>
        </div>
        <figure class="window reveal" style="--d:200ms">
            <div class="frame">{video(p["video"])}</div>
            <figcaption>Domaine {p["num"]}</figcaption>
        </figure>
    </div>
</header>
<main class="body3">
    <span class="tag reveal">Thématiques</span>
    <ul class="grid3">{cells}</ul>
</main>'''

GEN={1:(CSS1,CSS1M,page1),2:(CSS2,CSS2M,page2),3:(CSS3,CSS3M,page3)}
for key,p in PAGES.items():
    css,cssm,fn=GEN[p['design']]
    html=HEAD.format(title=p['title'],catch=p['catch'],css=css,css_m=cssm,idx=IDX,ddlinks=''.join(f'<a role="menuitem" href="{k}.html"'+(' class="cur"' if k==key else '')+f'>{PAGES[k]["title"]}<small>{PAGES[k]["num"]}</small></a>' for k in ORDER))+fn(key)+tail(key).replace('{extra_js}','')
    html=html.replace('{extra_js}','')
    open(OUT+key+'.html','w',encoding='utf-8').write(html)
    print(key, len(html))
