---
title: "Event ontology"
subtitle: ""
summary: "Definitions of the event classes that Globalise uses to classify events in the VOC archives, grouped into seven categories."
type: "page"
slug: "event-ontology"
status: "draft"

authors: []
datePublished: ""
dateUpdated: "2026-11-16"

featured: false

hero:
  src: ""
  alt: ""
  caption: ""
  credit: ""
  source: ""
  licence: ""

related: ["data-model-and-ontologies", "globalise-data", "how-the-data-was-produced", "technical-documentation"]
---

# Event ontology

<!-- Sources: categories, class labels and definitions from draft v3 in https://github.com/globalise-huygens/glob-portal-infomodel/issues/149 (comments of 2026-11-12 by Stella Verkijk); event type identifiers in the live event annotations (e.g. https://data.globalise.huygens.knaw.nl/hdl:20.500.14722/annotations:events:NL-HaNA_1.04.02_1056_0125), retrieved 2026-11-16. -->

<!-- TODO: anchors and identifiers. Every class has an explicit anchor (<a id="..."></a>) on the line before its heading, so that persistent URIs such as https://w3id.org/globalise/BeingAtAPlace can redirect to this page (…/event-ontology#BeingAtAPlace). Rules:
  * The anchor must be exactly the local name of the class as used in the ontology's .ttl file. Anchors are case-sensitive: BeingAtAPlace and beingAtAPlace are different anchors.
  * Check that the same names are used everywhere else: the .ttl file, the w3id redirect rules (perma-id/w3id.org), the event annotations on the portal and the old wiki. The live annotations currently link to https://github.com/globalise-huygens/nlp-event-detection/wiki#Translocation (classified_as), which matches the anchors here; but their "type" field holds other names (e.g. "Voyage", "CorrespondenceEvent") that do not appear in this list. Decide which identifier is authoritative and update the data to point to the w3id URIs.
  * Do not rely on the anchors that the portal generates from headings: they are based on the English label, which may change.
  * Never change or remove an anchor once it is published. If a class is renamed, keep the old anchor as an extra <a id> so that existing links keep working.
  * HavingInternalState+ and HavingInternalState- contain "+" and "-", which are awkward in URIs and HTML ids. Check their local names in the .ttl file and use those.
  * Check that the portal's markdown renderer keeps raw <a id> elements (some renderers strip HTML).
  * If the categories also get URIs, give them explicit anchors in the same way. -->

