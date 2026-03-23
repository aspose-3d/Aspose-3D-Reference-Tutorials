---
date: 2026-03-23
description: Leer hoe je lineaire extrusie met slices uitvoert met Aspose.3D voor
  .NET. Maak gedetailleerde 3D-modellen met stap‑voor‑stap codevoorbeelden.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Hoe lineaire extrusie met slices uit te voeren met Aspose.3D voor .NET
url: /nl/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe lineaire extrusie met slices uit te voeren met Aspose.3D voor .NET

## Introductie

Welkom in de wereld van 3D-ontwerp met Aspose.3D voor .NET! In deze tutorial ontdek je **hoe lineaire extrusie** met slices werkt, een techniek waarmee je het detailniveau van je modellen kunt beheersen. Of je nu een ervaren ontwikkelaar bent of net begint, we leiden je stap voor stap, leggen het waarom achter elke handeling uit en geven je praktische tips die je meteen kunt toepassen.

## Snelle Antwoorden
- **Wat is lineaire extrusie met slices?** Het is een methode om een 2D-profiel uit te breiden naar 3D terwijl je opgeeft hoeveel tussenliggende doorsneden (slices) worden gegenereerd.  
- **Waarom slices gebruiken?** Meer slices geven een soepelere kromming; minder slices houden het mesh lichtgewicht.  
- **Vereisten?** Aspose.3D voor .NET, een .NET‑compatibele IDE en basiskennis van C#.  
- **Typische uitvoeringstijd?** Het voorbeeld draait in minder dan een seconde op een moderne pc.  
- **Uitvoerformaat?** Het voorbeeld slaat op als Wavefront OBJ, maar Aspose.3D ondersteunt vele formaten.

## Wat is lineaire extrusie met slices?

Lineaire extrusie neemt een 2‑D-vorm (een profiel) en strekt deze uit langs een rechte lijn om een 3‑D‑solid te creëren. De eigenschap **Slices** bepaalt hoeveel tussenliggende doorsneden tussen het begin en einde van de extrusie worden ingevoegd, wat invloed heeft op de gladheid en het aantal polygonen.

## Waarom slices gebruiken bij lineaire extrusie?

- **Mesh-dichtheid beheersen:** Fijn afstemmen van de balans tussen visuele kwaliteit en bestandsgrootte.  
- **Prestaties optimaliseren:** Gebruik minder slices voor realtime-toepassingen, meer voor renders met hoge resolutie.  
- **Creatieve flexibiliteit:** Combineer verschillende slice-aantallen op afzonderlijke objecten om het ontwerpintentie te benadrukken.

## Vereisten

Voordat je begint, zorg ervoor dat je het volgende hebt:

