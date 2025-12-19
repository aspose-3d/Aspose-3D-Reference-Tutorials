---
date: 2025-12-19
description: Leer hoe je een 3D‑scène maakt en een 3D‑obj exporteert met Twist Offset
  in Linear Extrusion met Aspose.3D voor Java.
linktitle: Create 3d scene with Twist Offset – Aspose.3D Java
second_title: Aspose.3D Java API
title: Maak 3D‑scene met Twist Offset – Aspose.3D Java
url: /nl/java/linear-extrusion/using-twist-offset/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3d scene met Twist Offset – Aspose.3D voor Java

## Introductie

In de dynamische wereld van 3D‑graphics is leren hoe je **maak 3d scene** met lineaire extrusie een echte game‑changer. Met Aspose.3D voor Java kun je je 3D‑modelleringvaardigheden verbeteren door de Twist Offset‑functie toe te voegen aan je lineaire extrusieproces. Deze tutorial leidt je door de stappen om Twist Offset te gebruiken in lineaire extrusie met Aspose.3D voor Java, en biedt je de tools om verbluffende 3D‑scènes te maken.

## Snelle antwoorden
- **Wat doet Twist Offset?** Het verschuift het begin van de draai langs het extrusiepad, waardoor je meer controle over de geometrie krijgt.  
- **Welk bestandsformaat wordt gebruikt voor export?** Het voorbeeld slaat het model op als een Wavefront OBJ (`.obj`).  
- **Heb ik een licentie nodig voor ontwikkeling?** Een gratis proefversie werkt voor testen; een commerciële licentie is vereist voor productie.  
- **Welke Java‑versie is vereist?** Java 8 of hoger.  
- **Kan ik het aantal slices wijzigen?** Ja – de `setSlices`‑methode bepaalt de gladheid van de draai.

## Vereisten

Voordat je aan de tutorial begint, zorg ervoor dat je de volgende vereisten hebt:

- Java‑omgeving: Zorg ervoor dat je een Java‑ontwikkelomgeving op je systeem hebt ingesteld.  
- Aspose.3D voor Java: Download en installeer de Aspose.3D‑bibliotheek vanaf de [download link](https://releases.aspose.com/3d/java/).  
- Documentatie: Maak jezelf vertrouwd met de [Aspose.3D voor Java documentatie](https://reference.aspose.com/3d/java/).  

## Import pakketten

Importeer in je Java‑project de benodigde pakketten om Aspose.3D voor Java te gaan gebruiken. Zorg ervoor dat je de vereiste bibliotheken opneemt voor een naadloze integratie.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Stap 1: Zet de omgeving op

Begin met het opzetten van je Java‑ontwikkelomgeving en zorg ervoor dat Aspose.3D voor Java correct is geïnstalleerd.

## Stap 2: Initialiseert het basisprofiel

Maak een basisprofiel voor extrusie, in dit geval een `RectangleShape` met een afrondingsstraal van 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
// Initialize the base profile to be extruded
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Stap 3: Maak een 3D‑scene

Bouw een 3D‑scene om je geëxtrudeerde objecten in onder te brengen.

```java
// Create a scene
Scene scene = new Scene();
```

## Stap 4: Maak nodes

Genereer nodes binnen de scene om verschillende entiteiten te vertegenwoordigen.

```java
// Create left node
Node left = scene.getRootNode().createChildNode();
// Create right node
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 5: Voer lineaire extrusie uit

Gebruik lineaire extrusie op zowel de linker‑ als rechter‑nodes met verschillende eigenschappen.

```java
// Perform linear extrusion on left node using twist and slices property
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});

// Perform linear extrusion on right node using twist, twist offset, and slices property
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setTwistOffset(new Vector3(3, 0, 0)); }});
```

## Stap 6: Sla de 3D‑scene op

Sla je nieuw gemaakte 3D‑scene op met het opgegeven bestandsformaat.

```java
// Save 3D scene
scene.save(MyDir + "TwistOffsetInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Hoe sla je 3d model op en exporteer je 3d obj

De `scene.save`‑aanroep in de vorige stap **slaat het 3d model** op als een OBJ‑bestand, een breed ondersteund **export 3d obj**‑formaat. Je kunt de bestandsnaam wijzigen of een ander ondersteund formaat kiezen (bijv. STL, FBX) door de `FileFormat`‑enum aan te passen.

## Conclusie

Gefeliciteerd! Je hebt met succes Twist Offset geïmplementeerd in lineaire extrusie met Aspose.3D voor Java. Deze krachtige functie opent een wereld aan mogelijkheden voor je 3D‑modellering, waardoor je **3d scene** kunt maken met ingewikkelde twists en offsets, en vervolgens **3d model** kunt opslaan in een formaat dat klaar is voor downstream‑pijplijnen.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor Java gebruiken in niet‑commerciële projecten?

A1: Ja, Aspose.3D voor Java kan zowel in commerciële als niet‑commerciële projecten worden gebruikt. Bekijk de [licentieopties](https://purchase.aspose.com/buy) voor meer details.

### V2: Waar kan ik ondersteuning vinden voor Aspose.3D voor Java?

A2: Bezoek het [Aspose.3D voor Java forum](https://forum.aspose.com/c/3d/18) voor hulp en om contact te maken met de community.

### V3: Is er een gratis proefversie beschikbaar voor Aspose.3D voor Java?

A3: Ja, je kunt een gratis proefversie verkennen via de [releases‑pagina](https://releases.aspose.com/).

### V4: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D voor Java?

A4: Verkrijg een tijdelijke licentie voor je project door [deze link](https://purchase.aspose.com/temporary-license/) te bezoeken.

### V5: Zijn er extra voorbeelden en tutorials beschikbaar?

A5: Ja, raadpleeg de [documentatie](https://reference.aspose.com/3d/java/) voor meer voorbeelden en diepgaande tutorials.

## Veelgestelde vragen

**V: Is deze tutorial onderdeel van een Aspose 3d tutorialserie?**  
A: Ja – het is een officiële **aspose 3d tutorial** die een specifieke functie van de bibliotheek demonstreert.

**V: Kan ik een andere vorm gebruiken in plaats van een rechthoek?**  
A: Absoluut. Elke `IProfile`‑implementatie (bijv. `CircleShape`, aangepaste `PolygonShape`) kan worden geëxtrudeerd.

**V: Wat gebeurt er als ik `setTwistOffset` weglaten?**  
A: De extrusie begint te draaien vanaf de oorsprong van het profiel, wat resulteert in een symmetrische draai.

**V: Hoe verhoog ik de gladheid van de draai?**  
A: Verhoog de waarde die aan `setSlices` wordt doorgegeven; een hoger aantal slices levert een gladdere geometrie op.

**V: Welke andere bestandsformaten kan ik exporteren naast OBJ?**  
A: Aspose.3D ondersteunt STL, FBX, GLTF, 3MF en verschillende andere via de `FileFormat`‑enum.

---

**Last Updated:** 2025-12-19  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}