---
title: Laden en opslaan - Aangepaste laadopties
linktitle: Laden en opslaan - Aangepaste laadopties
second_title: Aspose.3D .NET-API
description: Ontdek Aspose.3D voor .NET, de ultieme oplossing voor het naadloos laden en opslaan van 3D-modellen.
type: docs
weight: 15
url: /nl/net/loading-and-saving/custom-load-options/
---
## Invoering

Welkom in de wereld van Aspose.3D voor .NET – een krachtige bibliotheek waarmee ontwikkelaars naadloos met 3D-bestanden kunnen werken. In deze zelfstudie verdiepen we ons in de fijne kneepjes van het laden en opslaan van 3D-modellen, met de nadruk op aangepaste laadopties. Of u nu een doorgewinterde ontwikkelaar of een nieuwkomer bent, deze gids begeleidt u stap voor stap door het proces, zodat u het volledige potentieel van Aspose.3D voor .NET kunt benutten.

## Vereisten

Voordat we aan deze reis beginnen, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Zorg ervoor dat de bibliotheek is geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).

- Documentmap: maak een map om uw 3D-modelbestanden op te slaan.

Nu je de essentie hebt, gaan we duiken in de spannende wereld van 3D-modelmanipulatie!

## Naamruimten importeren

Laten we eerst de benodigde naamruimten importeren. Dit zal het toneel vormen voor onze reis naar het Aspose.3D-rijk.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Laden en opslaan - Aangepaste laadopties

### Stap 1: Discreet3DS-bestanden laden

```csharp
private static void Discreet3DSLoadOption()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Aangepaste opties instellen
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Stap 2: OBJ-bestanden laden

```csharp
private static void ObjLoadOption()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Aangepaste opties instellen
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Stap 3: STL-bestanden laden

```csharp
private static void STLLoadOption()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Aangepaste opties instellen
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Stap 4: U3D-bestanden laden

```csharp
private static void U3DLoadOption()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Aangepaste opties instellen
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });
}
```

### Stap 5: glTF-bestanden laden

```csharp
private static void glTFLoadOptions()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Aangepaste opties instellen
    loadOpt.FlipTexCoordV = true;
    scene.Open(dataDir + "Duck.gltf", loadOpt);
}
```

### Stap 6: PLY-bestanden laden

```csharp
private static void PlyLoadOptions()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Aangepaste opties instellen
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open(RunExamples.GetDataFilePath("vase-v2.ply"), loadPLYOpts);
}
```

### Stap 7: FBX-bestanden laden

```csharp
private static void FBXLoadOptions()
{
    // Het pad naar de documentenmap.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Aangepaste opties instellen
    scene.Open(dataDir + "test.FBX", opt);

    // Uitvoereigenschappen gedefinieerd in GlobalSettings in FBX-bestand
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusie

Gefeliciteerd! U heeft met succes door de ingewikkelde wereld van het laden en opslaan van 3D-modellen genavigeerd met Aspose.3D voor .NET. Deze tutorial behandelde verschillende bestandsformaten en hun aangepaste laadopties, waardoor u gemakkelijk 3D-middelen kunt manipuleren.

## Veelgestelde vragen

### Vraag 1: Is Aspose.3D voor .NET geschikt voor beginners?

A1: Absoluut! Aspose.3D voor .NET biedt een gebruiksvriendelijke interface, waardoor het toegankelijk is voor ontwikkelaars van alle niveaus.

### Vraag 2: Kan ik Aspose.3D gebruiken voor commerciële projecten?

A2: Ja, Aspose.3D voor .NET wordt geleverd met een commerciële licentie, zodat u het in uw projecten kunt gebruiken.

### Vraag 3: Zijn er beperkingen op de ondersteunde bestandsformaten?

 A3: Aspose.3D voor .NET ondersteunt een breed scala aan populaire 3D-bestandsindelingen, waaronder OBJ, STL, FBX en meer. Verwijs naar de[documentatie](https://reference.aspose.com/3d/net/) voor een uitgebreide lijst.

### Vraag 4: Is er een proefversie beschikbaar?

A4: Ja, u kunt de mogelijkheden van Aspose.3D voor .NET verkennen door het[gratis proefperiode](https://releases.aspose.com/).

### V5: Waar kan ik ondersteuning zoeken voor Aspose.3D voor .NET?

A5: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor steun en hulp van de gemeenschap.