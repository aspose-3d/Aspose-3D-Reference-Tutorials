---
date: 2026-05-24
description: Leer hoe u 3D-extrusie met slices maakt met Aspose.3D for Java. Deze
  stapsgewijze gids behandelt lineaire extrusie, het instellen van de afrondingsstraal
  en het exporteren van OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Maak 3D-extrusie met slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Maak 3D-extrusie met slices – Aspose.3D for Java
url: /nl/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3D-extrusie met slices – Aspose.3D voor Java

## Inleiding

Als je **create 3d extrusion** objecten wilt maken die er glad en precies uitzien, is het regelen van het aantal slices de sleutel. In deze tutorial lopen we door hoe je slices specificeert tijdens het uitvoeren van een lineaire extrusie met Aspose.3D for Java. Je zult zien waarom het aantal slices belangrijk is, hoe je een afrondingsstraal instelt, en hoe je het resultaat exporteert als een OBJ‑bestand dat in elke 3‑D‑pipeline kan worden gebruikt.

## Snelle antwoorden
- **Wat regelt “slices”?** Het aantal tussenliggende doorsneden dat wordt gebruikt om het extrusieoppervlak te benaderen.  
- **Welke methode stelt het aantal slices in?** `LinearExtrusion.setSlices(int)`  
- **Kan ik de afrondingsstraal van het profiel wijzigen?** Ja, via `RectangleShape.setRoundingRadius(double)`  
- **Welk bestandsformaat wordt in dit voorbeeld gebruikt?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Heb ik een licentie nodig om de code uit te voeren?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.

`LinearExtrusion.setSlices(int)` stelt in hoeveel tussenliggende slices de extrusie zal genereren.  
`RectangleShape.setRoundingRadius(double)` definieert de hoekstraal van een rechthoekig profiel.

## Hoe maak je 3d-extrusie in Java met slices?

Laad je 2‑D‑profiel, kies een slice‑aantal, stel de afrondingsstraal in, en roep `save` aan – de volledige workflow past in een handvol regels. Aspose.3D for Java behandelt de geometriecreatie, slice‑interpolatie en OBJ‑export automatisch, zodat je je kunt concentreren op visuele kwaliteit in plaats van laag‑niveau mesh‑berekeningen.

## Wat is een lineaire extrusie met slices?

Een lineaire extrusie met slices verandert een vlakke 2‑D‑vorm in een 3‑D‑solid door deze langs een rechte lijn te vegen terwijl een configureerbaar aantal tussenliggende doorsneden wordt gegenereerd. Het aantal slices beïnvloedt direct hoe soepel gebogen randen, zoals afgeronde hoeken, worden weergegeven.

## Waarom Aspose.3D voor Java gebruiken om 3d-extrusie te maken?

Aspose.3D biedt **volledige programmatische controle** over elke extrusieparameter, ondersteunt **meer dan 50 invoer‑ en uitvoerformaten** (inclusief OBJ, FBX, STL en GLTF), en kan **modellen van honderden pagina's** verwerken zonder het volledige bestand in het geheugen te laden. Het draait op elk Java‑ondersteund platform, vereist geen native DLL‑s en garandeert deterministische resultaten op Windows, Linux en macOS.

## Vereisten

1. **Java Development Kit** – JDK 8 of hoger geïnstalleerd.  
2. **Aspose.3D for Java** – Download de bibliotheek van de officiële site [here](https://releases.aspose.com/3d/java/).  
3. Een IDE of teksteditor naar keuze.

## Pakketten importeren

Voeg de Aspose.3D‑namespace toe aan je project zodat je toegang hebt tot de 3‑D‑modelleringklassen.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Stapsgewijze handleiding

### Stap 1: De scène opzetten en het profiel definiëren

`RectangleShape` is een klasse die een 2‑D‑rechthoekprofiel definieert.  
Eerst maken we een `RectangleShape` aan en geven we het een **rounding radius** zodat de hoeken glad zijn.  
`Scene` is de hoofdcontainer voor alle nodes en geometrie.  
Vervolgens initialiseren we een nieuwe `Scene` die alle geometrie zal bevatten.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Stap 2: Kind‑node‑objecten maken voor elke extrusie

`Node` vertegenwoordigt een element in de scenegrafiek dat geometrie en transformaties kan bevatten.  
Elk stuk geometrie bevindt zich onder een `Node`. Hier genereren we twee sibling‑nodes – één voor een low‑slice extrusie en een andere voor een high‑slice extrusie – en verplaatsen de linkse node een beetje naar de zijkant zodat de resultaten gemakkelijk te vergelijken zijn.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Stap 3: Lineaire extrusie uitvoeren en slices instellen

`LinearExtrusion` is de klasse die een solid creëert door een profiel lineair te vegen.  
`LinearExtrusion` is de klasse van Aspose.3D die een solid genereert door een 2‑D‑profiel langs een rechte lijn te extruderen. Met een **anonymous inner class** roepen we `setSlices` aan om de gladheid te regelen. De linkse node krijgt slechts 2 slices (grof), terwijl de rechtse node 10 slices krijgt (glad).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Stap 4: OBJ exporteren – de scène opslaan

Tenslotte schrijven we de scène naar een Wavefront OBJ‑bestand, een formaat dat breed wordt ondersteund door 3‑D‑editors en game‑engines. Dit demonstreert de **export OBJ Java**‑functionaliteit van Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **Extrusie lijkt plat** | Slice‑aantal ingesteld op 1 of 0 | Zorg ervoor dat `setSlices` wordt aangeroepen met een waarde ≥ 2. |
| **Afgeronde hoeken zien er gekarteld uit** | Afrondingsstraal te klein ten opzichte van het slice‑aantal | Vergroot ofwel de straal of het slice‑aantal voor soepelere curven. |
| **Bestand niet gevonden bij opslaan** | `MyDir` wijst naar een niet‑bestaande map | Maak de map vooraf aan of gebruik een absoluut pad. |

## Veelgestelde vragen

**Q: Hoe kan ik Aspose.3D voor Java downloaden?**  
A: Je kunt de bibliotheek downloaden [here](https://releases.aspose.com/3d/java/).

**Q: Waar kan ik de documentatie voor Aspose.3D vinden?**  
A: Raadpleeg de documentatie [here](https://reference.aspose.com/3d/java/).

**Q: Is er een gratis proefversie beschikbaar?**  
A: Ja, je kunt een gratis proefversie verkennen [here](https://releases.aspose.com/).

**Q: Hoe kan ik ondersteuning krijgen voor Aspose.3D?**  
A: Bezoek het supportforum [here](https://forum.aspose.com/c/3d/18).

**Q: Kan ik een tijdelijke licentie aanschaffen?**  
A: Ja, een tijdelijke licentie kan worden verkregen [here](https://purchase.aspose.com/temporary-license/).

---

**Laatst bijgewerkt:** 2026-05-24  
**Getest met:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Auteur:** Aspose

## Gerelateerde tutorials

- [Maak 3D-extrusie Java met Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Hoe richting instellen in lineaire extrusie met Aspose.3D voor Java](/3d/java/linear-extrusion/setting-direction/)
- [Maak 3D-scène met twist in lineaire extrusie – Aspose.3D voor Java](/3d/java/linear-extrusion/applying-twist/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}