---
date: 2026-01-07
description: Leer hoe je een 2D‑profiel lineair extrudeert en een 3D‑model OBJ exporteert
  met Aspose.3D voor .NET. Deze tutorial over lineaire extrusie leidt je stap voor
  stap.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Hoe lineair extruderen met Aspose.3D voor .NET
url: /nl/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe lineair extruderen met Aspose.3D voor .NET

## Introductie

Welkom bij onze **linear extrusion tutorial**! In deze gids ontdek je **hoe je lineair kunt extruderen** een 2‑D‑profiel en dit omtovert tot een volledig 3‑D‑object met behulp van Aspose.3D voor .NET. Of je nu een CAD‑achtige applicatie bouwt of gewoon **3d model obj**‑bestanden moet exporteren voor verdere verwerking, deze stap‑voor‑stap walkthrough geeft je het vertrouwen om krachtige geometrie‑creatie aan je projecten toe te voegen.

## Snelle antwoorden
- **Wat is linear extrusion?** Een 2‑D‑vorm langs een rechte lijn uitbreiden om een 3‑D‑solid te creëren.  
- **Welke bibliotheek gebruiken we?** Aspose.3D voor .NET.  
- **Heb ik een licentie nodig?** Een tijdelijke licentie werkt voor testen; een volledige licentie is vereist voor productie.  
- **Kan ik exporteren naar OBJ?** Ja – de uiteindelijke scene wordt opgeslagen als een Wavefront OBJ‑bestand.  
- **Hoeveel regels code?** Minder dan 30 regels C# plus verklarende opmerkingen.

## Wat is Linear Extrusion?

Linear extrusion neemt een plat profiel (zoals een rechthoek of cirkel) en veegt het langs een rechte lijn, eventueel met twists, scaling of offsets. Het resultaat is een solid die kan worden gerenderd, bewerkt of geëxporteerd voor gebruik in andere 3‑D‑tools.

## Waarom Aspose.3D gebruiken voor Linear Extrusion?

* **Zero‑dependency:** Geen externe CAD‑kernels nodig.  
* **Full .NET support:** Werkt met .NET Framework, .NET Core, en .NET 5/6+.  
* **Export flexibility:** Direct opslaan naar OBJ, STL, FBX en vele andere formaten.  
* **Rich API:** Beheer slices, twist en offsets met slechts een paar eigenschappen.

## Vereisten

Voordat je begint, zorg dat je het volgende hebt:

1. **Aspose.3D geïnstalleerd** – download het van [here](https://releases.aspose.com/3d/net/).  
2. **Documentatie toegang** – volg de installatiegids [here](https://reference.aspose.com/3d/net/).  
3. Een .NET‑ontwikkelomgeving (Visual Studio, VS Code, of Rider) met de vereiste namespaces.

## Namespaces importeren

Include the essential namespaces to unlock Aspose.3D functionality:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Deze namespaces geven je toegang tot `Scene`, `LinearExtrusion`, `RectangleShape` en hulpprogramma‑klassen zoals `Vector3`.

## Lineaire extrusie uitvoeren

Hieronder staat de volledige workflow. Elke stap wordt in gewone taal uitgelegd vóór het bijbehorende code‑blok, zodat je kunt volgen zonder te raden wat de code doet.

### Stap 1: Initialiseer het basisprofiel

Eerst maak je de 2‑D‑vorm die geëxtrudeerd zal worden. In dit voorbeeld gebruiken we een rechthoek met een kleine afrondingsradius.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Waarom dit belangrijk is:* Het profiel bepaalt de doorsnede van het uiteindelijke 3‑D‑object. Pas `RoundingRadius`, breedte of hoogte aan om verschillende silhouetten te krijgen.

### Stap 2: Pas Linear Extrusion toe

Nu vegen we het profiel 10 eenheden langs de Z‑as, voegen we 100 slices toe voor gladheid, centreren we de geometrie en passen we een volledige 360°‑twist met een offset toe.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro tip:* Speel met `Slices` om performance versus visuele kwaliteit in balans te brengen, en experimenteer met `Twist` voor spiraaleffecten.

### Stap 3: Maak een Scene

Een `Scene` fungeert als de container voor alle 3‑D‑entiteiten – zie het als het canvas.

```csharp
Scene scene = new Scene();
```

### Stap 4: Voeg de extrusie toe aan de Scene

Koppel de geëxtrudeerde geometrie aan de root‑node van de scene zodat deze deel wordt van de renderbare hiërarchie.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Stap 5: Sla het 3‑D‑model op

Tot slot exporteer je de scene naar een breed ondersteund OBJ‑bestand. Dit demonstreert de **export 3d model obj**‑functionaliteit van Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Wanneer je het resulterende `LinearExtrusion.obj` opent in een 3‑D‑viewer, zie je een gedraaide rechthoekige prisma – precies wat de code beschrijft.

## Veelvoorkomende valkuilen & tips

| Probleem | Waarom het gebeurt | Hoe op te lossen |
|----------|--------------------|------------------|
| **Profile not visible** | Vergeten de extrusie aan de scene toe te voegen. | Zorg dat `CreateChildNode` wordt aangeroepen. |
| **Twist looks flat** | `Slices` te laag, waardoor ruwe geometrie ontstaat. | Verhoog `Slices` (bijv. 200) voor een soepelere twist. |
| **Export fails** | Uitvoermap bestaat niet of er ontbreekt schrijfrechten. | Gebruik `RunExamples.GetOutputFilePath` of maak de map handmatig aan. |
| **Unexpected scaling** | `Center` ingesteld op `false` verschuift de geometrie. | Stel `Center = true` tenzij je een offset nodig hebt. |

## Veelgestelde vragen

### Q1: Is Aspose.3D geschikt voor beginners?

**A1:** Absoluut! Aspose.3D biedt een gebruiksvriendelijke API, en deze tutorial leidt je stap‑voor‑stap door de basis van lineaire extrusie.

### Q2: Kan ik Aspose.3D gebruiken voor commerciële projecten?

**A2:** Ja, Aspose.3D heeft licentie‑opties voor zowel persoonlijk als commercieel gebruik. Bekijk [here](https://purchase.aspose.com/buy) voor details.

### Q3: Hoe kan ik tijdelijke licenties krijgen voor testen?

**A3:** Bezoek [this link](https://purchase.aspose.com/temporary-license/) om tijdelijke licenties voor testdoeleinden te verkrijgen.

### Q4: Waar vind ik community‑ondersteuning?

**A4:** Word lid van het [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) om contact te maken met een levendige community en hulp te zoeken.

### Q5: Is er een gratis proefversie beschikbaar?

**A5:** Zeker! Download de gratis proefversie [here](https://releases.aspose.com/) om de mogelijkheden van Aspose.3D zelf te ervaren.

---

**Laatst bijgewerkt:** 2026-01-07  
**Getest met:** Aspose.3D 24.11 for .NET  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## DOELKEYWORDS:

**Primaire sleutelwoord (HOGE PRIORITEIT):**
how to linear extrude

**Secundaire sleutelwoorden (ONDERSTEUNEND):**
export 3d model obj, linear extrusion tutorial

**Strategie voor sleutelwoordintegratie:**
1. Primaire sleutelwoord: Gebruik 3‑5 keer (titel, meta, eerste alinea, H2‑kop, body)  
2. Secundaire sleutelwoorden: Gebruik 1‑2 keer elk (koppen, body‑tekst)  
3. Alle sleutelwoorden moeten natuurlijk geïntegreerd worden – prioriteit aan leesbaarheid boven aantal  
4. Als een sleutelwoord niet natuurlijk past, gebruik een semantische variant of sla het over