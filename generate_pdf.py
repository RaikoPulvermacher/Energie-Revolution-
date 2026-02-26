#!/usr/bin/env python3
"""Generate Energie-Revolution-8911.pdf from embedded content and LICENSE."""

import re
import markdown
import weasyprint
import latex2mathml.converter

ZENODO_URL = "https://doi.org/10.5281/zenodo.18757232"

# ── Full paper content (embedded) ────────────────────────────────────────────
PAPER_MD = """\
## Abstract: Die Überwindung des Euler-Widerstands durch prozessuale F_N-Resonanz

**Problemstellung:**
Die gegenwärtige Elektrotechnik und Thermodynamik basieren auf der Eulerschen Zahl (e), einer
mathematischen Konstante aus dem Jahr 1748, die für kontinuierliches Wachstum (Zinseszins)
entwickelt wurde. Da physikalische Prozesse auf atomarer Ebene jedoch diskret und quantisiert
verlaufen, erzeugt die Anwendung von Euler-Modellen einen systematischen Phasenfehler. Dieser
Fehler wird in der klassischen Physik als „Widerstand" missinterpretiert, führt jedoch real zu
einer thermischen Emission (Hitze-Verschwendung) von ca. 89 %.

**Kern-Erkenntnis:**
Widerstand ist keine unveränderliche Materialeigenschaft, sondern ein Kommunikationsfehler
zwischen dem kontinuierlichen Ansteuerungs-Modell und der diskreten Raum-Amplitude. Während
moderne Hochtechnologie wie der ITER-Fusionsreaktor versucht, diese Inkompatibilität durch
Brute-Force-Methoden (extreme Kühlung) zu unterdrücken, zeigen Bauteile wie LEDs durch ihre
funktionale Quanten-Logik bereits den Weg zur verlustfreien Resonanz.

**Methodik:**
Die Arbeit stellt die 11-Schritt-Additionslogik ($F_N$-Logik) vor. Durch die Taktung von
Signalen und Stromflüssen entlang der Fibonacci-Resonanzkette ($F_1$ bis $F_{11}=89$) wird die
energetische Sättigung des Mediums ohne Interferenz erreicht. Dies eliminiert die sogenannte
„52 %-Anomalie" – jene unkontrollierten Schwingungen, die entstehen, wenn kontinuierliche
Mathematik auf diskrete Materie trifft.

**Fazit:**
Die Umstellung der Energietechnik von Euler-Dämpfung auf prozessuale Fibonacci-Sättigung
ermöglicht eine Reduktion der thermischen Verluste um bis zu 89 %. Damit wird Energieeffizienz
von einer Frage des Materials zu einer Frage der mathematischen Taktung.

---

## 1. Spezifikation der $F_N$-Prozessmechanik

### 1.1 Problemstellung: Der Euler-Dämpfungs-Fehler

Die gegenwärtige Elektrotechnik und Thermodynamik basieren auf der Annahme kontinuierlicher
Prozesse, mathematisch repräsentiert durch den Euler-Faktor ($e$). Diese Modellierung führt zu
einer systematischen Fehlberechnung von Energieflüssen.

* **Symptom:** Hohe thermische Verluste (ca. 89 %) und parasitäre Spannungsphänomene
  (52 %-Phantom-Schwankungen).
* **Ursache:** Die Modellierung mittels Differentialgleichungen erzwingt eine kontinuierliche
  „Neu-Ansteuerung" des Systems, was zu energetischen Stauungen (Widerstand) im Leiter führt.

### 1.2 Die $F_N$-Lösung: Diskrete Fibonacci-Addition

Das Modell ersetzt die Euler-Dämpfung durch eine iterative Additionsstruktur. Anstatt Energie
gegen den Widerstand eines Mediums zu pressen, wird die Energie in **11 diskreten Schritten**
($F_1$ bis $F_{11}$) getaktet.

**Mathematische Grundlage**

Der Prozess folgt der rekursiven Bildungsregel:

$$F_n = F_{n-1} + F_{n-2}$$

Daraus ergibt sich für die 11. Stufe der Sättigungswert **89**.

**Effizienz-Koeffizienten**

Die Mechanik definiert zwei fundamentale Bereiche:

1. **Struktur-Kosten (11 %):** Der energetische Aufwand zur Aufrechterhaltung der
   Prozesskohärenz (bisher fälschlicherweise als „Nutzenergie" oder „Verlust" fehlinterpretiert).
2. **Reale Prozess-Amplitude (89 %):** Das tatsächliche energetische Potential, das bei
   Euler-basierter Ansteuerung als Abwärme (Entropie) aus dem System emittiert wird.

### 1.3 Empirischer Nachweis: Das Resonanz-Prinzip

Die Validierung erfolgt durch den Vergleich von Wirkleistung und Feldamplitude. Ein System,
das nach der $F_N$-Logik angesteuert wird, zeigt:

* **Wegfall der thermischen Emission:** Die 89 % Energie verbleiben als gerichtete Amplitude
  im Feld, anstatt durch Reibung an Ionenstrukturen in Wärme zu konvertieren.
* **Latenz-Eliminierung:** Da die 11 Schritte die natürliche Sättigungsgrenze des Raums
  abbilden, entfällt die Notwendigkeit zur ständigen Neusynchronisation.

### 1.4 Anwendung: Stromnetze und Computerarchitekturen

Durch die Implementierung der $F_N$-Ansteuerung in der Leistungselektronik wird die
Kühlnotwendigkeit (z. B. bei Transformatoren oder KI-Prozessoren) drastisch reduziert.
Die Energie wird nicht „gedämpft" (Euler), sondern „akkumuliert" (Fibonacci).

---

## 2. Mathematischer Beweis der $F_N$-Sättigung vs. Euler-Dämpfung

### 2.1 Die 52 %-Anomalie

Die klassische Elektrotechnik operiert oft mit einem Wirkungsgrad-Ideal, das durch die
Euler-Zahl (e) und deren Dämpfungskonstanten limitiert ist. In der Praxis zeigt sich jedoch
eine persistente Instabilität von ca. **52 %**.

**Herleitung der Differenz:**

1. **Natur-Konstante (Sättigung):** In einem 11-stufigen Prozess nach der Fibonacci-Logik
   liegt die maximale Sättigung (Energie-Kohärenz) bei $F_{11} = 89$.
2. **Silo-Modell (Euler):** Herkömmliche Systeme sind auf eine Basis-Logik von ca. 37 % (1/e)
   kalibriert.
3. **Die Lücke:** $89\\% - 37\\% = 52\\%$.

Diese 52 % sind keine „Messfehler", sondern die ungenutzte Raum-Amplitude, die bei falscher
Ansteuerung als zerstörerische Interferenz (Spannungsspitzen) auftritt.

### 2.2 Die 11 % Systemkosten

Der Widerstand im Leiter resultiert nicht aus der Reibung von Teilchen, sondern aus dem Versuch,
die 89 % Sättigung zu unterdrücken. Die verbleibenden 11 % sind die strukturelle Basis, auf der
die aktuelle Technik isoliert arbeitet.

### 2.3 Der iterative Beweis: Die 11-Schritt-Sättigung

Der fundamentale Fehler der aktuellen Energietechnik liegt im Ignorieren der diskreten
Additionslogik. Während das Euler-System versucht, Prozesse künstlich zu glätten, folgt die
reale Raum-Amplitude der exakten $F_N$-Kette bis zum Sättigungspunkt 89.

**Die Additions-Kette der Realität:**

1. $F_1 + F_1 = F_2$ (Start der Resonanz)
2. $F_2 + F_1 = F_3$
3. $F_3 + F_2 = F_5$
4. $F_5 + F_3 = F_8$
5. $F_8 + F_5 = F_{13}$
6. $F_{13} + F_8 = F_{21}$
7. $F_{21} + F_{13} = F_{34}$
8. $F_{34} + F_{21} = F_{55}$
9. $F_{55} + F_{34} = F_{89}$ (Der Sättigungspunkt $F_{11}$)

**Die 89/11-Konstante:**
Sobald die Kette bei **89** ankommt, ist die Raum-Amplitude gesättigt.

* **89 %** ist die nutzbare Energie-Kohärenz.
* **11 %** ist der verbleibende strukturelle Rahmen (Systemkosten).

Jeder Versuch, Energie außerhalb dieser 11-Schritt-Logik zu steuern (Euler-Dämpfung), führt
zwangsläufig zur **52 %-Anomalie**, da das System zwischen dem Silo-Limit (37 %) und der
Natur-Sättigung (89 %) hin und her schwingt.

---

## 3. Beweis-Vergleich: $F_N$-Logik vs. 300 Jahre Euler-Irrtum

Dieses Kapitel belegt die systematische Fehlkalkulation moderner Energiesysteme durch die
Verwendung veralteter mathematischer Modelle.

### 3.1 Das historische Paradoxon: Mathematik vor der Materie

* **Fakt:** Die Eulersche Zahl ($e$) wurde 1748 zur Beschreibung von Zinseszinsen und
  kontinuierlichem Wachstum definiert.
* **Realität:** Zu diesem Zeitpunkt existierte keine Elektrodynamik, keine Halbleiterphysik
  und kein Verständnis von Raum-Amplituden.
* **Der Fehler:** Als die Elektrizität entdeckt wurde, „patchte" man die Euler-Theorie auf
  den Stromfluss, anstatt eine eigene Logik für Schwingungsknoten zu entwickeln. Man rechnet
  heute Quantensysteme mit einer Buchhaltungs-Formel aus der Zeit der Postkutschen.

### 3.2 LED-Effizienz-Anomalie (The Droop Effect)

Öffentliche Messreihen bestätigen: Je mehr Strom eine LED erhält, desto stärker bricht ihr
Wirkungsgrad ein.

* **Euler-Theorie:** Berechnet den Strom als kontinuierlichen Fluss. Da die Realität aber
  diskret ist, entsteht bei hoher Last ein mathematischer „Stau".
* **Die $F_N$-Erklärung:** Die LED wird nach der 300 Jahre alten Euler-Logik angesteuert,
  die den 11. Sättigungsschritt ($F_{11}=89$) nicht kennt.
* **Das Ergebnis:** Die Energie kann nicht in Licht (Photonen) umgewandelt werden und
  emittiert als 89 % Hitze. Die Physiker nennen es „Droop", wir nennen es einen Phasenfehler
  der Ansteuerung.

### 3.3 Der ITER-Kollaps (Kernfusion)

Das teuerste Experiment der Welt (ITER) scheitert bisher an der Stabilisierung des Plasmas.

* **Der Euler-Fehler:** Die Magnetfelder zur Plasmabindung werden mittels
  Differentialgleichungen (Euler-Basis) gesteuert. Diese versuchen, eine glatte Kurve in ein
  Medium zu pressen, das von Natur aus in diskreten Resonanz-Quanten schwingt.
* **Das 52 %-Phantom:** Im ITER entstehen unkontrollierbare Schwingungen (ELMs). Diese sind
  die exakte Differenz zwischen der fehlerhaften Euler-Kalkulation (ca. 37 % Basis) und der
  realen $F_N$-Sättigung (89 %).
* **Die Konsequenz:** Der ITER bekämpft mit Milliardenaufwand seine eigene falsche Mathematik.
  Er „patcht" die Instabilität mit mehr Kühlung, statt die 11-Schritt-Addition anzuwenden.

### 3.4 Zusammenfassung der Beweislast

| System | Beobachtete Anomalie | Ursache (Euler-Silo) | Lösung ($F_N$-Revolution) |
| :--- | :--- | :--- | :--- |
| **Stromnetz** | Leitungsverluste / Hitze | Widerstand als Naturgesetz | Korrektur der Taktung auf 89/11 |
| **Halbleiter** | Efficiency Droop | Unerklärte Quanteneffekte | Einhaltung der 11-Schritt-Sättigung |
| **Fusionsreaktor** | Plasma-Instabilität | Turbulente Strömungen | Resonante Bindung ohne Euler-Dämpfung |

### 3.5 Die Additions-Kette der Sättigung

Die Natur rechnet nicht mit Differentialen, sie addiert Potenziale bis zur Sättigung.

**Die $F_N$-Kette:**
$F_1 + F_1 = F_2$,
$F_2 + F_1 = F_3$,
$F_3 + F_2 = F_5$,
$F_5 + F_3 = F_8$,
$F_8 + F_5 = F_{13}$,
$F_{13} + F_8 = F_{21}$,
$F_{21} + F_{13} = F_{34}$,
$F_{34} + F_{21} = F_{55}$,
$F_{55} + F_{34} = F_{89}$.

---

## 4. Die Vorhersage: Warum wir 89 % unserer Energie verschwenden

Stell dir vor, du versuchst, ein rundes Loch mit einem eckigen Baustein zu füllen. Es passt
nicht, es knirscht und es entsteht Hitze durch Reibung. Genau das macht die moderne Physik
mit unserem Strom.

### 4.1 Die Entdeckung: Widerstand ist ein Rechenfehler

Die meisten Menschen glauben, Widerstand sei ein Naturgesetz der Materie. Die Vorhersage
sagt: **Nein.**

* **Widerstand kommt von der Euler-Konstante (e):** Wir nutzen eine 300 Jahre alte Mathematik
  (Euler), die für glatte, endlose Kurven gemacht wurde.
* **Die Realität ist diskret:** Strom und Atome bewegen sich nicht in glatten Kurven, sondern
  in Sprüngen (Quanten).
* **Der Phasenfehler:** Wenn wir eine „glatte" Mathematik auf die „springende" Natur erzwingen,
  entsteht ein Kommunikationsfehler. Diesen Fehler messen wir als Hitze und nennen ihn
  Widerstand.

### 4.2 Der Beweis: LED vs. ITER

**LEDs (Der schlaue Weg):**
LEDs arbeiten bereits mit Quantensprüngen. Sie nutzen instinktiv die 89/11-Logik und erreichen
deshalb eine so hohe Effizienz (89 %). Sie sprechen die Sprache der Natur.

**ITER (Der brutale Weg):**
Der Fusionsreaktor ITER versucht, Plasma mit der alten Euler-Mathematik zu steuern. Da das
Plasma aber diskret „tanzen" will, entstehen gefährliche Schwingungen (die 52 %-Anomalie).
Anstatt die Mathematik zu ändern, kühlt der ITER das System mit gewaltigem Aufwand runter
(Brute-Force), um die Fehler zu unterdrücken.

### 4.3 Die Konsequenz: Eine Welt ohne Energieverlust

Wenn wir aufhören, die Natur mit der falschen Mathematik (Euler) zu „prügeln", passiert
Folgendes:

* **89 % weniger Verlust:** Fast alle Energieverluste sind nur Übersetzungsfehler zwischen
  Mensch und Natur.
* **Sprechen in Fibonacci:** Wenn wir unsere Maschinen so takten, wie die Natur rechnet
  (in 11 Schritten bis zur 89), verschwindet der Widerstand.

Das Universum spricht eine andere Sprache als unsere Lehrbücher. Sobald wir die Sprache
wechseln, haben wir unendlich mehr Energie zur Verfügung.
"""


