---
date: 2026-09-08
description: Hoe de grootte van 3d-modellen te verkleinen door een sfeer mesh te genereren
  in Java en deze te comprimeren met Google Draco via Aspose.3D. Leer de volledige
  workflow in enkele minuten.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: Hoe 3d-modellen te verkleinen – Sfeer mesh maken in Java met Google Draco
og_description: Hoe de grootte van 3d-modellen te verkleinen door een sfeer mesh te
  maken in Java en deze te comprimeren met Google Draco via Aspose.3D. Verkrijg een
  .drc-bestand tot 95% kleiner in enkele minuten.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Hoe de grootte van 3d-modellen te verkleinen met een Java-sfeer mesh en
  Draco
schemas:
- author: Aspose
  dateModified: '2026-09-08'
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
title: Hoe de grootte van 3d-modellen te verkleinen met een Java-sfeer mesh en Draco
url: /nl/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe 3d-modelgrootte te verkleinen met een Java-sfeer mesh en Draco

## Introductie

Als je op zoek bent naar een snelle manier om **3d-modelgrootte te verkleinen** terwijl je nog steeds geometrie van hoge kwaliteit levert, ben je hier op de juiste plek. In deze tutorial lopen we door het genereren van een sferische mesh met **Aspose.3D for Java** en vervolgens het comprimeren van die mesh met **Google Draco**. Aan het einde heb je een kant-en-klare `.drc`-file die dramatisch kleiner is dan het origineel, waardoor het perfect is voor web‑gebaseerde viewers, mobiele games, of elke Java‑applicatie met beperkte bandbreedte.

## Snelle antwoorden
- **Waar gaat deze tutorial over?** Een sferische mesh maken in Java en deze comprimeren met Google Draco via Aspose.3D.  
- **Primaire bibliotheek?** Aspose.3D for Java (gebruikt voor zowel mesh‑creatie als Draco‑export).  
- **Typische implementatietijd?** Ongeveer 10‑15 minuten voor een basis-sfeer.  
- **Belangrijke voorwaarde?** Een Java‑ontwikkelomgeving met de Aspose.3D JAR‑bestanden op de classpath.  
- **Resultaat?** Een `.drc`‑file die **3d-modelgrootte** met tot 95 % verkleint ten opzichte van een niet‑gecomprimeerde mesh.

## Hoe 3d-modelgrootte te verkleinen?

De `Sphere`‑klasse genereert een getrianguleerde sferische geometrie op basis van de opgegeven straal‑ en tessellatie‑parameters. Laad je sfeer met `new Sphere(1.0, 32, 32)` en exporteer deze direct naar Draco met `scene.save("sphere.drc", SaveFormat.Draco)`. De `scene.save`‑methode schrijft de huidige scene naar een bestand in het opgegeven formaat. Aspose.3D behandelt de conversie intern, zodat je handmatige coderingsstappen vermijdt. De Draco‑exporteur past automatisch geometrie‑kwantisatie en vertex‑deduplicatie toe, waardoor bestanden vaak 80‑95 % kleiner zijn terwijl de visuele getrouwheid behouden blijft.

## Wat betekent “3d-modelgrootte verkleinen” in de context van 3d‑ontwikkeling?

**Het verkleinen van 3d‑modelgrootte** betekent het verminderen van de hoeveelheid geometrie‑data die moet worden overgedragen of opgeslagen, zonder merkbare degradatie van de visuele kwaliteit. Draco bereikt dit door vertex‑posities, normals en andere attributen te coderen in een zeer compact binair formaat. In combinatie met Aspose.3D blijft de volledige workflow binnen Java, zodat je geen native binaries hoeft te beheren.

## Waarom Google Draco‑meshcompressie gebruiken met Aspose.3D?

Google Draco in combinatie met Aspose.3D biedt een efficiënte pipeline die mesh‑bestanden dramatisch verkleint terwijl ze eenvoudig te integreren blijven in Java‑projecten. De bibliotheek behandelt alle low‑level codering, zodat ontwikkelaars zich kunnen concentreren op het creëren van geometrie zonder zich bezig te houden met native Draco‑binaries, wat leidt tot snellere ontwikkeling en kleinere assets voor web en mobiel.

- **Massieve grootte‑reductie:** Draco kan mesh‑data met tot 95 % verminderen voor typische modellen, waardoor een 5 MB OBJ wordt omgezet in een 0.3 MB `.drc`.  
- **Snelle runtime‑decodering:** Engines zoals Unity, Unreal en three.js decoderen Draco native, wat leidt tot snellere laadtijden.  
- **Naadloze Java‑integratie:** Aspose.3D abstraheert de native Draco‑bibliotheek, waardoor je binnen het Java‑ecosysteem blijft.  
- **Alles‑in‑één Aspose 3D‑export:** Dezelfde API die je gebruikt om geometrie te creëren, behandelt ook de export, waardoor de pipeline wordt vereenvoudigd.

## Vereisten

