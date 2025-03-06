---
title: Centrum in lineaire extrusie
linktitle: Centrum in lineaire extrusie
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D-modellering met Aspose.3D voor .NET. Centreer lineaire extrusietechnieken, creëer verbluffende ontwerpen en laat uw creativiteit de vrije loop.
weight: 10
url: /nl/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centrum in lineaire extrusie

## Invoering

Welkom bij deze uitgebreide handleiding over het beheersen van lineaire extrusie met Aspose.3D voor .NET. Als u uw vaardigheden op het gebied van 3D-modelleren wilt verbeteren en verbluffende extrusies wilt maken, bent u hier aan het juiste adres. In deze tutorial gaan we dieper in op de lineaire extrusietechniek, waarbij we ons specifiek concentreren op het centreeraspect om uw ontwerpen naar een geheel nieuw niveau te brengen.

## Vereisten

Voordat we aan deze spannende reis beginnen, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:

- Basiskennis van de programmeertaal C#.
- Visual Studio is op uw computer geïnstalleerd.
-  Aspose.3D voor .NET-bibliotheek, die u kunt downloaden van de[Aspose.3D .NET-documentatie](https://reference.aspose.com/3d/net/).
-  Zorg ervoor dat u toegang heeft tot de[Aspose.3D .NET-documentatie](https://reference.aspose.com/3d/net/) ter referentie tijdens de hele tutorial.

## Naamruimten importeren

Laten we om te beginnen de benodigde naamruimten importeren. Deze zullen de basis leggen voor ons meesterwerk op het gebied van 3D-modellering.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Stap 1: Initialiseer het basisprofiel

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Stap 2: Maak een 3D-scène

```csharp
Scene scene = new Scene();
```

## Stap 3: Maak linker- en rechterknooppunten

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Stap 4: Voer lineaire extrusie uit op het linkerknooppunt

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Stap 5: Stel het grondvlak in ter referentie

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Stap 6: Voer lineaire extrusie uit op het rechterknooppunt

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Stap 7: Stel het grondvlak in ter referentie (rechterknooppunt)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Stap 8: Bewaar 3D-scène

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusie

Gefeliciteerd! Je beheerst met succes de kunst van lineaire extrusie met centrering met behulp van Aspose.3D voor .NET. Experimenteer gerust met verschillende parameters en ontdek de enorme mogelijkheden die deze techniek biedt.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt voornamelijk .NET-talen zoals C# en VB.NET.

### V2: Waar kan ik ondersteuning vinden voor Aspose.3D-gerelateerde zoekopdrachten?

 A2: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor toegewijde ondersteuning en discussies.

### V3: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?

 A3: Ja, u heeft toegang tot de gratis proefperiode[hier](https://releases.aspose.com/).

### V4: Hoe kan ik een tijdelijke licentie verkrijgen voor Aspose.3D voor .NET?

 A4: U kunt een tijdelijke licentie aanschaffen[hier](https://purchase.aspose.com/temporary-license/).

### V5: Waar kan ik de Aspose.3D voor .NET-licentie kopen?

 A5: Koop uw licentie[hier](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