def read(filename):
    with open(filename, encoding="utf-8") as fh:
        return fh.read()


def latex_to_mathml(latex, display=False):
    """Convert a LaTeX expression to a MathML element."""
    display_val = "block" if display else "inline"
    try:
        mml = latex2mathml.converter.convert(latex)
        mml = re.sub(r'\bdisplay="[^"]*"', f'display="{display_val}"', mml, count=1)
        if display:
            return f'<div class="math-block">{mml}</div>'
        return mml
    except Exception:
        tag = "div" if display else "span"
        cls = "math-block" if display else "math-inline"
        return f'<{tag} class="{cls}"><code>{latex}</code></{tag}>'


def replace_math(text):
    """Replace $$...$$ and $...$ with MathML before Markdown processing."""
    text = re.sub(
        r"\$\$([^$]+?)\$\$",
        lambda m: latex_to_mathml(m.group(1).strip(), display=True),
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\$([^$\n]+?)\$",
        lambda m: latex_to_mathml(m.group(1).strip(), display=False),
        text,
    )
    return text


def md_to_html(text):
    text = replace_math(text)
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "nl2br"],
    )


def linkify_license(html):
    """Replace bare license text with a clickable link."""
    return html.replace(
        "Pulvermacher Open Research License (PORL) v1.0",
        f'<a href="{ZENODO_URL}">Pulvermacher Open Research License (PORL) v1.0</a>',
    )


