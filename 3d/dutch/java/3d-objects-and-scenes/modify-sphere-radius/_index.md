---
date: 2026-10-03
description: Leer hoe je een bol in Java maakt en een OBJ‑bestand exporteert met Aspose.3D,
  de toonaangevende Java‑3D‑bibliotheek voor het converteren van 3D‑modellen.
images:
- /java/3d-objects-and-scenes/modify-sphere-radius/og-image.png
keywords:
- create sphere java
- save 3d as obj
- java convert 3d model
- write obj file java
lastmod: 2026-10-03
linktitle: 'Maak een bol in Java: Converteer 3D naar OBJ met Aspose.3D'
og_description: Leer hoe je een bol in Java maakt en een OBJ‑bestand exporteert met
  Aspose.3D. Deze stapsgewijze handleiding laat zien hoe je een bol toevoegt, de straal
  wijzigt en opslaat als OBJ.
og_image_alt: 'Guide: create sphere java and export OBJ using Aspose.3D'
og_title: Maak een bol in Java – Exporteer OBJ met Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-10-03'
  description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  headline: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to create sphere java and export OBJ file using Aspose.3D,
    the leading Java 3D library for converting 3D models.
  name: 'Create sphere java: Convert 3D to OBJ with Aspose.3D'
  steps:
  - name: Initialize a Scene
    text: '**Definition anchor:** The `Scene` class is Aspose.3D''s top‑level container
      that holds geometry, lights, and cameras for a 3D model. Creating a `Scene`
      gives you a workspace where you can add and manipulate objects. Creating a `Scene`
      gives you a container for all geometry, lights, and cameras. This'
  - name: Initialize a Sphere
    text: '**Definition anchor:** The `Sphere` class represents a geometric sphere
      primitive with a configurable radius, center, and material. By default it starts
      with a radius of 1.0. A `Sphere` object starts with a default radius of 1.0.
      Think of it as a blank canvas for the shape you want to export.'
  - name: Set the Desired Radius
    text: The `setRadius(double)` method updates the sphere’s size by assigning a
      new radius value in the same units used by the scene. Here we **write obj file
      java**‑style code that sets the exact radius. Replace `10` with any `double`
      value that matches your design requirements.
  - name: Add Sphere to the Scene
    text: This line **adds sphere to scene** by creating a child node under the root
      node. It’s the moment the geometry becomes part of the scene graph.
  - name: Export the Model as OBJ
    text: The `save(String, FileFormat)` method writes the entire scene to the specified
      file using the chosen format, such as OBJ. Calling `scene.save` **exports obj
      file java**‑style, effectively **save scene as obj**. The generated `sphere.obj`
      can be opened in any standard 3D viewer.
  type: HowTo
