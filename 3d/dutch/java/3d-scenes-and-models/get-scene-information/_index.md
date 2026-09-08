---
date: 2026-09-08
description: Leer hoe je eenheden definieert en een scène exporteert naar FBX in Java
  met Aspose.3D. Deze stapsgewijze gids laat zien hoe je de toepassingsnaam, meeteenheden
  instelt en 3D‑scène‑informatie opvraagt.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Hoe FBX opslaan en 3D‑scène‑informatie ophalen in Java
og_description: Leer hoe je eenheden definieert en een scène exporteert naar FBX in
  Java met Aspose.3D. De gids behandelt het instellen van de toepassingsnaam, meeteenheden
  en het ophalen van 3D‑scène‑informatie in enkele stappen.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Hoe eenheden definiëren en een scène exporteren naar FBX in Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Hoe eenheden definiëren en een scène exporteren naar FBX in Java
url: /nl/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe eenheden definiëren en scène exporteren naar FBX in Java

## Inleiding

Als je op zoek bent naar een duidelijke, praktische gids over **hoe eenheden te definiëren** en **een scène naar FBX te exporteren** terwijl je bruikbare metadata uit je 3D‑scènes haalt, ben je hier aan het juiste adres. In deze tutorial lopen we elke stap door met behulp van de **Aspose.3D for Java**‑bibliotheek: van het maken van een scène, **het instellen van de applicatienaam**, **het definiëren van meeteenheden**, tot uiteindelijk **het exporteren van de scène naar FBX**. Aan het einde heb je een kant‑klaar FBX‑bestand dat de asset‑informatie bevat die je nodig hebt voor downstream‑pijplijnen.

## Snelle antwoorden
- **Wat is het primaire doel?** Exporteer een scène naar FBX die aangepaste asset‑informatie bevat.  
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java.  
- **Heb ik een licentie nodig?** Een gratis proefversie werkt voor ontwikkeling; een commerciële licentie is vereist voor productie.  
- **Kan ik de meeteenheden wijzigen?** Ja – gebruik `setUnitName` en `setUnitScaleFactor`.  
- **Waar wordt de output opgeslagen?** Naar het pad dat je opgeeft in `scene.save(...)`.  

## Voorvereisten

Voordat we beginnen, zorg ervoor dat je het volgende hebt:

- Een stevige kennis van de basis Java‑syntaxis.  
- **Aspose.3D for Java** gedownload en aan je project toegevoegd (je kunt het verkrijgen van de officiële) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Je favoriete Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans, enz.) correct geconfigureerd.

## Importeer pakketten

In je Java‑bronbestand importeer je de Aspose.3D‑klassen die scène‑beheer en bestandsformaatondersteuning bieden.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Houd de importlijst minimaal om onnodige afhankelijkheden te vermijden en de compile‑tijden te verbeteren.

## Wat is het proces voor het opslaan van een FBX‑bestand?

Om een scène op te slaan als een FBX‑bestand maak je een `Scene`, stel je gewenste asset‑metadata in, definieer je de meeteenheid, en roep je vervolgens `scene.save(path, FileFormat.FBX7500ASCII)` aan. Deze reeks schrijft geometrie, materialen en metadata naar een ASCII‑FBX die kan worden geïnspecteerd of geïmporteerd door downstream‑tools.

### Stap 1: initialiseert een 3D‑scène

De `Scene`‑klasse is de top‑level container van Aspose.3D die een volledige 3D‑scène vertegenwoordigt, inclusief geometrie, lichten, camera's en metadata. Maak eerst een leeg `Scene`‑object aan. Dit wordt de container voor alle geometrie, lichten, camera's en asset‑metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Hoe de applicatienaam in Java in te stellen

Het `AssetInfo`‑object slaat metadata op zoals de applicatienaam, leverancier en versie voor de scène. Het toevoegen van aangepaste metadata helpt downstream‑tools de bron van het bestand te identificeren. Gebruik het `AssetInfo`‑object om **de applicatienaam** (en leverancier) **in te stellen** voordat je het bestand opslaat.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Waarom dit belangrijk is:** Veel pijplijnen filteren of taggen assets op basis van de oorspronkelijke applicatie, waardoor deze stap essentieel is voor grote projecten.

### Stap 3: meeteenheden definiëren