- Aspose.3D voor .NET Library – download deze van [hier](https://releases.aspose.com/3d/net/).  
- Een IDE die C# ondersteunt (Visual Studio, Rider, VS Code, enz.).  
- Basiskennis van C#-syntaxis en objectgeoriënteerde concepten.  
- Een nieuwsgierigheid om te experimenteren met 3‑D‑geometrie!

## Namespaces importeren

Importeer eerst de namespaces die je toegang geven tot de kernklassen van Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Stapsgewijze gids

### Stap 1: Initialiseert het basisprofiel

We beginnen met een eenvoudige rechthoekige vorm en geven deze een kleine afrondingsstraal zodat de randen niet perfect scherp zijn.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Stap 2: Maak een 3D‑scene

Een `Scene` fungeert als de container voor alle nodes, meshes, lichten en camera's.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Stap 3: Voeg linker- en rechternodes toe

We maken twee sibling‑nodes onder de root van de scene. De linkernode krijgt een laag slice‑aantal, de rechternode een hoog slice‑aantal, zodat je het visuele verschil kunt vergelijken.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Stap 4: Voer lineaire extrusie uit op de linkernode (lage detail)

Hier extruderen we de rechthoek met slechts **2 slices**. Dit levert een grof mesh op—ideaal voor snelle previews.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Stap 5: Voer lineaire extrusie uit op de rechternode (hoge detail)

Nu gebruiken we **10 slices** voor een veel gladder resultaat. Merk op hoe de geometrie fijner wordt.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Stap 6: Sla de 3D‑scene op

Schrijf tenslotte de scene naar een OBJ‑bestand. Vervang `"Your Output Directory"` door een geldig pad op jouw machine.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **Geen bestand aangemaakt** | Uitvoerpad is ongeldig of er ontbreken schrijfrechten. | Gebruik een absoluut pad en zorg ervoor dat de map bestaat. |
| **Object ziet er plat uit** | `Slices` ingesteld op 1 of 0. | Stel `Slices` in op minimaal 2 voor een zichtbare extrusie. |
| **Onverwachte geometrie** | Afrondingsstraal te groot voor de grootte van de rechthoek. | Pas `RoundingRadius` aan naar een waarde kleiner dan de helft van de kleinste zijde van de rechthoek. |

## Veelgestelde vragen

**Q: Kan ik de extrusierichting wijzigen?**  
A: Ja. Gebruik de `Transform`-eigenschap op de node om de geëxtrudeerde geometrie te roteren of te verplaatsen vóór het opslaan.

**Q: Ondersteunt Aspose.3D andere extrusietypen?**  
A: Absoluut. Naast `LinearExtrusion` kun je `RevolveExtrusion`, `SweepExtrusion` en meer gebruiken.

**Q: Naar welke bestandsformaten kan ik exporteren?**  
A: Aspose.3D ondersteunt OBJ, STL, FBX, 3MF, Collada en vele anderen. Verander gewoon de `FileFormat`‑enum.

**Q: Is er een manier om programmatically een materiaal in te stellen?**  
A: Ja. Na het maken van de node, wijs een `Material` toe aan de `Entity`‑collectie.

**Q: Hoe beïnvloedt het aantal slices het geheugenverbruik?**  
A: Meer slices verhogen het aantal vertices en faces, waardoor het geheugenverbruik evenredig stijgt. Gebruik profiling om de optimale balans voor jouw doelformaat te vinden.

## Originele FAQ's

### Q1: Kan ik Aspose.3D voor .NET gebruiken met andere programmeertalen?

A1: Aspose.3D is voornamelijk ontworpen voor .NET, maar je kunt interoperabiliteitsopties verkennen met talen zoals Python via .NET‑bindings.

### Q2: Waar kan ik gedetailleerde documentatie vinden voor Aspose.3D voor .NET?

A2: Raadpleeg de documentatie [hier](https://reference.aspose.com/3d/net/) voor diepgaande informatie over de mogelijkheden en het gebruik van Aspose.3D.

### Q3: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?

A3: Ja, je kunt je gratis proefversie [hier](https://releases.aspose.com/) downloaden om de functies van de bibliotheek te verkennen voordat je een aankoop doet.

### Q4: Hoe kan ik technische ondersteuning krijgen voor Aspose.3D voor .NET?

A4: Bezoek het Aspose.3D‑forum [hier](https://forum.aspose.com/c/3d/18) om hulp te zoeken en contact te maken met de community.

### Q5: Kan ik een tijdelijke licentie gebruiken voor Aspose.3D voor .NET?

A5: Ja, verkrijg een tijdelijke licentie [hier](https://purchase.aspose.com/temporary-license/) voor evaluatiedoeleinden.

## Conclusie

Je hebt nu gezien **hoe lineaire extrusie** met slices werkt met Aspose.3D voor .NET, de impact van verschillende slice‑aantallen onderzocht, en geleerd hoe je je werk kunt exporteren. Experimenteer met andere profielen, speel met de `Slices`‑waarde, en integreer materialen of verlichting om productie‑klare 3‑D‑assets te maken.

---

**Last Updated:** 2026-03-23  
**Tested With:** Aspose.3D 24.11 for .NET (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}