This page defines the classes of the Globalise **event ontology**: the types of events, such as a ship arriving, goods being traded or someone falling ill, that the event detection models recognise in the VOC archives. Each event annotation on the portal is classified with one of these classes. For how the ontology fits into the Globalise data model, see [The event ontology](/pages/research-responsibly/data/data-model.md#the-event-ontology) on the Data model & ontologies page.

The ontology distinguishes **dynamic events**, which change a situation (such as *Arriving* or *Buying*), from **static events**, situations that hold for some time (such as *Being at a place* or *Having in possession*). On the portal, the classes are grouped into seven categories. Each class has an English and a Dutch label; the name in `code` is the class name in the ontology.

## Categories

| Category | Dutch | Description |
| --- | --- | --- |
| [Movement & transport](#movement-transport) | Verplaatsing en vervoer | Movement of people, ships and goods (departures, arrivals, voyages, shipments). |
| [Possession, trade, finances](#possession-trade-finances) | Bezit, handel, financiën | Having something in one's possession and handing it over: giving, receiving, gifts and losing possession. Producing, trading, buying, selling and financial transactions. |
| [Communication & meetings](#communication-meetings) | Communicatie en ontmoetingen | Exchanging information, deliberating and requesting, and people or ships meeting or visiting each other. |
| [Relations, employment, leadership](#relations-employment-leadership) | Relaties, beroep, leiderschap | Relations between people, groups or polities: alliances, cooperation, contracts and treaties, and how these begin, change or end. Employment and (changes in) leadership. |
| [Coercion, control, punishment](#coercion-control-punishment) | Dwang, controle, bestraffing | Taking control of people or property against their will: arrest, seizure, enslavement, coercion and punishment. |
| [Conflict & violence](#conflict-violence) | Conflict en geweld | Disputes, wars, attacks, sieges, killings, and uprisings and mutinies. |
| [Improvement & deterioration](#improvement-deterioration) | Verbetering en verslechtering | Illness, injury, recovery and death of people or animals. Damage, destruction, shipwreck and repair of objects such as ships, buildings or crops, and other changes for the better or worse. |

<a id="movement-transport"></a>

## Movement & transport

*Dutch: Verplaatsing en vervoer*

Movement of people, ships and goods (departures, arrivals, voyages, shipments).

<a id="Translocation"></a>

### Movement

`Translocation` · Dutch: *Verplaatsing*

A person, ship or object moves from one place to another.

*Dutch definition:* Een persoon, schip of voorwerp gaat van de ene naar de andere plaats.

<a id="Leaving"></a>

### Departure

`Leaving` · Dutch: *Vertrek*

Someone or something leaves a place, for example a ship setting sail.

*Dutch definition:* Iemand of iets verlaat een plaats, bijvoorbeeld een schip dat uitzeilt.

<a id="Arriving"></a>

### Arrival

`Arriving` · Dutch: *Aankomst*

Someone or something arrives at a place, for example a ship reaching port.

*Dutch definition:* Iemand of iets komt aan op een plaats, bijvoorbeeld een schip dat een haven bereikt.

<a id="Voyage"></a>

### Voyage

`Voyage` · Dutch: *Reis*

A ship or group of ships makes a longer journey.

*Dutch definition:* Een schip of groep schepen maakt een langere tocht.

<a id="Transportation"></a>

### Transport

`Transportation` · Dutch: *Vervoer*

People or goods are carried somewhere, for example cargo being loaded and shipped.

*Dutch definition:* Personen of goederen worden ergens heen gebracht, bijvoorbeeld lading die wordt ingeladen en verscheept.

<a id="BeingAtAPlace"></a>

### Presence at a place

`BeingAtAPlace` · Dutch: *Aanwezigheid op een plaats*

Someone or something is, or stays, at a particular place.

*Dutch definition:* Iemand of iets bevindt zich of verblijft op een bepaalde plaats.

<a id="possession-trade-finances"></a>

## Possession, trade, finances

*Dutch: Bezit, handel, financiën*

Having something in one's possession and handing it over: giving, receiving, gifts and losing possession. Producing, trading, buying, selling and financial transactions.

<a id="ChangeOfPossession"></a>

### Change of ownership

`ChangeOfPossession` · Dutch: *Overgang van bezit*

Something or someone passes from one owner or holder to another.

*Dutch definition:* Iets of iemand gaat over van de ene eigenaar of houder naar de andere.

<a id="Giving"></a>

### Giving

`Giving` · Dutch: *Geven*

Someone gives something or someone to another person or party, for example a gift.

*Dutch definition:* Iemand geeft iets of iemand aan een ander, bijvoorbeeld een geschenk.

<a id="Getting"></a>

### Receiving

`Getting` · Dutch: *Ontvangen*

Someone gets or receives something, for example goods, letters or news.

*Dutch definition:* Iemand krijgt of ontvangt iets, bijvoorbeeld goederen, brieven of berichten.

<a id="Trade"></a>

### Trade

`Trade` · Dutch: *Handel*

Goods change owner in exchange for money or other goods.

*Dutch definition:* Goederen wisselen van eigenaar in ruil voor geld of andere goederen.

<a id="Buying"></a>

### Purchase

`Buying` · Dutch: *Aankoop*

Someone buys something or someone, paying with money or goods.

*Dutch definition:* Iemand koopt iets of iemand en betaalt met geld of goederen.

<a id="Selling"></a>

### Sale

`Selling` · Dutch: *Verkoop*

Someone sells something or someone in exchange for money or goods.

*Dutch definition:* Iemand verkoopt iets of iemand in ruil voor geld of goederen.

<a id="FinancialTransaction"></a>

### Payment

`FinancialTransaction` · Dutch: *Betaling*

Money changes hands, for example a payment, loan or settlement of accounts.

*Dutch definition:* Geld wisselt van eigenaar, bijvoorbeeld bij een betaling, lening of vereffening.

<a id="LosingPossession"></a>

### Loss of possession

`LosingPossession` · Dutch: *Verlies van bezit*

Someone loses something they owned or held.

*Dutch definition:* Iemand raakt iets kwijt dat hij of zij bezat of onder zich had.

<a id="Production"></a>

### Production

`Production` · Dutch: *Productie*

A commodity is made, grown or built.

*Dutch definition:* Een product wordt gemaakt, verbouwd of gebouwd.

<a id="HavingInPossession"></a>

### Possession

`HavingInPossession` · Dutch: *Bezit*

Someone holds something or someone for a period of time, for example goods in stock.

*Dutch definition:* Iemand heeft iets of iemand gedurende een periode in bezit of in bewaring, bijvoorbeeld goederen in voorraad.

<a id="BeingInDebt"></a>

### Debt

`BeingInDebt` · Dutch: *Schuld*

A person or organisation owes money.

*Dutch definition:* Een persoon of organisatie heeft een schuld.

<a id="communication-meetings"></a>

## Communication & meetings

*Dutch: Communicatie en ontmoetingen*

Exchanging information, deliberating and requesting, and people or ships meeting or visiting each other.

<a id="Communication"></a>

### Communication

`Communication` · Dutch: *Communicatie*

Information is exchanged: speaking, writing, reporting, discussing or deciding.

*Dutch definition:* Er wordt informatie uitgewisseld: spreken, schrijven, berichten, overleggen of besluiten.

<a id="Request"></a>

### Request

`Request` · Dutch: *Verzoek*

Someone asks for something.

*Dutch definition:* Iemand vraagt om iets.

<a id="Encounter"></a>

### Encounter

`Encounter` · Dutch: *Ontmoeting*

People, organisations or ships meet, either planned or by chance.

*Dutch definition:* Personen, organisaties of schepen komen elkaar tegen, gepland of toevallig.

<a id="Visit"></a>

### Visit

`Visit` · Dutch: *Bezoek*

Someone visits a person or organisation. This includes diplomatic visits.

*Dutch definition:* Iemand bezoekt een persoon of organisatie, ook diplomatieke bezoeken.

<a id="SocialInteraction"></a>

### Other interaction

`SocialInteraction` · Dutch: *Overige interactie*

People interact in a way that fits no more specific class.

*Dutch definition:* Mensen hebben contact op een manier die niet onder een specifiekere klasse valt.

<a id="relations-employment-leadership"></a>

## Relations, employment, leadership

*Dutch: Relaties, beroep, leiderschap*

Relations between people, groups or polities: alliances, cooperation, contracts and treaties, and how these begin, change or end. Employment and (changes in) leadership.

<a id="BeginningARelationship"></a>

### Start of a relationship

`BeginningARelationship` · Dutch: *Begin van een relatie*

People or organisations start a relationship, for example through a marriage or alliance.

*Dutch definition:* Personen of organisaties gaan een relatie aan, bijvoorbeeld door een huwelijk of bondgenootschap.

<a id="AlteringARelationship"></a>

### Intentional change in a relationship

`AlteringARelationship` · Dutch: *Opzettelijke verandering in een relatie*

A continuing relationship changes.

*Dutch definition:* Een voortdurende relatie verandert.

<a id="RelationshipChange"></a>

### Change in a relationship (general)

`RelationshipChange` · Dutch: *Verandering in een relatie (algemeen)*

A relationship begins, changes or ends.

*Dutch definition:* Een relatie begint, verandert of eindigt.

<a id="EndingARelationship"></a>

### End of a relationship

`EndingARelationship` · Dutch: *Einde van een relatie*

People or organisations end a relationship.

*Dutch definition:* Personen of organisaties beëindigen een relatie.

<a id="BeginningContractualAgreement"></a>

### Concluding an agreement

`BeginningContractualAgreement` · Dutch: *Sluiten van een overeenkomst*

Parties enter into an agreement, contract or treaty.

*Dutch definition:* Partijen sluiten een overeenkomst, contract of verdrag.

<a id="ExtendingContractualAgreement"></a>

### Extending an agreement

`ExtendingContractualAgreement` · Dutch: *Verlengen van een overeenkomst*

An existing agreement is extended or renewed.

*Dutch definition:* Een bestaande overeenkomst wordt verlengd of vernieuwd.

<a id="EndingContractualAgreement"></a>

### Ending or breaking an agreement

`EndingContractualAgreement` · Dutch: *Beëindigen of verbreken van een overeenkomst*

An agreement ends, either by mutual consent or because one party breaks it.

*Dutch definition:* Een overeenkomst eindigt, in onderling overleg of doordat een partij haar verbreekt.

<a id="JoiningAnOrganization"></a>

### Entering service

`JoiningAnOrganization` · Dutch: *In dienst treden*

Someone starts working for an organisation.

*Dutch definition:* Iemand gaat werken voor een organisatie.

<a id="LeavingAnOrganization"></a>

### Leaving service

`LeavingAnOrganization` · Dutch: *Uit dienst treden*

Someone stops working for an organisation.

*Dutch definition:* Iemand stopt met werken voor een organisatie.

<a id="Replacing"></a>

### Replacement

`Replacing` · Dutch: *Vervanging*

Someone or something is replaced by another in a position or role.

*Dutch definition:* Iemand of iets wordt in een functie of rol vervangen door een ander.

<a id="Mismanagement"></a>

### Mismanagement

`Mismanagement` · Dutch: *Wanbestuur*

A region is badly governed or managed.

*Dutch definition:* Een gebied wordt slecht bestuurd of beheerd.

<a id="BeingInARelationship"></a>

### Relationship

`BeingInARelationship` · Dutch: *Relatie*

People or organisations are in some kind of relationship, for example family ties, friendship or alliance.

*Dutch definition:* Personen of organisaties staan in een of andere relatie tot elkaar, bijvoorbeeld familie, vriendschap of bondgenootschap.

<a id="Collaboration"></a>

### Cooperation

`Collaboration` · Dutch: *Samenwerking*

People, organisations or polities work together, not always voluntarily.

*Dutch definition:* Personen, organisaties of rijken werken samen, niet altijd vrijwillig.

<a id="HavingContractualAgreement"></a>

### Agreement

`HavingContractualAgreement` · Dutch: *Overeenkomst*

Parties are bound by an agreement, contract or treaty.

*Dutch definition:* Partijen zijn gebonden aan een overeenkomst, contract of verdrag.

<a id="BeingAtPeace"></a>

### Peace

`BeingAtPeace` · Dutch: *Vrede*

Two parties are explicitly at peace with each other.

*Dutch definition:* Twee partijen leven uitdrukkelijk in vrede met elkaar.

<a id="BeingLeader"></a>

### Leadership

`BeingLeader` · Dutch: *Leiderschap*

Someone leads a group, organisation or territory, for example as ruler or commander.

*Dutch definition:* Iemand staat aan het hoofd van een groep, organisatie of gebied, bijvoorbeeld als vorst of bevelhebber.

<a id="BeingEmployed"></a>

### Employment

`BeingEmployed` · Dutch: *Dienstverband*

Someone holds a position and is paid for their work.

*Dutch definition:* Iemand bekleedt een functie en wordt voor het werk betaald.

<a id="coercion-control-punishment"></a>

## Coercion, control, punishment

*Dutch: Dwang, controle, bestraffing*

Taking control of people or property against their will: arrest, seizure, enslavement, coercion and punishment.

<a id="TakingUnderControl"></a>

### Seizure or arrest

`TakingUnderControl` · Dutch: *Inbeslagname of arrestatie*

Someone takes control of a person, group or thing, for example arresting someone or seizing a ship.

*Dutch definition:* Iemand krijgt een persoon, groep of zaak in zijn macht, bijvoorbeeld door iemand te arresteren of een schip in beslag te nemen.

<a id="Enslaving"></a>

### Enslavement

`Enslaving` · Dutch: *Tot slaaf maken*

People are enslaved: taken and held as property.

*Dutch definition:* Mensen worden tot slaaf gemaakt: gevangengenomen en als bezit behandeld.

<a id="ForceToAct"></a>

### Coercion

`ForceToAct` · Dutch: *Dwang*

Someone forces another party to do, or not do, something, with a stated or implied threat. Ordinary orders do not count.

*Dutch definition:* Iemand dwingt een ander iets te doen of te laten, met een uitgesproken of impliciete dreiging. Gewone bevelen vallen hier niet onder.

<a id="Punishing"></a>

### Punishment

`Punishing` · Dutch: *Bestraffing*

Someone is punished by an authority, for example by a court sentence or physical punishment.

*Dutch definition:* Iemand wordt gestraft door een autoriteit, bijvoorbeeld door een vonnis of lijfstraf.

<a id="Occupation"></a>

### Occupation

`Occupation` · Dutch: *Bezetting*

Holding control over (a) person(s) or a territory. For example, an armed group holding control over an area.

*Dutch definition:* Controle houden over een persoon of personen of een gebied. Bijvoorbeeld een gewapende groep die een gebied onder controle houdt.

<a id="conflict-violence"></a>

## Conflict & violence

*Dutch: Conflict en geweld*

Disputes, wars, attacks, sieges, killings, and uprisings and mutinies.

<a id="StartingConflict"></a>

### Outbreak of a conflict

`StartingConflict` · Dutch: *Ontstaan van een conflict*

A conflict or dispute begins.

*Dutch definition:* Een conflict of geschil begint.

<a id="EndingConflict"></a>

### End of a conflict

`EndingConflict` · Dutch: *Einde van een conflict*

A conflict or dispute comes to an end.

*Dutch definition:* Een conflict of geschil wordt beëindigd.

<a id="StartingAWar"></a>

### Outbreak of war

`StartingAWar` · Dutch: *Uitbreken van een oorlog*

An armed conflict begins between rulers, polities, the Company or other parties.

*Dutch definition:* Een gewapend conflict begint tussen vorsten, rijken, de Compagnie of andere partijen.

<a id="ViolentContest"></a>

### Violent confrontation

`ViolentContest` · Dutch: *Gewelddadige confrontatie*

Two parties clash using violence.

*Dutch definition:* Twee partijen treden elkaar met geweld tegemoet.

<a id="Attacking"></a>

### Attack

`Attacking` · Dutch: *Aanval*

Someone or something is attacked with the intention to cause harm.

*Dutch definition:* Iemand of iets wordt aangevallen met de bedoeling schade toe te brengen.

<a id="Besieging"></a>

### Siege

`Besieging` · Dutch: *Belegering*

A place is surrounded and cut off by enemy forces to make it surrender.

*Dutch definition:* Een plaats wordt door vijandelijke troepen omsingeld en afgesloten om haar tot overgave te dwingen.

<a id="Invasion"></a>

### Invasion

`Invasion` · Dutch: *Inval*

Armed forces enter an area uninvited.

*Dutch definition:* Gewapende troepen dringen ongevraagd een gebied binnen.

<a id="Killing"></a>

### Killing

`Killing` · Dutch: *Doden*

Someone kills a person or animal.

*Dutch definition:* Iemand doodt een mens of dier.

<a id="Uprising"></a>

### Uprising

`Uprising` · Dutch: *Opstand*

People rise up against an authority.

*Dutch definition:* Mensen komen in opstand tegen het gezag.

<a id="Mutiny"></a>

### Mutiny

`Mutiny` · Dutch: *Muiterij*

A group rises up against its superiors, especially on a ship or in an army.

*Dutch definition:* Een groep komt in opstand tegen de meerderen, veelal aan boord van een schip of in het leger.

<a id="BeingInConflict"></a>

### Conflict

`BeingInConflict` · Dutch: *Conflict*

Two people or groups are in conflict with each other.

*Dutch definition:* Twee personen of groepen zijn met elkaar in conflict.

<a id="Unrest"></a>

### Unrest

`Unrest` · Dutch: *Onrust*

Public order is disturbed or authority is resisted.

*Dutch definition:* De openbare orde wordt verstoord of er wordt verzet gepleegd tegen het gezag.

<a id="improvement-deterioration"></a>

## Improvement & deterioration

*Dutch: Verbetering en verslechtering*

Illness, injury, recovery and death of people or animals. Damage, destruction, shipwreck and repair of objects such as ships, buildings or crops, and other changes for the better or worse.

<a id="Damaging"></a>

### Damage

`Damaging` · Dutch: *Beschadiging*

Something gets damaged.

*Dutch definition:* Iets raakt beschadigd.

<a id="Repairing"></a>

### Repair

`Repairing` · Dutch: *Reparatie*

Something is repaired so that it works or can be used again.

*Dutch definition:* Iets wordt gerepareerd zodat het weer werkt of gebruikt kan worden.

<a id="Destroying"></a>

### Destruction

`Destroying` · Dutch: *Vernieling*

Something gets destroyed, for example by fire or demolition.

*Dutch definition:* Iets wordt vernield, bijvoorbeeld door brand of afbraak.

<a id="Sinking"></a>

### Sinking

`Sinking` · Dutch: *Zinken*

A ship sinks.

*Dutch definition:* Een schip zinkt.

<a id="InternalChange"></a>

### Change of condition

`InternalChange` · Dutch: *Verandering van toestand*

The condition or nature of someone or something changes.

*Dutch definition:* De toestand of aard van iemand of iets verandert.

<a id="ScalarChange"></a>

### Gradual change

`ScalarChange` · Dutch: *Geleidelijke verandering*

Something becomes more or less of something, for example better or worse.

*Dutch definition:* Iets wordt meer of minder, bijvoorbeeld beter of slechter.

<a id="QuantityChange"></a>

### Change in quantity or price

`QuantityChange` · Dutch: *Verandering in hoeveelheid of prijs*

An amount, price or value changes.

*Dutch definition:* Een hoeveelheid, prijs of waarde verandert.

<a id="Increasing"></a>

### Increase

`Increasing` · Dutch: *Toename*

An amount, price or value goes up.

*Dutch definition:* Een hoeveelheid, prijs of waarde stijgt.

<a id="Decreasing"></a>

### Decrease

`Decreasing` · Dutch: *Afname*

An amount, price or value goes down.

*Dutch definition:* Een hoeveelheid, prijs of waarde daalt.

<a id="FallingIll"></a>

### Falling ill or injured

`FallingIll` · Dutch: *Ziek of gewond raken*

A person or animal falls ill or gets injured.

*Dutch definition:* Een mens of dier wordt ziek of raakt gewond.

<a id="Healing"></a>

### Recovery

`Healing` · Dutch: *Genezing*

A person or animal recovers from illness or injury.

*Dutch definition:* Een mens of dier herstelt van ziekte of verwonding.

<a id="Dying"></a>

### Dying

`Dying` · Dutch: *Overlijden*

A person or animal dies.

*Dutch definition:* Een mens of dier sterft.

<a id="BeingDamaged"></a>

### Damaged state

`BeingDamaged` · Dutch: *Beschadigde staat*

Something is damaged.

*Dutch definition:* Iets is beschadigd.

<a id="BeingDestroyed"></a>

### Destroyed state

`BeingDestroyed` · Dutch: *Vernielde staat*

Something is destroyed.

*Dutch definition:* Iets is vernield.

<a id="HavingAMedicalCondition"></a>

### Illness or injury

`HavingAMedicalCondition` · Dutch: *Ziekte of letsel*

A person or animal suffers from an illness, injury or disability.

*Dutch definition:* Een mens of dier lijdt aan een ziekte, verwonding of handicap.

<a id="HavingInternalState+"></a>

### Improved condition

`HavingInternalState+` · Dutch: *Verbeterde toestand*

Someone or something is in a better condition than before.

*Dutch definition:* Iemand of iets is in betere toestand dan voorheen.

<a id="HavingInternalState-"></a>

### Deteriorated condition

`HavingInternalState-` · Dutch: *Verslechterde toestand*

Someone or something is in a worse condition than before.

*Dutch definition:* Iemand of iets is in slechtere toestand dan voorheen.

<a id="BeingDead"></a>

### Being dead

`BeingDead` · Dutch: *Overleden zijn*

A person or animal is dead.

*Dutch definition:* Een mens of dier is dood.
