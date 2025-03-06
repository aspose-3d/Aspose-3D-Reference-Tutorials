---
title: Transformatieknooppunt door transformatiematrix
linktitle: Transformatieknooppunt door transformatiematrix
second_title: Aspose.3D .NET-API
description: Transformeer knooppunten moeiteloos in 3D-scènes met Aspose.3D voor .NET. Leer stapsgewijze knooppunttransformaties met een tutorial.
weight: 21
url: /nl/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformatieknooppunt door transformatiematrix

## Invoering

In het dynamische domein van 3D-graphics en visualisaties is de mogelijkheid om objecten binnen een scène te manipuleren een cruciaal aspect. Aspose.3D voor .NET stelt ontwikkelaars in staat knooppunten naadloos te transformeren met behulp van transformatiematrices, waardoor een laag creativiteit en controle wordt toegevoegd aan 3D-scènes. Deze tutorial leidt u stap voor stap door het proces van het transformeren van een knooppunt in een 3D-scène.

## Vereisten

Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

1.  Aspose.3D voor .NET-bibliotheek: Zorg ervoor dat de Aspose.3D-bibliotheek in uw .NET-project is geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).

2. Ontwikkelomgeving: Zet een werkende .NET-ontwikkelomgeving op en maak, als u dat nog niet heeft gedaan, een nieuw project waarin u de transformaties implementeert.

## Naamruimten importeren

Begin met het importeren van de benodigde naamruimten in uw .NET-project. Deze naamruimten bieden de essentiële klassen en methoden voor manipulatie van 3D-scènes.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Nu we de basisbeginselen hebben besproken, gaan we het transformatieproces opsplitsen in een stapsgewijze handleiding.

## Stap 1: Initialiseer scène

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Initialiseer scèneobject
Scene scene = new Scene();

```

In deze stap maken we een nieuwe lege 3D-scène.

## Stap 2: Mesh maken en aan scène koppelen

```csharp
// Roep de Common-klasse aan om mesh te maken met behulp van de polygon builder-methode om de mesh-instantie in te stellen
Mesh mesh = (new Box()).ToMesh();

// Maak een containerknooppunt voor de mesh.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Hier genereren we een mesh met behulp van de polygoonbouwermethode en wijzen deze toe aan het knooppunt, waarmee we de geometrie voor onze kubus vaststellen.

## Stap 3: Stel een aangepaste vertaalmatrix in

```csharp
// Stel een aangepaste vertaalmatrix in
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Definieer een aangepaste vertaalmatrix om de specifieke transformatie te bepalen die op het knooppunt wordt toegepast. Pas de matrixwaarden indien nodig aan voor de gewenste transformatie.

Neem het kubusknooppunt op in de scène, zodat het onderdeel wordt van de algehele 3D-omgeving.

## Stap 4: Sla de scène op

```csharp
// Het pad naar de documentenmap.
var output = "TransformationToNode.fbx";

// Sla 3D-scènes op in de ondersteunde bestandsformaten
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Geef de uitvoermap en bestandsnaam op en sla de 3D-scène vervolgens op in het gewenste bestandsformaat. In dit voorbeeld slaan we het op in het FBX7500ASCII-formaat.

## Conclusie

Gefeliciteerd! U hebt met succes een knooppunt getransformeerd met behulp van een transformatiematrix in een 3D-scène met Aspose.3D voor .NET. Deze mogelijkheid opent deuren naar diverse en visueel boeiende 3D-toepassingen.

## Veelgestelde vragen

### Vraag 1: Wat is een transformatiematrix in 3D-graphics?

A1: Een transformatiematrix is een wiskundige representatie die wordt gebruikt om verschillende transformaties (translatie, rotatie, schaling) toe te passen op objecten in de 3D-ruimte.

### Vraag 2: Kan ik meerdere transformaties op één knooppunt toepassen?

A2: Ja, u kunt meerdere transformaties combineren door hun respectievelijke matrices te vermenigvuldigen en het resultaat op het knooppunt toe te passen.

### Vraag 3: Zijn er andere ondersteunde bestandsformaten voor het opslaan van 3D-scènes?

 A3: Aspose.3D voor .NET ondersteunt verschillende bestandsindelingen, waaronder STL, GLTF, OBJ en meer. Verwijs naar de[documentatie](https://reference.aspose.com/3d/net/) voor een uitgebreide lijst.

### V4: Hoe kan ik een tijdelijke licentie verkrijgen voor Aspose.3D voor .NET?

 A4: Bezoek de[tijdelijke licentiepagina](https://purchase.aspose.com/temporary-license/)op de Aspose-website om een tijdelijke licentie voor evaluatiedoeleinden te verkrijgen.

### Vraag 5: Waar kan ik hulp zoeken of verbinding maken met de Aspose.3D-gemeenschap?

 A5: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om vragen te stellen, ervaringen te delen en contact te maken met andere ontwikkelaars die Aspose.3D gebruiken.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
