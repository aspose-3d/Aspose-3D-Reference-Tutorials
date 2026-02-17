---
date: 2026-01-27
description: Leer Java 3D-modellering door cilinders met een scheefgetrokken onderkant
  te maken met Aspose.3D voor Java. Deze beginners‑3D‑tutorial laat zien hoe je Aspose
  3D installeert, een scheeftransformatie toepast en een OBJ‑bestand exporteert in
  Java.
linktitle: Java 3D Modeling – Sheared Bottom Cylinders with Aspose.3D
second_title: Aspose.3D Java API
title: Java 3D-modellering – Schuine ondercylinders met Aspose.3D
url: /nl/java/cylinders/creating-cylinders-with-sheared-bottom/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D-modellering – Schuine onderkant cilinders met Aspose.3D

## Introductie

Welkom bij deze **java 3d modeling** tutorial! In deze stapsgewijze gids laten we zien hoe je een cilinder maakt waarvan de onderkant scheef is, met behulp van de Aspose.3D bibliotheek voor Java. Of je nu een **beginner 3d tutorial** volgt of een aangepaste schuiftransformatie wilt toevoegen aan een bestaand model, je ziet precies hoe je de scène opzet, de schuif toepast en uiteindelijk **export OBJ file java** gebruikt in andere tools.

## Snelle antwoorden
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java  
- **Kan ik Aspose 3D via Maven installeren?** Ja – voeg de Aspose.3D afhankelijkheid toe aan je `pom.xml`  
- **Is een licentie vereist voor ontwikkeling?** Een tijdelijke licentie is voldoende voor testen; een volledige licentie is nodig voor productie  
- **Welk bestandsformaat wordt gedemonstreerd?** Wavefront OBJ (`.obj`)  
- **Hoe lang duurt het voorbeeld om uit te voeren?** Minder dan een seconde op een typische werkstation  

## Vereisten

Voordat we beginnen, zorg ervoor dat je het volgende hebt:

- Java Development Kit (JDK) geïnstalleerd op je systeem.  
- **Installeer Aspose 3D** – download de bibliotheek van de officiële site [hier](https://releases.aspose.com/3d/java/).  
- Een IDE of build‑tool (Maven/Gradle) om de Aspose.3D afhankelijkheid te beheren.  

## Pakketten importeren

Eerst importeren we de klassen die we nodig hebben voor de scène, geometrie en bestandsafhandeling.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Maak een scène

Een scène is de container voor alle 3‑D objecten. We beginnen met het maken van een lege scène.

```java
// ExStart:3
// Create a scene
Scene scene = new Scene();
// ExEnd:3
```

## Stap 2: Maak Cylinder 1 – Hoe een cilinder scheef maken

Nu bouwen we de eerste cilinder en **passen we een schuiftransformatie** toe op de onderkant. Dit demonstreert **hoe een cilinder te scheef maken** geometrie direct via de API.

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

## Stap 3: Maak Cylinder 2 – Standaard cilinder (geen scheefheid)

Ter vergelijking voegen we een tweede cilinder toe die **geen** scheefde onderkant heeft.

```java
// ExStart:5
// Create cylinder 2
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// Add cylinder 2 without a ShearBottom to the scene
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

## Stap 4: Sla de scène op – Export OBJ File Java

Tot slot exporteren we de scène naar een Wavefront OBJ‑bestand, waarmee we het gebruik van **export obj file java** illustreren.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

## Waarom dit belangrijk is voor Java 3D-modellering

Het toevoegen van een scheefheid aan een primitief stelt je in staat meer organische vormen te creëren zonder externe modelleringstools te gebruiken. Deze techniek is handig voor:

- Architecturale visualisaties waarbij schuine bases vereist zijn.  
- Game‑assets die aangepaste voetafdrukken nodig hebben terwijl de geometrie licht blijft.  
- Snelle prototyping waarbij je afmetingen programmatisch wilt aanpassen.  

## Veelvoorkomende problemen & oplossingen

| Probleem | Oplossing |
|----------|-----------|
| **Scheefheid lijkt te extreem** | Pas de `Vector2` waarden aan; ze vertegenwoordigen de scheefheidsfactor (bereik 0‑1). |
| **OBJ‑bestand wordt niet geopend in viewer** | Controleer of de doelmap bestaat en dat je schrijfrechten hebt. |
| **Licentie‑exception tijdens uitvoering** | Pas een tijdelijke of permanente licentie toe vóór het maken van de scène (`License license = new License(); license.setLicense("Aspose.3D.lic");`). |

## Veelgestelde vragen

**V: Kan ik Aspose.3D voor Java gebruiken met andere Java 3D‑bibliotheken?**  
A: Aspose.3D is ontworpen om onafhankelijk te werken. Hoewel je het kunt integreren met andere bibliotheken, biedt het al een volledige API voor de meeste 3‑D‑taken.

**V: Is Aspose.3D geschikt voor beginners in 3D-modellering?**  
A: Absoluut. De API is eenvoudig, en deze **beginner 3d tutorial** toont de kernconcepten met minimale code.

**V: Waar kan ik extra ondersteuning vinden voor Aspose.3D voor Java?**  
A: Bezoek het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor community‑hulp en officiële antwoorden.

**V: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?**  
A: Je kunt een tijdelijke licentie krijgen [hier](https://purchase.aspose.com/temporary-license/).

**V: Waar kan ik een volledige Aspose.3D voor Java licentie kopen?**  
A: Aankoopopties zijn beschikbaar [hier](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2026-01-27  
**Getest met:** Aspose.3D 24.11 for Java  
**Auteur:** Aspose