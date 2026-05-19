---
date: 2026-03-28
description: Leer hoe u materiaaleigenschappen kunt weergeven, de diffuse kleur kunt
  wijzigen en 3D-materiaaleigenschappen kunt aanpassen met Aspose.3D voor .NET. Stapsgewijze
  codevoorbeelden inbegrepen.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Lijst materiaaleigenschappen in 3D‑scènes met Aspose.3D
url: /nl/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lijst materiaaleigenschappen in 3D‑scènes met Aspose.3D

## Introductie

Als je **materialeigenschappen weergeven** van een 3D‑model wilt en vervolgens zaken zoals de diffuse kleur wilt aanpassen, ben je hier op het juiste adres. Aspose.3D for .NET biedt een nette, object‑georiënteerde API waarmee je materiaal‑attributen kunt inspecteren, ophalen en wijzigen zonder je C#‑code te verlaten. In deze tutorial lopen we door het laden van een scene, het enumereren van de materiaaleigenschappen en het wijzigen van waarden zoals de diffuse component—zodat je je modellen precies het gewenste uiterlijk kunt geven.

## Snelle antwoorden
- **Wat is het primaire doel?** Materialeigenschappen weergeven en aanpassen (bijv. diffuse kleur).  
- **Welke bibliotheek is vereist?** Aspose.3D for .NET.  
- **Heb ik een licentie nodig?** Een tijdelijke of volledige licentie is vereist voor productiegebruik.  
- **Ondersteunde bestandsformaten?** FBX, OBJ, STL, STL‑ASCII, 3MF, en meer.  
- **Typische implementatietijd?** Ongeveer 10‑15 minuten voor een basis script dat eigenschappen weergeeft.

## Wat is **materialeigenschappen weergeven**?
Materialeigenschappen weergeven betekent itereren over de `PropertyCollection` van een materiaal om elke eigenschapsnaam en de huidige waarde te lezen. Dit is nuttig voor debugging, visuele inspectie, of het bouwen van UI‑besturingselementen die gebruikers in staat stellen materiaaleigenschappen tijdens runtime aan te passen.

## Waarom Aspose.3D gebruiken om **materialeigenschappen te benaderen**?
- **Geen externe converters** – werk direct met native .NET‑objecten.  
- **Rijk eigenschapsmodel** – ondersteunt aangepaste FBX‑specifieke attributen naast standaard PBR‑waarden.  
- **Cross‑platform** – werkt op .NET Framework, .NET Core, en .NET 5/6+.  

## Voorvereisten

