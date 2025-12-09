---
date: 2025-12-09
description: Leer hoe je Aspose kunt gebruiken om aangepaste cilinders met schuine
  bodems te maken in Java, perfect voor Java 3D-modellering en het opslaan van scènes
  als OBJ.
language: nl
linktitle: 'How to Use Aspose: Create Cylinders with Sheared Bottom in Java'
second_title: Aspose.3D Java API
title: 'Hoe Aspose te gebruiken: cilinders met een schuine bodem maken in Java'
url: /java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe Aspose te gebruiken: Cilinders met scheefgetrokken bodem maken in Java

## Inleiding

In deze praktische tutorial ontdek je **hoe je Aspose** kunt gebruiken om een cilinder te bouwen waarvan de bodem scheefgetrokken is – een techniek die vaak nodig is in *java 3d modeling* projecten. We lopen elke stap door, van het opzetten van de scène tot het opslaan van het uiteindelijke model als een OBJ‑bestand. Aan het einde heb je een herbruikbaar code‑fragment dat je in elke Java‑gebaseerde 3D‑applicatie kunt gebruiken.

## Snelle antwoorden
- **Wat betekent “shear bottom”?** Het kantelt de basis van de cilinder met een opgegeven hoek in het XY‑vlak.  
- **Welke bibliotheek behandelt de 3D‑wiskunde?** Aspose.3D for Java biedt de `Cylinder` en `Vector2` klassen.  
- **Heb ik een licentie nodig om het voorbeeld uit te voeren?** Een tijdelijke licentie werkt voor evaluatie; een volledige licentie is vereist voor productie.  
- **Kan ik het model exporteren naar andere formaten?** Ja—gebruik `scene.save(..., FileFormat.WAVEFRONTOBJ)` om een OBJ‑bestand te krijgen.  
- **Welke Java‑versie is vereist?** JDK 8 of hoger is voldoende.

## Wat betekent “how to use aspose” in de context van 3D-modellering?

Aspose.3D for Java is een high‑level API die de complexiteit van 3D‑geometrie, bestandsformaten en transformaties abstraheert. In plaats van te werken met low‑level vertex‑buffers, roep je intuïtieve methoden aan zoals `new Cylinder(...)` en laat je Aspose het zware werk doen.

## Waarom Aspose gebruiken voor Java 3D-modellering?

- **Snelle ontwikkeling:** Bouw complexe vormen met een paar regels code.  
- **Brede formaatondersteuning:** Exporteer naar OBJ, STL, FBX en meer.  
- **Cross‑platform:** Werkt op elk OS dat Java ondersteunt.  
- **Consistente API:** Dezelfde code werkt voor desktop-, server- of Android‑omgevingen.

## Vereisten

- **Java Development Kit (JDK) 8+** geïnstalleerd en geconfigureerd in je IDE.  
- **Aspose.3D for Java** bibliotheek toegevoegd aan de classpath van je project. Je kunt het downloaden van de officiële site [hier](https://releases.aspose.com/3d/java/).  
- **Een tijdelijke of volledige licentie** (optioneel voor proefruns).

## Importpakketten

Om te beginnen, importeer je de essentiële Aspose.3D‑klassen en Java‑hulpmiddelen:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Maak een scène

Een *scene* is de container die alle 3D‑objecten, lichten en camera's bevat. Beschouw het als het podium waarop je je cilinders plaatst.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Stap 2: Maak Cylinder 1 (Scheefgetrokken bodem)

Nu maken we de eerste cilinder en passen we een shear‑transformatie toe op de bodem. De `setShearBottom`‑methode neemt een `Vector2` waarbij de X‑component de shear‑factor langs de X‑as vertegenwoordigt en de Y‑component langs de Y‑as.

```java
// ExStart:4
// Create cylinder 1
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Customized shear bottom for cylinder 1
cylinder1.setShearBottom(new Vector2(0, 0.83)); // Shear 47.5deg in the xy plane (z-axis)
// Add cylinder 1 to the scene
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

> **Pro tip:** De shear‑factor `0.83` komt overeen met ongeveer 47,5°; pas deze waarde aan om de exacte hoek te krijgen die je nodig hebt.

## Stap 3: Maak Cylinder 2 (Standaard)

Ter vergelijking voegen we een tweede cilinder toe zonder shear. Dit helpt je het visuele verschil direct in het geëxporteerde OBJ‑bestand te zien.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Stap 4: Sla de scène op (Hoe de scène op te slaan als OBJ)

Tot slot slaan we de scène op schijf op. De constante `FileFormat.WAVEFRONTOBJ` vertelt Aspose om een OBJ‑bestand te schrijven, wat breed ondersteund wordt door 3D‑editors zoals Blender en Maya.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

> **Opmerking:** Vervang `"Your Document Directory"` door een absoluut of relatief pad dat geschikt is voor jouw omgeving.

## Veelvoorkomende problemen en oplossingen

| Probleem | Oorzaak | Oplossing |
|----------|---------|-----------|
| **Cilinder verschijnt plat** | Onjuiste shear‑factor (buiten bereik 0‑1) | Gebruik een waarde tussen 0 en 1; pas geleidelijk aan tijdens het previewen. |
| **OBJ‑bestand laadt niet in viewer** | Ontbrekende materiaaldeclaraties | Voeg een eenvoudig materiaal toe aan elke node of exporteer als STL voor alleen‑geometrie testen. |
| **LicenseException tijdens uitvoering** | Geen geldig licentiebestand | Plaats `Aspose.3D.lic` in de project‑root of gebruik de `License`‑klasse om deze programmatisch te laden. |

## Veelgestelde vragen

### V1: Kan ik Aspose.3D for Java gebruiken met andere Java 3D‑bibliotheken?

**A:** Aspose.3D for Java is ontworpen om onafhankelijk te werken. Hoewel je het kunt integreren met andere bibliotheken, biedt het een volledige set functies voor de meeste 3D‑modelleringstaken op zichzelf.

### V2: Is Aspose.3D geschikt voor beginners in 3D-modellering?

**A:** Ja, Aspose.3D biedt een gebruiksvriendelijke API die low‑level details abstraheert, waardoor het toegankelijk is voor zowel beginners als ervaren ontwikkelaars.

### V3: Waar kan ik extra ondersteuning vinden voor Aspose.3D for Java?

**A:** Bezoek het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor community‑ondersteuning, tutorials en discussies.

### V4: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?

**A:** Je kunt een tijdelijke licentie krijgen [hier](https://purchase.aspose.com/temporary-license/).

### V5: Kan ik Aspose.3D for Java kopen?

**A:** Ja, je kunt Aspose.3D for Java aanschaffen [hier](https://purchase.aspose.com/buy).

## Conclusie

We hebben stap voor stap **hoe je Aspose** kunt gebruiken om twee cilinders te maken — één met een scheefgetrokken bodem en één standaard — en vervolgens het resultaat als een OBJ‑bestand opgeslagen. Deze techniek is een bouwsteen voor meer geavanceerde 3D‑modellen, zoals aangepaste onderdelen, architecturale elementen of game‑assets. Voel je vrij om te experimenteren met verschillende shear‑waarden, stralen en hoogtes om aan de behoeften van je project te voldoen.

---

**Last Updated:** 2025-12-09  
**Tested With:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}