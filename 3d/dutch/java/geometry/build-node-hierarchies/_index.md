---
title: Bouw knooppunthiërarchieën in 3D-scènes met Java en Aspose.3D
linktitle: Bouw knooppunthiërarchieën in 3D-scènes met Java en Aspose.3D
second_title: Aspose.3D Java-API
description: Leer hoe u dynamische 3D-scènes in Java bouwt met Aspose.3D. Creëer moeiteloos knooppunthiërarchieën en til uw grafische 3D-game naar een hoger niveau.
type: docs
weight: 16
url: /nl/java/geometry/build-node-hierarchies/
---
## Invoering

In de dynamische wereld van 3D-graphics en Java-programmering is het creëren en beheren van knooppunthiërarchieën in 3D-scènes een cruciale vaardigheid. Aspose.3D voor Java stelt ontwikkelaars in staat dit naadloos te bereiken en biedt een robuuste set tools voor het eenvoudig creëren van ingewikkelde 3D-scènes. In deze zelfstudie begeleiden we u bij het bouwen van knooppunthiërarchieën met Aspose.3D voor Java, zodat zelfs beginners dit kunnen volgen.

## Vereisten

Voordat u zich verdiept in de zelfstudie, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

1. Java-ontwikkelomgeving: Zorg ervoor dat er een Java-ontwikkelomgeving op uw computer is geïnstalleerd.
2.  Aspose.3D voor Java-bibliotheek: Download en installeer de Aspose.3D voor Java-bibliotheek van de[downloadpagina](https://releases.aspose.com/3d/java/).
3. Documentmap: maak een map om uw 3D-scènebestanden op te slaan.

## Pakketten importeren

Begin met het importeren van de benodigde pakketten om Aspose.3D voor Java-functionaliteiten te gebruiken. Voeg de volgende regels toe aan uw Java-code:

```java
import com.aspose.threed.*;

```

## Stap 1: Initialiseer het scèneobject

```java
// Initialiseer scèneobject
Scene scene = new Scene();
```

## Stap 2: Maak een onderliggend knooppunt en mesh

```java
// Haal een onderliggend knooppuntobject op
Node top = scene.getRootNode().createChildNode();

// Maak het eerste kubusknooppunt
Node cube1 = top.createChildNode("cube1");
Mesh mesh = Common.createMeshUsingPolygonBuilder(); // Gebruik uw methode voor het maken van mesh
cube1.setEntity(mesh);
cube1.getTransform().setTranslation(new Vector3(-10, 0, 0));

// Maak het tweede kubusknooppunt
Node cube2 = top.createChildNode("cube2");
cube2.setEntity(mesh);
cube2.getTransform().setTranslation(new Vector3(10, 0, 0));
```

## Stap 3: Pas rotatie toe op het bovenste knooppunt

```java
// Roteer het bovenste knooppunt, wat invloed heeft op alle onderliggende knooppunten
top.getTransform().setRotation(Quaternion.fromEulerAngle(Math.PI, 4, 0));
```

## Stap 4: Bewaar 3D-scène

```java
// Sla 3D-scène op in het ondersteunde bestandsformaat (in dit geval FBX)
String MyDir = "Your Document Directory";
MyDir = MyDir + "NodeHierarchy.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nNode hierarchy added successfully to document.\nFile saved at " + MyDir);
```

Deze stapsgewijze handleiding biedt een solide basis voor het bouwen van knooppunthiërarchieën in 3D-scènes met behulp van Aspose.3D voor Java. Experimenteer met verschillende parameters en pas de code aan uw specifieke vereisten aan.

## Conclusie

Het beheersen van de creatie van knooppunthiërarchieën is een belangrijke mijlpaal in uw reis met Aspose.3D voor Java. Met deze tutorial beschikt u over de kennis om naadloos door de complexiteit van 3D-scènes te navigeren. Laat nu uw creativiteit de vrije loop en bouw met vertrouwen boeiende 3D-omgevingen.

## Veelgestelde vragen

### Vraag 1: Is Aspose.3D voor Java geschikt voor beginners?

A1: Absoluut! Aspose.3D voor Java biedt een gebruiksvriendelijke interface, waardoor deze toegankelijk is voor zowel beginners als ervaren ontwikkelaars.

### Vraag 2: Kan ik Aspose.3D voor Java gebruiken voor commerciële projecten?

 A2: Ja, dat kan. Bezoek de[aankooppagina](https://purchase.aspose.com/buy) voor licentiegegevens.

### V3: Hoe kan ik ondersteuning krijgen voor Aspose.3D voor Java?

 A3: Sluit je aan bij de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om hulp te krijgen van de gemeenschap en het Aspose-ondersteuningsteam.

### Vraag 4: Is er een gratis proefversie beschikbaar?

 A4: Zeker! Ontdek de functies met de[gratis proefperiode](https://releases.aspose.com/) voordat u een toezegging doet.

### Vraag 5: Waar kan ik de documentatie vinden?

 A5: Raadpleeg de[documentatie](https://reference.aspose.com/3d/java/) voor gedetailleerde informatie over Aspose.3D voor Java.