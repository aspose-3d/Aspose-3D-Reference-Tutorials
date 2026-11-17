---
date: 2026-11-17
description: Hoe de grootte van een 3d-model te verkleinen door een sphere mesh in
  Java te genereren en deze te comprimeren met Google Draco via Aspose.3D. Leer de
  volledige workflow in enkele minuten.
images:
- /java/3d-mesh-data/compress-meshes-google-draco/og-image.png
keywords:
- create sphere mesh
- how to compress 3d
- reduce 3d model size
- aspose 3d java
- compress 3d mesh
lastmod: 2026-11-17
linktitle: Hoe 3d-modelgrootte te verkleinen – Maak een Sphere Mesh in Java met Google
  Draco
og_description: Maak een sphere mesh en comprimeer een 3D-model met Java via Aspose.3D
  en Google Draco. Deze tutorial laat zien hoe je een sphere genereert, exporteert
  naar .drc en tot 95 % grootte‑reductie bereikt in enkele minuten.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Maak een sphere mesh en comprimeer een 3D-model met Java en Draco
schemas:
- author: Aspose
  dateModified: '2026-11-17'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Hoe de grootte van een 3d-model te verkleinen met een Java sphere mesh en Draco
url: /nl/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe 3d-modelgrootte te verkleinen met een Java-sfeer mesh en Draco

## Inleiding

Aspose.3D for Java is een bibliotheek die het mogelijk maakt om 3‑D-modellen te maken, te manipuleren en te converteren direct vanuit Java-code. Als je op zoek bent naar een snelle manier om **3d-modelgrootte te verkleinen** terwijl je toch hoogwaardige geometrie levert, ben je hier op de juiste plek. In deze tutorial lopen we door het genereren van een sferische mesh met **Aspose.3D for Java** en vervolgens die mesh comprimeren met **Google Draco**. Aan het einde heb je een kant‑klaar `.drc`‑bestand dat dramatisch kleiner is dan het origineel, waardoor het perfect is voor web‑gebaseerde viewers, mobiele games, of elke Java‑applicatie met beperkte bandbreedte.

## Snelle antwoorden
- **Waar gaat deze tutorial over?** Een sferische mesh maken in Java en deze comprimeren met Google Draco via Aspose.3D.  
- **Primaire bibliotheek?** Aspose.3D for Java (gebruikt voor zowel mesh‑creatie als Draco‑export).  
- **Typische implementatietijd?** Ongeveer 10‑15 minuten voor een basis-sfeer.  
- **Belangrijke voorwaarde?** Een Java‑ontwikkelomgeving met de Aspose.3D‑JARs op het classpath.  
- **Resultaat?** Een `.drc`‑bestand dat **3d-modelgrootte** verkleint met tot 95 % vergeleken met een onbewerkte mesh.

## Hoe 3d-modelgrootte te verkleinen?