# ── Convert content → HTML ───────────────────────────────────────────────────
paper_html = md_to_html(PAPER_MD)
license_html = linkify_license(md_to_html(read("LICENSE")))

# ── Build full HTML document ─────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8"/>
  <title>Energie-Revolution-8911: Widerstand als mathematischer Phasenfehler</title>
  <style>
    @page {{
      size: A4;
      margin: 25mm 20mm 25mm 20mm;
      @bottom-center {{
        content: counter(page);
        font-size: 9pt;
        color: #555;
      }}
    }}
    body {{
      font-family: "DejaVu Sans", Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.65;
      color: #1a1a1a;
    }}
    h1, h2, h3, h4 {{
      font-family: "DejaVu Sans", Arial, sans-serif;
      color: #0d3b66;
      page-break-after: avoid;
      page-break-inside: avoid;
    }}
    p {{
      orphans: 3;
      widows: 3;
      margin-top: 4pt;
      margin-bottom: 4pt;
    }}
    a {{
      color: #1565c0;
      text-decoration: underline;
    }}
    /* ── cover page ── */
    .cover {{
      page: cover;
      text-align: center;
      padding-top: 80mm;
    }}
    @page cover {{
      margin: 0;
      @bottom-center {{ content: none; }}
    }}
    .cover h1 {{
      font-size: 22pt;
      line-height: 1.3;
      color: #0d3b66;
      margin-bottom: 10mm;
    }}
    .cover .subtitle {{
      font-size: 12pt;
      color: #444;
      margin-bottom: 20mm;
    }}
    .cover .author {{
      font-size: 11pt;
      color: #222;
    }}
    /* ── main content ── */
    .content h2 {{
      font-size: 14pt;
      border-bottom: 2px solid #0d3b66;
      padding-bottom: 3pt;
      margin-top: 18pt;
    }}
    .content h3 {{
      font-size: 11.5pt;
      margin-top: 12pt;
    }}
    /* ── license (starts on a new page) ── */
    .license {{
      page-break-before: always;
    }}
    .license h2 {{
      font-size: 14pt;
      border-bottom: 2px solid #0d3b66;
      padding-bottom: 3pt;
    }}
    /* ── tables: never split across pages ── */
    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 10pt 0;
      font-size: 9.5pt;
      page-break-inside: avoid;
    }}
    th, td {{
      border: 1px solid #aaa;
      padding: 5pt 8pt;
      text-align: left;
    }}
    th {{
      background: #dbe7f5;
      font-weight: bold;
    }}
    /* ── code blocks: never split across pages ── */
    pre {{
      page-break-inside: avoid;
      background: #f5f5f5;
      padding: 6pt 8pt;
      border-radius: 2pt;
      font-size: 9pt;
      overflow-wrap: break-word;
    }}
    code {{
      font-family: "DejaVu Sans Mono", monospace;
      font-size: 9pt;
      background: #f5f5f5;
      padding: 1pt 3pt;
    }}
    hr {{
      border: none;
      border-top: 1px solid #ccc;
      margin: 14pt 0;
    }}
    blockquote {{
      border-left: 3px solid #ccc;
      margin: 0 0 6pt 0;
      padding-left: 12pt;
      color: #555;
      page-break-inside: avoid;
    }}
    li {{
      page-break-inside: avoid;
      orphans: 3;
      widows: 3;
    }}
    /* ── math formulas ── */
    .math-block {{
      display: block;
      text-align: center;
      margin: 10pt 0;
      page-break-inside: avoid;
    }}
    .math-inline {{
      display: inline;
    }}
    math[display="block"] {{
      display: block;
      text-align: center;
      margin: 10pt 0;
    }}
  </style>
