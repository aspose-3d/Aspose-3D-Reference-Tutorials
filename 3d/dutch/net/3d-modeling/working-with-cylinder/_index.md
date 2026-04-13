---
date: 2026-03-26
description: Leer hoe je een cilinder maakt en een OBJ‑bestand exporteert met Aspose.3D
  voor .NET. Deze beginnersvriendelijke gids behandelt het opzetten van een 3D‑scene
  en het exporteren van OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hoe maak je een cilinder met schuine bodem – Aspose.3D voor .NET
url: /nl/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe een Cilinder met Schuine Bodem te Maken – Aspose.3D voor .NET

## Inleiding
Als je je afvraagt **hoe je cilinder**‑objecten maakt met een aangepaste schuine bodem in een .NET‑omgeving, ben je hier op de juiste plek. In deze tutorial lopen we elke stap door — van het opzetten van een 3‑D‑scene tot het exporteren van het uiteindelijke model als een OBJ‑bestand — zodat je je *beginner 3D‑modelleervaardigheden* kunt verbeteren met **Aspose.3D voor .NET**.

## Snelle Antwoorden
- **Welke klasse is primair om een 3D‑model te starten?** `Scene` maakt de root‑container voor alle geometrie.  
- **Welke methode exporteert het model naar OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Heb ik een licentie nodig voor testen?** Een gratis proefversie is beschikbaar — zie de proeflink in de FAQ.  
- **Kan ik de schuine hoek aanpassen?** Ja, wijzig `ShearBottom` met een `Vector2`‑waarde.  
- **Is dit geschikt voor beginners?** Absoluut; de API abstraheert low‑level mesh‑verwerking.

## Wat is een 3D‑Scene?
Een *3D‑scene* is een hiërarchische container die alle geometrische entiteiten, lichten, camera’s en transformaties bevat. In Aspose.3D biedt de `Scene`‑klasse een nette manier om je modellen te organiseren en later te exporteren.

## Waarom OBJ Exporteren?
OBJ is een breed ondersteund, tekstgebaseerd formaat dat veel 3‑D‑toepassingen (Blender, Maya, Unity) kunnen importeren. Exporteren naar OBJ stelt je in staat je cilindermodellen te delen of verder te bewerken buiten .NET.

## Vereisten
Voordat we beginnen, zorg dat je het volgende hebt:

- Basiskennis van C# en .NET‑ontwikkeling.  
- **Aspose.3D voor .NET** geïnstalleerd – je kunt het downloaden **[hier](https://releases.aspose.com/3d/net/)**.  
- Een .NET‑IDE (Visual Studio, Rider, of VS Code) klaar voor coderen.

## Namespaces Importeren
Breng eerst de benodigde namespaces in scope zodat de API‑types worden herkend.

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

## Stap 1: Een 3D‑Scene Maken
Het `Scene`‑object fungeert als de root van je modelhiërarchie.

```csharp
Scene scene = new Scene();
```

## Stap 2: Cilinder 1 Maken
We genereren de eerste cilinder met een straal van 2, hoogte 10 en 20 radiale segmenten.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Stap 3: Schuine Bodem Aanpassen voor Cilinder 1
Pas een schuine transformatie toe, schakel fan‑cylinder‑generatie in, en pas andere eigenschappen aan om de gewenste vorm te bereiken.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Stap 4: Cilinder 1 aan de Scene Toevoegen
Plaats de eerste cilinder op een handige locatie met een translatie‑transformatie.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Stap 5: Cilinder 2 Maken
Een tweede cilinder wordt gemaakt met dezelfde basisafmetingen maar zonder aangepaste schuine bodem — perfect voor een naast‑elkaar vergelijking.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Stap 6: Cilinder 2 aan de Scene Toevoegen
We voegen simpelweg de tweede cilinder toe aan de scenegrafiek.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Stap 7: De Scene Exporteren als OBJ‑Bestand
Tot slot slaan we de volledige scene op als een OBJ‑bestand zodat het in elke standaard 3‑D‑viewer kan worden geopend.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Veelvoorkomende Problemen en Oplossingen
| Probleem | Waarom Het Optreedt | Oplossing |
|----------|----------------------|-----------|
| **OBJ‑bestand is leeg** | De scene bevat geen geometrie. | Zorg ervoor dat beide cilinders zijn toegevoegd aan `scene.RootNode`. |
| **Shear ziet er verkeerd uit** | `ShearBottom` verwacht de tangens van de hoek. | Gebruik `Math.Tan(angleInRadians)` of de gegeven `0.83` voor ~47,5°. |
| **Bestandspad‑fouten** | Ongeldige of ontbrekende map. | Gebruik `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Veelgestelde Vragen
### Is Aspose.3D voor .NET geschikt voor beginners?
Absoluut! Aspose.3D voor .NET biedt een high‑level API die de wiskundig intensieve delen van 3‑D‑modellering abstraheert, waardoor het toegankelijk is voor ontwikkelaars van elk vaardigheidsniveau.

### Kan ik verschillende schuine hoeken toepassen op cilinders?
Ja, elke `Cylinder`‑instantie heeft zijn eigen `ShearBottom`‑eigenschap, zodat je een unieke hoek aan elk object kunt toewijzen.

### Is er een proefversie beschikbaar?
Ja, je kunt de gratis proefversie verkennen **[hier](https://releases.aspose.com/)**.

### Waar vind ik extra ondersteuning?
Bezoek het **[Aspose.3D‑forum](https://forum.aspose.com/c/3d/18)** voor community‑hulp, code‑samples en discussies.

### Hoe kan ik een tijdelijke licentie verkrijgen?
Vraag je tijdelijke licentie **[hier](https://purchase.aspose.com/temporary-license/)** aan.

**Aanvullende V&A**

**V: Hoe exporteer ik het model in een ander formaat, zoals STL?**  
A: Vervang `FileFormat.WavefrontOBJ` door `FileFormat.STL` in de `scene.Save`‑aanroep.

**V: Kan ik de cilinders na creatie animeren?**  
A: Ja, je kunt key‑frame‑animaties toevoegen aan node‑transformaties met de `Animation`‑klassen die door Aspose.3D worden geleverd.

**V: Ondersteunt de API .NET Core?**  
A: De bibliotheek is volledig compatibel met .NET Core, .NET 5+ en .NET 6+.

---

**Laatst bijgewerkt:** 2026-03-26  
**Getest met:** Aspose.3D voor .NET (laatste release)  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}