- **Java Development Kit (JDK)** – versie 8 of hoger.  
- **Aspose.3D for Java** – download de nieuwste JAR‑bestanden van de **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **Basiskennis van Google Draco** – je gebruikt de wrapper van Aspose.3D, dus er is geen native Draco‑installatie vereist.

## Pakketten importeren

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

Maak een nieuw Java‑project (elke IDE werkt) en voeg alle Aspose.3D‑JAR‑bestanden toe aan de classpath. Houd je bronbestanden in een package zoals `com.example.draco` voor duidelijkheid.

### Stap 2: hoe een sferische mesh te maken in Java

De `Sphere`‑klasse is de ingebouwde geometriegenerator van Aspose.3D die een getrianguleerde mesh produceert met een configureerbare straal en tessellatie.  

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

> **Pro tip:** De `Sphere`‑klasse genereert een getrianguleerde mesh met een standaardstraal van 1.0. Je kunt een aangepaste straal, tessellatie of materiaalparameters doorgeven als je een ander detailniveau nodig hebt vóór compressie.

### Stap 3: exporteer de mesh naar Draco‑formaat

Nadat de sfeer is toegevoegd aan een `Scene`‑object, roep je `scene.save("sphere.drc", SaveFormat.Draco)` aan. Aspose.3D selecteert automatisch de optimale compressie‑instellingen, maar je kunt ze fijn afstellen door `DracoCompressionOptions` aan te passen als je het kleinste mogelijke bestand nodig hebt. `DracoCompressionOptions` stelt je in staat om Draco‑compressie‑instellingen zoals kwantisatie en compressieniveau aan te passen.

### Stap 4: controleer de output

Open het gegenereerde `.drc`‑bestand met een Draco‑viewer (bijv. three.js `DRACOLoader`) om te controleren of de geometrie correct wordt gerenderd. Je zult een dramatische verkleining van de bestandsgrootte opmerken — vaak een factor tien of meer.

## Veelvoorkomende gebruikssituaties

| Scenario | Waarom modelgrootte verkleinen? | Hoe deze tutorial helpt |
|----------|-------------------------------|--------------------------|
| Web‑gebaseerde productconfigurators | Snellere paginaladingen bij trage verbindingen | Draco‑gecomprimeerde `.drc`‑bestanden laden in seconden |
| Mobiele AR/VR‑apps | Lagere geheugenvoetafdruk op apparaten | Kleinere meshes houden de app responsief |
| Cloud‑gerenderde scènes | Verminder bandbreedtekosten | Eén‑klik export vanuit Aspose.3D naar Draco |

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| **`NoClassDefFoundError` voor Draco‑klassen** | Aspose.3D JAR‑bestanden niet op de classpath | Controleer of *alle* Aspose.3D JAR‑bestanden zijn opgenomen en dat de versie overeenkomt met de documentatie. |
| **Uitvoerbestand is leeg** | `MyDir` wijst naar een niet‑bestaande map | Maak de map programmatisch aan (`Files.createDirectories(Paths.get(MyDir))`) vóór het schrijven van het bestand. |
| **Gecomprimeerde mesh ziet er vervormd uit** | Gebruik van een laag compressieniveau of onvoldoende tessellatie | Schakel over naar `DracoCompressionLevel.OPTIMAL` en verhoog de tessellatie van de sfeer (bijv. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` selecteert de hoogste compressiekwaliteit voor Draco‑output. |

## Veelgestelde vragen

**V: Is Aspose.3D compatibel met verschillende 3d‑bestandsformaten?**  
A: Ja, Aspose.3D ondersteunt OBJ, FBX, STL, GLTF en vele anderen, waardoor het een veelzijdige keuze is voor **Aspose 3d export**‑pipelines.

**V: Kan ik Google Draco gebruiken voor compressie in andere programmeertalen?**  
A: Absoluut. Draco biedt native bibliotheken voor C++, Python en JavaScript. Deze tutorial richt zich op Java, maar de concepten zijn toepasbaar in andere talen.

**V: Waar kan ik extra Aspose.3D‑documentatie vinden?**  
A: Bezoek de **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** voor volledige API‑referenties en meer voorbeelden.

**V: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D?**  
A: Bekijk de tijdelijke licentie‑opties op de **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**V: Is er een community‑forum voor Aspose.3D‑ondersteuning?**  
A: Ja, neem deel aan de discussie op het **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Conclusie

In deze gids hebben we laten zien hoe je **3d-modelgrootte** kunt verkleinen door een sferische mesh te maken in Java en deze vervolgens te comprimeren met Google Draco via Aspose.3D. Door deze beknopte stappen te volgen kun je mesh‑bestanden drastisch verkleinen, laadtijden verbeteren en je Java‑gebaseerde 3d‑applicaties responsief en bandbreedte‑vriendelijk houden.

---

**Last Updated:** 2026-09-08  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose

## Gerelateerde tutorials

- [Verminder 3D-bestandsgrootte – Scènes comprimeren met Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Genereer een Draco‑puntwolk van sferen met Aspose.3D for Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Leer hoe je meshes trianguleert voor geoptimaliseerde rendering in Java met Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}