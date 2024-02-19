# Teplotní ztráty

<p>Program řeší výpočet teplotních ztrát a porovnává je s katalogem dostupných izolací dle tohoto zadání:

<i>Do hořáku proudí 1500 m3/hod. zemního plynu. Jako okysličovadlo je použit atmosférický vzduch o relativní vlhkosti 50%. Teplota okysličovadla i plynu je 40 °C a míchání probíhá za
atmosférického tlaku (101325 Pa).</i> </p>

<ul>
    <li>Průměrná teplota uvnitř $T_{in}$ = 22 &deg;C</li>
    <li> Průměrná teplota venku $T_{out}$ = 6 &deg;C </li>
    <li>Plocha stěny $S$ = 200 m<sup>2</sup></li>
    <li>Tepelná vodivost železobetonu $\lambda_{bet}$ = 1,43 W&middot;m<sup>-1</sup>&middot;K<sup>-1</sup></li>
    <li>Tepelná vodivost perlitové omítky $\lambda_{per}$ = 0,1 W&middot;m<sup>-1</sup>&middot;K<sup>-1</sup></li>
    <li>Tepelná vodivost vápenné omítky $\lambda_{vap}$ = 0,88 W&middot;m<sup>-1</sup>&middot;K<sup>-1</sup></li>
    <li>Součinitel přestupu tepla na vnitřní straně $\alpha_{in}$ = 7 W&middot;m<sup>-2</sup>&middot;K<sup>-1</li>
    <li>Součinitel přestupu tepla na vnější straně $\alpha_{out}$ = 17 W&middot;m<sup>-2</sup>&middot;K<sup>-1</li>
    <li>Tloušťka stěny $\delta_{bet}$ = 0,2 m</li>
    <li>Tloušťka izolace $\delta_{izol}$ = 0,1 m</li>
    <li>Tloušťka perlitové omítky $\delta_{per}$ = 0,015 m</li>
    <li>Tloušťka vápenné omítky $\delta_{vap}$ = 0,015 m</li>
    <li>Cena plynu $C_{plyn}$ = 4 Kč&middot;kWh<sup>-1</li>
    <li>Tepelná vodivost a cena za 1 m<sup>2</sup> izolace viz katalog.</li>
</ul>

<p>Program je rozdělen do dvou souboru data.py a tep_ztraty.ipynb. První soubor je skript v Pythonu, který z staženého souboru HTML importuje data a následně je uloží do excelového souboru data.xlsx pomocí knihovny Pandas. Vzhledem k tomu, že vstupní data obsahují množství nepřesností, jsou opravy provedeny přímo v kódu. Druhý soubor je Jupyter Notebook, který načítá data z Excelu a pomocí Python kódu, společně s teoretickým vysvětlením a zadáním úkolu, tato data analyzuje a zobrazuje v konečném grafu.</p>

<p>Z důvodů udržení stálosti výsledků v čase, například kvůli možným změnám na webu poskytovatele, byl preferován import dat z již stažených HTML souborů. Ve skutečnosti by bylo efektivnější extrahovat data přímo z webových stránek pomocí nástrojů pro web scraping, jako je Beautiful Soup, a zavést systém pro ověřování dat namísto jejich přímé úpravy v kódu. Možným řešením by bylo, v případě, že určité hodnoty přesáhnou očekávané limity, ukládat je do odděleného souboru pro ruční revizi nebo je z analýzy vyloučit. Zároveň by bylo vhodné zvážit použití SQL databáze namísto ukládání dat do Excelových souborů.</p>

<p>Program vznikl jako součást mé bakalářské práce (odkaz <a href="https://www.vut.cz/studenti/zav-prace/detail/116680">zde</a>) jež měl ukázat využití Pythonu pro technické výpočty konkrétně z pohledu procesního inženýrství.
Další programy z této práce:</p>

<ul>
    <li><a href="https://github.com/JanKomis/vyparovani">Částečné vypařování</a></li>
    <li><a href="https://github.com/JanKomis/spalovaniJupyter">Spalování zemního plynu</a></li>
    <li><a href="https://github.com/JanKomis/vyparnikH2O">Výparník H2O</a></li>
    <li><a href="https://github.com/JanKomis/vypousteniNadrze">Vypouštění nádrže</a></li>
</ul>

# Vytvořeno pomocí

<p align="left">
<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" height="36" alt="CSS3" /></a>
<a href="https://jupyter.org" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/640px-Jupyter_logo.svg.png" height="36" alt="Jupyter" /></a>
<a href="https://jupyter.org" target="_blank" rel="noreferrer"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Microsoft_Excel_2013-2019_logo.svg/2170px-Microsoft_Excel_2013-2019_logo.svg.png" height="36" alt="Jupyter" /></a>
<a href="https://pandas.pydata.org" target="_blank" rel="noreferrer"><img src="https://github.com/JanKomis/teplotniZtraty/assets/48412748/2ec047f2-65a4-48b3-8b24-8982e95578cd" height="36" alt="Jupyter" /></a>


</p>

