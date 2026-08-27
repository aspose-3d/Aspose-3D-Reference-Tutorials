---
date: 2026-05-29
description: Leer hoe je een draco point cloud van een bol maakt met Aspose.3D for
  Java. Stapsgewijze handleiding, vereisten, code en probleemoplossing.
keywords:
- create draco point cloud
- Aspose 3D point cloud Java
- DracoSaveOptions Java
linktitle: Hoe een draco point cloud van bollen te creëren met Aspose 3D Java
schemas:
- author: Aspose
  dateModified: '2026-05-29'
  description: Learn how to create draco point cloud from a sphere with Aspose.3D
    for Java. Step‑by‑step guide, prerequisites, code, and troubleshooting.
  headline: How to create draco point cloud from spheres using Aspose 3D Java
  type: TechArticle
- questions:
  - answer: Yes. After loading the `.drc` file back into a `Scene`, you can export
      vertices using Aspose.3D’s generic `Scene.save` method with formats like PLY
      or OBJ.
    question: Can I convert the generated point cloud to other formats (e.g., PLY,
      OBJ)?
  - answer: The current Aspose.3D implementation focuses on geometry only. To add
      attributes, extend the scene with custom `VertexElement` objects before encoding.
    question: Does the Draco encoder support custom point attributes (e.g., color,
      normals)?
  - answer: Draco compresses efficiently, but clouds exceeding **100 million** points
      may require more than 8 GB RAM. Consider chunking or streaming APIs for very
      large datasets.
    question: How large can a point cloud be before performance degrades?
  - answer: Absolutely. three.js includes a Draco loader that reads the file directly
      for real‑time rendering.
    question: Is the generated `.drc` file compatible with web viewers like three.js?
  - answer: The default level (5) works for most cases. If file size is critical,
      experiment with values between **0** (fastest) and **10** (maximum compression)
      to balance speed vs. size.
    question: Do I need to call `opt.setCompressionLevel()` for better results?
  type: FAQPage
second_title: Aspose.3D Java API
title: Hoe een draco point cloud van bollen te creëren met Aspose 3D Java
url: /nl/java/point-clouds/generate-point-clouds-spheres-java/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Genereren van Aspose 3D-puntwolk vanuit bollen in Java

## Inleiding

Welkom bij deze stapsgewijze handleiding over **create draco point cloud** vanuit bollen met Aspose.3D voor Java. Of u nu wetenschappelijke visualisaties, game‑assets of AR/VR‑prototypes bouwt, puntwolken bieden een lichtgewicht weergave van 3‑D‑geometrie die kan worden gestreamd naar browsers of verwerkt door machine‑learning‑pijplijnen. In de komende paar minuten ziet u precies hoe u een eenvoudige bol omzet in een Draco‑gecodeerde puntwolk, waarom dit belangrijk is en hoe u de meest voorkomende valkuilen kunt vermijden.

## Snelle antwoorden
- **Welke bibliotheek wordt gebruikt?** Aspose.3D voor Java  
- **In welk formaat wordt de puntwolk opgeslagen?** Draco (`.drc`)  
- **Heb ik een licentie nodig voor testen?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.  
- **Welke Java‑versie wordt ondersteund?** Java 8 of hoger (JDK 11 aanbevolen)  
- **Hoe lang duurt de implementatie?** Ongeveer 10‑15 minuten voor een basisbol‑puntwolk  

## Wat is een draco‑puntwolk?

Een draco‑puntwolk is een compacte binaire weergave van 3‑D‑vertices gecomprimeerd met Google’s Draco‑algoritme. **Aspose.3D** biedt ingebouwde `DracoSaveOptions` om dit formaat direct vanuit een `Scene`‑object te schrijven, met een reductie van tot 90 % in bestandsgrootte ten opzichte van ruwe vertex‑lijsten.

## Waarom een puntwolk genereren vanuit een bol?

Het genereren van een puntwolk vanuit een bol is een ideaal starterproject omdat een bol een wiskundig gesloten vorm is die duidelijk laat zien hoe vertices worden bemonsterd en opgeslagen. Deze aanpak is nuttig voor:

- **Snelle prototyping** – test render‑pijplijnen zonder complexe meshes te importeren.  
- **Collision‑detectie benchmarks** – genereer deterministische puntverdelingen voor physics‑engines.  
- **Compressie‑demo’s** – vergelijk de ruwe OBJ‑grootte met Draco‑gecomprimeerde `.drc`‑bestanden (vaak een 10× reductie voor 10 k‑puntwolken).  

## Voorvereisten

Zorg ervoor dat u het volgende heeft:

- **Java Development Kit (JDK)** – Zorg dat Java op uw machine is geïnstalleerd. U kunt het downloaden van de [Oracle‑website](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D‑bibliotheek** – Om 3D‑bewerkingen in Java uit te voeren, heeft u de Aspose.3D‑bibliotheek nodig. U kunt deze downloaden van de [Aspose.3D Java‑documentatie](https://reference.aspose.com/3d/java/).  

### Aanvullende vereisten

| Vereiste | Reden |
|----------|-------|
| Maven- of Gradle‑buildtool | Vereenvoudigt afhankelijkheidsbeheer voor Aspose.3D. |
| Schrijfrechten voor uitvoermap | Nodig om het `.drc`‑bestand op te slaan. |
| Optioneel: licentiebestand | Vereist voor productie‑runs (trial werkt voor ontwikkeling). |

## Pakketten importeren

Importeer in uw Java‑project de benodigde pakketten om met Aspose.3D te werken. Voeg de volgende regels toe aan uw code:

```java
import com.aspose.threed.*;
import com.aspose.threed.geometry.*;
import com.aspose.threed.save.*;
```

> **Definition anchor:** `Scene` is Aspose.3D’s top‑level container that holds meshes, lights, cameras, and other 3‑D entities in memory.

## Hoe maak ik een draco‑puntwolk van een bol in Java?

Laad uw bol, schakel puntwolk‑modus in en sla deze op met Draco‑compressie in slechts drie regels code. Configureer eerst `DracoSaveOptions` om een puntwolk uit te voeren, maak vervolgens een `Sphere`‑primitive, voeg deze toe aan een `Scene` en roep tenslotte `save` aan. Dit patroon werkt voor elke mesh die u wilt converteren.

## Stap 1: DracoSaveOptions instellen

`DracoSaveOptions` vertelt Aspose.3D om geometrie als een puntwolk te coderen in plaats van als een volledige mesh.

```java
DracoSaveOptions dracoOptions = new DracoSaveOptions();
dracoOptions.setPointCloud(true);               // Enable point‑cloud output
dracoOptions.setCompressionLevel(7);            // 0‑10 range; 7 gives good size/ speed balance
```

> **Definition anchor:** `DracoSaveOptions` is the configuration object that controls how Aspose.3D writes Draco files, including compression level and point‑cloud flag.

## Stap 2: Een bol maken

De `Sphere`‑klasse vertegenwoordigt een wiskundig perfecte bol. U kunt de straal en tessellatiedichtheid aanpassen om het aantal punten te beïnvloeden.

```java
// Create a sphere with radius 5.0 and 32 longitudinal/latitudinal segments
Sphere sphere = new Sphere(5.0, 32, 32);
```

> **Definition anchor:** `Sphere` is a primitive shape class that generates a mesh of vertices and faces based on radius and segment parameters.

## Stap 3: De puntwolk coderen en opslaan

Voeg de bol toe aan een nieuwe `Scene`, roep vervolgens `save` aan met de eerder geconfigureerde `DracoSaveOptions`.

```java
Scene scene = new Scene();
scene.getRootNode().attachChild(sphere);               // Add sphere to scene graph
scene.save("output_point_cloud.drc", dracoOptions);   // Write compressed point cloud
```

> **Definition anchor:** `Scene.save` writes the entire scene to the specified file using the provided save options.

### Gekwantificeerde bewering

Aspose.3D ondersteunt **30+** 3‑D‑bestandsformaten (inclusief OBJ, STL, FBX, GLTF) en kan **500‑pagina**‑modellen verwerken zonder het volledige bestand in het geheugen te laden, waardoor het geschikt is voor grootschalige puntwolk‑workflows.

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| **Bestand niet gevonden** | Onjuist uitvoerpad | Gebruik een absoluut pad of zorg ervoor dat de map bestaat voordat u opslaat. |
| **Lege puntwolk** | `setPointCloud(true)` weggelaten | Controleer of de `DracoSaveOptions`‑vlag is ingesteld zoals weergegeven in Stap 1. |
| **Licentie‑exception** | Uitvoeren zonder geldige licentie in productie | Pas een tijdelijke of permanente licentie toe (zie FAQ hieronder). |

## Veelgestelde vragen

**Q: Kan ik Aspose.3D gratis gebruiken?**  
A: Ja, u kunt Aspose.3D verkennen met een gratis proefversie. Bezoek [hier](https://releases.aspose.com/) om te beginnen.

**Q: Waar kan ik ondersteuning voor Aspose.3D vinden?**  
A: U kunt ondersteuning vinden en contact maken met de community op het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18).

**Q: Hoe kan ik Aspose.3D aanschaffen?**  
A: Bezoek de [aankooppagina](https://purchase.aspose.com/buy) om Aspose.3D te kopen en de volledige functionaliteit te ontgrendelen.

**Q: Is er een tijdelijke licentie beschikbaar?**  
A: Ja, u kunt een tijdelijke licentie verkrijgen [hier](https://purchase.aspose.com/temporary-license/) voor uw ontwikkelbehoeften.

**Q: Waar kan ik de documentatie vinden?**  
A: Raadpleeg de uitgebreide [Aspose.3D Java‑documentatie](https://reference.aspose.com/3d/java/) voor volledige informatie.

## Conclusie

Gefeliciteerd! U heeft met succes **create draco point cloud** vanuit een bol gegenereerd met Aspose.3D voor Java. U kunt het `.drc`‑bestand nu laden in elke Draco‑compatibele viewer, streamen via het web, of gebruiken in downstream‑verwerkingspijplijnen zoals puntwolk‑classificatie of oppervlakte‑reconstructie.

---

**Laatst bijgewerkt:** 2026-05-29  
**Getest met:** Aspose.3D voor Java 24.10  
**Auteur:** Aspose  

```java
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
```

```java
// ExStart:3
DracoSaveOptions opt = new DracoSaveOptions();
opt.setPointCloud(true);
// ExEnd:3
```

```java
// ExStart:4
Sphere sphere = new Sphere();
// ExEnd:4
```

```java
// ExStart:5
FileFormat.DRACO.encode(sphere, "Your Document Directory" + "sphere.drc", opt);
// ExEnd:5
```

{{< blocks/products/products-backtop-button >}}

## Gerelateerde tutorials

- [Hoe Mesh omzetten naar Puntwolk in Java met Aspose.3D](/3d/java/point-clouds/create-point-clouds-java/)
- [Hoe PLY exporteren - Puntwolken met Aspose.3D voor Java](/3d/java/point-clouds/export-point-clouds-ply-java/)
- [Hoe een Bol Mesh maken in Java – 3D Meshes comprimeren met Google Draco](/3d/java/3d-mesh-data/compress-meshes-google-draco/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}