Het eenheidssysteem bepaalt de schaal in de echte wereld van de scène; Aspose.3D laat je een eenheidsnaam en een schaalfactor ten opzichte van meters opgeven. In dit voorbeeld gebruiken we een oude Egyptische eenheid genaamd “pole” met een aangepaste schaalfactor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Pas `unitScaleFactor` aan om overeen te komen met de werkelijke grootte van je modellen; 1.0 staat voor een 1‑op‑1‑mapping met de gekozen eenheid.

### Stap 4: scène exporteren naar FBX

Nu de asset‑informatie is toegevoegd, slaan we de scène op als een FBX‑bestand. De optie `FileFormat.FBX7500ASCII` produceert een mens‑leesbare ASCII‑FBX, wat handig is voor debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Onthoud:** Vervang `"Your Document Directory"` door een absoluut pad of een pad relatief aan de werkmap van je project.

## Waarom scène exporteren naar FBX met Aspose.3D?

Aspose.3D ondersteunt **meer dan 50 invoer‑ en uitvoerformaten** en kan multi‑honderd‑pagina scènes verwerken zonder het volledige bestand in het geheugen te laden, waardoor je volledige controle krijgt over het geëxporteerde bestand—metadata, eenheden en geometrie—zonder een zware 3D‑authoring‑applicatie nodig te hebben. Dit maakt geautomatiseerde asset‑generatie, batch‑verwerking en server‑side conversies snel en betrouwbaar.

## Veelvoorkomende gebruikssituaties

- **Game‑asset‑pijplijnen** – embed creator‑informatie direct in FBX‑bestanden voor versie‑tracking.  
- **Architecturale visualisatie** – sla projectspecifieke eenheden op om schaalfouten te voorkomen bij het importeren in render‑engines.  
- **Geautomatiseerde rapportage** – genereer FBX‑bestanden on‑the‑fly met metadata die downstream‑analyse‑tools kunnen lezen.  
- **Cloud‑gebaseerde 3D‑diensten** – programmeermatig scènes creëren en exporteren zonder GUI, perfect voor SaaS‑platformen.

## Probleemoplossing & tips

| Probleem | Oplossing |
|-------|----------|
| **Bestand niet gevonden na opslaan** | Controleer of `MyDir` naar een bestaande map wijst en dat je applicatie schrijfrechten heeft. |
| **Eenheden lijken onjuist in externe viewer** | Controleer `unitScaleFactor` opnieuw; sommige viewers verwachten meters als basiseenheid. |
| **Asset‑metadata ontbreekt** | Zorg ervoor dat je `scene.getAssetInfo()` **vóór** het opslaan aanroept; wijzigingen na `save()` worden niet bewaard. |
| **Prestatie‑knelpunt bij grote scènes** | Gebruik `scene.optimize()` vóór het opslaan om het geheugenverbruik te verminderen. |
| **ASCII FBX is te groot** | Schakel over naar binaire FBX door `FileFormat.FBX7500` te gebruiken (zie FAQ). |

## Veelgestelde vragen

**V: Hoe wijzig ik het uitvoerformaat naar binaire FBX?**  
A: Vervang `FileFormat.FBX7500ASCII` door `FileFormat.FBX7500` bij het aanroepen van `scene.save(...)`.

**V: Kan ik aangepaste, door de gebruiker gedefinieerde metadata toevoegen naast de ingebouwde asset‑velden?**  
A: Ja, gebruik `scene.getUserData().add("Key", "Value")` om extra sleutel‑waardeparen in te sluiten.

**V: Ondersteunt Aspose.3D andere exportformaten zoals OBJ of GLTF?**  
A: Ja. Verander simpelweg de `FileFormat`‑enum naar `OBJ` of `GLTF2` indien nodig.

**V: Welke Java‑versie is vereist?**  
A: Aspose.3D for Java ondersteunt Java 8 en hoger.

**V: Is het mogelijk een bestaand FBX‑bestand te laden, de asset‑info te wijzigen en opnieuw op te slaan?**  
A: Absoluut. Laad het bestand met `new Scene("input.fbx")`, wijzig `scene.getAssetInfo()`, en sla vervolgens op.

---

**Laatst bijgewerkt:** 2026-09-08  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose

## Gerelateerde tutorials

- [3D‑bestandsgrootte verkleinen – Scènes comprimeren met Aspose.3D for Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Hoe vector3‑kleur in Java in te stellen: Diffuse‑kleur wijzigen en 3D‑eigenschappen beheren in Java‑scènes met Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}