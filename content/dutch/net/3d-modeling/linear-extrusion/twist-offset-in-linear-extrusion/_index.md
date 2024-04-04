---
title: Twist-offset bij lineaire extrusie
linktitle: Twist-offset bij lineaire extrusie
second_title: Aspose.3D .NET-API
description: Ontdek de magie van Aspose.3D voor .NET met onze stapsgewijze handleiding over Twist Offset in lineaire extrusie. Verbeter uw 3D-projecten moeiteloos.
type: docs
weight: 15
url: /nl/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---
## Invoering

Welkom in de wereld van Aspose.3D voor .NET, een veelzijdige bibliotheek waarmee ontwikkelaars gemakkelijk 3D-manipulatie kunnen uitvoeren. In deze tutorial zullen we dieper ingaan op een van de intrigerende functies: de "Twist Offset in lineaire extrusie." Als je er klaar voor bent om je 3D-programmeervaardigheden te verbeteren, laten we er dan meteen in duiken!

## Vereisten

Voordat we aan deze spannende reis beginnen, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET-bibliotheek: Download en installeer de bibliotheek van de .NET-bibliotheek[pagina vrijgeven](https://releases.aspose.com/3d/net/).

- Uw ontwikkelomgeving: Zorg ervoor dat uw ontwikkelomgeving is ingesteld en gereed is voor gebruik.

## Naamruimten importeren

Begin met het importeren van de benodigde naamruimten om toegang te krijgen tot de functionaliteit van Aspose.3D voor .NET. In jouw code kan dit er als volgt uitzien:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Laten we het voorbeeld nu opsplitsen in beheersbare stappen om de Twist Offset in lineaire extrusie onder de knie te krijgen:

## Stap 1: Initialiseer het basisprofiel

Begin met het maken van een basisprofiel, hier geïllustreerd door een rechthoekige vorm met een gespecificeerde afrondingsradius.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Stap 2: Maak een scène

Genereer een 3D-scène om uw knooppunten en vormen te hosten.

```csharp
Scene scene = new Scene();
```

## Stap 3: Maak knooppunten

Construeer knooppunten binnen de scène, zowel links als rechts.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Stap 4: Lineaire extrusie op het linkerknooppunt

Voer lineaire extrusie uit op het linkerknooppunt met behulp van de eigenschap Twist and Slices.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Stap 5: Lineaire extrusie op rechterknooppunt met twist-offset

Voer op het rechterknooppunt lineaire extrusie uit met behulp van de eigenschap Twist, Twist Offset en Slices.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Stap 6: Bewaar 3D-scène

Sla de 3D-scène op in de gewenste uitvoermap en geef het bestandsformaat op als WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Gefeliciteerd! U hebt de Twist Offset met succes geïmplementeerd in lineaire extrusie met behulp van Aspose.3D voor .NET.

## Conclusie

In deze tutorial hebben we de krachtige mogelijkheden van Aspose.3D voor .NET onderzocht, waarbij we ons specifiek richtten op Twist Offset in lineaire extrusie. Met deze nieuwe vaardigheden bent u goed uitgerust om dynamiek in uw 3D-projecten te brengen.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt voornamelijk .NET-talen, maar Aspose biedt vergelijkbare bibliotheken voor Java en andere platforms.

### V2: Hoe verkrijg ik een tijdelijke licentie voor Aspose.3D voor .NET?

 A2: Bezoek[deze link](https://purchase.aspose.com/temporary-license/)het verkrijgen van een tijdelijke licentie voor testdoeleinden.

### V3: Is er een communityforum voor Aspose.3D voor .NET?

 A3: Absoluut! Sluit je aan bij de community op[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om met collega-ontwikkelaars in contact te komen en hulp te zoeken.

### Vraag 4: Zijn er aanvullende voorbeelden en documentatie beschikbaar?

 A4: Ontdek de[documentatie](https://reference.aspose.com/3d/net/) voor uitgebreide handleidingen en voorbeelden.

### V5: Waar kan ik Aspose.3D voor .NET kopen?

 A5: Ga naar[deze link](https://purchase.aspose.com/buy) om een aankoop te doen en het volledige potentieel van Aspose.3D te ontsluiten.