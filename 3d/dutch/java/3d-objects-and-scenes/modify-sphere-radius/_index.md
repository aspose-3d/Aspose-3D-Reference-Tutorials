---
date: 2025-11-30
description: Leer hoe je Aspose in Java kunt gebruiken om de straal van een 3D-sfeer
  aan te passen. Deze stapsgewijze handleiding behandelt de Aspose.3D Java‑bibliotheek,
  hoe je de straal instelt, een sfeer aan de scène toevoegt en een OBJ‑bestand schrijft
  in Java.
language: nl
linktitle: 'How to Use Aspose: Modify 3D Sphere Radius in Java with Aspose.3D'
second_title: Aspose.3D Java API
title: 'Hoe Aspose te gebruiken: de straal van een 3D-sfeer aanpassen in Java met
  Aspose.3D'
url: /java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe Aspose te gebruiken: 3D-sfeerstraal wijzigen in Java met Aspose.3D

## Introductie

Als je op zoek bent naar **hoe Aspose te gebruiken** om met 3D-modellen in Java te werken, ben je op de juiste plek. In deze tutorial lopen we stap voor stap door alles wat nodig is om de grootte van een sfeer te wijzigen, deze aan een scène toe te voegen en uiteindelijk een OBJ‑bestand te schrijven met de **Aspose.3D Java‑bibliotheek**. Aan het einde heb je een herbruikbare code‑fragment dat je in elke Java‑gebaseerde 3D‑applicatie kunt plaatsen.

## Snelle antwoorden
- **Wat is het primaire doel van deze gids?** Om te laten zien hoe je de straal van een sfeer wijzigt met Aspose.3D in Java.  
- **Welke bibliotheek gebruiken we?** De Aspose.3D Java bibliotheek (een volledig uitgeruste **java 3d library**).  
- **Hoe stel ik de straal in?** Roep `sphere.setRadius(double)` aan op een `Sphere` object.  
- **Kan ik exporteren naar OBJ?** Ja – gebruik `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Heb ik een licentie nodig?** Een gratis proefversie werkt voor ontwikkeling; een licentie is vereist voor productie.

## Wat is Aspose.3D voor Java?

Aspose.3D is een **java 3d library** die ontwikkelaars in staat stelt 3D‑bestanden te maken, bewerken en converteren zonder externe afhankelijkheden. Het ondersteunt populaire formaten zoals OBJ, FBX, STL en meer, waardoor het ideaal is voor games, CAD‑tools en wetenschappelijke visualisaties.

## Waarom Aspose.3D gebruiken om de grootte van een sfeer te wijzigen?

- **Geen native 3D‑engine nodig** – alle bewerkingen worden uitgevoerd op het objectmodel.  
- **Cross‑platform** – werkt op elk besturingssysteem dat Java ondersteunt.  
- **Hoge‑precisie geometrie** – je kunt exacte straalwaarden instellen, niet alleen benaderende schaling.  

## Vereisten

Zorg ervoor dat je het volgende hebt:

- Basiskennis van Java‑programmeren.  
- Aspose.3D bibliotheek geïnstalleerd – je kunt deze downloaden via de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- Java Development Kit (JDK) geïnstalleerd op je machine.

## Pakketten importeren

Om te beginnen, importeer je de benodigde klassen in je Java‑project:

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Stap 1: Een scène initialiseren

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

Hier maken we een nieuwe **3D scene** die al onze geometrie zal bevatten.

## Stap 2: Een sfeer initialiseren

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

Een `Sphere` object vertegenwoordigt een perfecte sfeer‑primitive. Op dit moment gebruikt hij de standaardstraal van 1.0.

## Stap 3: Hoe de straal van een sfeer instellen

```java
// set radius
sphere.setRadius(10);
```

Deze regel toont **hoe je de straal instelt**. Je kunt `10` vervangen door elke `double`‑waarde om de gewenste grootte te bereiken.

## Stap 4: Sfeer toevoegen aan de scène

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

De oproep **voegt sfeer toe aan scène** (of “add sphere to scene”) door een kind‑node onder de root‑node te creëren.

## Stap 5: OBJ‑bestand schrijven in Java

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Tot slot **schrijven we een OBJ‑bestand in Java‑stijl** met `scene.save`. Het uitvoerbestand `sphere.obj` kan worden geopend in elke 3D‑viewer die het Wavefront OBJ‑formaat ondersteunt.

## Veelvoorkomende problemen en oplossingen

| Issue | Solution |
|-------|----------|
| **Sphere appears too small in the viewer** | Controleer of de straalwaarde correct is ingesteld; onthoud dat eenheden willekeurig zijn tenzij je een schaal‑transformatie toepast. |
| **Exported OBJ has no material** | Aspose.3D schrijft alleen geometrie; voeg een materiaal toe aan de sfeer als je texturen nodig hebt (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Zorg ervoor dat je een tijdelijke of permanente licentiebestand hebt geladen voordat je de `Scene` maakt. |

## Veelgestelde vragen

### V: Waar kan ik de documentatie voor Aspose.3D voor Java vinden?

A: Je kunt de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) raadplegen voor uitgebreide informatie en gebruiksrichtlijnen.

### V: Hoe download ik Aspose.3D voor Java?

A: Download de bibliotheek vanaf de releases‑pagina: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

### V: Is er een gratis proefversie beschikbaar voor Aspose.3D voor Java?

A: Ja, verken de functies met een gratis proefversie via [Aspose.3D Free Trial](https://releases.aspose.com/).

### V: Waar kan ik ondersteuning krijgen voor Aspose.3D voor Java?

A: Word lid van de Aspose‑community op het [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) hulp en discussies.

### V: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?

A: Verkrijg een tijdelijke licentie via [Temporary License](https://purchase.aspose.com/temporary-license/).

### V: Kan ik deze code gebruiken met andere 3D-formaten zoals STL?

A: Absoluut – wijzig gewoon de `FileFormat`‑enum bij het aanroepen van `scene.save`, bijvoorbeeld `FileFormat.STL`.

## Conclusie

Je hebt nu geleerd **hoe je Aspose kunt gebruiken** om de straal van een sfeer te wijzigen, deze aan een scène toe te voegen en het resultaat als een OBJ‑bestand te exporteren in Java. Voel je vrij om te experimenteren met andere primitives, materialen toe te passen of meerdere transformaties te combineren om rijkere 3D‑modellen te bouwen.

**Last Updated:** 2025-11-30  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}