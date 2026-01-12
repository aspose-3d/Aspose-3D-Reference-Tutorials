---
date: 2026-01-12
description: Leer hoe je een shear bottom cylinder maakt en hoe je een 3D‑model in
  OBJ exporteert met Aspose.3D voor .NET. Volg deze stapsgewijze gids om 3D‑modellering
  te beheersen.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hoe maak je een shear bottom cylinder met Aspose.3D voor .NET
url: /nl/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aangepaste Shear Bottom Cylinder

## Introduction
Welcome to our comprehensive guide where **u leert hoe u shear bottom cylinder-modellen maakt** with Aspose.3D for .NET. Whether you’re building a game asset, a mechanical part, or a visual demo, this tutorial shows you exactly how to shape a cylinder’s bottom, apply a shear, and finally **exporteer het 3D-model OBJ** file for use in any downstream pipeline. Let’s walk through each step together, so you can start producing custom geometry in minutes.

## Quick Answers
- **Wat is een shear bottom cylinder?** Een cilinder waarvan het bodemvlak schuin (gesheerd) is in plaats van vlak.  
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for .NET.  
- **Hoe exporteer ik het model?** Gebruik `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Heb ik een licentie nodig?** Een proefversie is beschikbaar; een commerciële licentie is vereist voor productie.  
- **Welke voorwaarden zijn vereist?** .NET-ontwikkelomgeving en het Aspose.3D NuGet‑pakket.

## What is a shear bottom cylinder?
Een shear bottom cylinder is een standaard cilindrisch mesh waarvan het bodemvlak is getransformeerd door een shear‑operatie. Hiermee kunt u schuine bases, hellingen of aangepaste connectoren maken zonder handmatig vertices te bewerken.

## Why use Aspose.3D for this task?
- **Volledige controle** over geometrie‑parameters (radius, hoogte, segmenten).  
- **Ingebouwde shear‑ondersteuning** via de `ShearBottom`‑eigenschap, waardoor u geen low‑level mesh‑manipulatie hoeft te doen.  
- **Één‑klik export** naar populaire formaten zoals OBJ, FBX en STL, waardoor integratie met andere tools naadloos verloopt.

## Prerequisites
Voordat we beginnen, zorg ervoor dat u het volgende heeft:

- Basiskennis van C# en .NET.  
- Aspose.3D for .NET geïnstalleerd. U kunt het downloaden **[here](https://releases.aspose.com/3d/net/)**.  
- Een .NET‑compatibele IDE (Visual Studio, Rider of VS Code).

## Import Namespaces
Importeer in uw C#‑bestand de benodigde namespaces:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Step 1: Create a Scene
Maak eerst een nieuwe 3‑D‑scene aan die al onze objecten zal bevatten.

```csharp
Scene scene = new Scene();
```

## Step 2: Create Cylinder 1
Maak de primaire cilinder die we gaan aanpassen met een gesheerde bodem.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 3: Customize Shear Bottom for Cylinder 1
Pas de shear toe, schakel fan‑generatie in en pas andere eigenschappen aan om de gewenste vorm te bereiken.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Step 4: Add Cylinder 1 to the Scene
Plaats de aangepaste cilinder in de scene en verplaats deze een beetje naar rechts zodat we beide objecten naast elkaar kunnen zien.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Step 5: Create Cylinder 2
Maak een tweede, eenvoudige cilinder voor vergelijking.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Step 6: Add Cylinder 2 to the Scene
Voeg de tweede cilinder toe zonder aangepaste shear — dit helpt het effect van de vorige stappen te illustreren.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Step 7: Save the Scene
Exporteer tenslotte de hele scene als een OBJ‑bestand zodat u deze kunt openen in Blender, Maya of een andere 3‑D‑viewer.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Common Issues & Tips
- **Shear‑waarden**: De `Vector2` neemt X‑ en Y‑shearfactoren. Een waarde van `0.83` komt ongeveer overeen met 47,5°, maar u kunt deze aanpassen voor verschillende hoeken.  
- **Exportpad**: Zorg ervoor dat de opgegeven map bestaat en dat u schrijfrechten heeft; anders zal `scene.Save` een uitzondering werpen.  
- **Prestaties**: Overweeg bij zeer hoge‑segment cilinders het aantal segmenten (`20` in het voorbeeld) te verlagen om de OBJ‑bestandsgrootte beheersbaar te houden.

## Frequently Asked Questions

### Is Aspose.3D for .NET suitable for beginners?
Absoluut! Aspose.3D for .NET biedt een gebruiksvriendelijke API, waardoor het toegankelijk is voor zowel beginners als ervaren ontwikkelaars.

### Can I apply different shearing angles to cylinders?
Ja, u kunt de `ShearBottom` voor elke cilinder afzonderlijk aanpassen, waardoor u unieke effecten kunt bereiken.

### Is there a trial version available?
Ja, u kunt de gratis proefversie verkennen **[here](https://releases.aspose.com/)**.

### Where can I find additional support?
Bezoek het **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** voor community‑ondersteuning en discussies.

### How can I obtain a temporary license?
Haal uw tijdelijke licentie **[here](https://purchase.aspose.com/temporary-license/)**.

**Additional Q&A**

**Q: How do I change the export format to FBX?**  
A: Replace `FileFormat.WavefrontOBJ` with `FileFormat.FBX` in the `scene.Save` call.

**Q: Hoe wijzig ik het exportformaat naar FBX?**  
A: Vervang `FileFormat.WavefrontOBJ` door `FileFormat.FBX` in de `scene.Save`‑aanroep.

**Q: Can I animate the cylinder after exporting?**  
A: OBJ does not support animation; use FBX or GLTF if you need animated data.

**Q: Kan ik de cilinder animeren na het exporteren?**  
A: OBJ ondersteunt geen animatie; gebruik FBX of GLTF als u geanimeerde data nodig heeft.

**Q: What if I need a larger cylinder radius?**  
A: Adjust the first two parameters of the `Cylinder` constructor (e.g., `new Cylinder(4, 4, …)`).

**Q: Wat als ik een grotere cilinderstraal nodig heb?**  
A: Pas de eerste twee parameters van de `Cylinder`‑constructor aan (bijv. `new Cylinder(4, 4, …)`).

## Conclusion
U heeft nu geleerd hoe u **shear bottom cylinder**‑modellen maakt en deze exporteert als OBJ‑bestanden met Aspose.3D for .NET. Experimenteer met verschillende shear‑waarden, segmentaantallen en exportformaten om aan de behoeften van uw project te voldoen. Veel plezier met modelleren!

---

**Last Updated:** 2026-01-12  
**Tested With:** Aspose.3D for .NET 24.11 (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}