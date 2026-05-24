---
date: 2026-05-24
description: Leer hoe je een vorm kunt extruderen met Aspose.3D for Java. Deze Java
  3D-modelleringshandleiding behandelt lineaire extrusie, centrumbesturing, richting,
  slices, twist en meer!
keywords:
- how to extrude shape
- java 3d geometry
- create 3d model java
- create solid from 2d
linktitle: 3D-modellen maken met lineaire extrusie in Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  headline: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  type: TechArticle
- description: Learn how to extrude shape using Aspose.3D for Java. This java 3d modeling
    tutorial covers linear extrusion, center control, direction, slices, twist and
    more!
  name: How to Extrude Shape - Creating 3D Models with Linear Extrusion in Java
  steps:
  - name: Define the 2‑D profile
    text: Create a `Polygon` or `Polyline` that represents the shape you want to extrude.
      *A `Polygon` represents a closed shape defined by vertices, while a `Polyline`
      is an open series of line segments.* Ready to get started? [Perform Linear Extrusion
      Now](./performing-linear-extrusion/) For a detailed tuto
  - name: Configure extrusion options
    text: 'Set the center, direction, slices, twist, and twist offset on an `Extrusion`
      object. *The `Extrusion` class encapsulates all parameters needed to generate
      a 3‑D mesh from a 2‑D profile.* Get hands‑on with center control: [Control Center
      in Linear Extrusion](./controlling-center/) Read more about cen'
  - name: Add the extrusion to the scene
    text: 'Instantiate a `Scene`, attach the extrusion mesh, and export to your desired
      format. *`Scene` is the container that holds all 3‑D objects and handles exporting
      to various file formats.* Ready to set the direction? [Explore Now](./setting-direction/)
      Learn more about direction: [Setting Direction in '
  - name: Export or render
    text: 'Use `Scene.save()` to write the model to OBJ, STL, or any supported format.
      *`Scene.save()` writes the entire scene to the specified file format, applying
      any necessary post‑processing.* Start specifying slices: [Learn More](./specifying-slices/)
      Detailed guide: [Specifying Slices in Linear Extrusio'
  type: HowTo
- questions:
  - answer: Yes, a valid Aspose license is required for production use, but a free
      trial is available for evaluation.
    question: Can I use Aspose.3D for Java in a commercial project?
  - answer: The library works with Java 8 and newer runtimes, including Java 11, 17,
      and 21.
    question: Which Java versions are supported?
  - answer: Aspose.3D handles mesh generation efficiently, but you can call `scene.dispose()`
      when you’re done with large scenes to free native resources.
    question: Do I need to manage memory for large extrusions?
  - answer: Absolutely – you can create several extrusion objects, position them independently,
      and add them to the same scene.
    question: Can I combine multiple extrusion operations in one model?
  - answer: Yes, the “Applying Twist” and “Using Twist Offset” tutorials demonstrate
      how to set both properties on the same extrusion object.
    question: Is there sample code for applying twist and twist offset together?
  type: FAQPage
second_title: Aspose.3D Java API
title: Hoe vorm extruderen - 3D-modellen maken met lineaire extrusie in Java
url: /nl/java/linear-extrusion/
weight: 23
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe vorm extruderen – 3D-modellen maken met lineaire extrusie in Java

Als je je ooit hebt afgevraagd **how to extrude shape** in een Java‑applicatie, dan ben je op de juiste plek. In deze tutorial lopen we de lineaire extrusie‑functies van Aspose.3D for Java door, en laten we zien hoe je eenvoudige 2‑D‑profielen kunt omzetten in volledige 3‑D‑modellen. Of je nu een CAD‑achtige viewer bouwt, een game‑asset‑pipeline, of gewoon experimenteert met geometrie, het beheersen van lineaire extrusie geeft je het vertrouwen om complexe vormen te creëren met slechts een paar regels code.

## Snelle antwoorden
- **Wat is lineaire extrusie?** Een 2‑D‑schets omzetten in een 3‑D‑solid door deze langs een richting uit te breiden.  
- **Welke bibliotheek helpt je?** Aspose.3D for Java biedt een fluent API voor extrusietaken.  
- **Heb ik een licentie nodig?** Een gratis trial werkt voor leren; een commerciële licentie is vereist voor productie.  
- **Welke Java‑versie is vereist?** Java 8 of hoger.  
- **Kan ik twists of offsets toepassen?** Ja – de API ondersteunt twist‑hoek en twist‑offset direct.

## Wat is “how to extrude shape” in Java?
De `Extrusion`‑operatie is de kernfunctie van Aspose.3D die een vlakke contour omzet in een volumetrisch mesh. In eenvoudige termen lever je een 2‑D‑profiel (bijvoorbeeld een rechthoek of een aangepaste veelhoek), vertel je de engine hoe ver deze moet worden uitgetrokken, en de bibliotheek bouwt de 3‑D‑geometrie voor je.

## Waarom Aspose.3D for Java gebruiken?
Aspose.3D ondersteunt **50+ invoer‑ en uitvoerformaten** – waaronder OBJ, STL, FBX en GLTF – en kan meshes genereren met tot **10 000 vertices per extrusie** zonder de volledige scène in het geheugen te laden. De cross‑platform engine draait op Windows, Linux en macOS, en levert consistente resultaten, of je nu op een desktop‑werkstation of een headless CI‑server werkt.

## Vereisten
- Java 8 of nieuwer geïnstalleerd op je ontwikkelmachine.  
- Maven of Gradle voor dependency‑beheer.  
- Een Aspose.3D for Java licentiebestand (optioneel voor trial).  

## Hoe werkt lineaire extrusie?
Lineaire extrusie creëert een 3‑D‑solid door een 2‑D‑profiel langs een rechte lijn te vegen. De engine trianguleert eerst het profiel, dupliceert het vervolgens op elke slice langs de extrusie‑as, en naait tenslotte de slices aan elkaar om een waterdichte mesh te vormen. Dit proces berekent automatisch de normals en UV‑coördinaten, zodat je het resultaat kunt renderen zonder extra geometrieverwerking.

## Wat zijn de belangrijkste parameters voor een lineaire extrusie?
Lineaire extrusie kan worden aangepast met verschillende parameters. Het **center** definieert het draaipunt van het profiel vóór extrusie. De **direction**‑vector bepaalt de extrusie‑as, standaard de positieve Z‑as. **Slices** regelen hoeveel tussenliggende doorsneden worden gegenereerd, wat de gladheid beïnvloedt voor gedraaide of taps toelopende vormen. **Twist angle** roteert het profiel geleidelijk van begin tot eind, terwijl **twist offset** een lineaire verplaatsing langs de as toevoegt, waardoor spiraalvormen mogelijk worden.

- **Center** – Het draaipunt rondom welk het profiel vóór extrusie wordt gepositioneerd.  
- **Direction** – Een vector die de extrusie‑as definieert; standaard is de positieve Z‑as.  
- **Slices** – Het aantal tussenliggende doorsneden; meer slices geven soepelere overgangen voor gedraaide of taps toelopende extrusies.  
- **Twist Angle** – De totale rotatie die op het profiel wordt toegepast van begin tot eind, uitgedrukt in graden.  
- **Twist Offset** – Een lineaire offset die het profiel langs de extrusie‑as verplaatst terwijl het draait, waardoor spiraalvormen mogelijk zijn.

## Lineaire extrusie uitvoeren in Aspose.3D for Java
Laad je profiel, configureer de parameters, en laat de API de mesh genereren. De volgende stappen schetsen de typische workflow.

### Stap 1: Definieer het 2‑D‑profiel
Maak een `Polygon` of `Polyline` die de vorm vertegenwoordigt die je wilt extruderen.  
*Een `Polygon` stelt een gesloten vorm voor die door vertices wordt gedefinieerd, terwijl een `Polyline` een open reeks lijnsegmenten is.*  
Klaar om te beginnen? [Voer lineaire extrusie nu uit](./performing-linear-extrusion/)  
Voor een gedetailleerde tutorial, zie [Lineaire extrusie uitvoeren in Aspose.3D for Java](./performing-linear-extrusion/).

### Stap 2: Configureer extrusie‑opties
Stel het center, de direction, slices, twist en twist offset in op een `Extrusion`‑object.  
*De `Extrusion`‑klasse omvat alle parameters die nodig zijn om een 3‑D‑mesh te genereren vanuit een 2‑D‑profiel.*  
Hands‑on met center‑controle: [Center regelen in lineaire extrusie](./controlling-center/)  
Lees meer over center‑controle: [Center regelen in lineaire extrusie met Aspose.3D for Java](./controlling-center/)

### Stap 3: Voeg de extrusie toe aan de scène
Instantieer een `Scene`, voeg de extrusie‑mesh toe, en exporteer naar het gewenste formaat.  
*`Scene` is de container die alle 3‑D‑objecten bevat en het exporteren naar verschillende bestandsformaten afhandelt.*  
Klaar om de richting in te stellen? [Ontdek nu](./setting-direction/)  
Lees meer over richting: [Richting instellen in lineaire extrusie met Aspose.3D for Java](./setting-direction/)

### Stap 4: Exporteren of renderen
Gebruik `Scene.save()` om het model naar OBJ, STL of een ander ondersteund formaat te schrijven.  
*`Scene.save()` schrijft de volledige scène naar het opgegeven bestandsformaat, met eventuele noodzakelijke post‑processing.*  
Begin met het specificeren van slices: [Meer informatie](./specifying-slices/)  
Gedetailleerde gids: [Slices specificeren in lineaire extrusie met Aspose.3D for Java](./specifying-slices/)

## Hoe een twist toepassen op een extrusie?
Pas een twist toe door de `twistAngle`‑eigenschap op de extrusie‑opties in te stellen. De engine roteert elke slice evenredig, waardoor een helicale werking ontstaat. Door de hoek aan te passen kun je alles maken van subtiele torsie tot volledige 360°‑spiralen, nuttig voor decoratieve elementen of functionele veren.  
Klaar om te twistsen? [Twist nu toepassen](./applying-twist/)  
Volledig voorbeeld: [Twist toepassen in lineaire extrusie met Aspose.3D for Java](./applying-twist/)

## Hoe twist offset gebruiken voor spiraalvormen?
Twist offset verplaatst elke slice langs de extrusie‑as terwijl deze roteert, waardoor een spiraaltrap of kurkentreker‑geometrie ontstaat. Het combineren van twist‑hoek met een positieve offset levert een soepele helicale helling op, terwijl een negatieve offset dalende spiralen kan creëren. Deze techniek is ideaal voor het modelleren van schroefdraad, veren of artistieke linten.  
Verbeter je vaardigheden: [Leer twist offset](./using-twist-offset/)  
Uitgebreide gids: [Twist offset gebruiken in lineaire extrusie met Aspose.3D for Java](./using-twist-offset/)

## Veelvoorkomende gebruikssituaties voor lineaire extrusie
- **Mechanical parts** – Snel bouten, assen en beugels genereren vanuit eenvoudige schetsen.  
- **Architectural elements** – Vloerplannen extruderen tot muren of kolommen voor BIM‑prototypes.  
- **Game assets** – Low‑poly props zoals hekken, buizen of decoratieve relingen direct uit 2‑D‑kunst maken.  
- **Educational tools** – Wiskundige oppervlakken visualiseren door parametrische curven te extruderen.

## Veelvoorkomende problemen oplossen
- **Missing faces** – Zorg ervoor dat het profiel een gesloten lus is; open contouren veroorzaken gaten.  
- **Excessive memory usage** – Verlaag het aantal `slices` of schakel `scene.setMemoryOptimization(true)` in.  
- **Incorrect twist direction** – Positieve hoeken roteren met de klok mee wanneer je langs de extrusierichting kijkt; gebruik negatieve waarden om te keren.

## Veelgestelde vragen

**Q: Kan ik Aspose.3D for Java gebruiken in een commercieel project?**  
A: Ja, een geldige Aspose‑licentie is vereist voor productiegebruik, maar een gratis trial is beschikbaar voor evaluatie.

**Q: Welke Java‑versies worden ondersteund?**  
A: De bibliotheek werkt met Java 8 en nieuwere runtimes, inclusief Java 11, 17 en 21.

**Q: Moet ik geheugen beheren voor grote extrusies?**  
A: Aspose.3D verwerkt mesh‑generatie efficiënt, maar je kunt `scene.dispose()` aanroepen wanneer je klaar bent met grote scènes om native resources vrij te geven.

**Q: Kan ik meerdere extrusie‑operaties combineren in één model?**  
A: Absoluut – je kunt meerdere extrusie‑objecten maken, ze onafhankelijk positioneren en toevoegen aan dezelfde scène.

**Q: Is er voorbeeldcode voor het toepassen van twist en twist offset samen?**  
A: Ja, de tutorials “Twist toepassen” en “Twist offset gebruiken” laten zien hoe beide eigenschappen op hetzelfde extrusie‑object in te stellen.

---

**Laatst bijgewerkt:** 2026-05-24  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose  

{{< blocks/products/products-backtop-button >}}

## Gerelateerde tutorials

- [Java 3D Graphics Tutorial – Center in Linear Extrusion](/3d/java/linear-extrusion/controlling-center/)
- [Hoe de richting instellen in lineaire extrusie met Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Maak 3D-extrusie met slices – Aspose.3D for Java](/3d/java/linear-extrusion/specifying-slices/)

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}