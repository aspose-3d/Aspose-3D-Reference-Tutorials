---
title: Transformeer 3D-knooppunten met Euler-hoeken in Java met Aspose.3D
linktitle: Transformeer 3D-knooppunten met Euler-hoeken in Java met Aspose.3D
second_title: Aspose.3D Java-API
description: Ontdek de wereld van 3D-transformaties in Java met Aspose.3D. Volg onze stapsgewijze handleiding om dynamische Euler-hoeken aan uw 3D-knooppunten toe te voegen.
weight: 19
url: /nl/java/geometry/transform-3d-nodes-with-euler-angles/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformeer 3D-knooppunten met Euler-hoeken in Java met Aspose.3D

## Invoering

Welkom bij deze stapsgewijze zelfstudie over het transformeren van 3D-knooppunten met Euler-hoeken in Java met behulp van Aspose.3D. In deze gids zullen we ons verdiepen in het proces van het toevoegen van transformaties aan een 3D-knooppunt, waarbij we Euler-hoeken gebruiken om dynamische positionering en oriëntatie te bereiken.

## Vereisten

Voordat we ingaan op de tutorial, zorg ervoor dat je aan de volgende vereisten voldoet:

- Basiskennis van Java-programmeren.
- Java Development Kit (JDK) op uw computer geïnstalleerd.
-  Aspose.3D-bibliotheek, die u kunt verkrijgen[Aspose.3D Java-documentatie](https://reference.aspose.com/3d/java/).

## Pakketten importeren

 Begin met het importeren van de benodigde pakketten in uw Java-project. Zorg ervoor dat de Aspose.3D-bibliotheek correct is toegevoegd aan uw klassenpad. Als je het nog niet hebt gedownload, kun je de downloadlink vinden[hier](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## Stap 1. Initialiseer scène en knooppunt

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialiseer scèneobject
Scene scene = new Scene();

// Initialiseer het knooppuntklasseobject
Node cubeNode = new Node("cube");
```

## Stap 2. Maak mesh en stel de geometrie in

```java
// Roep de Common-klasse aan om mesh te maken met behulp van de polygon builder-methode om de mesh-instantie in te stellen
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Wijs het knooppunt naar de Mesh-geometrie
cubeNode.setEntity(mesh);
```

## Stap 3. Stel Euler-hoeken en vertaling in

```java
// Euler-hoeken
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Vertaling instellen
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Stap 4. Voeg knooppunt toe aan scène

```java
// Voeg een kubus toe aan de scène
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Stap 5. Bewaar 3D-scène

```java
// Het pad naar de documentenmap.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Sla 3D-scènes op in de ondersteunde bestandsformaten
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Zorg ervoor dat u "Uw documentenmap" vervangt door het juiste pad op uw computer.

## Conclusie

Gefeliciteerd! Je hebt met succes 3D-knooppunten getransformeerd met behulp van Euler-hoeken in Java met Aspose.3D. Experimenteer met verschillende hoeken en vertalingen om dynamische en boeiende 3D-scènes te creëren.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor Java gebruiken in commerciële projecten?

 A1: Ja, dat kan. Bezoek de[aankooppagina](https://purchase.aspose.com/buy) voor licentiegegevens.

### Vraag 2: Waar kan ik ondersteuning vinden voor Aspose.3D?

 A2: De[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) is de plek om hulp te zoeken en verbinding te maken met de gemeenschap.

### Vraag 3: Is er een gratis proefperiode beschikbaar?

 A3: Ja, u kunt de[gratis proefperiode](https://releases.aspose.com/) om de mogelijkheden van Aspose.3D te ervaren.

### Vraag 4: Hoe kan ik een tijdelijke licentie verkrijgen?

 A4: U kunt een tijdelijke licentie verkrijgen[hier](https://purchase.aspose.com/temporary-license/).

### Vraag 5: Waar kan ik de documentatie vinden?

 A5: De[documentatie](https://reference.aspose.com/3d/java/) biedt uitgebreide richtlijnen voor het gebruik van Aspose.3D voor Java.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