- questions:
  - answer: You can refer to the [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/)
      for comprehensive guidance.
    question: Where can I find the documentation for Aspose.3D for Java?
  - answer: 'Download the library from the releases page: [Download Aspose.3D for
      Java](https://releases.aspose.com/3d/java/).'
    question: How do I download Aspose.3D for Java?
  - answer: Yes, explore the features with a free trial by visiting [Aspose.3D Free
      Trial](https://releases.aspose.com/).
    question: Is there a free trial available for Aspose.3D for Java?
  - answer: Join the Aspose community at [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18)
      for assistance and discussions.
    question: Where can I get support for Aspose.3D for Java?
  - answer: Get a temporary license by visiting [Temporary License](https://purchase.aspose.com/temporary-license/).
    question: How can I obtain a temporary license for Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- modify sphere radius
- export OBJ
- aspose.3d
- java 3d
- 3d conversion
title: 'Maak een bol in Java: Converteer 3D naar OBJ met Aspose.3D'
url: /nl/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak een bol in Java en exporteer naar OBJ

## Introductie

In deze tutorial leer je hoe je **een bol in Java** maakt, de straal aanpast, en vervolgens **3D opslaat als OBJ** met behulp van de Aspose.3D Java‑bibliotheek. We lopen elke regel code door, leggen uit waarom elke stap belangrijk is, en geven je praktische tips zodat je deze workflow met vertrouwen kunt integreren in games, CAD‑tools of wetenschappelijke visualisaties.

## Snelle antwoorden
- **Wat is het hoofddoel van deze tutorial?** Om te demonstreren hoe je een bol in Java maakt, de grootte aanpast, en het model exporteert als OBJ met Java.
- **Welke bibliotheek levert de 3D‑functionaliteit?** Aspose.3D, een volledig uitgeruste **java 3d library tutorial**.
- **Hoe wijzig ik de grootte van de bol?** Roep `sphere.setRadius(double)` aan op de `Sphere`‑instantie.
- **Kan ik het OBJ‑bestand direct vanuit Java schrijven?** Ja—gebruik `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.
- **Heb ik een licentie nodig voor productie?** Een gratis proefversie is voldoende voor ontwikkeling; een permanente licentie is vereist voor commercieel gebruik.

## Wat is Aspose.3D voor Java?

Aspose.3D voor Java is een uitgebreide **java 3d library** die ontwikkelaars in staat stelt 3D‑bestanden te maken, bewerken en converteren zonder externe afhankelijkheden. Het ondersteunt meer dan **50 invoer‑ en uitvoerformaten**—inclusief OBJ, FBX, STL en GLTF—waardoor naadloze integratie in elke 3‑D‑pipeline mogelijk is.

## Waarom 3D naar OBJ converteren?

Converteren naar OBJ levert een universeel ondersteunde, platte‑tekst representatie van geometrie op die door elk 3D‑tool kan worden gelezen, wat ideaal is voor snelle prototyping, cross‑platform asset‑uitwisseling en eenvoudige debugging van vertex‑data. Omdat OBJ‑bestanden lichtgewicht en mens‑leesbaar zijn, kun je ze indien nodig inspecteren of aanpassen met een eenvoudige teksteditor.

## Vereisten

- Basiskennis van Java‑programmeren.  
- Aspose.3D‑bibliotheek geïnstalleerd – download deze van de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 of hoger geïnstalleerd op je ontwikkelmachine.

## Import pakketten

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Hoe de straal van een bol in Java aanpassen?

`Sphere` is een geometrisch primitief dat een bol in Aspose.3D vertegenwoordigt.

Load de `Sphere`‑object, roep `setRadius` aan met de gewenste waarde, en sla vervolgens de scene op als OBJ—deze volledige workflow kan in vijf beknopte stappen worden uitgevoerd. De aanpak werkt voor elke numerieke straal en garandeert dat de geëxporteerde OBJ exact de grootte weergeeft die je opgeeft.

### Stap 1: Initialiseer een scene

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** De `Scene`‑klasse is de top‑level container van Aspose.3D die geometrie, lichten en camera's voor een 3D‑model bevat. Een `Scene` aanmaken geeft je een werkruimte waarin je objecten kunt toevoegen en manipuleren.

Een `Scene` creëert een container voor alle geometrie, lichten en camera's. Hier zullen we later **een bol aan de scene toevoegen**.

### Stap 2: Initialiseer een bol

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** De `Sphere`‑klasse vertegenwoordigt een geometrisch bol‑primitief met een configureerbare straal, centrum en materiaal. Standaard start het met een straal van 1.0.

Een `Sphere`‑object start met een standaardstraal van 1.0. Beschouw het als een leeg canvas voor de vorm die je wilt exporteren.

### Stap 3: Stel de gewenste straal in

**Definition anchor:** De `setRadius(double)`‑methode stelt de straal van de bol in dezelfde eenheden in die door de scene worden gebruikt.  

```java
// set radius
sphere.setRadius(10);
```

Hier schrijven we **obj‑bestand java**‑stijl code die de exacte straal instelt. Vervang `10` door elke `double`‑waarde die aan je ontwerpeisen voldoet.

### Stap 4: Voeg de bol toe aan de scene

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Deze regel **voegt de bol toe aan de scene** door een kind‑node onder de root‑node te creëren. Het is het moment waarop de geometrie deel wordt van de scene‑graph.

### Stap 5: Exporteer het model als OBJ

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

De `save(String, FileFormat)`‑methode schrijft de volledige scene naar het opgegeven bestand met het gekozen formaat, zoals OBJ. Het aanroepen van `scene.save` **exporteert obj‑bestand java**‑stijl, effectief **scene opslaan als obj**. Het gegenereerde `sphere.obj` kan worden geopend in elke standaard 3D‑viewer.

## Veelvoorkomende problemen en oplossingen

| Probleem | Oplossing |
|----------|-----------|
| **Bol verschijnt te klein in de viewer** | Controleer of de straalwaarde correct is ingesteld; onthoud dat eenheden willekeurig zijn tenzij je een schaaltransformatie toepast. |
| **Geëxporteerde OBJ heeft geen materiaal** | Aspose.3D schrijft alleen geometrie; voeg een materiaal toe aan de bol als je texturen nodig hebt (`sphere.setMaterial(...)`). |
| **Licentie‑exception tijdens runtime** | Zorg ervoor dat je een tijdelijk of permanent licentiebestand hebt geladen voordat je de `Scene` aanmaakt. |

## Veelgestelde vragen

**Q: Waar kan ik de documentatie voor Aspose.3D voor Java vinden?**  
A: Je kunt de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) raadplegen voor uitgebreide begeleiding.

**Q: Hoe download ik Aspose.3D voor Java?**  
A: Download de bibliotheek van de releases‑pagina: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Is er een gratis proefversie beschikbaar voor Aspose.3D voor Java?**  
A: Ja, verken de functies met een gratis proefversie via [Aspose.3D Free Trial](https://releases.aspose.com/).

**Q: Waar kan ik ondersteuning krijgen voor Aspose.3D voor Java?**  
A: Word lid van de Aspose‑community op het [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) voor hulp en discussies.

**Q: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?**  
A: Verkrijg een tijdelijke licentie via [Temporary License](https://purchase.aspose.com/temporary-license/).

**Q: Kan ik deze code gebruiken met andere 3D‑formaten zoals STL?**  
A: Absoluut – wijzig gewoon de `FileFormat`‑enum bij het aanroepen van `scene.save`, bijvoorbeeld `FileFormat.STL`.

---

**Laatst bijgewerkt:** 2026-10-03  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose

## Gerelateerde tutorials

- [How to Set Normals on 3D Objects in Java Using Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [How to Embed Texture in FBX with Java – Apply Materials to 3D Objects using Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [How to Change Plane Orientation and Export OBJ in Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}