**Why Should This Work?**

Achtergrond bij de challenge — voor de studentengroep

*Geert Crombez* *& Emma Tack, Ghent Health Psychology Lab*

---

**Het probleem**

Een gezondheidsapp die werkt maar niet kan zeggen waarom, is bijna even onbruikbaar als een die niet werkt. Je kan er niets uit leren, niets aan verbeteren, en niets van overdragen naar een volgende context of doelgroep.

In de praktijk zit de redenering achter zo'n app wel ergens, maar niet in het systeem: in een rapport, een slideset, het hoofd van de ontwerper. Zodra de app gebouwd is, kan niemand nog nagaan welke feature welke determinant moest veranderen, of dat ook gelukt is, en of er ongewenste effecten bijkwamen.

White box betekent hier: de programmatheorie zit *in* het systeem — machineleesbaar, bevraagbaar en toetsbaar — en niet in een document ernaast.

**Twee soorten black box**

Het loont om die twee meteen uit elkaar te houden, want de tweede is het eigenlijke onderwerp van deze challenge.

1. **Het model is ondoorzichtig.** Gewichten in een netwerk, geen zicht op waarom een voorspelling is wat ze is. Daar bestaat een antwoord voor: bouw het interpreteerbaar in plaats van het achteraf uit te leggen.

2. **De redenering staat nergens.** Er is geen plek in het systeem waar staat: deze feature mikt op deze determinant, bij deze persoon, in deze fase, met deze verwachting. Dat probleem bestaat ook in apps met volledig transparante regels, en het is het moeilijkere van de twee.

**Let op het verschil met explainable AI.** Een SHAP-plot vertelt welke variabelen het model gebruikte. Het zegt niets over welke veronderstelling over gedragsverandering erachter zat, en al zeker niet of die klopt. Uitleg over een correlatiemachine blijft een uitspraak over het model, niet over de wereld.

**Causaal redeneren: waarom een keten niet volstaat**

De standaardvoorstelling is een keten: techniek → determinant → gedrag → gezondheidsuitkomst. Die keten is een goed vertrekpunt en ze bestaat al in machineleesbare vorm, in de BCT-taxonomie en de Behaviour Change Intervention Ontology. Je hoeft dus niet van nul te beginnen.

Maar de keten alleen is misleidend. Een oorzaak is zelden voldoende en zelden noodzakelijk. Ze is doorgaans een onmisbaar onderdeel van een bundel die samen voldoende is, terwijl die bundel zelf niet noodzakelijk is, want er bestaan andere bundels die hetzelfde effect geven. Rothman tekent dat als causale taarten: elke taart is een voldoende verzameling componenten, elke punt is noodzakelijk binnen die taart, en geen enkele taart is noodzakelijk.

Concreet: een herinnering veroorzaakt geen gedrag. Een herinnering samen met een concreet plan, een moment zonder tijdsdruk en een omgeving die het toelaat, kan wel volstaan. En er is een tweede bundel die het zonder herinnering doet, bijvoorbeeld een vaste context-cue in een omgeving die het gedrag vanzelf uitlokt.

Vier gevolgen voor je ontwerp:

1. **Representeer conjuncties én disjuncties.** Het model is een verzameling recepten — elk een combinatie van voorwaarden die samen volstaan — en niet één keten van pijlen. Een graaf met alleen enkelvoudige verbindingen kan dat niet uitdrukken.

2. **"Werkt deze techniek?" is de verkeerde vraag.** De juiste is: in welke combinatie, bij wie, in welke context. Een gemiddeld effect over alle gebruikers verbergt precies de informatie die je nodig hebt.

3. **Personalisatie wordt een zoekprobleem.** Voor deze persoon: welke voldoende bundel is het goedkoopst te vervolledigen, en welk element ontbreekt er nog? Dat is een scherpere en beter implementeerbare formulering van tailoring dan "de juiste boodschap op het juiste moment".

4. **De evaluatie moet mee.** Een lineair mediatiemodel vindt configuraties niet. Wat wel past: factoriële opzetten waarin componenten gecombineerd worden, micro-randomisatie over combinaties in het dagelijks leven, en configurationele analyse waarin je expliciet zoekt naar voldoende verzamelingen van condities.

**De fase hoort in het model, niet ernaast**

Motivatieopbouw, gedragsverandering en gedragsbehoud vragen elk een ander proximaal doel. Dezelfde techniek heeft daardoor in fase 1 een ander effect dan in fase 2, soms een negatief: planningsondersteuning geven aan iemand die nog niet overtuigd is, demotiveert. De fase maakt dus deel uit van de condities die bepalen welke bundel voldoende is, en elke claim in je model draagt best een conditie die zegt in welke fase ze geldt.

