---
title: Knooppunt transformeren door Euler-hoeken in 3D-scènes
linktitle: Knooppunt transformeren door Euler-hoeken in 3D-scènes
second_title: Aspose.3D .NET-API
description: Leer moeiteloos 3D-knooppunten transformeren met Aspose.3D voor .NET. Volg onze stapsgewijze handleiding voor verbluffende resultaten in uw projecten.
type: docs
weight: 19
url: /nl/net/geometry-and-hierarchy/transformation-node-euler-angles/
---
## Invoering

Welkom bij deze uitgebreide tutorial over het transformeren van knooppunten met Euler-hoeken in 3D-scènes met behulp van Aspose.3D voor .NET. In deze gids duiken we in de opwindende wereld van 3D-graphics en onderzoeken we het proces van het toevoegen van transformaties aan een knooppunt met behulp van Euler-hoeken. Aspose.3D voor .NET biedt krachtige tools voor het werken met 3D-scènes en meshes, waardoor het een uitstekende keuze is voor ontwikkelaars die op zoek zijn naar veelzijdigheid en efficiëntie in hun projecten.

## Vereisten

Voordat we ingaan op de tutorial, zorg ervoor dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET-bibliotheek: Zorg ervoor dat de Aspose.3D-bibliotheek is geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).

- Ontwikkelomgeving: Stel de .NET-ontwikkelomgeving van uw voorkeur in, zoals Visual Studio.

## Naamruimten importeren

Begin met het importeren van de benodigde naamruimten om toegang te krijgen tot de functionaliteit van Aspose.3D voor .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Laten we het voorbeeld nu in meerdere stappen opsplitsen voor een duidelijk begrip.

## Stap 1: Initialiseer het scèneobject

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Initialiseer scèneobject
Scene scene = new Scene();
```

 Begin met het maken van een nieuwe 3D-scène met behulp van de`Scene` klas.

## Stap 2: Initialiseer het knooppuntklasseobject

```csharp
// Initialiseer het knooppuntklasseobject
Node cubeNode = new Node("cube");
```

 Maak een knooppunt binnen de scène met behulp van de`Node`klas. Dit knooppunt zal dienen als de container voor ons 3D-object.

## Stap 3: Maak mesh met Polygon Builder

```csharp
// Roep de Common-klasse aan om mesh te maken met behulp van de polygon builder-methode om de mesh-instantie in te stellen
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 
```

 Roep een methode aan (in dit geval`CreateMeshUsingPolygonBuilder` uit een gewoonte`Common` class) om een mesh voor het 3D-object te genereren.

## Stap 4: Wijs het knooppunt naar de mesh-geometrie

```csharp
// Wijs het knooppunt naar de Mesh-geometrie
cubeNode.Entity = mesh;
```

Koppel de gemaakte mesh aan het knooppunt.

## Stap 5: Stel Euler-hoeken en vertaling in

```csharp
// Euler-hoeken
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Vertaling instellen
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Definieer de Euler-hoeken en vertaling voor het knooppunt om het in de 3D-ruimte te positioneren.

## Stap 6: Voeg kubus toe aan de scène

```csharp
// Voeg een kubus toe aan de scène
scene.RootNode.ChildNodes.Add(cubeNode);
```

Neem het knooppunt op in de hiërarchie van de scène.

## Stap 7: Sla de 3D-scène op

```csharp
// Het pad naar de documentenmap.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Sla 3D-scènes op in de ondersteunde bestandsformaten
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Geef de uitvoermap op en sla de 3D-scène, inclusief het getransformeerde knooppunt, op in het gewenste bestandsformaat (in dit geval FBX7500ASCII).

## Conclusie

Gefeliciteerd! Je hebt met succes geleerd hoe je een knooppunt met Euler-hoeken kunt transformeren in 3D-scènes met behulp van Aspose.3D voor .NET. Deze krachtige bibliotheek opent de deur naar eindeloze mogelijkheden in de ontwikkeling van 3D-graphics.

## Veelgestelde vragen

### Vraag 1: Is Aspose.3D compatibel met andere 3D-modelleringstools?

A1: Aspose.3D ondersteunt verschillende 3D-bestandsformaten, waardoor de compatibiliteit met populaire modelleringstools wordt verbeterd.

### Vraag 2: Kan ik meerdere transformaties op één knooppunt toepassen?

A2: Ja, u kunt meerdere transformaties combineren en toepassen om complexe effecten te bereiken.

### V3: Waar kan ik aanvullende Aspose.3D-documentatie vinden?

 A3: Raadpleeg de[documentatie](https://reference.aspose.com/3d/net/) voor gedetailleerde informatie en voorbeelden.

### V4: Heb ik een licentie nodig voor het gebruik van Aspose.3D voor .NET?

 A4: Ja, u kunt een licentie verkrijgen[hier](https://purchase.aspose.com/buy) of verken een[gratis proefperiode](https://releases.aspose.com/).

### Vraag 5: Heeft u hulp nodig of heeft u specifieke vragen?

A5: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor gemeenschapssteun.