- Aspose.3D for .NET geïnstalleerd in je project. Download het [hier](https://releases.aspose.com/3d/net/).
- Een map op schijf om je 3‑D‑bronbestanden op te slaan (bijv. een FBX‑bestand met ingebedde textures).

Nu je de basis hebt geregeld, duiken we in de code.

## Namespaces importeren

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Stap 1: 3D‑scene laden

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Stap 2: **Materialeigenschappen benaderen** van de eerste node

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Stap 3: **Materialeigenschappen weergeven** – zie elk naam/waarde‑paar

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Stap 4: **Hoe diffuse aanpassen** – wijzig de Diffuse‑eigenschap

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Stap 5: **Eigenschap ophalen op naam** – verkrijg een sterk getypeerde instantie

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Stap 6: Doorloop de eigen eigenschappen van een eigenschap (geavanceerd)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Hoe **3D‑materiaalkleur wijzigen** naast diffuse
Als je speculaire, omgevings‑ of emissieve kleuren wilt beïnvloeden, vervang dan simpelweg `"Diffuse"` door `"Specular"` of `"Ambient"` in de `props["..."]`‑toewijzing hierboven. Dezelfde `Vector3`‑ of `Vector4`‑structuren zijn van toepassing.

## Hoe **materiaalkleur bijwerken in C#**
Het wijzigen van het visuele uiterlijk van een materiaal komt neer op het bijwerken van de juiste eigenschap in de `PropertyCollection`. Of je nu de diffuse, speculaire of een aangepaste kleureigenschap wilt aanpassen, het patroon blijft hetzelfde:

1. Haal de eigenschap op via de exacte naam (hoofdlettergevoelig).  
2. Wijs een nieuwe `Vector3` (RGB) of `Vector4` (RGBA) waarde toe.  

Omdat de API direct met C#‑objecten werkt, kun je **materiaalkleur C#** code bijwerken zonder tussenliggende bestanden of converters. Dit maakt het perfect voor realtime‑editors of batch‑verwerkings‑pipelines.

## Veelvoorkomende valkuilen & tips
- **Hoofdlettergevoeligheid van eigenschapsnamen** – Aspose.3D‑eigenschapssleutels zijn hoofdlettergevoelig; gebruik de exacte naam die in de lijstoutput wordt getoond.  
- **Ontbrekende eigenschap** – Niet alle materialen exposen elke PBR‑attribuut. Controleer `props.ContainsKey("Specular")` voordat je deze benadert.  
- **Wijzigingen opslaan** – Na het aanpassen van eigenschappen, roep `scene.Save("output.fbx");` aan om de wijzigingen op te slaan.

## Conclusie

Je hebt nu geleerd hoe je **materialeigenschappen kunt weergeven**, **een eigenschap kunt ophalen op naam**, en **de diffuse kleur kunt wijzigen** (of een andere materiaaleigenschap) met Aspose.3D for .NET. Experimenteer met verschillende eigenschapstypen om het uiterlijk van je 3‑D‑assets nauwkeurig af te stemmen, en onthoud dat je **materiaalkleur C#** kunt bijwerken met slechts één regel code.

## Veelgestelde vragen

### Q1: Kan ik Aspose.3D for .NET gebruiken met andere 3D‑bestandformaten?

A1: Ja, Aspose.3D ondersteunt verschillende 3D‑bestandformaten, waaronder FBX, STL en nog veel meer.

### Q2: Hoe kan ik een tijdelijke licentie voor Aspose.3D for .NET verkrijgen?

A2: Bezoek [hier](https://purchase.aspose.com/temporary-license/) om een tijdelijke licentie te verkrijgen.

### Q3: Is er een community‑forum voor Aspose.3D‑gebruikers?

A3: Ja, je kunt ondersteuning en discussies vinden op het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18).

### Q4: Waar kan ik gedetailleerde documentatie voor Aspose.3D for .NET vinden?

A4: Raadpleeg de [documentatie](https://reference.aspose.com/3d/net/) voor uitgebreide richtlijnen.

### Q5: Kan ik Aspose.3D for .NET gratis uitproberen voordat ik koop?

A5: Zeker! Download de [gratis proefversie](https://releases.aspose.com/) om de functies te verkennen.

## Veelgestelde vragen

**Q: Wat betekent `Vector3(1, 0, 1)`?**  
A: Het stelt de diffuse kleur in op magenta (rood = 1, groen = 0, blauw = 1) in lineaire kleurruimte.

**Q: Moet ik `scene.Save` aanroepen na het wijzigen van eigenschappen?**  
A: Ja, het opslaan van de scene schrijft je aanpassingen naar schijf; anders blijven de wijzigingen alleen in het geheugen.

**Q: Kan ik aangepaste FBX‑attributen opsommen?**  
A: Absoluut. De `PropertyCollection` bevat alle aangepaste attributen, die je kunt benaderen via `GetProperty("customName")`.

**Q: Is er een manier om meerdere materialen in batch bij te werken?**  
A: Loop door `scene.RootNode.ChildNodes` en herhaal de stappen voor eigenschap‑aanpassing voor elk materiaal.

**Q: Ondersteunt Aspose.3D .NET 6?**  
A: Ja, de bibliotheek is volledig compatibel met .NET 6 en later.

---

**Laatst bijgewerkt:** 2026-03-28  
**Getest met:** Aspose.3D 24.11 for .NET  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}