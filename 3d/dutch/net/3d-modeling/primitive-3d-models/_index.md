---
title: Primitieve 3D-modellen maken
linktitle: Primitieve 3D-modellen maken
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D-modellering met Aspose.3D voor .NET. Creëer moeiteloos verbluffende primitieve modellen.
weight: 10
url: /nl/net/3d-modeling/primitive-3d-models/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Primitieve 3D-modellen maken

## Invoering

Welkom in de opwindende wereld van 3D-modellering met Aspose.3D voor .NET! In deze uitgebreide tutorial verkennen we stap voor stap het proces van het maken van primitieve 3D-modellen met Aspose.3D. Of u nu een doorgewinterde ontwikkelaar of een nieuwsgierige beginner bent, deze gids helpt u de kracht van Aspose.3D te benutten om visueel verbluffende 3D-elementen voor uw projecten te maken.

## Vereisten

Voordat we in de fascinerende wereld van 3D-modellering duiken, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Download en installeer de Aspose.3D voor .NET-bibliotheek van de[download link](https://releases.aspose.com/3d/net/).

- Ontwikkelomgeving: Zet een .NET-ontwikkelomgeving op, zorg voor compatibiliteit met Aspose.3D.

Nu u over de essentiële zaken beschikt, gaan we aan onze reis beginnen om stap voor stap primitieve 3D-modellen te maken.

## Naamruimten importeren

Begin met het importeren van de benodigde naamruimten om toegang te krijgen tot de functionaliteit van Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Met deze naamruimten bent u klaar om de kracht van Aspose.3D in uw .NET-toepassing te ontketenen.

## Stap 1: Initialiseer een scèneobject

```csharp
//Initialiseer een Scene-object
Scene scene = new Scene();
```

Maak een nieuw scèneobject, dat dient als canvas voor uw 3D-meesterwerk.

## Stap 2: Maak een doosmodel

```csharp
// Maak een Box-model
scene.RootNode.CreateChildNode("box", new Box());
```

Voeg een doosmodel toe aan de hoofdmap van uw scène. Pas de afmetingen en eigenschappen van de doos aan volgens uw creatieve visie.

## Stap 3: Maak een cilindermodel

```csharp
// Maak een cilindermodel
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Verbeter uw scène door een cilindermodel te introduceren. Pas de parameters aan om de gewenste vorm en grootte te bereiken.

## Stap 4: Sla de tekening op in FBX-formaat

```csharp
// Sla de tekening op in het FBX-formaat
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Sla uw 3D-meesterwerk op in het FBX-formaat. Kies een geschikte uitvoermap en bestandsnaam voor uw creatie.

## Stap 5: Succesbericht weergeven

```csharp
// Succesbericht weergeven
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Vier je prestatie! De scène is met succes opgebouwd uit primitieve 3D-modellen en het bestand is opgeslagen.

## Conclusie

 Gefeliciteerd! U hebt met succes verbluffende 3D-modellen gemaakt met Aspose.3D voor .NET. Deze gids behandelt de basisprincipes, maar de mogelijkheden zijn onbeperkt. Ontdek de[documentatie](https://reference.aspose.com/3d/net/) voor meer geavanceerde functies en technieken.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt voornamelijk .NET, maar er zijn andere versies beschikbaar voor Java en andere platforms.

### Vraag 2: Is er een gratis proefversie beschikbaar?

 A2: Ja, u kunt de mogelijkheden van Aspose.3D verkennen met een[gratis proefperiode](https://releases.aspose.com/).

### V3: Waar kan ik ondersteuning vinden voor Aspose.3D voor .NET?

 A3: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor gemeenschapsondersteuning en discussies.

### Vraag 4: Hoe kan ik een tijdelijke licentie verkrijgen?

 A4: U kunt een tijdelijke licentie verkrijgen[hier](https://purchase.aspose.com/temporary-license/).

### Vraag 5: Zijn er voorbeeldtutorials beschikbaar?

 A5: Ja, bekijk meer tutorials en voorbeelden in de[documentatie](https://reference.aspose.com/3d/net/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
