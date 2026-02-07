---
date: 2026-02-07
description: Leer hoe je cilindermodels met verschoven bovenkanten maakt in Aspose.3D
  voor Java, voeg kindknooppunt‑Java‑stappen toe en exporteer 3D‑model‑OBJ‑bestanden
  eenvoudig.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hoe een cilinder met een verschoven bovenkant te maken in Aspose.3D voor Java
url: /nl/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe maak je een cilinder met offset bovenkant in Aspose.3D voor Java

## Introductie

Als je op zoek bent naar **how to create cylinder** objecten met een aangepaste offset bovenkant in een Java‑gebaseerde 3D‑scene, maakt Aspose.3D het proces eenvoudig. In deze tutorial lopen we elke stap door — van het opzetten van de scene tot het exporteren van het uiteindelijke model als een OBJ‑bestand — zodat je offset‑top cilinders kunt integreren in je applicaties met vertrouwen. Aan het einde van de gids beheers je hoe je cilinder‑vormen met aangepaste offsets kunt maken in slechts een paar regels code.

## Snelle antwoorden
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java  
- **Kan ik de bovenkant van een cilinder offsetten?** Ja, met `setOffsetTop`  
- **Hoe voeg ik een child node toe in Java?** Roep `createChildNode` aan op de root‑node  
- **Naar welk formaat kan ik exporteren?** Wavefront OBJ (`export 3d model obj`)  
- **Heb ik een licentie nodig voor testen?** Een tijdelijke licentie is beschikbaar voor evaluatie  

## Wat is “how to create cylinder” met een offset bovenkant?

Een cilinder met een offset bovenkant maken betekent dat het bovenste ronde vlak verschoven is ten opzichte van de basis, waardoor je taps toelopende of asymmetrische vormen kunt modelleren zonder handmatige vertex‑manipulatie. Aspose.3D biedt een speciale constructor en een `OffsetTop`‑eigenschap om dit te bereiken in slechts een paar regels code.

## Waarom Aspose.3D voor Java gebruiken?

- **High‑level API:** Geen noodzaak om low‑level mesh‑data te beheren.  
- **Cross‑platform:** Werkt in elke JVM‑compatibele omgeving.  
- **Built‑in exporters:** Direct opslaan naar OBJ, STL, FBX en meer.  
- **Extensible:** Gemakkelijk child nodes toevoegen, transformaties toepassen en integreren met andere Java‑bibliotheken.

## Voorvereisten

Voordat we beginnen, zorg ervoor dat je het volgende hebt:

- **Java Development Kit (JDK)** – een compatibele versie geïnstalleerd.  
- **Aspose.3D for Java library** – download de nieuwste JAR van de officiële site [hier](https://releases.aspose.com/3d/java/).  
- Een IDE naar keuze (Eclipse, IntelliJ IDEA, NetBeans, enz.).

## Importeer pakketten

Importeer eerst de klassen die we nodig hebben. Plaats deze statements bovenaan je Java‑bestand:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Stapsgewijze handleiding

### Stap 1: Maak een scene

Een scene fungeert als de container voor alle 3D‑objecten.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Stap 2: Initialiseert cilinder met offset bovenkant

Hier beantwoorden we **how to create cylinder** met een aangepaste offset. De constructor definieert radius, hoogte, slices, stacks en of de cilinder gesloten is. Daarna verschuiven we de bovenkant met `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Stap 3: Hoe **add child node Java** – Bevestig de eerste cilinder

We maken een child node onder de root‑node van de scene en verplaatsen de cilinder naar een gewenste locatie.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Stap 4: Initialiseert een tweede cilinder (geen offset)

Ter vergelijking voegen we een gewone cilinder toe zonder offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Stap 5: Hoe **add child node Java** – Bevestig de tweede cilinder

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Stap 6: Hoe **export OBJ** – Sla de scene op als OBJ

Tot slot exporteren we de volledige scene (beide cilinders) als een Wavefront OBJ‑bestand, dat breed ondersteund wordt door 3D‑tools.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Wanneer je het programma uitvoert, vind je `CustomizedOffsetTopCylinder.obj` in de opgegeven map, klaar om geopend te worden in Blender, Maya of een andere OBJ‑compatibele viewer.

## Waarom dit belangrijk is – Praktische toepassingsgevallen

- **Architecturale visualisatie:** Offset‑top cilinders zijn perfect voor het modelleren van kolommen die naar het plafond toe taps toelopen.  
- **Mechanische onderdelen:** Maak zuigers of tandwielbehuizingen waarbij het bovenoppervlak opzettelijk verschoven is.  
- **Game‑assets:** Genereer snel verschillende zuilvormen zonder handmatig meshes te maken.

## Hoe exporteer je OBJ – Sla scene op als OBJ

De Aspose 3D export‑OBJ‑functionaliteit stelt je in staat je modellen te delen met vrijwel elke 3D‑pipeline. Door de `scene.save(..., FileFormat.WAVEFRONTOBJ)`‑methode te gebruiken, **how to export obj** je bestanden direct vanuit Java, waardoor je geen derde‑partij converters meer nodig hebt.

## Hoe voeg je child node toe Java – Geometrie bevestigen

Het toevoegen van child nodes is de standaard manier om een scene‑graph te organiseren. Elke aanroep van `createChildNode` retourneert een node die onafhankelijk kan worden getransformeerd, daarom verschijnt het **add child node java** patroon twee keer in deze tutorial.

## Export 3D‑model OBJ – Gebruik Aspose 3D Export OBJ

Als je je modellen moet distribueren naar ontwerpers, biedt de **export 3d model obj** functie een lichtgewicht, tekstgebaseerde representatie die werkt in alle belangrijke 3D‑applicaties. Dezelfde API‑aanroep die in Stap 6 wordt gebruikt, demonstreert de **aspose 3d export obj** workflow.

## Veelvoorkomende problemen en oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| **OBJ‑bestand is leeg** | Scene niet correct opgeslagen of verkeerd pad. | Controleer of de uitvoermap bestaat en dat je schrijfrechten hebt. |
| **Offset niet toegepast** | Gebruik van een oudere Aspose.3D‑versie. | Update naar de nieuwste bibliotheek waarin `setOffsetTop` wordt ondersteund. |
| **Child node niet zichtbaar** | Transformatie niet toegepast. | Zorg ervoor dat je `getTransform().setTranslation` aanroept na het creëren van de child node. |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met verschillende Java‑IDE's?**  
A: Ja, het werkt naadloos met Eclipse, IntelliJ IDEA, NetBeans en andere IDE's.

**Q: Kan ik texturen toepassen op de gemaakte 3D‑objecten?**  
A: Absoluut! Gebruik de `Material`‑klasse om texturen en oppervlakteeigenschappen toe te wijzen.

**Q: Zijn er licentie‑opties voor Aspose.3D?**  
A: Er zijn verschillende licentiemodellen beschikbaar; je kunt ze bekijken [hier](https://purchase.aspose.com/buy).

**Q: Hoe kan ik hulp krijgen of ervaringen delen?**  
A: Word lid van het Aspose.3D‑communityforum [hier](https://forum.aspose.com/c/3d/18) voor ondersteuning en discussie.

**Q: Is er een tijdelijke licentie beschikbaar voor testen?**  
A: Ja, een tijdelijke licentie kan worden verkregen voor evaluatie [hier](https://purchase.aspose.com/temporary-license/).

**Laatst bijgewerkt:** 2026-02-07  
**Getest met:** Aspose.3D for Java 24.12 (latest)  
**Auteur:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}