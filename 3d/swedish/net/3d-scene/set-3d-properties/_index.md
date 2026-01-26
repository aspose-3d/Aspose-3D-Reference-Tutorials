---
date: 2026-01-17
description: Lär dig hur du listar materialegenskaper, ändrar diffus färg och modifierar
  3D‑materialattribut med Aspose.3D för .NET. Steg‑för‑steg‑kodexempel inkluderade.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Lista materialegenskaper i 3D‑scener med Aspose.3D
url: /sv/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lista materialegenskaper i 3D‑scener med Aspose.3D

## Introduktion

Om du behöver **lista materialegenskaper** för en 3D‑modell och sedan justera saker som diffusionsfärgen, är du på rätt plats. Aspose.3D för .NET ger dig ett rent, objekt‑orienterat API som låter dig inspektera, hämta och ändra materialattribut utan att lämna din C#‑kod. I den här handledningen går vi igenom hur du laddar en scen, enumererar dess materialegenskaper och ändrar värden såsom diffusionskomponenten—så att du kan ge dina modeller exakt det utseende du vill ha.

## Snabba svar
- **Vad är huvudmålet?** Lista materialegenskaper och ändra dem (t.ex. diffusionsfärg).  
- **Vilket bibliotek krävs?** Aspose.3D för .NET.  
- **Behöver jag en licens?** En tillfällig eller full licens krävs för produktionsbruk.  
- **Stödda filformat?** FBX, OBJ, STL, STL‑ASCII, 3MF och fler.  
- **Typisk implementeringstid?** Cirka 10‑15 minuter för ett grundläggande skript som listar egenskaper.

## Vad är **lista materialegenskaper**?
Att lista materialegenskaper innebär att iterera över ett materials `PropertyCollection` för att läsa varje egenskapsnamn och dess aktuella värde. Detta är användbart för felsökning, visuell inspektion eller för att bygga UI‑kontroller som låter användare justera materialinställningar i realtid.

## Varför använda Aspose.3D för att **åtkomma materialegenskaper**?
- **Ingen extern konverterare** – arbeta direkt med inbyggda .NET‑objekt.  
- **Rik egenskapsmodell** – stöder anpassade FBX‑specifika attribut utöver standard‑PBR‑värden.  
- **Plattformsoberoende** – fungerar på .NET Framework, .NET Core och .NET 5/6+.  

## Förutsättningar

- Aspose.3D för .NET installerat i ditt projekt. Ladda ner det [här](https://releases.aspose.com/3d/net/).
- En mapp på disken för att lagra dina 3‑D‑källfiler (t.ex. en FBX‑fil med inbäddade texturer).

Nu när du har grunderna på plats, låt oss dyka ner i koden.

## Importera namnrymder

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

## Steg 1: Ladda 3D‑scen

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Steg 2: **Åtkom materialegenskaper** för den första noden

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Steg 3: **Lista materialegenskaper** – se varje namn/värde‑par

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

## Steg 4: **Hur man ändrar diffuse** – modifiera Diffuse‑egenskapen

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Steg 5: **Hämta egenskap efter namn** – få en starkt‑typad instans

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Steg 6: Traversera en egenskaps egna egenskaper (avancerat)

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

## Hur man **ändrar 3D‑materialfärg** utöver diffuse
Om du behöver påverka spekulära, omgivande eller emissiva färger, ersätt helt enkelt `"Diffuse"` med `"Specular"` eller `"Ambient"` i `props["..."]`‑tilldelningen ovan. Samma `Vector3`‑ eller `Vector4`‑strukturer gäller.

## Vanliga fallgropar & tips
- **Skiftlägeskänslighet för egenskapsnamn** – Aspose.3D‑egenskapsnycklar är skiftlägeskänsliga; använd exakt det namn som visas i listutdata.  
- **Saknad egenskap** – Inte alla material exponerar varje PBR‑attribut. Kontrollera `props.ContainsKey("Specular")` innan du åtkommer.  
- **Spara ändringar** – Efter att ha modifierat egenskaper, anropa `scene.Save("output.fbx");` för att bestå ändringarna.

## Slutsats

Du har nu lärt dig hur man **listar materialegenskaper**, **hämtar en egenskap efter namn** och **ändrar diffusionsfärgen** (eller någon annan materialattribut) med Aspose.3D för .NET. Experimentera med olika egenskapstyper för att finjustera utseendet på dina 3‑D‑tillgångar.

## Vanliga frågor

### Q1: Kan jag använda Aspose.3D för .NET med andra 3D‑filformat?

A1: Ja, Aspose.3D stöder olika 3D‑filformat, inklusive FBX, STL och många fler.

### Q2: Hur kan jag skaffa en tillfällig licens för Aspose.3D för .NET?

A2: Besök [här](https://purchase.aspose.com/temporary-license/) för att skaffa en tillfällig licens.

### Q3: Finns det ett community‑forum för Aspose.3D‑användare?

A3: Ja, du kan hitta support och diskussioner på [Aspose.3D‑forumet](https://forum.aspose.com/c/3d/18).

### Q4: Var kan jag hitta detaljerad dokumentation för Aspose.3D för .NET?

A4: Se [dokumentationen](https://reference.aspose.com/3d/net/) för omfattande vägledning.

### Q5: Kan jag prova Aspose.3D för .NET gratis innan jag köper?

A5: Absolut! Ladda ner [gratis provversionen](https://releases.aspose.com/) för att utforska funktionerna.

## Vanligt förekommande frågor

**Q: Vad representerar `Vector3(1, 0, 1)`?**  
A: Den sätter diffusionsfärgen till magenta (röd = 1, grön = 0, blå = 1) i linjärt färgrymd.

**Q: Behöver jag anropa `scene.Save` efter att ha ändrat egenskaper?**  
A: Ja, att spara scenen skriver dina ändringar till disk; annars förblir förändringarna bara i minnet.

**Q: Kan jag enumerera anpassade FBX‑attribut?**  
A: Absolut. `PropertyCollection` kommer att inkludera alla anpassade attribut, som du kan komma åt via `GetProperty("customName")`.

**Q: Finns det ett sätt att batch‑uppdatera flera material?**  
A: Loopa igenom `scene.RootNode.ChildNodes` och upprepa stegen för egenskapsmodifiering för varje material.

**Q: Stöder Aspose.3D .NET 6?**  
A: Ja, biblioteket är fullt kompatibelt med .NET 6 och senare.

**Senast uppdaterad:** 2026-01-17  
**Testat med:** Aspose.3D 24.11 för .NET  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}