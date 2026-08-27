---
date: 2026-06-03
description: Leer hoe je een scène kunt exporteren als FBX en 3D-cilinder, -doos en
  andere primitieve modellen kunt maken met Aspose.3D voor Java.
keywords:
- export scene as fbx
- convert 3d model fbx
- Aspose 3D primitives
- Java 3D modeling
linktitle: Primitieve 3D-modellen bouwen met Aspose.3D voor Java
schemas:
- author: Aspose
  dateModified: '2026-06-03'
  description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  headline: Export scene as FBX and build cylinder with Aspose.3D Java
  type: TechArticle
- description: Learn how to export scene as FBX and create 3D cylinder, box, and other
    primitive models using Aspose.3D for Java.
  name: Export scene as FBX and build cylinder with Aspose.3D Java
  steps:
  - name: Initialize a Scene Object
    text: The `Scene` class is Aspose.3D's top‑level container that holds all nodes,
      lights, cameras, and materials in memory.
  - name: Build a 3D box model
    text: The `Box` class represents a rectangular prism and is useful for testing
      the coordinate system. Adding it as a child of the scene’s root node positions
      it at the origin.
  - name: Create a 3D cylinder model
    text: The `Cylinder` class is Aspose.3D's built‑in cylinder primitive. It comes
      with default dimensions (radius = 1, height = 2) but you can customise them
      via its constructor.
  - name: Save the drawing in the FBX format
    text: After assembling the scene, export it so other tools (e.g., Unity, Blender)
      can read it. We use the `FBX7500ASCII` format, which is widely supported and
      human‑readable.
  type: HowTo
