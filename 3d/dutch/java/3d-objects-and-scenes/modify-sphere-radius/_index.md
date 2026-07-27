---
date: 2026-07-27
description: Leer hoe je de sphere radius in Java kunt wijzigen en een OBJ‑bestand
  kunt exporteren met Aspose.3D, de toonaangevende Java‑3D‑bibliotheek voor het converteren
  van 3D naar OBJ.
keywords:
- modify sphere radius java
- export obj file java
- aspose 3d java
lastmod: 2026-07-27
linktitle: 'Sphere Radius Wijzigen in Java: 3D Converteren naar OBJ met Aspose.3D'
og_description: Wijzig de sphere radius in Java en exporteer een OBJ‑bestand met Aspose.3D.
  Deze tutorial laat stap‑voor‑stap zien hoe je een sphere toevoegt, de grootte aanpast
  en opslaat als OBJ.
og_image_alt: 'Guide: modify sphere radius Java and export OBJ using Aspose.3D'
og_title: Sphere Radius Wijzigen in Java – 3D Converteren naar OBJ met Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-07-27'
  description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  headline: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
  type: TechArticle
- description: Learn how to modify sphere radius Java and export OBJ file Java using
    Aspose.3D, the leading Java 3D library for converting 3D to OBJ.
  name: 'Modify Sphere Radius Java: Convert 3D to OBJ with Aspose.3D'
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
title: 'Sphere Radius Wijzigen in Java: 3D Converteren naar OBJ met Aspose.3D'
url: /nl/java/3d-objects-and-scenes/modify-sphere-radius/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Convert 3D naar OBJ: Voeg een bol toe & wijzig de straal in Java

## Introductie

Als je snel en programmatically de **modify sphere radius java** wilt aanpassen, laat deze gids je precies zien hoe je een bol aan een scène toevoegt, de straal wijzigt en het resulterende OBJ‑bestand schrijft met behulp van de **Aspose.3D Java library**. We lopen elke regel code door, leggen uit waarom elke stap belangrijk is, en geven tips om veelvoorkomende valkuilen te vermijden—zodat je de workflow met vertrouwen kunt integreren in games, CAD‑tools of wetenschappelijke visualisaties.

## Snelle Antwoorden
- **What is the main goal of this tutorial?** Om te demonstreren hoe je 3D naar OBJ converteert door een bol te maken, de straal aan te passen en het model in Java te exporteren.  
- **Which library provides the 3D functionality?** Aspose.3D, een volledige **java 3d library tutorial**.  
- **How do I change the sphere size?** Roep `sphere.setRadius(double)` aan op de `Sphere`‑instantie.  
- **Can I write the OBJ file directly from Java?** Ja—gebruik `scene.save("file.obj", FileFormat.WAVEFRONTOBJ)`.  
- **Do I need a license for production?** Een gratis proefversie is voldoende voor ontwikkeling; een permanente licentie is vereist voor commercieel gebruik.

## Wat is Aspose.3D voor Java?

Aspose.3D for Java is een uitgebreide **java 3d library** die ontwikkelaars in staat stelt 3D‑bestanden te maken, bewerken en converteren zonder externe afhankelijkheden. Het ondersteunt meer dan **50 input- en outputformaten**—inclusief OBJ, FBX, STL en GLTF—waardoor naadloze integratie in elke 3‑D‑pipeline mogelijk is.

## Waarom 3D naar OBJ converteren?

Converteren naar OBJ levert een universeel leesbare, platte‑tekstrepresentatie van geometrie op die kan worden geïnspecteerd, bewerkt en geïmporteerd door vrijwel elke 3D‑applicatie, waardoor het ideaal is voor snelle prototyping en cross‑platform asset‑uitwisseling.

- **Universele compatibiliteit** – OBJ wordt ondersteund door vrijwel elke 3D‑viewer, game‑engine en modelleringssoftware.  
- **Lichtgewicht export** – OBJ slaat geometrie op in een platte‑tekstformaat, wat gemakkelijk te inspecteren en debuggen is.  
- **Workflowflexibiliteit** – Je kunt OBJ‑bestanden on‑the‑fly genereren vanuit server‑side Java‑code, waardoor geautomatiseerde pipelines voor asset‑creatie mogelijk zijn.

## Vereisten

- Basiskennis van Java‑programmeren.  
- Aspose.3D‑bibliotheek geïnstalleerd – download deze van de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/).  
- JDK 8 of later geïnstalleerd op je ontwikkelmachine.

## Importpakketten

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Sphere;

import java.io.IOException;
```

## Hoe de straal van een bol in Java te wijzigen?

Laad het `Sphere`‑object, roep `setRadius` aan met de gewenste waarde, en sla vervolgens de scène op als OBJ—deze volledige workflow kan in vijf beknopte stappen worden uitgevoerd. De aanpak werkt voor elke numerieke straal en garandeert dat de geëxporteerde OBJ de exacte grootte weergeeft die je opgeeft.

### Stap 1: Initialiseer een scène

```java
// ExStart:WorkingWithSphereRadius

