---
date: 2026-01-14
description: Leer hoe je een camera aan een scène toevoegt en de scène exporteert
  als FBX met Aspose.3D voor .NET – een stapsgewijze handleiding om cameratargets
  in te stellen en 3D‑animaties te maken.
linktitle: Add Camera to Scene and Set Up Targets for 3D Animation
second_title: Aspose.3D .NET API
title: Camera toevoegen aan de scène en doelen instellen voor 3D‑animatie
url: /nl/net/animation/setup-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Camera toevoegen aan scène en doelen instellen voor 3D-animatie

## Introductie

Als je een 3D-animatie maakt, is het eerste wat je nodig hebt een goed gepositioneerde camera. In deze tutorial leer je **hoe je een camera aan een scène toevoegt**, het doel definieert, en uiteindelijk **de scène exporteert als FBX** met Aspose.3D voor .NET. We lopen elke stap door, leggen uit waarom het belangrijk is, en geven je praktische tips zodat je overtuigende 3D-animaties kunt maken met vertrouwen.

## Snelle antwoorden
- **Wat is de eerste stap om een camera toe te voegen?** Initialiseer een `Scene` object dat de camera‑node host.  
- **Welk bestandsformaat wordt gebruikt voor export in deze gids?** FBX (`.fbx`).  
- **Heb ik een licentie nodig om de voorbeeldcode uit te voeren?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.  
- **Welke .NET‑versies worden ondersteund?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Kan ik de camerapositie na creatie wijzigen?** Ja – wijzig `cameraNode.Transform.Translation` op elk moment.

## Wat is **add camera to scene**?
Een camera aan een scène toevoegen betekent het creëren van een `Camera`‑entiteit, deze koppelen aan een node in de scène‑grafiek, en positioneren zodat deze naar een doelpunt “kijkt”. Dit bepaalt het perspectief van de kijker wanneer de scène wordt gerenderd of geëxporteerd.

## Waarom camera‑doelen instellen en exporteren als FBX?
- **Controleer het gezichtspunt** – precieze camerapositie stelt je in staat je animatie exact te kaderen zoals je je voorstelt.  
- **Interoperabiliteit** – FBX wordt breed ondersteund door game‑engines, Maya, Blender en andere 3D‑tools, waardoor het eenvoudig is om assets te delen.  
- **Herbruikbare assets** – zodra de camera en het doel zijn opgeslagen, kun je de scène in meerdere projecten hergebruiken.

## Voorvereisten

Voordat je aan de tutorial begint, zorg dat je de volgende voorvereisten hebt:

- Basiskennis van C# en het .NET‑framework.  
- Aspose.3D voor .NET bibliotheek geïnstalleerd. Je kunt het downloaden [hier](https://releases.aspose.com/3d/net/).  
- Een ontwikkelomgeving klaar voor 3D‑programmeren.

## Namespaces importeren

Om het proces te starten, importeer je de benodigde namespaces in je project. Deze namespaces zijn essentieel om de kracht van Aspose.3D voor .NET te benutten:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Stapsgewijze handleiding

### Stap 1: Scene‑object initialiseren

Begin met het initialiseren van het scene‑object. Dit dient als het canvas waarop je 3D‑animatie tot leven komt.

```csharp
// ExStart:SetupTargetAndCamera
// Initialize scene object
Scene scene = new Scene();
```

### Stap 2: Een camera‑node maken

Vervolgens maak je een child‑node die de camera bevat. Het geven van een betekenisvolle naam aan de node helpt de scène‑hiërarchie georganiseerd te houden.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Stap 3: De camera positioneren

Specificeer de translatie voor de camera‑node. Dit bepaalt de initiële positie van de camera in de 3D‑ruimte.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Stap 4: Het camera‑doel definiëren

Een camera heeft een doelpunt nodig om naar te kijken. We creëren een andere child‑node die als focuspunt fungeert en wijzen deze toe aan de `Target`‑eigenschap van de camera.

```csharp
cameraNode.GetEntity<Camera>().Target = scene.RootNode.CreateChildNode("target");
```

### Stap 5: De geconfigureerde scène opslaan

Exporteer tenslotte de scène naar een FBX‑bestand (of een ander ondersteund formaat). Vervang `"Your Output Directory"` door het daadwerkelijke pad waar je het bestand wilt opslaan.

```csharp
var output = "Your Output Directory" + "camera-test.fbx";
scene.Save(output);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Oplossing |
|----------|-----------|
| **Camera verschijnt onder de verkeerde hoek** | Controleer of de target‑node zich op de verwachte positie bevindt. Je kunt ook `cameraNode.GetEntity<Camera>().UpVector` instellen om de oriëntatie te regelen. |
| **Geëxporteerde FBX opent niet in andere tools** | Zorg ervoor dat je een recente versie van Aspose.3D gebruikt (de bibliotheek schrijft automatisch een compatibele FBX‑versie). |
| **Pad niet gevonden fout bij `scene.Save`** | Gebruik een absoluut pad of zorg ervoor dat de uitvoermap bestaat voordat je `Save` aanroept. |

## Veelgestelde vragen

### Q1: Is Aspose.3D compatibel met andere 3D-modelleringshulpmiddelen?

A1: Aspose.3D ondersteunt verschillende bestandsformaten, waardoor het compatibel is met populaire 3D-modelleringshulpmiddelen.

### Q2: Kan ik Aspose.3D gebruiken voor game‑ontwikkeling?

A2: Absoluut! Aspose.3D stelt ontwikkelaars in staat om eenvoudig 3D‑assets voor games te maken.

### Q3: Waar kan ik extra ondersteuning vinden voor Aspose.3D?

A3: Bezoek het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor community‑ondersteuning en discussies.

### Q4: Is er een gratis proefversie beschikbaar?

A4: Ja, je kunt een gratis proefversie verkennen [hier](https://releases.aspose.com/).

### Q5: Hoe verkrijg ik een tijdelijke licentie?

A5: Verkrijg een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/).

## Conclusie

Je hebt nu geleerd hoe je **add camera to scene** kunt uitvoeren, het doel kunt instellen, en het resultaat kunt exporteren als een FBX‑bestand met Aspose.3D voor .NET. Met deze basis kun je rijkere animaties bouwen, experimenteren met meerdere camera’s, en de geëxporteerde scènes integreren in game‑engines of visual‑effects‑pijplijnen.

---

**Laatst bijgewerkt:** 2026-01-14  
**Getest met:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}