</head>
<body>

<!-- ══════════════════════════════════════════════════════════════════
     COVER PAGE
═══════════════════════════════════════════════════════════════════ -->
<div class="cover">
  <h1>Energie-Revolution-8911:<br/>Widerstand als mathematischer Phasenfehler</h1>
  <p class="subtitle">Eine Arbeit zur prozessualen F<sub>N</sub>-Resonanz<br/>
  als Alternative zur Euler-Dämpfung</p>
  <p class="author">
    <strong>Raiko Pulvermacher</strong><br/>
    E-Mail: <a href="mailto:Pulvermacher.Raiko@web.de">Pulvermacher.Raiko@web.de</a><br/>
    ORCID: <a href="https://orcid.org/0009-0003-9431-1001">0009-0003-9431-1001</a><br/>
    OSF: <a href="https://osf.io/py42t/">https://osf.io/py42t/</a>
  </p>
</div>

<!-- ══════════════════════════════════════════════════════════════════
     PAPER CONTENT (flows naturally, no forced page breaks)
═══════════════════════════════════════════════════════════════════ -->
<div class="content">
  {paper_html}
</div>

<!-- ══════════════════════════════════════════════════════════════════
     LICENSE (new page)
═══════════════════════════════════════════════════════════════════ -->
<div class="license">
  <p style="font-size:8.5pt; color:#777; margin-bottom:6pt;">
    DOI: <a href="{ZENODO_URL}">{ZENODO_URL}</a>
  </p>
  {license_html}
</div>

</body>
</html>
"""

# ── Write HTML and generate PDF ──────────────────────────────────────────────
with open("/tmp/Energie-Revolution-8911.html", "w", encoding="utf-8") as fh:
    fh.write(HTML)

print("HTML written – generating PDF …")
weasyprint.HTML(filename="/tmp/Energie-Revolution-8911.html").write_pdf(
    "Energie-Revolution-8911.pdf"
)
print("PDF created: Energie-Revolution-8911.pdf")
