---
title: Conversie van niet-PBR naar PBR-materiaal
linktitle: Conversie van niet-PBR naar PBR-materiaal
second_title: Aspose.3D .NET-API
description: Verken Aspose.3D voor .NET - Converteer moeiteloos niet-PBR naar PBR-materialen. Uitgebreide tutorial en krachtige API.
weight: 16
url: /nl/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Conversie van niet-PBR naar PBR-materiaal

## Invoering

Welkom bij deze stapsgewijze handleiding over het gebruik van Aspose.3D voor .NET om niet-PBR (Physically Based Rendering) naar PBR-materialen te converteren. Aspose.3D is een krachtige API waarmee ontwikkelaars naadloos kunnen werken met 3D-bestandsindelingen in hun .NET-toepassingen.

## Vereisten

Voordat we in de tutorial duiken, moet je ervoor zorgen dat je aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Zorg ervoor dat de Aspose.3D voor .NET-bibliotheek is geïnstalleerd. Je kunt de downloadlink vinden[hier](https://releases.aspose.com/3d/net/).

- Basiskennis van C#: Deze tutorial gaat ervan uit dat je een fundamenteel begrip hebt van programmeren in C#.

- IDE (Integrated Development Environment): Kies de IDE van uw voorkeur voor .NET-ontwikkeling, zoals Visual Studio.

## Naamruimten importeren

Begin in uw C#-code met het importeren van de benodigde naamruimten:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Stap 1: Initialiseer een nieuwe 3D-scène

Begin met het maken van een nieuwe 3D-scène met behulp van de volgende code:

```csharp
// ExStart: Niet_PBRnaarPBRMateriaal
// initialiseer een nieuwe 3D-scène
var scene = new Scene();
```

## Stap 2: Maak een 3D-object

Maak vervolgens een 3D-object, bijvoorbeeld een doos:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Stap 3: Materiaalconversie configureren

Materiaalconversieopties instellen voor conversie van niet-PBR naar PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Stap 4: Opslaan in GLTF 2.0-indeling

Sla de geconverteerde scène op in GLTF 2.0-formaat:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd: Niet_PBRnaarPBRMateriaal
```

Herhaal deze stappen indien nodig voor uw specifieke gebruiksscenario, en zorg ervoor dat elk detail correct is geconfigureerd.

## Conclusie

Gefeliciteerd! Je hebt met succes geleerd hoe je niet-PBR-materialen naar PBR-materialen kunt converteren met behulp van Aspose.3D voor .NET. Deze krachtige tool biedt eindeloze mogelijkheden voor manipulatie van 3D-afbeeldingen in uw .NET-toepassingen.

## Veelgestelde vragen

### Vraag 1: Is Aspose.3D compatibel met alle 3D-bestandsformaten?

A1: Ja, Aspose.3D ondersteunt een breed scala aan 3D-bestandsformaten, wat flexibiliteit in uw projecten biedt.

### Vraag 2: Kan ik Aspose.3D gebruiken voor commerciële toepassingen?

 A2: Absoluut! Aspose.3D is een commercieel product en u kunt het kopen[hier](https://purchase.aspose.com/buy).

### Vraag 3: Heb ik een tijdelijke licentie nodig om te testen?

 A3: Ja, u kunt een tijdelijke licentie verkrijgen voor testdoeleinden[hier](https://purchase.aspose.com/temporary-license/).

### V4: Waar kan ik ondersteuning vinden voor Aspose.3D?

 A4: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor gemeenschapsondersteuning en discussies.

### Vraag 5: Is er een gratis proefversie beschikbaar?

 A5: Ja, u kunt een gratis proefversie uitproberen[hier](https://releases.aspose.com/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
