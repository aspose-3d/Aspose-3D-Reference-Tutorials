---
date: 2025-12-05
description: Leer hoe je cilindermodels met offset‑toppen maakt in Aspose.3D voor
  Java, voeg kindknooppunt‑Java‑stappen toe en exporteer eenvoudig 3D‑model‑OBJ‑bestanden.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hoe een cilinder met offset‑bovenkant te maken in Aspose.3D voor Java
url: /nl/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe een Cilinder met Offset Bovenkant te Maken in Aspose.3D voor Java

## Introductie

Als je **how to create cylinder** objecten wilt maken met een aangepaste offset bovenkant in een Java‑gebaseerde 3D‑scene, maakt Aspose.3D het proces eenvoudig. In deze tutorial lopen we elke stap door—van het opzetten van de scene tot het exporteren van het uiteindelijke model als een OBJ‑bestand—zodat je offset‑top cilinders kunt integreren in je applicaties met vertrouwen.

## Snelle Antwoorden
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java  
- **Kan ik de bovenkant van een cilinder offsetten?** Ja, met `setOffsetTop`  
- **Hoe voeg ik een child node toe in Java?** Roep `createChildNode` aan op de root‑node  
- **Naar welk formaat kan ik exporteren?** Wavefront OBJ (`export 3d model obj`)  
- **Heb ik een licentie nodig voor testen?** Een tijdelijke licentie is beschikbaar voor evaluatie  

## Wat is “how to create cylinder” met een offset bovenkant?

Een cilinder met een offset bovenkant betekent dat het bovenste ronde vlak verschoven is ten opzichte van de basis, waardoor je taps toelopende of asymmetrische vormen kunt modelleren zonder handmatige vertex‑manipulatie. Aspose.3D biedt een speciale constructor en een `OffsetTop`‑eigenschap om dit te bereiken in slechts een paar regels code.

## Waarom Aspose.3D voor Java gebruiken?

- **High‑level API:** Geen noodzaak om low‑level mesh‑data te beheren.  
- **Cross‑platform:** Werkt in elke JVM‑compatibele omgeving.  
- **Built‑in exporters:** Direct opslaan naar OBJ, STL, FBX en meer.  
- **Extensible:** Gemakkelijk child nodes toevoegen, transformaties toepassen en integreren met andere Java‑bibliotheken.

## Vereisten

Voordat we beginnen, zorg dat je het volgende hebt:

- **Java Development Kit (JDK)** – een compatibele versie geïnstalleerd.  
- **Aspose.3D for Java library** – download de nieuwste JAR van de officiële site [here](https://releases.aspose.com/3d/java/).  
- Een IDE naar keuze (Eclipse, IntelliJ IDEA, NetBeans, enz.).

## Pakketten Importeren

Ten eerste importeer je de klassen die we nodig hebben. Plaats deze statements bovenaan je Java‑bestand:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Stapsgewijze Gids

### Stap 1: Een Scene Maken

Een scene fungeert als de container voor alle 3D‑objecten.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Stap 2: Cilinder Initialiseren met Offset Bovenkant

Hier beantwoorden we **how to create cylinder** met een aangepaste offset. De constructor definieert radius, hoogte, slices, stacks en of de cilinder gesloten is. Daarna verschuiven we de bovenkant met `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Stap 3: Hoe **add child node Java** – De Eerste Cilinder Toevoegen

We maken een child node onder de root‑node van de scene en verplaatsen de cilinder naar een gewenste locatie.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Stap 4: Een Tweede Cilinder Initialiseren (Geen Offset)

Ter vergelijking voegen we een reguliere cilinder toe zonder offset.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Stap 5: Hoe **add child node Java** – De Tweede Cilinder Toevoegen

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Stap 6: Hoe **export 3d model OBJ** – De Scene Opslaan

Tot slot exporteren we de volledige scene (beide cilinders) als een Wavefront OBJ‑bestand, dat breed ondersteund wordt door 3D‑tools.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Wanneer je het programma uitvoert, vind je `CustomizedOffsetTopCylinder.obj` in de opgegeven map, klaar om geopend te worden in Blender, Maya of een andere OBJ‑compatibele viewer.

## Veelvoorkomende Problemen en Oplossingen

| Probleem | Reden | Oplossing |
|----------|-------|-----------|
| **OBJ‑bestand is leeg** | Scene niet correct opgeslagen of verkeerd pad. | Controleer of de output‑directory bestaat en je schrijfrechten hebt. |
| **Offset niet toegepast** | Een oudere Aspose.3D‑versie wordt gebruikt. | Update naar de nieuwste bibliotheek waarin `setOffsetTop` wordt ondersteund. |
| **Child node niet zichtbaar** | Transformatie niet toegepast. | Zorg ervoor dat je `getTransform().setTranslation` aanroept na het maken van de child node. |

## Veelgestelde Vragen

**Q: Is Aspose.3D compatibel met verschillende Java‑IDE's?**  
A: Ja, het werkt naadloos met Eclipse, IntelliJ IDEA, NetBeans en andere IDE's.

**Q: Kan ik texturen toepassen op de gemaakte 3D‑objecten?**  
A: Absoluut! Gebruik de `Material`‑klasse om texturen en oppervlakte‑eigenschappen toe te wijzen.

**Q: Zijn er licentieopties voor Aspose.3D?**  
A: Er zijn verschillende licentiemodellen beschikbaar; je kunt ze bekijken [here](https://purchase.aspose.com/buy).

**Q: Hoe kan ik hulp krijgen of ervaringen delen?**  
A: Word lid van het Aspose.3D‑communityforum [here](https://forum.aspose.com/c/3d/18) voor ondersteuning en discussie.

**Q: Is er een tijdelijke licentie beschikbaar voor testen?**  
A: Ja, een tijdelijke licentie kan verkregen worden voor evaluatie [here](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Laatst bijgewerkt:** 2025-12-05  
**Getest met:** Aspose.3D for Java 24.12 (latest)  
**Auteur:** Aspose