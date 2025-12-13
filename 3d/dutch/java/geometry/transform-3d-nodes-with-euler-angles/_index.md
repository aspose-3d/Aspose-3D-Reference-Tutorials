---
date: 2025-12-13
description: Leer hoe je Aspose 3D Java gebruikt om 3D‑knooppunten te transformeren.
  Deze gids laat zien hoe je Euler‑hoeken gebruikt, 3D‑rotatie toevoegt en translatie
  in Java instelt.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Transformeer 3D‑knooppunten met Euler‑hoeken
url: /nl/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformeer 3D‑knooppunten met Euler‑hoeken in Java met Aspose.3D

## Introductie

In deze tutorial ontdek je **hoe je aspose 3d java** kunt gebruiken om 3D‑knooppunten te transformeren door Euler‑hoeken toe te passen. Aan het einde van de gids kun je rotatie 3d toevoegen, vertaling java instellen, en dynamische scènes creëren die reageren op realtime‑gegevens.

## Snelle antwoorden
- **Welke bibliotheek behandelt 3D‑transformaties in Java?** Aspose 3D for Java.  
- **Welke methode stelt rotatie in met Euler‑hoeken?** `setEulerAngles()` op de transform van het knooppunt.  
- **Hoe verplaats ik een knooppunt in de ruimte?** Gebruik `setTranslation()` met een `Vector3`.  
- **Heb ik een licentie nodig voor productie?** Ja, een commerciële Aspose 3D‑licentie is vereist.  
- **Kan ik exporteren naar FBX?** Absoluut – `scene.save(..., FileFormat.FBX7500ASCII)` werkt direct.

## Vereisten

Voordat we in de tutorial duiken, zorg ervoor dat je de volgende vereisten hebt:

- Basiskennis van Java‑programmeren.  
- Java Development Kit (JDK) geïnstalleerd op je machine.  
- Aspose.3D‑bibliotheek, die je kunt verkrijgen via [Aspose.3D Java Documentation](https://reference.aspose.com/3d/java/).

## Pakketten importeren

Begin met het importeren van de benodigde pakketten in je Java‑project. Zorg ervoor dat de Aspose.3D‑bibliotheek correct is toegevoegd aan je classpath. Als je deze nog niet hebt gedownload, kun je de downloadlink vinden [hier](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Werken met Euler‑hoeken

### Stap 1. Scene en knooppunt initialiseren

Eerst maak je een scene en een knooppunt die de geometrie bevatten die je wilt transformeren.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Stap 2. Mesh maken en geometrie instellen

Vervolgens genereer je een eenvoudige mesh (een kubus in dit geval) en koppel je deze aan het knooppunt.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Rotatie 3D toevoegen aan een knooppunt

### Stap 3. Euler‑hoeken en vertaling instellen

Nu passen we de rotatie toe met Euler‑hoeken en verplaatsen we het knooppunt naar een zichtbare positie.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Vertaling Java instellen – Het knooppunt positioneren

De bovenstaande vertaalstap toont **set translation java** in de praktijk: het knooppunt wordt 20 eenheden langs de Z‑as verschoven zodat je het na het renderen kunt zien.

### Stap 4. Knoop toevoegen aan scene

Koppel het getransformeerde knooppunt aan de root‑knoop van de scene.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

### Stap 5. 3D‑scene opslaan

Exporteer tenslotte de scene naar een FBX‑bestand (of een ander ondersteund formaat).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Zorg ervoor dat je `"Your Document Directory"` vervangt door het juiste pad op je machine.

## Conclusie

Gefeliciteerd! Je hebt met succes 3D‑knooppunten getransformeerd met Euler‑hoeken in Java met **aspose 3d java**. Experimenteer met verschillende hoeken en vertalingen om dynamische en boeiende 3D‑scènes te creëren.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor Java gebruiken in commerciële projecten?

A1: Ja, dat kan. Bezoek de [purchase page](https://purchase.aspose.com/buy) voor licentie‑details.

### V2: Waar kan ik ondersteuning vinden voor Aspose.3D?

A2: Het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) is de plek om hulp te zoeken en contact te maken met de community.

### V3: Is er een gratis proefversie beschikbaar?

A3: Ja, je kunt de [free trial](https://releases.aspose.com/) verkennen om de mogelijkheden van Aspose.3D te ervaren.

### V4: Hoe kan ik een tijdelijke licentie verkrijgen?

A4: Je kunt een tijdelijke licentie verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

### V5: Waar kan ik de documentatie vinden?

A5: De [documentation](https://reference.aspose.com/3d/java/) biedt uitgebreide begeleiding voor het gebruik van Aspose.3D voor Java.

## Veelgestelde vragen

**V: Wat is het verschil tussen Euler‑hoeken en quaternionrotatie?**  
A: Euler‑hoeken zijn intuïtief (pitch, yaw, roll) maar kunnen lijden onder gimbal lock, terwijl quaternions dat probleem vermijden en beter zijn voor vloeiende interpolaties.

**V: Kan ik meerdere transformaties op hetzelfde knooppunt combineren?**  
A: Ja. Roep `setEulerAngles`, `setTranslation` en `setScale` in willekeurige volgorde aan; de bibliotheek combineert ze tot één transformatiematrix.

**V: Is het mogelijk om te exporteren naar andere formaten zoals OBJ of STL?**  
A: Absoluut. Vervang `FileFormat.FBX7500ASCII` door `FileFormat.OBJ` of `FileFormat.STL` in de `scene.save`‑aanroep.

**V: Hoe pas ik dezelfde rotatie toe op meerdere knooppunten tegelijk?**  
A: Maak een bovenliggend knooppunt, pas de rotatie toe op het bovenliggende knooppunt, en voeg onderliggende knooppunten toe. Alle kinderen erven de transformatie.

**V: Moet ik na het opslaan enige opruimingsmethoden aanroepen?**  
A: De Java‑garbage‑collector behandelt de meeste bronnen, maar je kunt expliciet `scene.dispose()` aanroepen als je met grote scenes werkt in een langdurige applicatie.

---

**Last Updated:** 2025-12-13  
**Tested With:** Aspose.3D 23.12 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}