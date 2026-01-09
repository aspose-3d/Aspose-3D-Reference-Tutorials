---
date: 2026-01-09
description: Leer hoe je een 3D‑scène maakt en een 3D‑model opslaat met Aspose.3D
  voor .NET, inclusief export van Wavefront OBJ en lineaire extrusiesneden.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Maak 3D‑scène met lineaire extrusiesneden
url: /nl/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3D‑scène met lineaire extrusiesneden

## Introduction

Welkom in de wereld van 3D‑ontwerp met Aspose.3D voor .NET! In deze tutorial zult u **create 3d scene** objecten maken, lineaire extrusie toepassen met aangepaste slice‑aantallen, en uiteindelijk **save 3d model** als een Wavefront OBJ‑bestand. Of u nu een snelle prototype bouwt of een productie‑klare visualisatie, de onderstaande stappen laten u zien **how to use Aspose** om hoogwaardige geometrie direct vanuit C# te genereren.

## Quick Answers
- **What does “create 3d scene” mean?** Het betekent het bouwen van een Scene‑object dat alle 3D‑entiteiten (meshes, lights, cameras) bevat.  
- **Which format is used for export?** Het voorbeeld exporteert naar **Wavefront OBJ** (`export wavefront obj`).  
- **How many slices can I set?** U kunt elk geheel getal instellen; de demo toont 2 en 10 slices.  
- **Do I need a license?** Een tijdelijke of volledige licentie is vereist voor productiegebruik.  
- **Can I run this on .NET Core?** Ja, Aspose.3D ondersteunt .NET Framework en .NET Core.

## Prerequisites

Voordat u duikt in de wereld van 3D‑ontwerp met Aspose.3D, zorg ervoor dat u de volgende vereisten heeft:

- Aspose.3D for .NET Library: Zorg ervoor dat u de Aspose.3D‑bibliotheek geïnstalleerd heeft. U kunt deze downloaden van [here](https://releases.aspose.com/3d/net/).

- Integrated Development Environment (IDE): Gebruik een IDE naar keuze die compatibel is met .NET‑ontwikkeling.

- Basic Understanding of C#: Maak uzelf vertrouwd met de basisprincipes van de programmeertaal C#.

- Desire to Explore 3D Design: Een passie voor het creëren van visueel verbluffende 3D‑modellen!

## Import Namespaces

Om uw 3D‑ontwerpreis met Aspose.3D te beginnen, moet u de benodigde namespaces importeren. Dit zorgt ervoor dat uw code toegang heeft tot de vereiste klassen en functionaliteiten.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## How to create 3d scene with Linear Extrusion

Hieronder lopen we stap voor stap door de vereiste stappen om de scène te bouwen, extrusie toe te passen, en **save 3d model** als een OBJ‑bestand op te slaan. De uitleg is geschreven in een gesprekstoon zodat u gemakkelijk kunt volgen.

### Step 1: Initialize the Base Profile

Eerst definiëren we de 2‑D‑vorm die geëxtrudeerd zal worden. In dit geval een rechthoek met afgeronde hoeken.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Step 2: Create a 3D Scene

Een `Scene`‑object is de container voor alle geometrie, lichten en camera's – de kern van **creating a 3d scene**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Step 3: Create Left and Right Nodes

We voegen twee child‑nodes toe aan de root van de scène. Eén zal een laag slice‑aantal gebruiken, de andere een hoger aantal, zodat u het visuele verschil kunt zien.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Step 4: Perform Linear Extrusion on Left Node

Hier extruderen we de rechthoek met **2 slices**. Minder slices geven een grovere uitstraling.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Step 5: Perform Linear Extrusion on Right Node

Nu extruderen we hetzelfde profiel maar met **10 slices**, wat een gladder oppervlak oplevert.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Step 6: Save 3D Scene

Tot slot exporteren we de scène naar een Wavefront OBJ‑bestand. Dit demonstreert **how to save obj** en **export wavefront obj** met Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Common Issues and Solutions

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| OBJ‑bestand lijkt leeg | Uitvoerpad is onjuist of er ontbreken schrijfrechten. | Controleer of de map bestaat en de applicatie schrijfrechten heeft. |
| Slices beïnvloeden de gladheid niet | `Slices`‑waarde is te laag voor de grootte van de geometrie. | Verhoog het aantal slices of pas de profielafmetingen aan. |
| Licentie‑exception | Uitvoeren zonder een geldige licentie in een niet‑trial build. | Pas een tijdelijke of permanente licentie toe met `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Frequently Asked Questions

**Q: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?**  
A: Aspose.3D is voornamelijk ontworpen voor .NET, maar u kunt interoperabiliteitsopties verkennen met talen zoals Python via .NET‑bindings.

**Q: Waar kan ik gedetailleerde documentatie vinden voor Aspose.3D voor .NET?**  
A: Raadpleeg de documentatie [here](https://reference.aspose.com/3d/net/) voor diepgaande informatie over de mogelijkheden en het gebruik van Aspose.3D.

**Q: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?**  
A: Ja, u kunt uw gratis proefversie [here](https://releases.aspose.com/) downloaden om de functies van de bibliotheek te verkennen voordat u een aankoop doet.

**Q: Hoe kan ik technische ondersteuning krijgen voor Aspose.3D voor .NET?**  
A: Bezoek het Aspose.3D‑forum [here](https://forum.aspose.com/c/3d/18) voor hulp en om deel te nemen aan de community.

**Q: Kan ik een tijdelijke licentie gebruiken voor Aspose.3D voor .NET?**  
A: Ja, verkrijg een tijdelijke licentie [here](https://purchase.aspose.com/temporary-license/) voor evaluatiedoeleinden.

## Conclusion

Gefeliciteerd! U heeft met succes geleerd hoe u **create 3d scene** kunt maken, lineaire extrusie met aangepaste slice‑aantallen kunt toepassen, en **save 3d model** als een Wavefront OBJ‑bestand kunt opslaan met Aspose.3D voor .NET. Dit is slechts het begin van uw 3D‑ontwerpreis—voel u vrij om te experimenteren met verschillende profielen, slice‑waarden en exportformaten om het volledige potentieel van **3d modeling c#** te benutten.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2026-01-09  
**Getest met:** Aspose.3D 24.11 voor .NET  
**Auteur:** Aspose