// initialize a scene
Scene scene = new Scene();
```

**Definition anchor:** De `Scene`‑klasse is de top‑level container van Aspose.3D die geometrie, lichten en camera's voor een 3D‑model bevat. Het maken van een `Scene` geeft je een werkruimte waarin je objecten kunt toevoegen en manipuleren.

Het creëren van een `Scene` geeft je een container voor alle geometrie, lichten en camera's. Dit is waar we later **add sphere to scene** zullen toevoegen.

### Stap 2: Initialiseer een bol

```java
// initialize a Sphere
Sphere sphere = new Sphere();
```

**Definition anchor:** De `Sphere`‑klasse vertegenwoordigt een geometrische bol‑primitive met een configureerbare straal, centrum en materiaal. Standaard start deze met een straal van 1.0.

Een `Sphere`‑object start met een standaardstraal van 1.0. Beschouw het als een leeg canvas voor de vorm die je wilt exporteren.

### Stap 3: Stel de gewenste straal in

De `setRadius(double)`‑methode werkt de grootte van de bol bij door een nieuwe straalwaarde toe te wijzen in dezelfde eenheden die door de scène worden gebruikt.

```java
// set radius
sphere.setRadius(10);
```

Hier gebruiken we **write obj file java**‑stijl code die de exacte straal instelt. Vervang `10` door elke `double`‑waarde die overeenkomt met je ontwerpvereisten.

### Stap 4: Voeg de bol toe aan de scène

```java
// add sphere to the scene
scene.getRootNode().createChildNode(sphere);
```

Deze regel **adds sphere to scene** door een kind‑node onder de root‑node te creëren. Het is het moment waarop de geometrie deel wordt van de scene‑graph.

### Stap 5: Exporteer het model als OBJ

De `save(String, FileFormat)`‑methode schrijft de volledige scène naar het opgegeven bestand met het gekozen formaat, zoals OBJ.

```java
// save scene
scene.save("sphere.obj", FileFormat.WAVEFRONTOBJ);
```

Het aanroepen van `scene.save` **exports obj file java**‑stijl, effectief **save scene as obj**. Het gegenereerde `sphere.obj` kan worden geopend in elke standaard 3D‑viewer.

## Veelvoorkomende problemen en oplossingen

| Probleem | Oplossing |
|----------|-----------|
| **Sphere appears too small in de viewer** | Controleer of de radiuswaarde correct is ingesteld; onthoud dat eenheden willekeurig zijn tenzij je een schaaltransformatie toepast. |
| **Exported OBJ has no material** | Aspose.3D schrijft alleen geometrie; voeg een materiaal toe aan de bol als je texturen nodig hebt (`sphere.setMaterial(...)`). |
| **License exception at runtime** | Zorg ervoor dat je een tijdelijk of permanent licentiebestand hebt geladen voordat je de `Scene` maakt. |

## Veelgestelde vragen

**Q: Waar kan ik de documentatie voor Aspose.3D voor Java vinden?**  
A: U kunt de [Aspose.3D for Java documentation](https://reference.aspose.com/3d/java/) raadplegen voor uitgebreide begeleiding.

**Q: Hoe download ik Aspose.3D voor Java?**  
A: Download de bibliotheek van de releases-pagina: [Download Aspose.3D for Java](https://releases.aspose.com/3d/java/).

**Q: Is er een gratis proefversie beschikbaar voor Aspose.3D voor Java?**  
A: Ja, verken de functies met een gratis proefversie via [Aspose.3D Free Trial](https://releases.aspose.com/).

**Q: Waar kan ik ondersteuning krijgen voor Aspose.3D voor Java?**  
A: Word lid van de Aspose-community op [Aspose.3D Support Forum](https://forum.aspose.com/c/3d/18) voor hulp en discussies.

**Q: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?**  
A: Krijg een tijdelijke licentie via [Temporary License](https://purchase.aspose.com/temporary-license/).

**Q: Kan ik deze code gebruiken met andere 3D-formaten zoals STL?**  
A: Absoluut – wijzig gewoon de `FileFormat`‑enum bij het aanroepen van `scene.save`, bijv. `FileFormat.STL`.

---

**Last Updated:** 2026-07-27  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose

## Gerelateerde tutorials

- [Hoe normalen in te stellen op 3D‑objecten in Java met Aspose.3D Java API](/3d/java/geometry/set-up-normals-on-3d-objects/)
- [Hoe textuur in FBX in te sluiten met Java – Materialen toepassen op 3D‑objecten met Aspose.3D](/3d/java/geometry/apply-materials-to-3d-objects/)
- [Hoe de oriëntatie van een vlak te wijzigen en OBJ te exporteren in Java](/3d/java/3d-scenes-and-models/change-plane-orientation/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< blocks/products/products-backtop-button >}}
{{< /blocks/products/pf/main-wrap-class >}}