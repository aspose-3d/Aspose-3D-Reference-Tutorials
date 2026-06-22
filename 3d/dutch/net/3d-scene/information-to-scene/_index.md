---
date: 2026-03-26
description: Leer hoe u leveranciersinformatie aan een 3D‑scene kunt toevoegen en
  hoe u FBX‑bestanden kunt opslaan met Aspose.3D voor .NET. Volg deze stapsgewijze
  handleiding met kant‑klaar code.
linktitle: Extracting Information to Scene Assets
second_title: Aspose.3D .NET API
title: Hoe vendorinformatie toe te voegen en een FBX‑scène op te slaan met Aspose.3D
url: /nl/net/3d-scene/information-to-scene/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe Vendor‑informatie toe te voegen en FBX‑scene op te slaan met Aspose.3D

## Inleiding

Welkom bij deze uitgebreide tutorial die **hoe vendor**‑details toe te voegen aan een 3D‑scene laat zien en vervolgens **hoe FBX**‑bestanden op te slaan met Aspose.3D voor .NET. Of je nu architecturale visualisaties, game‑assets of technische modellen bouwt, het embedden van vendor‑ en applicatiemetadata maakt je scenes informatie­rijker en makkelijker te beheren in latere stappen. Laten we stap voor stap door het proces lopen.

## Snelle antwoorden
- **Wat betekent “add vendor”?** Het slaat de applicatie‑ en vendornaam op in het AssetInfo‑blok van de scene.  
- **Welk formaat ondersteunt vendor‑informatie?** FBX (ASCII of binary) behoudt de metadata bij het opslaan.  
- **Hoe FBX opslaan?** Gebruik `scene.Save(path, FileFormat.FBX7500ASCII)` of het binaire equivalent.  
- **Heb ik een licentie nodig?** Een gratis trial werkt voor ontwikkeling; een commerciële licentie is vereist voor productie.  
- **Kan ik meeteenheden wijzigen?** Ja, stel `AssetInfo.UnitName` en `AssetInfo.UnitScaleFactor` in.

## Wat is “how to add vendor” in een 3D‑scene?
Vendor‑informatie toevoegen betekent dat je de `AssetInfo`‑eigenschappen van een `Scene`‑object vult. Deze eigenschappen reizen mee met het bestand, zodat elke consument van het FBX‑bestand kan zien welke applicatie het heeft gemaakt en wie de vendor is.

## Waarom vendor‑informatie toevoegen?
- **Traceerbaarheid:** Identificeer snel de bron van een model in grote pipelines.  
- **Naleving:** Sommige sectoren vereisen expliciete vendor‑tagging voor asset‑beheer.  
- **Automatisering:** Scripts kunnen bestanden filteren of verwerken op basis van vendor‑metadata.

## Voorvereisten

- Aspose.3D voor .NET geïnstalleerd. Je kunt het downloaden van de [Aspose.3D for .NET page](https://releases.aspose.com/3d/net/).

## Importeer namespaces

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
```

## Hoe vendor‑informatie toe te voegen

### Stap 1: Initialiseer een 3D‑scene

```csharp
Scene scene = new Scene();
```

Het maken van een nieuwe `Scene` geeft je een schoon canvas om mee te werken.

### Stap 2: Stel applicatie‑ en vendor‑informatie in

```csharp
scene.AssetInfo.ApplicationName = "Egypt";
scene.AssetInfo.ApplicationVendor = "Manualdesk";
```

Hier demonstreren we **hoe vendor**‑gegevens toe te voegen door betekenisvolle strings toe te wijzen aan `ApplicationName` en `ApplicationVendor`.

### Stap 3: Definieer meeteenheden

```csharp
scene.AssetInfo.UnitName = "pole";
scene.AssetInfo.UnitScaleFactor = 0.6;
```

Het specificeren van het eenheidssysteem zorgt ervoor dat iedereen die het FBX‑bestand opent de afmetingen correct interpreteert. In dit voorbeeld is één “pole” gelijk aan 60 cm.

## Hoe FBX‑scene op te slaan

### Stap 4: Sla de scene op (how to save fbx)

```csharp
var output = "Your Output Directory" + "InformationToScene.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Deze regel toont **how to save fbx** met de ASCII‑versie van FBX 7.5.0. Als je de binaire versie verkiest, vervang je `FBX7500ASCII` door `FBX7500Binary`.

> **Pro‑tip:** Houd de bestandsextensie `.fbx` consistent met het formaat dat je kiest; anders kunnen sommige viewers de inhoud verkeerd interpreteren.

### Stap 5: Toon succes‑bericht

```csharp
Console.WriteLine("\nAsset information added successfully to Scene.\nFile saved at " + output);
```

Een vriendelijk console‑bericht bevestigt dat de scene, compleet met vendor‑metadata, naar schijf is geschreven.

## Veelvoorkomende problemen en oplossingen

| Probleem | Oplossing |
|----------|-----------|
| **Vendor‑info verschijnt niet in viewer** | Zorg ervoor dat je het bestand hebt opgeslagen als **FBX ASCII** of **Binary**; sommige oudere viewers lezen slechts één formaat. |
| **Pad bevat spaties** | Plaats het pad tussen aanhalingstekens of gebruik `Path.Combine` om een veilig bestandspad te bouwen. |
| **Schaal van eenheid lijkt verkeerd** | Controleer `UnitScaleFactor`; het is een vermenigvuldiger ten opzichte van meters. |
| **Licentie‑exception** | Gebruik de gratis trial voor testen; verkrijg een volledige licentie voor productie‑builds. |

## Veelgestelde vragen

**Q: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?**  
A: Aspose.3D ondersteunt voornamelijk .NET‑talen, maar je kunt interoperabiliteitsopties voor andere talen verkennen.

**Q: Is er een gratis trial beschikbaar voor Aspose.3D voor .NET?**  
A: Ja, je kunt de gratis trial [hier](https://releases.aspose.com/) verkrijgen.

**Q: Hoe krijg ik ondersteuning voor Aspose.3D‑gerelateerde vragen?**  
A: Bezoek het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor community‑ondersteuning.

**Q: Kan ik een tijdelijke licentie aanschaffen voor Aspose.3D voor .NET?**  
A: Ja, je kunt een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/) verkrijgen.

**Q: Waar vind ik gedetailleerde documentatie voor Aspose.3D voor .NET?**  
A: Raadpleeg de [documentation](https://reference.aspose.com/3d/net/) voor uitgebreide informatie.

---

**Laatst bijgewerkt:** 2026-03-26  
**Getest met:** Aspose.3D 24.11 voor .NET  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}