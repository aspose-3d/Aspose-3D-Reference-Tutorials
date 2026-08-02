---
date: 2026-08-02
description: Leer hoe u de extrusierichting kunt wijzigen bij lineaire extrusie en
  OBJ‑bestanden kunt exporteren met Aspose.3D voor Java. Volg onze stapsgewijze handleiding.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Extrusierichting wijzigen – Aspose.3D Java
og_description: Wijzig de extrusierichting bij lineaire extrusie met Aspose.3D voor
  Java en exporteer OBJ‑bestanden. Deze handleiding toont stapsgewijze code en tips
  voor ontwikkelaars.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Extrusierichting wijzigen – Aspose.3D Java‑tutorial
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Extrusierichting wijzigen in 3D-modellen – Aspose.3D Java
url: /nl/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verander Extrusieringsrichting in 3D-modellen – Aspose.3D Java

## Inleiding

In deze uitgebreide tutorial ontdek je **hoe je de extrusieringsrichting kunt wijzigen** bij het uitvoeren van een lineaire extrusie met Aspose.3D voor Java. Of je nu een CAD‑achtig hulpmiddel bouwt, assets voorbereidt voor een game‑engine, of onderdelen genereert voor 3‑D‑printen, het beheersen van de extrusieringsrichting stelt je in staat precies de vorm te maken die je nodig hebt. We lopen elke stap door, van het initialiseren van een profiel tot het opslaan van het resultaat als een OBJ‑bestand, zodat je ook **export 3D model OBJ** bestanden direct vanuit Java kunt exporteren.

## Snelle Antwoorden
- **Welke klasse voert lineaire extrusie uit?** `LinearExtrusion`
- **Welke methode stelt de extrusie‑vector in?** `setDirection(Vector3 direction)`
- **Kan het resultaat worden opgeslagen als OBJ?** Ja—gebruik `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Is een licentie vereist voor productie?** Een gratis proefversie is beschikbaar; een licentie is verplicht voor commercieel gebruik.
- **Welke IDE werkt het beste met Aspose.3D?** IntelliJ IDEA en Eclipse worden volledig ondersteund.

## Wat is lineaire extrusie?

Lineaire extrusie is het proces waarbij een 2‑D‑schets (zoals een rechthoek of cirkel) langs een rechte lijn wordt uitgerekt om een 3‑D‑solid te genereren. Standaard volgt de extrusie de positieve Z‑as, maar Aspose.3D laat je dat pad wijzigen met de eigenschap `setDirection`, waardoor je volledige controle krijgt over de uiteindelijke geometrie.

## Waarom de extrusierichting wijzigen bij lineaire extrusie?

Het wijzigen van de extrusierichting stelt je in staat nieuwe geometrie af te stemmen op bestaande objecten, hoekige componenten te maken zonder extra transformaties, en modellen te genereren die passen bij het coördinatensysteem dat vereist is door downstream‑pijplijnen (bijv. 3‑D‑printers of game‑engines). Dit elimineert de noodzaak voor nabewerking en vermindert de bestandsgrootte‑overhead tot 15 % wanneer directionele vectoren worden gebruikt die onnodige rotaties vermijden.

## Voorvereisten

- Basiskennis van Java.
- Aspose.3D‑bibliotheek geïnstalleerd. Je kunt deze downloaden van [hier](https://releases.aspose.com/3d/java/). Je kunt ook alle Aspose‑releases bekijken op de hoofdpagina [hier](https://releases.aspose.com/).
- Een IDE zoals Eclipse of IntelliJ IDEA.

## Importpakketten

De `com.aspose.threed`‑namespace biedt de kern‑3D‑klassen en hulptype.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Basisprofiel initialiseren

De `RectangleShape`‑klasse maakt het 2‑D‑profiel dat geëxtrudeerd zal worden. Een kleine afrondingsstraal geeft de randen een gladde uitstraling.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Stap 2: Een scène maken

De `Scene`‑klasse is de top‑level container van Aspose.3D die alle 3‑D‑nodes, lichten, camera’s en materialen bevat.

```java
Scene scene = new Scene();
```

## Stap 3: Nodes maken

Een `Node` vertegenwoordigt een object in de scene‑graph, waardoor je geometrie, transformaties en andere eigenschappen kunt koppelen.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 4: Lineaire extrusie uitvoeren op de linkernode

`LinearExtrusion` voert de extrusie‑operatie uit, waarbij een 2‑D‑profiel wordt omgezet in een 3‑D‑mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Stap 5: Lineaire extrusie uitvoeren op de rechternode met richting

Hier **wijzigen we de extrusierichting**. Door een aangepaste `Vector3` door te geven aan `setDirection`, volgt de extrusie de vector (0.3, 0.2, 1), waardoor een schuine vorm ontstaat die aansluit op het coördinatensysteem van de scène.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Stap 6: 3D‑scène opslaan

De `save`‑methode schrijft de scène naar een bestand in het opgegeven formaat.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| OBJ‑bestand lijkt leeg | Het profiel is niet toegevoegd aan een node | Zorg ervoor dat `createChildNode` wordt aangeroepen op een geldige node |
| Richting lijkt onveranderd | `setDirection` werd aangeroepen nadat de extrusie al was geconstrueerd | Stel de richting in binnen de `LinearExtrusion`‑initializer zoals getoond |
| Mesh met lage resolutie | `setSlices`‑waarde is te laag | Verhoog het aantal slices (bijv. 100 of meer) |

## Conclusie

Je weet nu **hoe je de extrusierichting kunt wijzigen** bij een lineaire extrusie, hoe je twist‑ en slice‑instellingen kunt aanpassen, en hoe je **export 3D model OBJ** bestanden kunt maken met Aspose.3D voor Java. Deze technieken geven je fijne controle over geometriecreatie en maken het eenvoudig om 3‑D‑assets in grotere pijplijnen te integreren.

## Veelgestelde vragen

**V:** Kan ik Aspose.3D gebruiken met andere programmeertalen?  
**A:** Ja—Aspose.3D biedt API's voor .NET en Java, waardoor cross‑platform ontwikkeling mogelijk is.

**V:** Is er een gratis proefversie beschikbaar voor Aspose.3D?  
**A:** Absoluut. Je kunt de volledige functionaliteit verkennen met een gratis proefversie [hier](https://releases.aspose.com/).

**V:** Waar vind ik gedetailleerde documentatie voor Aspose.3D voor Java?  
**A:** De uitgebreide referentie is beschikbaar [hier](https://reference.aspose.com/3d/java/).

**V:** Hoe krijg ik ondersteuning voor Aspose.3D?  
**A:** Bezoek het officiële [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor hulp van de community en het productteam.

**V:** Zijn tijdelijke licenties beschikbaar voor testen?  
**A:** Ja—tijdelijke licenties kunnen worden verkregen [hier](https://purchase.aspose.com/temporary-license/).

**Laatst bijgewerkt:** 2026-08-02  
**Getest met:** Aspose.3D for Java (latest release)  
**Auteur:** Aspose

{{< blocks/products/products-backtop-button >}}

## Gerelateerde tutorials

- [Hoe vorm extruderen - 3D‑modellen maken met lineaire extrusie in Java](/3d/java/linear-extrusion/)
- [3D‑extrusie maken in Java met Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Java 3D‑grafiektutorial – Centrum in lineaire extrusie](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}