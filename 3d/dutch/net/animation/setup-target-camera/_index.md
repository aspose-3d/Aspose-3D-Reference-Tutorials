---
date: 2026-04-08
description: Leer hoe je een camera aan een scène toevoegt en de scène exporteert
  als FBX met Aspose.3D voor .NET – een stapsgewijze handleiding om cameratargets
  in te stellen en 3D‑animaties te maken.
keywords:
- add camera to scene
- set camera target
- export scene as fbx
- how to add camera
- position camera in 3d
linktitle: Camera toevoegen aan scène en doelen instellen voor 3D‑animatie
second_title: Aspose.3D .NET API
title: Camera toevoegen aan scène en doelen instellen voor 3D‑animatie
url: /nl/net/animation/setup-target-camera/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Camera toevoegen aan scène en doelen instellen voor 3D-animatie

## Inleiding

Als je een 3D‑animatie maakt, is het eerste wat je nodig hebt een goed gepositioneerde camera. In deze tutorial leer je **hoe je een camera aan een scène toevoegt**, het doel definieert, en uiteindelijk **de scène exporteert als FBX** met Aspose.3D voor .NET. We lopen elke stap door, leggen uit waarom het belangrijk is, en geven praktische tips zodat je overtuigende 3D‑animaties kunt maken met vertrouwen. Aan het einde begrijp je ook hoe je **camera positioneert in 3D** ruimte voor optimale compositie.

## Snelle antwoorden
- **Wat is de eerste stap om een camera toe te voegen?** Initialiseer een `Scene` object dat de camera‑node host.  
- **Welk bestandsformaat wordt in deze gids gebruikt voor export?** FBX (`.fbx`).  
- **Heb ik een licentie nodig om de voorbeeldcode uit te voeren?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.  
- **Welke .NET‑versies worden ondersteund?** .NET Framework 4.5+, .NET Core 3.1+, .NET 5/6+.  
- **Kan ik de camera‑positie na creatie wijzigen?** Ja – wijzig `cameraNode.Transform.Translation` op elk moment.

## Wat is **add camera to scene**?
Een camera aan een scène toevoegen betekent het maken van een `Camera`‑entity, deze koppelen aan een node in de scène‑grafiek, en positioneren zodat deze naar een doelpunt “kijkt”. Dit bepaalt het perspectief van de kijker wanneer de scène wordt gerenderd of geëxporteerd.

## Waarom camera‑doelen instellen en exporteren als FBX?
- **Beheer het gezichtspunt** – precieze plaatsing van de camera laat je de animatie exact kaderen zoals je je voorstelt.  
- **Interoperabiliteit** – FBX wordt breed ondersteund door game‑engines, Maya, Blender en andere 3D‑tools, waardoor het eenvoudig is om assets te delen.  
- **Herbruikbare assets** – zodra de camera en het doel zijn opgeslagen, kun je de scène in meerdere projecten hergebruiken.

## Veelvoorkomende gebruikssituaties
- **Cinematische cut‑scenes** in games waarbij een vaste camera een personage volgt.  
- **Productvisualisaties** waarbij je een stabiel gezichtspunt nodig hebt om een model vanuit verschillende hoeken te tonen.  
- **Pre‑visualisatie** voor film‑ of AR/VR‑projecten, waardoor ontwerpers de camera‑plaatsing kunnen itereren vóór de uiteindelijke rendering.

## Voorvereisten

Voordat je aan de tutorial begint, zorg dat je de volgende voorvereisten hebt:

- Basiskennis van C# en het .NET‑framework.  
- Aspose.3D voor .NET bibliotheek geïnstalleerd. Je kunt het downloaden [hier](https://releases.aspose.com/3d/net/).  
- Een ontwikkelomgeving klaar voor 3D‑programmeren.

## Namespaces importeren

Om het proces op gang te brengen, importeer je de benodigde namespaces in je project. Deze namespaces zijn essentieel om de kracht van Aspose.3D voor .NET te benutten:

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

Maak vervolgens een child‑node die de camera zal bevatten. Het geven van een betekenisvolle naam aan de node helpt de scène‑hiërarchie georganiseerd te houden.

```csharp
// Get a child node object
Node cameraNode = scene.RootNode.CreateChildNode("camera", new Camera());
```

### Stap 3: De camera positioneren

Specificeer de translatie voor de camera‑node. Dit bepaalt de initiële positie van de camera in de 3D‑ruimte. Pas de `Vector3`‑waarden aan om **camera positioneert in 3D** te krijgen zoals nodig voor jouw opname.

```csharp
// Set camera node translation
cameraNode.Transform.Translation = new Vector3(100, 20, 0);
```

### Stap 4: Het camera‑doel definiëren

Een camera heeft een doelpunt nodig om naar te kijken. We maken een andere child‑node die fungeert als focuspunt en wijzen deze toe aan de `Target`‑eigenschap van de camera. Zo **stel je het camera‑doel in** voor een stabiel uitzicht.

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
| **Camera verschijnt onder de verkeerde hoek** | Controleer of de target‑node zich bevindt waar je verwacht. Je kunt ook `cameraNode.GetEntity<Camera>().UpVector` instellen om de orientatie te regelen. |
| **Geëxporteerde FBX opent niet in andere tools** | Zorg ervoor dat je een recente versie van Aspose.3D gebruikt (de bibliotheek schrijft automatisch een compatibele FBX‑versie). |
| **Pad niet gevonden fout bij `scene.Save`** | Gebruik een absoluut pad of zorg dat de output‑directory bestaat voordat je `Save` aanroept. |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met andere 3D‑modelleertools?**  
A: Aspose.3D ondersteunt verschillende bestandsformaten, waardoor compatibiliteit met populaire 3D‑modelleertools gegarandeerd is.

**Q: Kan ik Aspose.3D gebruiken voor game‑ontwikkeling?**  
A: Absoluut! Aspose.3D stelt ontwikkelaars in staat om 3D‑assets voor games moeiteloos te creëren.

**Q: Waar vind ik extra ondersteuning voor Aspose.3D?**  
A: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor community‑ondersteuning en discussies.

**Q: Is er een gratis proefversie beschikbaar?**  
A: Ja, je kunt een gratis proefversie verkennen [hier](https://releases.aspose.com/).

**Q: Hoe verkrijg ik een tijdelijke licentie?**  
A: Haal een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/).

## Conclusie

Je hebt nu geleerd hoe je **camera aan scène toevoegt**, het doel instelt, en het resultaat exporteert als een FBX‑bestand met Aspose.3D voor .NET. Met deze basis kun je rijkere animaties bouwen, experimenteren met meerdere camera’s, en de geëxporteerde scènes integreren in game‑engines of visual‑effects‑pijplijnen.

---

**Laatst bijgewerkt:** 2026-04-08  
**Getest met:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}