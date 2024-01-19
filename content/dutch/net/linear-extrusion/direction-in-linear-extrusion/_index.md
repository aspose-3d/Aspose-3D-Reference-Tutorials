---
title: Richting in lineaire extrusie
linktitle: Richting in lineaire extrusie
second_title: Aspose.3D .NET-API
description: Ontgrendel de wereld van 3D-modellering met Aspose.3D voor .NET. Leer richting lineaire extrusie, vergroot de creativiteit en maak moeiteloos meeslepende toepassingen.
type: docs
weight: 11
url: /nl/net/linear-extrusion/direction-in-linear-extrusion/
---
## Invoering

In de dynamische wereld van softwareontwikkeling is het creëren van meeslepende 3D-modellen een onmisbare vaardigheid. Aspose.3D voor .NET biedt ontwikkelaars een robuuste set tools om het potentieel van 3D-modellering in hun toepassingen te benutten. In deze tutorial duiken we in de intrigerende wereld van lineaire extrusie en verkennen we de nuances van de functie "Richting in lineaire extrusie".

## Vereisten

Voordat we aan deze spannende reis beginnen, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Download en installeer de bibliotheek van[Aspose.3D .NET-documentatie](https://reference.aspose.com/3d/net/).

- Ontwikkelomgeving: Zorg ervoor dat u een werkende .NET-ontwikkelomgeving hebt ingesteld.

## Naamruimten importeren

Importeer in uw .NET-project de benodigde naamruimten om toegang te krijgen tot de functionaliteit van Aspose.3D. Voeg de volgende regels toe aan het begin van uw code:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Stap 1: Initialiseer het basisprofiel

Begin met het initialiseren van het te extruderen basisprofiel. In dit voorbeeld maken we een rechthoekige vorm met een afrondingsstraal van 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Stap 2: Maak een 3D-scène

Leg de basis voor uw 3D-meesterwerk door een scène te creëren.

```csharp
Scene scene = new Scene();
```

## Stap 3: Maak knooppunten

Genereer knooppunten binnen de scène om verschillende componenten van uw 3D-omgeving weer te geven.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Stap 4: Lineaire extrusie zonder richting

 Voer lineaire extrusie uit op het linkerknooppunt met behulp van de`Twist` En`Slices` eigenschappen.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Stap 5: Lineaire extrusie met richting

 Breid de extrusiemogelijkheden uit door de integratie van de`Direction` eigenschap in het juiste knooppunt.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Stap 6: Sla de 3D-scène op

 Bewaar uw creatie door de 3D-scène op te slaan. Vervangen`"Your Output Directory"` met de gewenste map.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gefeliciteerd! Je hebt met succes lineaire extrusie geïmplementeerd met Aspose.3D voor .NET, waarbij je zowel de traditionele als de directionele benaderingen verkent.

## Conclusie

In deze tutorial navigeerden we door de fascinerende wereld van 3D-modellering met behulp van Aspose.3D voor .NET. Lineaire extrusie, met en zonder richting, opent eindeloze mogelijkheden voor ontwikkelaars die visueel verbluffende applicaties willen creëren. Met Aspose.3D heeft u de kracht van 3D-modellering binnen handbereik.

## Veelgestelde vragen

### V1: Hoe kan ik een tijdelijke licentie verkrijgen voor Aspose.3D voor .NET?

 A1: Bezoek[Tijdelijke licentie aanvragen](https://purchase.aspose.com/temporary-license/) om een tijdelijke vergunning te verkrijgen.

### Vraag 2: Waar kan ik ondersteuning vinden voor Aspose.3D?

 A2: Sluit je aan bij de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om hulp te zoeken en verbinding te maken met de gemeenschap.

### Vraag 3: Is er een gratis proefversie beschikbaar?

 A3: Ja, ontdek de functies met een gratis proefperiode op[Aspose.3D-releases](https://releases.aspose.com/).

### V4: Hoe koop ik Aspose.3D voor .NET?

 A4: Navigeer naar de[Aspose aankooppagina](https://purchase.aspose.com/buy) voor licentieopties en aankoopdetails.

### V5: Waar kan ik gedetailleerde documentatie vinden voor Aspose.3D voor .NET?

 A5: Raadpleeg de uitgebreide[Aspose.3D .NET-documentatie](https://reference.aspose.com/3d/net/) voor diepgaande informatie.