---
date: 2026-06-13
description: Leer een java 3d graphics tutorial over het regelen van het centrum in
  lineaire extrusie met Aspose.3D, inclusief hoe je de afrondingsstraal instelt en
  een OBJ-bestand opslaat in java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Het regelen van het centrum in lineaire extrusie met Aspose.3D voor Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Maak 3D Mesh Java – Centrum in lineaire extrusie
url: /nl/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3D Mesh Java – Middelpunt in Lineaire Extrusie

## Introductie

Als je 3‑D‑visualisaties bouwt in Java, is het beheersen van extrusietechnieken essentieel. Deze **java 3d graphics tutorial** laat je zien hoe je **create 3d mesh java** objecten maakt door het middelpunt van een lineaire extrusie te regelen met Aspose.3D for Java. Aan het einde van deze gids begrijp je waarom de `center`‑eigenschap belangrijk is, hoe je **set rounding radius** instelt, en hoe je **save obj file java**‑compatibele output opslaat. Je ziet ook hoe je **export 3d model obj** kunt gebruiken in elke belangrijke 3‑D‑editor.

## Snelle Antwoorden
- **Wat doet de center‑eigenschap?** Het bepaalt of de extrusie symmetrisch is ten opzichte van de oorsprong van het profiel.  
- **Heb ik een licentie nodig om de code uit te voeren?** Een tijdelijke licentie werkt voor testen; een volledige licentie is vereist voor productie.  
- **Welk bestandsformaat wordt gebruikt voor het resultaat?** De scène wordt opgeslagen als een Wavefront OBJ‑bestand.  
- **Kan ik het aantal slices wijzigen?** Ja, gebruik `setSlices(int)` op het `LinearExtrusion`‑object.  
- **Is Aspose.3D compatibel met Java 8+?** Absoluut – het ondersteunt alle moderne Java‑versies.

## Wat is een java 3d graphics tutorial?

Een **java 3d graphics tutorial** is een stapsgewijze gids die je leert hoe je Java‑bibliotheken gebruikt om driedimensionale objecten te maken, te manipuleren en te renderen. In deze tutorial leer je **create 3d mesh java** door een 2‑D‑profiel om te zetten in een volledig 3‑D‑model, de centrale uitlijning te regelen, extrusieranden af te ronden, en uiteindelijk het resultaat te exporteren als een OBJ‑bestand dat elk 3‑D‑programma kan lezen.

## Waarom Aspose.3D voor Java gebruiken?

Aspose.3D for Java biedt een high‑level API die de noodzaak van handmatige mesh‑berekeningen elimineert, zodat je je kunt concentreren op ontwerp in plaats van low‑level geometrie. Het ondersteunt **50+ input and output formats** — waaronder OBJ, FBX, STL en GLTF — zodat je **export 3d model obj** of elk ander formaat met één methode‑aanroep kunt exporteren. De bibliotheek verwerkt scènes van honderden pagina's zonder het volledige bestand in het geheugen te laden, en levert **tot 3× snellere prestaties** vergeleken met ruwe OpenGL‑pijplijnen op typische serverhardware.

## Vereisten

