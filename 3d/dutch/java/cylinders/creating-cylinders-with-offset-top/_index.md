---
date: 2026-08-12
description: Hoe 3D te genereren met Aspose.3D – maak een cilinder met verschoven
  bovenkant in Java, voeg een kindknooppunt toe, stel de verschoven bovenkant in,
  genereer een 3D-model, exporteer OBJ en evalueer met een tijdelijke licentie.
keywords:
- how to generate 3d
- aspose temporary license
- export obj file
- set offset top
- java 3d cylinder
lastmod: 2026-08-12
linktitle: Hoe 3D te genereren – een cilinder maken met verschoven bovenkant (Java)
og_description: Hoe 3D te genereren met Aspose.3D voor Java. Leer cilinderbovenzijden
  te verschuiven, kindknooppunten toe te voegen en OBJ te exporteren met een tijdelijke
  licentie.
og_image_alt: Guide showing Java code to create a cylinder with offset top and export
  OBJ using Aspose.3D
og_title: Hoe 3D te genereren – een cilinder maken met verschoven bovenkant (Java)
schemas:
- author: Aspose
  dateModified: '2026-08-12'
  description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  headline: How to generate 3d – create cylinder with offset top (Java)
  type: TechArticle
- description: How to generate 3d using Aspose.3D – create a cylinder with offset
    top in Java, add child node, set offset top, generate 3D model, export OBJ, and
    evaluate with a temporary license.
  name: How to generate 3d – create cylinder with offset top (Java)
  steps:
  - name: Create a Java 3D scene
    text: '`Scene` is the top‑level container that holds all nodes, meshes, lights,
      and cameras in a 3‑D environment.'
  - name: Initialize cylinder with offset top
    text: '`Cylinder` represents a cylindrical mesh and provides properties such as
      radius, height, and offset.'
  - name: Add child node Java – attach the first cylinder
    text: '`Node` is an element in the scene graph that can hold geometry and transformations.'
  - name: Java export OBJ – save the scene as OBJ
    text: '`FileFormat` enumerates the supported export formats such as OBJ, STL,
      and FBX.'
  type: HowTo
