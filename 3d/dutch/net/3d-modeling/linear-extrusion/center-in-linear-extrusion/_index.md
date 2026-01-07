---
date: 2026-01-07
description: Leer hoe je een grondvlak kunt toevoegen tijdens lineaire extrusie met
  Aspose.3D voor .NET en Wavefront OBJ‑bestanden kunt exporteren. Beheers centreren
  en grondtechnieken in 3‑D‑modellering.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Voeg grondvlak en centrum toe in lineaire extrusie
url: /nl/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Voeg vloervlak en centrering toe bij lineaire extrusie

## Introductie

Welkom bij deze uitgebreide gids over het beheersen van lineaire extrusie met Aspose.3D voor .NET. Als je **een vloervlak wilt toevoegen** aan je modellen en **Wavefront OBJ**-bestanden wilt exporteren terwijl de extrusie gecentreerd blijft, ben je hier op de juiste plek. In deze tutorial duiken we in de lineaire extrusietechniek, met specifieke focus op het centreren en hoe een vloervlak je helpt het resultaat duidelijker te visualiseren.

## Snelle antwoorden
- **Wat bereikt “voeg vloervlak toe”?** Het biedt een visuele referentie waardoor het gemakkelijk is te zien waar de extrusie zich bevindt op het X‑Z-vlak.  
- **Welk formaat wordt gebruikt om het model te exporteren?** De scène wordt opgeslagen als een Wavefront OBJ-bestand (`FileFormat.WavefrontOBJ`).  
- **Heb ik een licentie nodig om de code uit te voeren?** Een gratis proefversie werkt voor ontwikkeling; een permanente licentie is vereist voor productie.  
- **Kan ik de extrusielengte wijzigen?** Ja – wijzig de tweede parameter van `LinearExtrusion`.  
- **Is centreren optioneel?** Instellen van `Center = true` centreert de extrusie rond het profiel; `false` plaatst het aan één kant.

## Vereisten

Voordat we aan deze spannende reis beginnen, zorg ervoor dat je de volgende vereisten hebt:

- Basiskennis van de programmeertaal C#.  
- Visual Studio geïnstalleerd op je machine.  
- Aspose.3D voor .NET bibliotheek, die je kunt downloaden van de [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Zorg ervoor dat je toegang hebt tot de [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) voor referentie gedurende de tutorial.

## Namespaces importeren

Laten we om te beginnen de benodigde namespaces importeren. Deze vormen de basis voor ons 3D-modelleringsmeesterwerk.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Stap 1: Initialiseer het basisprofiel

We beginnen met het definiëren van een rechthoekig profiel dat geëxtrudeerd zal worden. De `RoundingRadius` voegt een subtiele afronding toe aan de hoeken.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Stap 2: Maak een 3D-scène

Een `Scene`-object fungeert als de container voor alle geometrie, verlichting en camera's.

```csharp
Scene scene = new Scene();
```

## Stap 3: Maak linker- en rechterknooppunten

Er worden twee broederknooppunten onder de root aangemaakt. Eén zal extrusie **zonder** centrering demonstreren, de andere **met** centrering. We verschuiven ook het linker knooppunt zodat de twee voorbeelden elkaar niet overlappen.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Stap 4: Voer lineaire extrusie uit op linker knooppunt (zonder centrering)

Hier extruderen we het profiel zonder centrering. Let op de `Center = false`-vlag.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Stap 5: Voeg vloervlak toe ter referentie (linker knooppunt)

Het toevoegen van een dunne doos fungeert als een **vloervlak** zodat je duidelijk kunt zien hoe de extrusie op de basis zit.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Stap 6: Voer lineaire extrusie uit op rechter knooppunt (met centrering)

Nu extruderen we hetzelfde profiel maar met centrering ingeschakeld. De geometrie wordt symmetrisch geplaatst rond de oorsprong van het profiel.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Stap 7: Voeg vloervlak toe ter referentie (rechter knooppunt)

Een tweede vloervlak wordt toegevoegd aan het rechter knooppunt om de visuele vergelijking consistent te houden.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Stap 8: Exporteer Wavefront OBJ-bestand

Tot slot **exporteren we Wavefront OBJ** zodat het resultaat kan worden geopend in elke standaard 3‑D-viewer.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Waarom een vloervlak toevoegen?

Het toevoegen van een vloervlak geeft je een directe visuele aanwijzing over de hoogte en uitlijning van de extrusie. Het is vooral handig wanneer je gecentreerde versus niet‑gecentreerde resultaten moet vergelijken, zoals in deze tutorial wordt gedemonstreerd.

## Veelvoorkomende problemen & tips

- **Vloervlak niet zichtbaar:** Zorg ervoor dat de dikte van het vlak (`0.01` in de `Box`-constructor) klein genoeg is om de extrusie niet te verbergen, maar groot genoeg om gerenderd te worden.  
- **Export mislukt:** Controleer of de uitvoermap bestaat en of je schrijfrechten hebt.  
- **Gecentreerde extrusie lijkt verschoven:** Controleer de `Center`-eigenschap; `true` centreert het profiel, `false` plaatst het aan één kant.

## Veelgestelde vragen

### Q1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt voornamelijk .NET-talen zoals C# en VB.NET.

### Q2: Waar kan ik ondersteuning vinden voor vragen over Aspose.3D?

A2: Bezoek het [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) voor toegewijde ondersteuning en discussies.

### Q3: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?

A3: Ja, je kunt de gratis proefversie [hier](https://releases.aspose.com/) gebruiken.

### Q4: Hoe kan ik een tijdelijke licentie verkrijgen voor Aspose.3D voor .NET?

A4: Je kunt een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/) verkrijgen.

### Q5: Waar kan ik de Aspose.3D voor .NET-licentie kopen?

A5: Koop je licentie [hier](https://purchase.aspose.com/buy).

### Q6: Kan ik de scène exporteren naar andere formaten naast OBJ?

A6: Ja, Aspose.3D ondersteunt vele formaten zoals STL, FBX en GLTF. Verander eenvoudig de `FileFormat`-enumwaarde in de `Save`-methode.

### Q7: Hoe wijzig ik het aantal slices van de extrusie?

A7: Pas de `Slices`-eigenschap aan in de `LinearExtrusion`-constructor om de maasdichtheid te regelen.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D for .NET latest version  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}