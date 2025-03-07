---
title: Knooppunt transformeren door Quaternion
linktitle: Knooppunt transformeren door Quaternion
second_title: Aspose.3D .NET-API
description: Leer hoe u 3D-knooppunten kunt transformeren met quaternionen met behulp van Aspose.3D voor .NET. Stap-voor-stap handleiding voor beginners.
weight: 20
url: /nl/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Knooppunt transformeren door Quaternion

## Invoering

Welkom bij een stapsgewijze handleiding voor het transformeren van een knooppunt per quaternion in 3D-scènes met behulp van Aspose.3D voor .NET. In deze zelfstudie verkennen we de krachtige mogelijkheden van Aspose.3D voor .NET en doorlopen we het proces van het toevoegen van transformaties aan een 3D-knooppunt met behulp van quaternionen.

## Vereisten

Voordat we ingaan op de tutorial, zorg ervoor dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Zorg ervoor dat de Aspose.3D-bibliotheek is geïnstalleerd. Je kunt het downloaden van de[pagina vrijgeven](https://releases.aspose.com/3d/net/).

- Ontwikkelomgeving: Richt uw .NET-ontwikkelomgeving in met de benodigde tools en configuraties.

- Basiskennis van 3D-concepten: Bekendheid met 3D-graphics en -concepten zal nuttig zijn.

## Naamruimten importeren

Neem in uw .NET-project de vereiste naamruimten voor Aspose.3D op:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Stap 1: Initialiseer het scèneobject

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Initialiseer scèneobject
Scene scene = new Scene();
```

## Stap 2: Initialiseer het knooppuntklasseobject

```csharp
// Initialiseer het knooppuntklasseobject
Node cubeNode = new Node("cube");
```

## Stap 3: Maak mesh met Polygon Builder

```csharp
// Roep de Common-klasse aan om mesh te maken met behulp van de polygon builder-methode om de mesh-instantie in te stellen
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Stap 4: Wijs het knooppunt naar de mesh-geometrie

```csharp
// Wijs het knooppunt naar de Mesh-geometrie
cubeNode.Entity = mesh;
```

## Stap 5: Stel de rotatie in met Quaternion

```csharp
// Rotatie instellen
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Stap 6: Stel de vertaling in

```csharp
// Vertaling instellen
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Stap 7: Voeg kubus toe aan de scène

```csharp
// Voeg een kubus toe aan de scène
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Stap 8: Bewaar 3D-scène

```csharp
// Het pad naar de documentenmap.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Sla 3D-scènes op in de ondersteunde bestandsformaten
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Conclusie

 Gefeliciteerd! Je hebt met succes geleerd hoe je een knooppunt per quaternion kunt transformeren in 3D-scènes met behulp van Aspose.3D voor .NET. Ontdek meer functies en mogelijkheden door te verwijzen naar de[documentatie](https://reference.aspose.com/3d/net/).

## Veelgestelde vragen

### Vraag 1: Wat is een quaternion in 3D-graphics?

A1: Quaternionen zijn wiskundige entiteiten die worden gebruikt om rotaties in de 3D-ruimte weer te geven.

### V2: Hoe kan ik Aspose.3D downloaden voor .NET?

 A2: U kunt de bibliotheek downloaden van de[pagina vrijgeven](https://releases.aspose.com/3d/net/).

### V3: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?

 A3: Ja, u kunt een gratis proefperiode krijgen van[hier](https://releases.aspose.com/).

### V4: Waar kan ik ondersteuning vinden voor Aspose.3D voor .NET?

 A4: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor ondersteuning en discussies.

### V5: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D?

 A5: Vraag een tijdelijke licentie aan[hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
