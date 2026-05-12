---
date: 2026-03-23
description: Leer hoe u een extrusie met een draai maakt met Aspose.3D voor .NET.
  Deze stap‑voor‑stap gids behandelt lineaire extrusie‑draai‑technieken.
linktitle: Twist in Linear Extrusion
second_title: Aspose.3D .NET API
title: Hoe een extrusie met een draai te maken in lineaire extrusie
url: /nl/net/3d-modeling/linear-extrusion/twist-in-linear-extrusion/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe een Extrusie met een Draai te Maken in Lineaire Extrusie

## Introductie

Als je .NET‑applicaties bouwt die opvallende 3D‑visualisaties nodig hebben, ontdek je al snel dat **hoe een extrusie te maken** een fundamentele vaardigheid is. Aspose.3D voor .NET biedt je een nette, high‑performance API om eenvoudige 2‑D‑profielen om te zetten in geavanceerde 3‑D‑modellen — vooral wanneer je er een draai aan toevoegt. In deze tutorial lopen we elke stap door, van het opzetten van de scène tot het opslaan van het uiteindelijke OBJ‑bestand, zodat je de kracht van lineaire extrusie met een draai in actie kunt zien.

## Snelle Antwoorden
- **Wat is de primaire klasse voor extrusie?** `LinearExtrusion`
- **Welke eigenschap voegt rotatie toe?** `Twist`
- **Hoeveel slices geven een glad resultaat?** Ongeveer 100 slices (pas aan indien nodig)
- **Kan ik andere vormen gebruiken?** Ja, elke `IProfile` zoals cirkels, polygonen of aangepaste curven
- **Welk bestandsformaat wordt in het voorbeeld gebruikt?** Wavefront OBJ (`.obj`)

## Vereisten

Voordat we beginnen, zorg dat je het volgende hebt:

- Aspose.3D voor .NET geïnstalleerd. Als je het nog niet hebt gedownload, haal het **[hier](https://releases.aspose.com/3d/net/)**.
- Een werkende .NET‑ontwikkelomgeving (Visual Studio, VS Code of een andere IDE naar keuze).
- Basiskennis van C#‑syntaxis en object‑georiënteerde concepten.

## Namespaces Importeren

In elk .NET‑project is het juiste gebruik van namespaces cruciaal. Begin met het importeren van de benodigde namespaces om de functionaliteiten van Aspose.3D effectief te benutten. Hieronder een voorbeeld‑fragment:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Stapsgewijze Gids

### Stap 1: Initialiseert het Basisprofiel

We beginnen met het definiëren van de vorm die geëxtrudeerd zal worden. In dit voorbeeld gebruiken we een rechthoek met een kleine afrondingsradius om de randen een subtiele curve te geven.

```csharp
// Initialize the base profile to be extruded
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

### Stap 2: Maak een 3D‑Scène

Een `Scene`‑object fungeert als het canvas waarop alle 3‑D‑entiteiten leven. Beschouw het als het podium voor je extrusie.

```csharp
// Create a scene 
Scene scene = new Scene();
```

### Stap 3: Voeg Links‑ en Rechts‑Nodes toe

Nodes laten je objecten hiërarchisch organiseren. We maken twee sibling‑nodes — één voor een rechte extrusie en een andere voor een gedraaide versie.

```csharp
// Create left node
var left = scene.RootNode.CreateChildNode();
// Create right node
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
```

### Stap 4: Voer Lineaire Extrusie met Draai uit op de Linker‑Node

De `Twist`‑eigenschap bepaalt hoeveel het profiel roteert tijdens het extruderen. Een waarde van **0** geeft een klassieke rechte extrusie.

```csharp
// Twist property defines the degree of the rotation while extruding the profile
// Perform linear extrusion on the left node using twist and slices property
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 0, Slices = 100 });
```

### Stap 5: Voer Lineaire Extrusie met Draai uit op de Rechter‑Node

Nu passen we een draai van 90 graden toe op hetzelfde profiel. Dit laat het **lineaire extrusie‑draai**‑effect duidelijk zien.

```csharp
// Perform linear extrusion on the right node using twist and slices property
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 90, Slices = 100 });
```

### Stap 6: Sla de 3D‑Scène op

Tot slot exporteren we de scène naar een formaat dat je in elke 3‑D‑viewer kunt bekijken. Het voorbeeld gebruikt Wavefront OBJ, maar Aspose.3D ondersteunt ook vele andere formaten.

```csharp
// Save 3D scene
scene.Save("Your Output Directory" + "TwistInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Waarom Lineaire Extrusie met een Draai Gebruiken?

- **Snelle prototyping:** Zet 2‑D‑schetsen om in 3‑D‑onderdelen zonder handmatig modelleren.
- **Ontwerpflexibiliteit:** Pas de `Twist`‑waarde aan om spiralen, helicale ribben of decoratieve elementen te creëren.
- **Prestatiefriendelijk:** De `Slices`‑parameter stelt je in staat om visuele nauwkeurigheid en runtime‑snelheid in balans te brengen.

## Veelvoorkomende Problemen & Tips

- **Te veel slices:** Hoewel 100 slices er glad uitzien, kunnen extreem hoge waarden de weergave vertragen. Test met lagere aantallen als de performance een probleem wordt.
- **Negatieve twist‑waarden:** Een negatieve `Twist` roteert in de tegenovergestelde richting — handig voor gespiegeld ontwerp.
- **Bestandspaden:** Zorg dat de output‑map bestaat en dat je schrijfrechten hebt; anders zal `scene.Save` een uitzondering werpen.

## Conclusie

In deze tutorial hebben we laten zien **hoe een extrusie te maken** met een draai met behulp van Aspose.3D voor .NET. Door de `Twist`‑ en `Slices`‑eigenschappen aan te passen kun je een breed scala aan vormen genereren, van eenvoudige gedraaide balken tot complexe helicale structuren, allemaal met slechts een paar regels code.

## Veelgestelde Vragen

**Q: Kan ik lineaire extrusie met een draai toepassen op andere vormen?**  
A: Absoluut! Elke klasse die `IProfile` implementeert — zoals `CircleShape`, `PolygonShape` of een aangepaste spline — kan met een draai geëxtrudeerd worden.

**Q: Wat stelt de `Twist`‑eigenschap precies voor?**  
A: Het geeft de totale rotatiehoek (in graden) aan die op het profiel wordt toegepast over de extrusielengte.

**Q: Heeft het verhogen van het aantal slices invloed op het geheugenverbruik?**  
A: Ja, meer slices genereren meer vertices en faces, wat extra geheugen verbruikt en de performance op low‑end apparaten kan beïnvloeden.

**Q: Kan ik lineaire extrusie combineren met andere Aspose.3D‑functies?**  
A: Zeker. Je kunt materialen, texturen of zelfs Booleaanse operaties toepassen na de extrusie om nog rijkere modellen te maken.

**Q: Waar kan ik hulp krijgen of ideeën bespreken met andere ontwikkelaars?**  
A: Word lid van de Aspose.3D‑community op **[Aspose Forum](https://forum.aspose.com/c/3d/18)** voor ondersteuning, voorbeelden en discussies.

---

**Laatst Bijgewerkt:** 2026-03-23  
**Getest Met:** Aspose.3D 24.11 for .NET  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}