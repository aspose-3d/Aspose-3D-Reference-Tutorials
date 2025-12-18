---
date: 2025-12-18
description: Leer hoe je een 3D‑scène maakt en een OBJ‑bestand opslaat met Aspose.3D
  voor Java. Volg onze stapsgewijze handleiding voor de lineaire extrusierichting.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Maak 3D‑scene – Stel extrusierichting in Aspose.3D Java
url: /nl/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D‑scene maken – Extrusierichting instellen Aspose.3D Java

## Inleiding

In deze tutorial leer je **hoe je 3d‑scene**‑objecten maakt en de extrusierichting beheert met Aspose.3D voor Java. Of je nu architecturale visualisaties, productprototypes of game‑assets bouwt, het beheersen van lineaire extrusie geeft je de flexibiliteit om complexe vormen snel te modelleren. We lopen elke stap door, van het toevoegen van nodes in Java tot **export 3d‑model obj**‑bestanden, zodat je het resultaat direct kunt zien.

## Snelle antwoorden
- **Wat betekent “create 3d scene”?** Het betekent het initialiseren van een Aspose.3D `Scene`‑object dat alle geometrie, lichten en camera's bevat.  
- **Hoe stel ik de extrusierichting in?** Gebruik de `setDirection(Vector3)`‑methode op een `LinearExtrusion`‑instantie.  
- **Welk formaat moet ik gebruiken voor export?** Het OBJ‑formaat (`FileFormat.WAVEFRONTOBJ`) wordt breed ondersteund voor 3‑D‑workflows.  
- **Heb ik een licentie nodig voor Aspose.3D?** Een gratis proefversie werkt voor ontwikkeling; een commerciële licentie is vereist voor productie.  
- **Kan ik meer nodes toevoegen in Java?** Ja—gebruik `scene.getRootNode().createChildNode()` om zoveel objecten toe te voegen als nodig.

## Wat is een “create 3d scene” workflow?

Een **create 3d scene** workflow begint met een leeg `Scene`‑object, voegt geometrie toe (zoals geëxtrudeerde profielen), positioneert deze met transformaties, en slaat uiteindelijk de scene op in een bestandsformaat zoals OBJ. Dit patroon vormt de ruggengraat van de meeste 3‑D‑applicaties die met Aspose.3D zijn gebouwd.

## Waarom extrusierichting instellen?

Het instellen van de extrusierichting laat je de vorm kantelen, roteren of scheef trekken tijdens het extruderen, waardoor je controle krijgt over de uiteindelijke geometrie zonder extra nabewerking. Het is vooral nuttig voor:

- Het maken van taps toelopende kolommen of op maat gemaakte buizen.  
- Het uitlijnen van extrusies met niet‑standaard assen in mechanische onderdelen.  
- Het genereren van artistieke vormen voor visuele effecten.

## Voorvereisten

Voordat we beginnen, zorg dat je het volgende hebt:

- Basiskennis van Java.  
- Aspose.3D‑bibliotheek geïnstalleerd – download deze van [hier](https://releases.aspose.com/3d/java/).  
- Een IDE zoals Eclipse of IntelliJ IDEA.

## Pakketten importeren

Importeer eerst de benodigde Aspose.3D‑klassen:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Basisprofiel initialiseren

Maak het 2‑D‑profiel dat geëxtrudeerd zal worden. In dit voorbeeld gebruiken we een afgeronde rechthoek:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Pro tip:** Pas de afrondingsstraal aan om te bepalen hoe scherp of zacht de hoeken van de rechthoek vóór extrusie verschijnen.

## Stap 2: Een scene maken

Nu **create 3d scene** die onze objecten zal hosten:

```java
Scene scene = new Scene();
```

## Stap 3: Nodes toevoegen in Java – Objecten positioneren

We voegen twee child‑nodes (links en rechts) toe aan de root‑node van de scene en verplaatsen de linkse een beetje naar de zijkant:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 4: Hoe extruderen – Linkse node (standaardrichting)

Extrudeer het profiel op de linkse node met de standaard Z‑as richting. We stellen ook een volledige 360° twist in en verhogen het aantal slices voor gladheid:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Stap 5: Hoe richting instellen – Rechterm node

Hier laten we **how to set direction** zien door een aangepaste `Vector3` te leveren. Dit kantelt de extrusie naar de vector (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Stap 6: OBJ‑bestand opslaan – 3D‑model exporteren

Tot slot **save obj file** om het resultaat in elke 3‑D‑viewer te bekijken:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Wanneer je het gegenereerde OBJ‑bestand opent, zie je twee geëxtrudeerde rechthoeken: één met de standaardrichting en één gekanteld volgens de vector die we hebben ingesteld.

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| OBJ‑bestand lijkt leeg | Scene niet opgeslagen of pad onjuist | Controleer of `MyDir` naar een schrijfbare map wijst en de bestandsnaam eindigt op `.obj`. |
| Extrusie ziet er plat uit | `setSlices` te laag | Verhoog `setSlices` (bijv. 200) voor een vloeiendere geometrie. |
| Richting lijkt niet veranderd | Vector niet genormaliseerd | Gebruik een genormaliseerde `Vector3` of pas de waarden aan om de gewenste kanteling te bereiken. |

## Veelgestelde vragen

### Q1: Kan ik Aspose.3D gebruiken met andere programmeertalen?
A1: Aspose.3D ondersteunt verschillende talen, waaronder .NET en Java.

### Q2: Is er een gratis proefversie beschikbaar voor Aspose.3D?
A2: Ja, je kunt de functies van Aspose.3D verkennen met een gratis proefversie [hier](https://releases.aspose.com/).

### Q3: Waar vind ik uitgebreide documentatie voor Aspose.3D voor Java?
A3: De volledige documentatie is beschikbaar [hier](https://reference.aspose.com/3d/java/).

### Q4: Hoe kan ik ondersteuning krijgen voor Aspose.3D?
A4: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor hulp of vragen.

### Q5: Zijn tijdelijke licenties beschikbaar voor Aspose.3D?
A5: Ja, je kunt een tijdelijke licentie verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

---

**Laatst bijgewerkt:** 2025-12-18  
**Getest met:** Aspose.3D 24.11 voor Java  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}