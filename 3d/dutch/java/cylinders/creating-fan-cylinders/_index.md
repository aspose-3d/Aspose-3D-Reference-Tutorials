---
date: 2025-12-09
description: Leer hoe je een kindknooppunt toevoegt, 3D‑objecten positioneert en de
  scène opslaat als OBJ terwijl je aangepaste ventilatorcilinders maakt met Aspose.3D
  voor Java.
language: nl
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Voeg kindknooppunt toe om fancilinders te bouwen met Aspose.3D voor Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Kindknooppunt toevoegen om ventilatorkilinders te bouwen met Aspose.3D voor Java

## Inleiding

Klaar om **een kindknooppunt toe te voegen** aan een 3‑D‑scene en opvallende ventilatorkilinders te maken? In deze tutorial lopen we elke stap door — van het opzetten van de scene, het positioneren van 3D‑objecten, tot het uiteindelijk **opslaan van de scene als OBJ** — met behulp van Aspose.3D voor Java. Of je nu een game‑asset verfijnt of snel een prototype bouwt, de concepten hier geven je stevige controle over je 3‑D‑modellen.

## Snelle antwoorden
- **Wat doet “add child node”?** Het voegt een nieuw object toe aan de scene‑graph, waarbij het de transformaties van zijn ouder erft.  
- **Hoe kan ik een 3D‑object positioneren?** Door een translatie (of rotatie/schaal) toe te passen op de transformatie van het knooppunt.  
- **Welk bestandsformaat wordt gebruikt voor export?** Het voorbeeld slaat het model op als een Wavefront OBJ‑bestand.  
- **Heb ik een licentie nodig om de code uit te voeren?** Een gratis proefversie werkt voor evaluatie; een licentie is vereist voor productie.  
- **Welke IDE werkt het beste?** Elke Java‑IDE (IntelliJ IDEA, Eclipse, VS Code) die JDK 8+ ondersteunt.

## Wat is “add child node” in Aspose.3D?
Een kindknooppunt toevoegen betekent dat je een nieuw knooppunt onder een bestaand ouderknooppunt in de hiërarchie van de scene maakt. Het kind erft het coördinatensysteem van de ouder, waardoor het eenvoudig is om **3d‑object**‑instanties relatief ten opzichte van elkaar te **positioneren**.

## Waarom een kindknooppunt toevoegen bij het bouwen van ventilatorkilinders?
- **Modulair ontwerp:** Elke cilinder (ventilator of niet‑ventilator) bevindt zich in zijn eigen knooppunt, wat latere bewerkingen vereenvoudigt.  
- **Transformatierfenning:** Verplaats, roteer of schaal de ouder en alle kinderen volgen automatisch.  
- **Nettere scene‑graph:** Verbetert de leesbaarheid en het debuggen van complexe modellen.

## Vereisten

- **Java Development Kit (JDK)** – download van de [officiële site](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – haal de nieuwste bibliotheek op via de [download‑link](https://releases.aspose.com/3d/java/).

## Pakketten importeren

Begin met het importeren van de benodigde pakketten in je Java‑project. Deze stap is cruciaal om toegang te krijgen tot de functionaliteit die Aspose.3D biedt.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Een scene maken

Eerst maken we een lege 3‑D‑scene die al onze objecten zal bevatten.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Stap 2: Een ventilatorkilinder maken

Vervolgens bouwen we een cilinder die wordt gerenderd als een ventilator (gedeeltelijke sweep).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Stap 3: Kindknooppunt toevoegen & 3D‑object positioneren

Nu **voegen we een kindknooppunt toe** aan de scene en **positioneren we het 3d‑object** door de translatie in te stellen. Hier wordt de ventilatorkilinder onderdeel van de scene‑graph.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Stap 4: Een niet‑ventilatorcilinder maken

Om de flexibiliteit van Aspose.3D te tonen, maken we ook een gewone cilinder zonder ventilator en voegen die toe als een ander kindknooppunt.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Stap 5: De scene opslaan als OBJ

Tot slot **slaan we de scene op als OBJ** zodat je het resultaat in elke standaard 3‑D‑viewer kunt bekijken.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Gefeliciteerd! Je hebt met succes **een kindknooppunt toegevoegd**, je objecten **gepositioneerd**, en het model **geëxporteerd**.

## Veelvoorkomende problemen & tips

| Probleem | Oplossing |
|----------|-----------|
| **Bestand niet gevonden** bij het opslaan | Zorg ervoor dat de doelmap bestaat en dat je schrijfrechten hebt. |
| **Cilinder lijkt plat** | Controleer de radius‑ en hoogte‑waarden; Aspose.3D verwacht eenheden in dezelfde schaal. |
| **Ventilatorsegment ziet er onvolledig uit** | Pas `ThetaLength` (in radialen) aan om de gewenste hoek te dekken. |
| **Scene niet zichtbaar in viewer** | Controleer of het OBJ‑bestand is opgeslagen met het bijbehorende `.mtl`‑bestand (materiaal) indien nodig. |

## Veelgestelde vragen

**V:** *Is Aspose.3D compatibel met andere Java‑bibliotheken voor 3D‑modellering?*  
**A:** Ja, Aspose.3D werkt naast andere Java‑3D‑bibliotheken, zodat je functies kunt combineren waar nodig.

**V:** *Kan ik het uiterlijk van de gegenereerde ventilatorkilinders verder aanpassen?*  
**A:** Absoluut. Je kunt materialen, texturen en verlichting toepassen met de `Material`‑ en `Light`‑klassen.

**V:** *Waar vind ik extra ondersteuning of hulp voor Aspose.3D?*  
**A:** Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor community‑hulp en officiële antwoorden.

**V:** *Is er een gratis proefversie beschikbaar voor Aspose.3D?*  
**A:** Ja, je kunt Aspose.3D verkennen met een [gratis proefversie](https://releases.aspose.com/) voordat je koopt.

**V:** *Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?*  
**A:** Haal een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/) voor test‑ en ontwikkelingsdoeleinden.

## Conclusie

In deze gids hebben we laten zien hoe je **een kindknooppunt toevoegt**, **een 3d‑object positioneert**, en **de scene opslaat als OBJ** terwijl je aangepaste ventilatorkilinders maakt met Aspose.3D voor Java. Deze bouwblokken geven je de flexibiliteit om complexe 3‑D‑hiërarchieën te construeren en ze te exporteren voor elke downstream‑workflow.

---

**Laatst bijgewerkt:** 2025-12-09  
**Getest met:** Aspose.3D 24.12 voor Java  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}