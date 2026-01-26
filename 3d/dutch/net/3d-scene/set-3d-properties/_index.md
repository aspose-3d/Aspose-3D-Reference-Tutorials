---
date: 2026-01-17
description: Leer hoe u materiaaleigenschappen kunt opsommen, de diffuse kleur kunt
  wijzigen en 3D-materiaaleigenschappen kunt aanpassen met Aspose.3D voor .NET. Stapsgewijze
  codevoorbeelden inbegrepen.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Materialeigenschappen opsommen in 3D‑scènes met Aspose.3D
url: /nl/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Materialeigenschappen opsommen in 3D‑scènes met Aspose.3D

## Introductie

Als je **materialeigenschappen** van een 3D‑model wilt **opsommen** en vervolgens zaken zoals de diffuse kleur wilt aanpassen, ben je hier op het juiste adres. Aspose.3D voor .NET biedt een nette, object‑georiënteerde API waarmee je materiaal‑attributen kunt inspecteren, ophalen en wijzigen zonder je C#‑code te verlaten. In deze tutorial lopen we door het laden van een scène, het enumereren van de materialeigenschappen en het wijzigen van waarden zoals de diffuse component—zodat je je modellen precies het gewenste uiterlijk kunt geven.

## Snelle antwoorden
- **Wat is het primaire doel?** Materialeigenschappen opsommen en wijzigen (bijv. diffuse kleur).  
- **Welke bibliotheek is vereist?** Aspose.3D voor .NET.  
- **Heb ik een licentie nodig?** Een tijdelijke of volledige licentie is vereist voor productiegebruik.  
- **Ondersteunde bestandsformaten?** FBX, OBJ, STL, STL‑ASCII, 3MF en meer.  
- **Typische implementatietijd?** Ongeveer 10‑15 minuten voor een basis‑script dat eigenschappen opsomt.

## Wat betekent **materialeigenschappen opsommen**?
Materialeigenschappen opsommen houdt in dat je over de `PropertyCollection` van een materiaal itereert om elke eigenschapsnaam en de huidige waarde te lezen. Dit is nuttig voor debugging, visuele inspectie of het bouwen van UI‑besturingselementen waarmee gebruikers materiaalinstellingen tijdens runtime kunnen aanpassen.

## Waarom Aspose.3D gebruiken om **materialeigenschappen te benaderen**?
- **Geen externe converters** – werk direct met native .NET‑objecten.  
- **Rijk eigenschapsmodel** – ondersteunt aangepaste FBX‑specifieke attributen naast standaard PBR‑waarden.  
- **Cross‑platform** – werkt op .NET Framework, .NET Core en .NET 5/6+.  

## Voorvereisten

- Aspose.3D voor .NET geïnstalleerd in je project. Download het [hier](https://releases.aspose.com/3d/net/).
- Een map op schijf om je 3‑D‑bronbestanden te bewaren (bijv. een FBX‑bestand met ingebedde textures).

Nu je de basis op orde hebt, duiken we in de code.

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

## Stap 1: 3D‑scène laden

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

## Stap 3: **Materialeigenschappen opsommen** – zie elk naam/waarde‑paar

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

## Stap 5: **Eigenschap ophalen op naam** – krijg een sterk getypeerd exemplaar

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Stap 6: Een eigenschap’s eigen eigenschappen doorlopen (geavanceerd)

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

## Hoe **3D‑materiaalkleur wijzigen** voorbij diffuse
Als je speculaire, ambient‑ of emissieve kleuren wilt beïnvloeden, vervang je simpelweg `"Diffuse"` door `"Specular"` of `"Ambient"` in de `props["..."]`‑toewijzing hierboven. Dezelfde `Vector3`‑ of `Vector4`‑structuren zijn van toepassing.

## Veelvoorkomende valkuilen & tips
- **Hoofdlettergevoeligheid van eigenschapsnamen** – Aspose.3D‑eigenschapssleutels zijn hoofdlettergevoelig; gebruik exact de naam die in de opsomming wordt getoond.  
- **Ontbrekende eigenschap** – Niet alle materialen exposen elke PBR‑attribuut. Controleer `props.ContainsKey("Specular")` voordat je er toegang toe krijgt.  
- **Wijzigingen opslaan** – Na het aanpassen van eigenschappen, roep `scene.Save("output.fbx");` aan om de wijzigingen te bewaren.

## Conclusie

Je hebt nu geleerd hoe je **materialeigenschappen kunt opsommen**, **een eigenschap op naam kunt ophalen** en **de diffuse kleur kunt wijzigen** (of een andere materiaaleigenschap) met Aspose.3D voor .NET. Experimenteer met verschillende eigenschapstypen om het uiterlijk van je 3‑D‑assets fijn af te stemmen.

## FAQ's

### Q1: Kan ik Aspose.3D voor .NET gebruiken met andere 3D‑bestandsformaten?

A1: Ja, Aspose.3D ondersteunt diverse 3D‑bestandsformaten, waaronder FBX, STL en nog veel meer.

### Q2: Hoe kan ik een tijdelijke licentie voor Aspose.3D voor .NET verkrijgen?

A2: Bezoek [hier](https://purchase.aspose.com/temporary-license/) om een tijdelijke licentie te verkrijgen.

### Q3: Is er een community‑forum voor Aspose.3D‑gebruikers?

A3: Ja, je kunt ondersteuning en discussies vinden op het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18).

### Q4: Waar vind ik uitgebreide documentatie voor Aspose.3D voor .NET?

A4: Raadpleeg de [documentatie](https://reference.aspose.com/3d/net/) voor uitgebreide richtlijnen.

### Q5: Kan ik Aspose.3D voor .NET gratis uitproberen vóór aankoop?

A5: Zeker! Download de [gratis proefversie](https://releases.aspose.com/) om de functionaliteit te verkennen.

## Veelgestelde vragen

**Q: Wat stelt `Vector3(1, 0, 1)` voor?**  
A: Het zet de diffuse kleur op magenta (rood = 1, groen = 0, blauw = 1) in lineaire kleurruimte.

**Q: Moet ik `scene.Save` aanroepen na het wijzigen van eigenschappen?**  
A: Ja, het opslaan van de scène schrijft je aanpassingen naar schijf; anders blijven de wijzigingen alleen in het geheugen.

**Q: Kan ik aangepaste FBX‑attributen enumereren?**  
A: Absoluut. De `PropertyCollection` bevat alle aangepaste attributen, die je kunt benaderen via `GetProperty("customName")`.

**Q: Is er een manier om meerdere materialen in één keer bij te werken?**  
A: Loop door `scene.RootNode.ChildNodes` en herhaal de stappen voor eigenschapsaanpassing voor elk materiaal.

**Q: Ondersteunt Aspose.3D .NET 6?**  
A: Ja, de bibliotheek is volledig compatibel met .NET 6 en later.

---

**Laatst bijgewerkt:** 2026-01-17  
**Getest met:** Aspose.3D 24.11 voor .NET  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}