- questions:
  - answer: Yes, it works seamlessly with Eclipse, IntelliJ IDEA, NetBeans, and other
      IDEs.
    question: Is Aspose.3D compatible with different Java IDEs?
  - answer: Absolutely! Use the `Material` class to assign textures and surface properties.
    question: Can I apply textures to the created 3D objects?
  - answer: Various licensing models are available; you can explore them **[Aspose
      purchase page](https://purchase.aspose.com/buy)**.
    question: Are there licensing options for Aspose.3D?
  - answer: Join the **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)**
      for support and discussion.
    question: How can I get help or share experiences?
  - answer: Yes, an **aspose temporary license** can be obtained for evaluation **[temporary
      license request page](https://purchase.aspose.com/temporary-license/)**.
    question: Is a temporary license available for testing?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- generate 3d
- aspose.3d
- java cylinder offset
title: Hoe 3D te genereren – een cilinder maken met verschoven bovenkant (Java)
url: /nl/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe 3d te genereren – cilinder maken met offset bovenkant (Java)

## Introductie

Als je **cilinder** objecten wilt maken met een aangepaste offset bovenkant in een Java‑gebaseerde 3D‑scene, maakt Aspose.3D het proces eenvoudig. In deze tutorial lopen we elke stap door — van het opzetten van de scene tot het exporteren van het uiteindelijke model als een OBJ‑bestand — zodat je offset‑top cilinders kunt integreren in je applicaties met vertrouwen. Aan het einde van de gids begrijp je ook hoe een **aspose temporary license** je in staat stelt deze functies te evalueren zonder een volledige aankoop.

## Snelle antwoorden
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java  
- **Kan ik de bovenkant van een cilinder offsetten?** Ja, via `setOffsetTop`  
- **Hoe voeg ik een child node toe in Java?** Roep `createChildNode` aan op de root‑node  
- **Naar welk formaat kan ik exporteren?** Wavefront OBJ (`export obj file`)  
- **Heb ik een licentie nodig voor testen?** Een **aspose temporary license** is beschikbaar voor evaluatie  

## Wat is een Aspose temporary license?

Een **aspose temporary license** is een kort‑lopende, gratis evaluatiesleutel die de volledige functionaliteit van Aspose.3D for Java ontgrendelt tijdens ontwikkeling en testen. Het verwijdert evaluatiewatermerken en stelt je in staat 3D‑modelfiles te genereren, zoals OBJ, STL of FBX, precies zoals een betaalde licentie dat zou doen.

## Waarom Aspose.3D voor Java gebruiken?

Aspose.3D biedt een high‑level, cross‑platform API die 3D‑creatie en export vereenvoudigt. Het bevat ingebouwde exporters voor meer dan 30 formaten, ondersteunt scene‑graph hiërarchieën, en laat je focussen op geometrie in plaats van low‑level mesh handling.

- **High‑level API:** Geen noodzaak om low‑level mesh‑data te beheren.  
- **Cross‑platform:** Werkt in elke JVM‑compatibele omgeving.  
- **Built‑in exporters:** Direct opslaan naar OBJ, STL, FBX en meer — Aspose.3D ondersteunt **30+** exportformaten.  
- **Extensible:** Voeg eenvoudig child nodes toe, pas transformaties toe, en integreer met andere Java‑bibliotheken.  

## Vereisten

- **Java Development Kit (JDK)** – een compatibele versie geïnstalleerd.  
- **Aspose.3D for Java library** – download de nieuwste JAR van de officiële site **[Aspose.3D for Java download page](https://releases.aspose.com/3d/java/)**.  
- Een IDE naar keuze (Eclipse, IntelliJ IDEA, NetBeans, etc.).

## Importeer pakketten

De volgende imports brengen de essentiële Aspose.3D‑klassen binnen die nodig zijn om een cilinder te maken en te exporteren.

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Stapsgewijze handleiding

### Stap 1: Maak een Java 3D‑scene

`Scene` is de top‑level container die alle nodes, meshes, lichten en camera's bevat in een 3‑D‑omgeving.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Stap 2: Initialiseert cilinder met offset bovenkant

`Cylinder` vertegenwoordigt een cilindrische mesh en biedt eigenschappen zoals radius, hoogte en offset.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Stap 3: Voeg child node toe in Java – koppel de eerste cilinder

`Node` is een element in de scene‑graph dat geometrie en transformaties kan bevatten.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Stap 4: Initialiseert een tweede cilinder (zonder offset)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Stap 5: Voeg child node toe in Java – koppel de tweede cilinder

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Stap 6: Java export OBJ – sla de scene op als OBJ

`FileFormat` somt de ondersteunde exportformaten op, zoals OBJ, STL en FBX.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Hoe een 3d‑model te genereren en OBJ te exporteren in Java

Om een 3D‑model te genereren, laad je de scene, pas je eventuele benodigde transformaties toe, en roep je vervolgens `scene.save("path/CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ)` aan. De **aspose temporary license** verwijdert het evaluatiewatermerk, waardoor je productie‑klare OBJ‑bestanden kunt maken zonder een volledige licentie aan te schaffen.

## Praktijkvoorbeelden

- **Architecturale visualisatie:** Offset‑top cilinders modelleren kolommen die naar het plafond toe taps toelopen.  
- **Mechanische onderdelen:** Maak zuigers of tandwielbehuizingen waarbij het bovenoppervlak opzettelijk verschoven is.  
- **Game‑assets:** Produceer gevarieerde zuilvormen on‑the‑fly, waardoor de noodzaak voor handgemaakte meshes vermindert.  

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|-------|--------|-----|
| **OBJ‑bestand is leeg** | Scene niet correct opgeslagen of verkeerd pad. | Controleer of de uitvoermap bestaat en je schrijfrechten hebt. |
| **Offset niet toegepast** | Een oudere Aspose.3D‑versie wordt gebruikt. | Werk bij naar de nieuwste bibliotheek waarin `setOffsetTop` wordt ondersteund. |
| **Child node niet zichtbaar** | Transformatie niet toegepast. | Zorg ervoor dat je `getTransform().setTranslation` aanroept na het creëren van de child node. |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met verschillende Java‑IDE's?**  
A: Ja, het werkt naadloos met Eclipse, IntelliJ IDEA, NetBeans en andere IDE's.

**Q: Kan ik texturen toepassen op de gemaakte 3D‑objecten?**  
A: Absoluut! Gebruik de `Material`‑klasse om texturen en oppervlaktespecificaties toe te wijzen.

**Q: Zijn er licentieopties voor Aspose.3D?**  
A: Er zijn verschillende licentiemodellen beschikbaar; je kunt ze bekijken op de **[Aspose purchase page](https://purchase.aspose.com/buy)**.

**Q: Hoe kan ik hulp krijgen of ervaringen delen?**  
A: Word lid van het **[Aspose.3D community forum](https://forum.aspose.com/c/3d/18)** voor ondersteuning en discussie.

**Q: Is er een tijdelijke licentie beschikbaar voor testen?**  
A: Ja, een **aspose temporary license** kan verkregen worden voor evaluatie via de **[temporary license request page](https://purchase.aspose.com/temporary-license/)**.

---

**Laatst bijgewerkt:** 2026-08-12  
**Getest met:** Aspose.3D for Java 24.12 (latest)  
**Auteur:** Aspose

---

{{< blocks/products/products-backtop-button >}}

## Gerelateerde tutorials

- [Hoe cilindermodellen te maken met Aspose.3D for Java](/3d/java/cylinders/)
- [Hoe een cilinder fan‑vorm te maken met Aspose.3D for Java](/3d/java/cylinders/creating-fan-cylinders/)
- [Child nodes maken en FBX exporteren in Java met Aspose.3D](/3d/java/geometry/build-node-hierarchies/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}