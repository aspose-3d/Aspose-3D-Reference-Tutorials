---
date: 2025-12-18
description: Leer hoe je een grondvlak toevoegt en de centereigenschap instelt bij
  lineaire extrusie met Aspose.3D voor Java, met stapsgewijze codevoorbeelden.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hoe een grondvlak en controlecentrum toe te voegen bij lineaire extrusie met
  Aspose.3D voor Java
url: /nl/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centrum regelen bij lineaire extrusie met Aspose.3D voor Java

## Inleiding

Wanneer je 3D‑scènes bouwt in Java, kan de mogelijkheid om **add ground plane** te gebruiken terwijl je nauwkeurig de **set center property** op een lineaire extrusie instelt, het verschil maken tussen een ruwe prototype en een gepolijste visualisatie. In deze tutorial lopen we het volledige proces door van het regelen van het extrusie‑centrum en het toevoegen van een grondvlak met Aspose.3D voor Java. Je ziet waarom dit belangrijk is, hoe je het instelt, en krijgt een kant‑klaar code‑voorbeeld dat je kunt aanpassen aan je eigen projecten.

## Snelle antwoorden
- **What does “add ground plane” do?** It creates a thin reference geometry that helps you see the extrusion’s position relative to the world axes.  
- **How do I set the center of a linear extrusion?** Use the `setCenter(boolean)` method on the `LinearExtrusion` object.  
- **Do I need a license to run the sample?** A temporary license works for testing; a full license is required for production.  
- **Which file format is used for saving?** The example saves to Wavefront OBJ (`.obj`).  
- **What Java version is required?** Java 8 or later is sufficient.

## Wat is “add ground plane” in een 3D‑scene?

Het toevoegen van een grondvlak betekent het invoegen van een dunne rechthoekige geometrie (vaak een doos met minimale dikte) die op het X‑Z‑vlak ligt. Het fungeert als een visueel vloeroppervlak, waardoor het makkelijker wordt om de hoogte en uitlijning van andere objecten te beoordelen, vooral wanneer je experimenteert met extrusie‑centra.

## Waarom de center‑eigenschap instellen bij een lineaire extrusie?

Standaard begint een lineaire extrusie vanaf de oorsprong van het profiel. Het instellen van de centre‑eigenschap (`setCenter(true)`) verschuift het profiel zodat de extrusie gecentreerd is rond de oorsprong, wat nuttig is voor symmetrische ontwerpen of wanneer je consistente uitlijning nodig hebt over meerdere objecten.

## Vereisten

Voordat we aan deze tutorial beginnen, zorg ervoor dat je de volgende vereisten hebt:

1. **Java Development Environment** – Zorg ervoor dat je een Java‑ontwikkelomgeving op je machine hebt geïnstalleerd.  
2. **Aspose.3D for Java** – Download en installeer de Aspose.3D‑bibliotheek. Je kunt de bibliotheek en de documentatie vinden [hier](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Maak een map aan om je Java‑documenten op te slaan. Laten we deze “Your Document Directory” noemen.

## Pakketten importeren

Importeer in je Java‑ontwikkelomgeving de benodigde pakketten voor Aspose.3D. Dit zorgt ervoor dat je code toegang heeft tot de functionaliteiten die de bibliotheek biedt.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Basisprofiel instellen

Initialiseer het basisprofiel dat geëxtrudeerd moet worden. In dit voorbeeld gebruiken we een rechthoek met een afrondingsstraal van 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Stap 2: Een 3D‑scene maken

Bouw de basis van je 3D‑wereld door een scene aan te maken.

```java
Scene scene = new Scene();
```

## Stap 3: Linker‑ en rechter‑nodes maken

Maak linker‑ en rechter‑nodes binnen je scene. Deze nodes dienen als canvas voor je 3D‑objecten.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 4: Lineaire extrusie met centre‑eigenschap (linker node)

Voer lineaire extrusie uit op de linker node **zonder centreren** en stel het aantal slices in op 3. Let op de `setCenter(false)`‑aanroep – dit is waar we de **set center property** op *false* zetten.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Stap 5: Ground plane toevoegen ter referentie (linker node)

Verbeter de visuele weergave door **add ground plane** toe te voegen aan de linker node. De dunne doos fungeert als vloer zodat je duidelijk de hoogte van de extrusie kunt zien.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Stap 6: Lineaire extrusie met centre‑eigenschap (rechter node)

Voer nu lineaire extrusie uit op de rechter node, dit keer **de extrusie centreren**. De `setCenter(true)`‑aanroep laat zien hoe je de **set center property** op *true* zet.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Stap 7: Ground plane toevoegen ter referentie (rechter node)

Net als aan de linkerkant, voeg een grondvlak toe aan de rechter node voor een consistente visuele basislijn.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Stap 8: De 3D‑scene opslaan

Sla je 3D‑scene op in Wavefront OBJ‑formaat zodat je deze in elke standaard 3D‑viewer kunt bekijken.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| Ground plane not visible | Box thickness is too small for the viewer’s scale. | Increase the thickness (first parameter of `Box`) or zoom out in the viewer. |
| Extrusion appears offset | `setCenter` value not set as intended. | Double‑check the boolean passed to `setCenter`. |
| File not saved | Incorrect directory path or missing write permissions. | Verify `MyDir` points to an existing folder with write access. |

## Veelgestelde vragen

**Q1: Kan ik Aspose.3D for Java gebruiken in commerciële projecten?**  
A1: Ja, Aspose.3D for Java is beschikbaar voor commercieel gebruik. Voor licentie‑details, bezoek [hier](https://purchase.aspose.com/buy).

**Q2: Is er een gratis proefversie beschikbaar?**  
A2: Ja, je kunt een gratis proefversie van Aspose.3D for Java verkennen [hier](https://releases.aspose.com/).

**Q3: Waar kan ik ondersteuning vinden voor Aspose.3D for Java?**  
A3: Het Aspose.3D community‑forum is een uitstekende plek om ondersteuning te zoeken en ervaringen te delen. Bezoek het forum [hier](https://forum.aspose.com/c/3d/18).

**Q4: Heb ik een tijdelijke licentie nodig voor testen?**  
A4: Ja, als je een tijdelijke licentie voor testdoeleinden nodig hebt, kun je er een verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

**Q5: Waar kan ik de documentatie vinden?**  
A5: De documentatie voor Aspose.3D for Java is beschikbaar [hier](https://reference.aspose.com/3d/java/).

## Conclusie

Het regelen van het centrum bij lineaire extrusie **en** het leren hoe je **add ground plane** toevoegt met Aspose.3D voor Java opent spannende mogelijkheden in 3D‑grafische ontwikkeling. Door de bovenstaande stappen te volgen, heb je nu een herbruikbaar patroon voor het maken van gecentreerde extrusies, visuele referentievlakken en het exporteren van het resultaat naar OBJ. Voel je vrij om te experimenteren met verschillende profielen, slice‑aantallen en transformaties om aan je eigen projectbehoeften te voldoen.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}