1. **Java Development Environment** – JDK 8 of nieuwer geïnstalleerd.  
2. **Aspose.3D for Java** – Download de bibliotheek en documentatie [hier](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Maak een map op uw computer om gegenereerde bestanden op te slaan; we noemen deze **“Your Document Directory.”**

## Pakketten importeren

Importeer in uw Java‑IDE de Aspose.3D‑klassen die u nodig heeft. Dit geeft de compiler toegang tot de extrusie‑ en scène‑bouwfuncties.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stapsgewijze Gids

### Stap 1: Basisprofiel instellen

Eerst maak je de 2‑D‑vorm die geëxtrudeerd zal worden. Hier gebruiken we een rechthoek en **set rounding radius** op 0.3, wat de hoeken afrondt en laat zien hoe je **round extrusion corners** kunt toepassen.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Stap 2: Een 3D‑scene maken

**Scene** is de top‑level container die alle 3‑D‑objecten, lichten en camera's bevat.

```java
Scene scene = new Scene();
```

### Stap 3: Voeg linker- en rechter‑nodes toe

Een **Node** vertegenwoordigt een transformeerbaar object in de scène‑grafiek, waardoor positionering en hiërarchie mogelijk zijn.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Stap 4: Lineaire Extrusie – Geen Center (Linker Node)

**LinearExtrusion** zet een 2‑D‑profiel om in een 3‑D‑mesh door het langs een rechte lijn te vegen.  
**setCenter(boolean)** schakelt in of de extrusie gecentreerd is rond de oorsprong van het profiel.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Stap 5: Voeg een grondvlak toe ter referentie (Linker Node)

Een dunne doos fungeert als een visueel vloeroppervlak, waardoor je de oriëntatie van de extrusie kunt zien.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Stap 6: Lineaire Extrusie – Gecentreerd (Rechter Node)

Herhaal nu de extrusie, dit keer met `center` ingeschakeld. De geometrie zal symmetrisch zijn rond de oorsprong van het profiel, waardoor je een perfect uitgebalanceerd **create 3d mesh java** resultaat krijgt.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Stap 7: Voeg een grondvlak toe ter referentie (Rechter Node)

Hetzelfde grondvlak voor de rechterkant, waardoor de vergelijking duidelijk wordt.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Stap 8: Sla de 3D‑scene op

Exporteer tenslotte de volledige scène naar een Wavefront OBJ‑bestand – een formaat dat gemakkelijk bruikbaar is in de meeste 3‑D‑editors. De `save`‑methode converteert automatisch de mesh naar de OBJ‑specificatie, waardoor je **save obj file java** kunt uitvoeren zonder extra nabewerking.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende Problemen en Oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **Extrusie lijkt verschoven** | `setCenter(false)` laat het profiel verankerd aan de hoek. | Gebruik `setCenter(true)` voor symmetrische resultaten. |
| **OBJ‑bestand is leeg** | Pad van de uitvoermap is onjuist of er ontbreken schrijfrechten. | Controleer of `MyDir` naar een bestaande map wijst en de applicatie schrijfrechten heeft. |
| **Afgeronde hoeken zien er scherp uit** | Rondingsstraal is te klein ten opzichte van de grootte van de rechthoek. | Verhoog de straalwaarde (bijv. `setRoundingRadius(0.5)`). |

## Veelgestelde Vragen

### Q1: Kan ik Aspose.3D voor Java gebruiken in commerciële projecten?

A1: Ja, Aspose.3D for Java is beschikbaar voor commercieel gebruik. Voor licentie‑details, bezoek [hier](https://purchase.aspose.com/buy).

### Q2: Is er een gratis proefversie beschikbaar?

A2: Ja, je kunt een gratis proefversie van Aspose.3D for Java verkennen [hier](https://releases.aspose.com/).

### Q3: Waar kan ik ondersteuning vinden voor Aspose.3D for Java?

A3: Het Aspose.3D‑communityforum is een uitstekende plek om ondersteuning te zoeken en uw ervaringen te delen. Bezoek het forum [hier](https://forum.aspose.com/c/3d/18).

### Q4: Heb ik een tijdelijke licentie nodig voor testen?

A4: Ja, als je een tijdelijke licentie voor testdoeleinden nodig hebt, kun je er een verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

### Q5: Waar kan ik de documentatie vinden?

A5: De documentatie voor Aspose.3D for Java is beschikbaar [hier](https://reference.aspose.com/3d/java/).

## Conclusie

Door deze **java 3d graphics tutorial** te voltooien, weet je nu hoe je **create 3d mesh java** objecten maakt, het middelpunt van een lineaire extrusie regelt, de rondingsstraal aanpast, en **save obj file java** output gebruikt met Aspose.3D. Deze technieken geven je fijnmazige controle over mesh‑symmetrie, wat essentieel is voor game‑assets, CAD‑prototypes en wetenschappelijke visualisaties. Voel je vrij om te experimenteren met verschillende profielen, slice‑aantallen en exportformaten om je 3‑D‑gereedschapskist uit te breiden.

---

**Laatst bijgewerkt:** 2026-06-13  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose

## Gerelateerde Tutorials

- [Maak 3D Extrusie Java met Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hoe Richting Instellen in Lineaire Extrusie met Aspose.3D voor Java](/3d/java/linear-extrusion/setting-direction/)
- [Maak 3D Scene met Twist in Lineaire Extrusie – Aspose.3D voor Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}