- questions:
  - answer: Aspose.3D primarily supports Java, but there are versions available for
      .NET and C++ as well.
    question: Can I use Aspose.3D for Java with other programming languages?
  - answer: Absolutely. It provides a comprehensive set of features—including mesh
      manipulation, material assignment, and animation—making it suitable for both
      simple primitives and intricate models.
    question: Is Aspose.3D suitable for complex 3D modeling tasks?
  - answer: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for community
      support and discussions.
    question: Where can I find additional help and support?
  - answer: Yes, you can explore a [free trial](https://releases.aspose.com/) before
      making a purchase decision.
    question: Can I try Aspose.3D before purchasing?
  - answer: You can obtain a [temporary license](https://purchase.aspose.com/temporary-license/)
      for Aspose.3D through the website.
    question: How do I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
title: Exporteer scène als FBX en bouw cilinder met Aspose.3D Java
url: /nl/java/primitive-3d-models/building-primitive-3d-models/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exporteer scène als FBX en bouw cilinder met Aspose.3D Java

## Inleiding

Als je ooit een **een 3D cylinder maken** (of een andere basisvorm) direct vanuit Java-code moest maken, maakt Aspose.3D de taak moeiteloos. In deze tutorial lopen we het volledige workflow door — van het opzetten van de omgeving tot **exporteer scène als FBX** — zodat je meteen programmatisch 3D-geometrie kunt genereren. Je ziet hoe de bibliotheek primitives behandelt, hoe je ze organiseert in een scene graph, en hoe je het resultaat opslaat in een formaat dat Unity, Blender of een andere 3D-tool kan lezen.

## Snelle antwoorden

- **Welke bibliotheek laat me een 3D cylinder maken in Java?** Aspose.3D for Java.  
- **Naar welk formaat kan ik de scène exporteren?** FBX (ASCII 7500) using `FileFormat.FBX7500ASCII`.  
- **Heb ik een licentie nodig voor ontwikkeling?** Een gratis proefversie werkt voor testen; een permanente licentie is vereist voor productie.  
- **Wat zijn de belangrijkste ondersteunde primitives?** Box, Cylinder, Sphere, Cone, en meer dan 10 extra vormen.  
- **Is de code compatibel met Java 8 en later?** Ja, Aspose.3D richt zich op JDK 8+.

## Wat is een 3D cylinder primitive?

Een cylinder primitive is een basis geometrische vorm gedefinieerd door een straal en hoogte. In veel 3D-pijplijnen dient het als bouwsteen voor complexere modellen zoals buizen, wielen of architecturale kolommen. Aspose.3D biedt een kant‑klare `Cylinder`‑klasse, zodat je de vertices niet handmatig hoeft te berekenen.

## Waarom Aspose.3D voor Java gebruiken?

Aspose.3D for Java biedt een uitgebreide, pure‑Java 3D‑engine die de noodzaak voor native bibliotheken elimineert, waardoor het ideaal is voor cross‑platform ontwikkeling. Het ondersteunt een breed scala aan import‑ en exportformaten, biedt een robuuste scene graph voor hiërarchische organisatie, en bevat ingebouwde primitives waarmee je geometrie kunt creëren met minimale code. Deze functies versnellen samen de ontwikkeling en verminderen onderhoudslast.

- **Full‑featured 3D engine** – ondersteunt import/export van **meer dan 30** populaire formaten (FBX, OBJ, STL, GLTF, 3DS, etc.).  
- **Pure Java API** – geen native afhankelijkheden, perfect voor cross‑platform projecten.  
- **Robust scene graph** – laat je objecten hiërarchisch organiseren, waardoor grote scènes gemakkelijk te beheren zijn.  
- **Easy licensing** – begin met een gratis proefversie, upgrade vervolgens naar een permanente licentie wanneer je live gaat.

## Voorvereisten

Voordat je in de code duikt, zorg ervoor dat je het volgende hebt:

1. **Java Development Kit (JDK)** – JDK 8 of nieuwer geïnstalleerd op je machine.  
2. **Aspose.3D for Java library** – download en installeer het vanaf de [download page](https://releases.aspose.com/3d/java/).  

## Importeer pakketten

Begin met het importeren van de core Aspose.3D namespace. Dit geeft je toegang tot `Scene`, `Box`, `Cylinder` en bestandsformaat‑constanten.

```java
import com.aspose.threed.*;
```

Nu de bibliotheek is gerefereerd, laten we een scène maken en wat primitive geometrie toevoegen.

## Hoe exporteer je scène als FBX en maak je 3D primitives?

Laad een nieuw `Scene`‑object, voeg primitive nodes toe (Box, Cylinder, etc.), en roep vervolgens `save` aan met het FBX7500ASCII‑formaat. In slechts een paar regels krijg je een volledig‑functioneel FBX‑bestand dat in elke belangrijke 3D‑editor kan worden geopend, waardoor naadloze integratie met game‑engines, render‑pijplijnen of AR/VR‑toepassingen mogelijk is.

### Stap 1: Initialiseert een Scene‑object

De `Scene`‑klasse is de top‑level container van Aspose.3D die alle nodes, lichten, camera's en materialen in het geheugen bevat.

```java
// The path to the documents directory.
String myDir = "Your Document Directory";

// Initialize a Scene object
Scene scene = new Scene();
```

### Stap 2: Bouw een 3D‑boxmodel

De `Box`‑klasse vertegenwoordigt een rechthoekig prisma en is nuttig voor het testen van het coördinatensysteem. Het toevoegen als kind van de root‑node van de scène positioneert het op de oorsprong.

```java
// Create a Box model
scene.getRootNode().createChildNode("box", new Box());
```

### Stap 3: Maak een 3D‑cylinder model

De `Cylinder`‑klasse is de ingebouwde cylinder primitive van Aspose.3D. Het wordt geleverd met standaardafmetingen (radius = 1, hoogte = 2) maar je kunt ze aanpassen via de constructor.

```java
// Create a Cylinder model
scene.getRootNode().createChildNode("cylinder", new Cylinder());
```

### Stap 4: Sla de tekening op in het FBX‑formaat

Na het samenstellen van de scène, exporteer je deze zodat andere tools (bijv. Unity, Blender) deze kunnen lezen. We gebruiken het `FBX7500ASCII`‑formaat, dat breed ondersteund en mens‑leesbaar is.

```java
// Save drawing in the FBX format
myDir = myDir + "test.fbx";
scene.save(myDir, FileFormat.FBX7500ASCII);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **File not found** when saving | `myDir` wijst naar een niet‑bestaande map | Zorg ervoor dat de map bestaat of maak deze aan met `new File(myDir).mkdirs();` |
| **Empty scene** after export | Er zijn geen nodes toegevoegd voordat `save` werd aangeroepen | Controleer of `createChildNode`‑calls worden uitgevoerd (debug met `scene.getRootNode().getChildCount()` ) |
| **License exception** | Uitvoeren zonder een geldige licentie in productie | Pas een tijdelijke of permanente licentie toe met `License license = new License(); license.setLicense("Aspose.3D.Java.lic");` |

## Veelgestelde vragen

**Q: Kan ik Aspose.3D voor Java gebruiken met andere programmeertalen?**  
A: Aspose.3D ondersteunt voornamelijk Java, maar er zijn ook versies beschikbaar voor .NET en C++.

**Q: Is Aspose.3D geschikt voor complexe 3D-modellerings taken?**  
A: Absoluut. Het biedt een uitgebreide set functies — waaronder mesh-manipulatie, materiaaltoewijzing en animatie — waardoor het geschikt is voor zowel eenvoudige primitives als ingewikkelde modellen.

**Q: Waar kan ik extra hulp en ondersteuning vinden?**  
A: Bezoek het [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) voor community‑ondersteuning en discussies.

**Q: Kan ik Aspose.3D uitproberen voordat ik koop?**  
A: Ja, je kunt een [free trial](https://releases.aspose.com/) verkennen voordat je een aankoopbeslissing maakt.

**Q: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D?**  
A: Je kunt een [temporary license](https://purchase.aspose.com/temporary-license/) voor Aspose.3D verkrijgen via de website.

## Conclusie

Je hebt nu geleerd hoe je **exporteer scène als FBX**, en hoe je **een 3D cylinder**, box en andere primitive modellen maakt met Aspose.3D for Java. Voel je vrij om te experimenteren met extra primitives zoals Sphere, Cone of Torus, en verken materiaaltoewijzingen om je modellen een realistisch uiterlijk te geven. Zodra je vertrouwd bent, kun je de gegenereerde FBX‑bestanden integreren in game‑engines, AR/VR‑pijplijnen, of elke downstream 3D‑workflow.

---

**Laatst bijgewerkt:** 2026-06-03  
**Getest met:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Auteur:** Aspose

## Gerelateerde tutorials

- [Hoe scène exporteren naar FBX en 3D scène‑informatie ophalen in Java](/3d/java/3d-scenes-and-models/get-scene-information/)
- [Hoe FBX exporteren en node‑hiërarchieën bouwen in Java](/3d/java/geometry/build-node-hierarchies/)
- [Hoe cilinder‑modellen maken met Aspose.3D voor Java](/3d/java/cylinders/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}