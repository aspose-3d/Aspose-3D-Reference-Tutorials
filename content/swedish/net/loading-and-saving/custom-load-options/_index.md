---
title: Anpassade laddningsalternativ
linktitle: Anpassade laddningsalternativ
second_title: Aspose.3D .NET API
description: Utforska Aspose.3D för .NET, den ultimata lösningen för sömlös laddning och lagring av 3D-modeller.
type: docs
weight: 15
url: /sv/net/loading-and-saving/custom-load-options/
---
## Introduktion

Välkommen till världen av Aspose.3D för .NET – ett kraftfullt bibliotek som ger utvecklare möjlighet att arbeta sömlöst med 3D-filer. I den här handledningen kommer vi att fördjupa oss i krångligheterna med att ladda och spara 3D-modeller, med fokus på anpassade laddningsalternativ. Oavsett om du är en erfaren utvecklare eller en nykomling, kommer den här guiden att leda dig genom processen steg för steg, vilket säkerställer att du utnyttjar den fulla potentialen hos Aspose.3D för .NET.

## Förutsättningar

Innan vi ger oss ut på denna resa, se till att du har följande förutsättningar på plats:

-  Aspose.3D för .NET: Se till att du har biblioteket installerat. Du kan ladda ner den[här](https://releases.aspose.com/3d/net/).

- Dokumentkatalog: Skapa en katalog för att lagra dina 3D-modellfiler.

Nu när du har det väsentliga, låt oss dyka in i den spännande världen av manipulation av 3D-modeller!

## Importera namnområden

Till att börja med, låt oss importera de nödvändiga namnrymden. Detta kommer att sätta scenen för vår resa in i Aspose.3D-sfären.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Laddar och sparar - anpassade laddningsalternativ

### Steg 1: Laddar Discreet3DS-filer

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Ställ in anpassade alternativ
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Ladda filen med laddningsalternativen
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Steg 2: Laddar OBJ-filer

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Ställ in anpassade alternativ
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Ladda filen med laddningsalternativen
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Steg 3: Ladda STL-filer

```csharp
private static void STLLoadOption()
{
    // Sökvägen till dokumentkatalogen.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Ställ in anpassade alternativ
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Ladda filen med laddningsalternativen
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Steg 4: Ladda U3D-filer

```csharp
private static void U3DLoadOption()
{
    // Sökvägen till dokumentkatalogen.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Ställ in anpassade alternativ
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Ladda filen med laddningsalternativen
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Steg 5: Ladda glTF-filer

```csharp
private static void glTFLoadOptions()
{
    // Sökvägen till dokumentkatalogen.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Ställ in anpassade alternativ
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Steg 6: Laddar PLY-filer

```csharp
private static void PlyLoadOptions()
{
    // Sökvägen till dokumentkatalogen.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Ställ in anpassade alternativ
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Steg 7: Ladda FBX-filer

```csharp
private static void FBXLoadOptions()
{
    // Sökvägen till dokumentkatalogen.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Ställ in anpassade alternativ
    scene.Open("test.FBX", opt);

    // Utdataegenskaper definierade i GlobalSettings i FBX-fil
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Slutsats

Grattis! Du har framgångsrikt navigerat genom den intrikata världen av att ladda och spara 3D-modeller med Aspose.3D för .NET. Den här handledningen täckte olika filformat och deras anpassade laddningsalternativ, vilket ger dig möjlighet att manipulera 3D-tillgångar med lätthet.

## FAQ's

### F1: Är Aspose.3D för .NET lämplig för nybörjare?

A1: Absolut! Aspose.3D för .NET tillhandahåller ett användarvänligt gränssnitt, vilket gör det tillgängligt för utvecklare på alla nivåer.

### F2: Kan jag använda Aspose.3D för kommersiella projekt?

S2: Ja, Aspose.3D för .NET kommer med en kommersiell licens, vilket gör att du kan använda den i dina projekt.

### F3: Finns det några begränsningar för filformaten som stöds?

 S3: Aspose.3D för .NET stöder ett brett utbud av populära 3D-filformat, inklusive OBJ, STL, FBX och mer. Referera till[dokumentation](https://reference.aspose.com/3d/net/) för en omfattande lista.

### F4: Finns det en testversion tillgänglig?

S4: Ja, du kan utforska funktionerna i Aspose.3D för .NET genom att ladda ner[gratis provperiod](https://releases.aspose.com/).

### F5: Var kan jag söka support för Aspose.3D för .NET?

 A5: Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för samhällsstöd och hjälp.