| **Fase** | **Proximale uitkomst** | **Typische voldoende bundel** | **Wat het systeem moet kunnen** |
| --- | --- | --- | --- |
| **1. Kennis- en motivatieopbouw** | Risicoperceptie, uitkomstverwachtingen, vertrouwen in eigen kunnen, intentie | Relevante en persoonlijke informatie + geloofwaardige bron + zicht op de eigen situatie + geen moralisering | Niet aansporen tot actie; meten of intentie en vertrouwen bewegen |
| **2. Gedragsverandering** | Actieplan, eerste uitvoering, omgaan met obstakels | Plan + cue op een haalbaar moment + gelegenheid + coping bij het obstakel | Leveren op ontvankelijke momenten; nagaan of het gedrag effectief volgt |
| **3. Gedragsbehoud** | Automatisme, herstel na terugval, omgeving die meewerkt | Stabiele context-cue + waarde in het gedrag zelf + steunende omgeving + herstelplan | Ondersteuning afbouwen; terugval detecteren en tijdelijk terugschakelen |
Fasen zijn geen eenrichtingsverkeer. Een drukke periode of een nieuwe job zet iemand terug in een vorige fase, en dat hoort in het model te zitten in plaats van als uitzondering behandeld te worden.

**Zet ook de ongewenste paden in het model**

Schuldgevoel, irritatie, afhankelijkheid van de app, compensatiegedrag, het verschuiven van verantwoordelijkheid naar het individu. Een model dat alleen de bedoelde effecten bevat, is een half model — en het zijn net de onbedoelde effecten die niemand achteraf nog kan terugvinden in de code. In de gezondheidspsychologie heet dat *dark logic*: vooraf bedenken wat er mis kan gaan hoort bij het ontwerpen.

**Wat zo'n systeem concreet kan bevatten**

Geen eisenlijst — jullie kiezen zelf waar het zwaartepunt ligt.

- **Kennislaag.** Determinanten, technieken, features, contexten en uitkomsten als expliciete entiteiten, met relaties die een verwachte richting, een conditie en een sterkte dragen.

- **Herkomst.** Bij elke claim: komt ze uit een meta-analyse, uit één studie, of uit de intuïtie van de ontwerper? Dat verschil zichtbaar maken is op zich al waardevol, want het is nu nergens zichtbaar.

- **Redeneerlaag.** Gegeven de toestand van deze persoon: welke bundels zijn nog haalbaar, en wat is de eerstvolgende ontbrekende schakel?

- **Voorspellingslaag.** Elke levering doet een expliciete voorspelling over de proximale uitkomst. Zonder voorspelling valt er niets te weerleggen en blijft het een mooi schema.

- **Leerlaag.** De geloofwaardigheid van claims wordt bijgesteld op basis van data. Het cruciale kenmerk: wat bijgewerkt wordt is de claim, niet een verborgen gewicht.

- **Experimenteerlaag.** Waar de onzekerheid het grootst is, randomiseert het systeem. Het stelt dus zijn eigen volgende experiment voor.

- **Uitleglaag voor twee publieken.** Voor de gebruiker: waarom zie ik dit? Voor de ontwerper: welke van onze aannames is gesneuveld?

**Schaal:** een werkend prototype met vijf determinanten en tien technieken is meer waard dan een onvolledige ontologie van tweehonderd klassen.

**Met wie praten**

Deze challenge heeft twee gebruikersgroepen. De eindgebruiker van de interventie, en — belangrijker hier — de ontwerper of onderzoeker die interventies bouwt en moet kunnen zien waarom iets werkt of faalt. Studenten gezondheidsbevordering maken elk jaar determinantenanalyses en programmatheorieën, en lopen precies tegen dit probleem aan; ook zij zijn dus een bruikbare gesprekspartner.

**Wat een sterk resultaat is**

Een systeem waaraan je kan vragen waarom deze persoon dit kreeg, welke aanname erachter zat, en of die klopte. Als demonstratiecriterium: laat het systeem minstens één van zijn eigen aannames verwerpen op basis van de data. Dat is overtuigender dan eender welke interface.

**Om te beginnen**

- Rothman, K. J. (1976). Causes. *American Journal of Epidemiology, 104*(6), 587–592. — zes bladzijden met een tekening: waarom oorzaken bundels zijn en waarom er meerdere bundels bestaan.

- Cartwright, N. (2011). A philosopher's view of the long road from RCTs to effectiveness. *The Lancet, 377*(9775), 1400–1401. — twee bladzijden over het verschil tussen "het werkte daar" en "het werkt hier". Belangrijk zodra je bevindingen uit de literatuur in een systeem stopt.

- Carey, R. N., e.a. (2019). Behavior change techniques and their mechanisms of action. *Annals of Behavioral Medicine, 53*(8), 693–707. — de koppelingen tussen technieken en mechanismen, uit de literatuur gehaald. Letterlijk een startgraaf, met de waarschuwing dat bijna geen van die koppelingen empirisch getoetst is.

- Michie, S., e.a. (2021). Development of the upper level of the Behaviour Change Intervention Ontology. *Wellcome Open Research, 5*, 123. — het bestaande machineleesbare begrippenkader.

- Rudin, C. (2019). Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead. *Nature Machine Intelligence, 1*(5), 206–215. — waarom post-hoc uitleg geen vervanging is voor een interpreteerbaar model.

Contact: geert.crombez@ugent.be