Laad je sfeer en comprimeer deze in twee eenvoudige stappen. Eerst **maak je een sferische mesh** met `new Sphere(1.0, 32, 32)`. Vervolgens exporteer je de scène direct naar Draco met `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D behandelt geometrie‑kwantisatie en vertex‑deduplicatie automatisch, waardoor bestanden meestal 80‑95 % kleiner zijn terwijl de visuele getrouwheid behouden blijft.

De `Sphere`‑klasse is de ingebouwde geometriegenerator van Aspose.3D die een getrianguleerde sferische mesh maakt. Hij accepteert een radius en tessellatie‑parameters, waardoor je het detailniveau vóór compressie kunt regelen.

## Wat betekent “3d-modelgrootte verkleinen” in de context van 3d-ontwikkeling?

**3d-modelgrootte verkleinen** betekent het verkleinen van de hoeveelheid geometrie‑data die moet worden overgedragen of opgeslagen, zonder de visuele kwaliteit merkbaar te verminderen. Draco bereikt dit door vertex‑posities, normalen en andere attributen te coderen in een zeer compact binair formaat. In combinatie met Aspose.3D blijft de volledige workflow binnen Java, zodat je geen native binaries hoeft te beheren.

## Waarom Google Draco mesh‑compressie gebruiken met Aspose.3D?

Google Draco gecombineerd met Aspose.3D biedt een efficiënte pijplijn die mesh‑bestanden dramatisch verkleint terwijl ze gemakkelijk te integreren blijven in Java‑projecten. De bibliotheek behandelt alle low‑level codering, zodat ontwikkelaars zich kunnen richten op het creëren van geometrie zonder zich bezig te houden met native Draco‑binaries, wat resulteert in snellere ontwikkeling en kleinere assets voor web en mobiel.

- **Enorme grootte‑reductie:** Draco kan mesh‑data met tot 95 % verminderen voor typische modellen, waardoor een 5 MB OBJ wordt omgezet in een 0.3 MB `.drc`.  
- **Snelle runtime‑decodering:** Engines zoals Unity, Unreal en three.js decoderen Draco native, wat leidt tot snellere laadtijden.  
- **Naadloze Java‑integratie:** Aspose.3D abstraheert de native Draco‑bibliotheek, zodat je binnen het Java‑ecosysteem kunt blijven.  
- **Alles‑in‑één Aspose 3D‑export:** Dezelfde API die je gebruikt om geometrie te maken, behandelt ook de export, waardoor de pijplijn wordt vereenvoudigd.  

Aspose.3D ondersteunt **meer dan 50 invoer‑ en uitvoerformaten** — waaronder OBJ, FBX, STL, GLTF en vele anderen — en kan modellen van honderden pagina's verwerken zonder het volledige bestand in het geheugen te laden.

## Voorvereisten

- **Java Development Kit (JDK)** – versie 8 of nieuwer.  
- **Aspose.3D for Java** – download de nieuwste JARs van de **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **Basic familiarity with Google Draco** – je gebruikt de wrapper van Aspose.3D, dus geen native Draco‑installatie vereist.

## Importeer pakketten

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Stapsgewijze handleiding

### Stap 1: het project opzetten

Maak een nieuw Java‑project (elke IDE werkt) en voeg alle Aspose.3D‑JARs toe aan het classpath. Houd je bronbestanden in een package zoals `com.example.draco` voor duidelijkheid.

### Stap 2: hoe een sferische mesh te maken in Java

De `Sphere`‑klasse is de ingebouwde geometriegenerator van Aspose.3D die een getrianguleerde sferische mesh maakt.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro tip:** De `Sphere`‑klasse genereert een getrianguleerde mesh met een standaardradius van 1.0. Je kunt een aangepaste radius, tessellatie of materiaaleigenschappen doorgeven als je een ander detailniveau vóór compressie nodig hebt.

### Stap 3: exporteer de mesh naar Draco‑formaat

De `Scene`‑klasse vertegenwoordigt een volledige 3‑D‑scene die meshes, lichten en camera's kan bevatten. De `DracoCompressionOptions`‑klasse stelt je in staat om Draco‑compressie‑instellingen aan te passen, zoals kwantisatie en compressieniveau. Nadat de sfeer is toegevoegd aan een `Scene`‑object, roep je `scene.save("sphere.drc", SaveFormat.Draco)` aan. Aspose.3D selecteert automatisch optimale compressie‑instellingen, maar je kunt ze fijn afstellen door `DracoCompressionOptions` aan te passen als je het kleinste mogelijke bestand nodig hebt. `DracoCompressionOptions` laat je

### Stap 4: controleer de output

De `DRACOLoader` is een three.js‑hulpmiddel dat Draco‑gecomprimeerde `.drc`‑bestanden laadt en converteert naar WebGL‑compatibele geometrie. Open het gegenereerde `.drc`‑bestand met een Draco‑viewer (bijv. three.js `DRACOLoader`) om te bevestigen dat de geometrie correct wordt gerenderd. Je zult een dramatische verkleining van de bestandsgrootte opmerken — vaak een factor tien of meer.

## Veelvoorkomende use‑cases

| Scenario | Waarom modelgrootte verkleinen? | Hoe deze tutorial helpt |
|----------|--------------------------------|--------------------------|
| Web‑gebaseerde productconfigurators | Snellere paginaladingen bij trage verbindingen | Draco‑gecomprimeerde `.drc`‑bestanden laden in seconden |
| Mobiele AR/VR‑apps | Kleiner geheugenverbruik op apparaten | Kleinere meshes houden de app responsief |
| Cloud‑gerenderde scenes | Bandbreedtekosten verlagen | Export met één klik van Aspose.3D naar Draco |

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| **`NoClassDefFoundError` for Draco classes** | Aspose.3D‑JARs niet op het classpath | Controleer of *alle* Aspose.3D‑JAR‑bestanden zijn opgenomen en dat de versie overeenkomt met de documentatie. |
| **Output file is empty** | `MyDir` wijst naar een niet‑bestaande map | Maak de map programmatisch aan (`Files.createDirectories(Paths.get(MyDir))`) voordat je het bestand schrijft. |
| **Compressed mesh looks distorted** | Gebruik van een laag compressieniveau of onvoldoende tessellatie | Schakel over naar `DracoCompressionLevel.OPTIMAL` en verhoog de tessellatie van de sfeer (bijv. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` selecteert de hoogste compressiekwaliteit voor Draco‑output. |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met verschillende 3d‑bestandsformaten?**  
A: Ja, Aspose.3D ondersteunt OBJ, FBX, STL, GLTF en vele anderen, waardoor het een veelzijdige keuze is voor **Aspose 3d export**‑pijplijnen.

**Q: Kan ik Google Draco gebruiken voor compressie in andere programmeertalen?**  
A: Absoluut. Draco biedt native bibliotheken voor C++, Python en JavaScript. Deze tutorial richt zich op Java, maar de concepten zijn toepasbaar in verschillende talen.

**Q: Waar kan ik extra Aspose.3D‑documentatie vinden?**  
A: Bezoek de **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** voor volledige API‑referenties en meer voorbeelden.

**Q: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?**  
A: Bekijk de tijdelijke licentie‑opties op de **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**Q: Is er een community‑forum voor Aspose.3D‑ondersteuning?**  
A: Ja, neem deel aan de discussie op het **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Conclusie

In deze gids hebben we laten zien hoe je **3d-modelgrootte** kunt verkleinen door een sferische mesh te maken in Java en deze vervolgens te comprimeren met Google Draco via Aspose.3D. Door deze beknopte stappen te volgen kun je mesh‑bestanden dramatisch verkleinen, laadtijden verbeteren en je Java‑gebaseerde 3d‑applicaties responsief en bandbreedte‑vriendelijk houden.

---

**Laatst bijgewerkt:** 2026-11-17  
**Getest met:** Aspose.3D for Java 24.12 (latest)  
**Auteur:** Aspose

## Gerelateerde tutorials

- [3D-bestandsgrootte verkleinen – Scenes comprimeren met Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Genereer een Draco‑puntwolk van sferen met Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Leer hoe je meshes trianguleert voor geoptimaliseerde rendering in Java met Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}