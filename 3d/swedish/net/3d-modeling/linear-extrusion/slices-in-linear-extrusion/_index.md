---
date: 2026-01-09
description: Lär dig hur du skapar en 3D-scen och sparar en 3D-modell med Aspose.3D
  för .NET, inklusive export av Wavefront OBJ och linjära extruderingsskivor.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Skapa 3D-scen med linjära extruderingsskivor
url: /sv/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Skapa 3D-scen med linjär extrudering i skivor

## Introduktion

Välkommen till världen av 3D-design med Aspose.3D för .NET! I den här handledningen kommer du att **create 3d scene** objekt, applicera linjär extrudering med anpassade skivantal och slutligen **save 3d model** som en Wavefront OBJ-fil. Oavsett om du bygger en snabb prototyp eller en produktionsklar visualisering, visar stegen nedan dig **how to use Aspose** för att generera högkvalitativ geometri direkt från C#.

## Snabba svar
- **What does “create 3d scene” mean?** Det betyder att bygga ett Scene‑objekt som innehåller alla 3D‑entiteter (meshes, lights, cameras).  
- **Which format is used for export?** Exemplet exporterar till **Wavefront OBJ** (`export wavefront obj`).  
- **How many slices can I set?** Du kan ange vilket heltal som helst; demonstrationen visar 2 och 10 skivor.  
- **Do I need a license?** En tillfällig eller fullständig licens krävs för produktionsanvändning.  
- **Can I run this on .NET Core?** Ja, Aspose.3D stödjer .NET Framework och .NET Core.

## Förutsättningar

Innan du dyker in i 3D-design med Aspose.3D, se till att du har följande förutsättningar:

- Aspose.3D for .NET Library: Se till att du har Aspose.3D‑biblioteket installerat. Du kan ladda ner det från [here](https://releases.aspose.com/3d/net/).

- Integrated Development Environment (IDE): Använd någon föredragen IDE som är kompatibel med .NET‑utveckling.

- Basic Understanding of C#: Bekanta dig med grunderna i programmeringsspråket C#.

- Desire to Explore 3D Design: Ett engagemang för att skapa visuellt imponerande 3D‑modeller!

## Importera namnrymder

För att påbörja din 3D‑designresa med Aspose.3D behöver du importera de nödvändiga namnrymderna. Detta säkerställer att din kod kan komma åt de erforderliga klasserna och funktionerna.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Så här skapar du 3d scene med linjär extrudering

Nedan går vi igenom varje steg som krävs för att bygga scenen, applicera extrudering och **save 3d model** som en OBJ‑fil. Förklaringarna är skrivna i en samtalston så att du enkelt kan följa med.

### Steg 1: Initiera basprofilen

Först definierar vi den 2‑D‑form som ska extruderas. I detta fall en rektangel med rundade hörn.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Steg 2: Skapa en 3D-scen

Ett `Scene`‑objekt är behållaren för all geometri, ljus och kameror – kärnan i **creating a 3d scene**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Steg 3: Skapa vänster- och högernoder

Vi lägger till två undernoder till scenroten. Den ena använder ett lågt skivantal, den andra ett högre, så att du kan se den visuella skillnaden.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Steg 4: Utför linjär extrudering på vänsternoden

Här extruderar vi rektangeln med **2 slices**. Färre skivor ger ett grövre utseende.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Steg 5: Utför linjär extrudering på högernoden

Nu extruderar vi samma profil men med **10 slices**, vilket ger en slätare yta.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Steg 6: Spara 3D-scen

Slutligen exporterar vi scenen till en Wavefront OBJ‑fil. Detta demonstrerar **how to save obj** och **export wavefront obj** med Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|---------|-------------------|--------|
| OBJ-filen verkar tom | Utdatavägen är felaktig eller saknar skrivbehörighet. | Verifiera att katalogen finns och att applikationen har skrivbehörighet. |
| Skivorna påverkar inte slätheten | `Slices`‑värdet är för lågt för geometrins storlek. | Öka antalet skivor eller justera profilens dimensioner. |
| Licensundantag | Kör utan en giltig licens i en icke‑testversion. | Applicera en tillfällig eller permanent licens med `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Vanliga frågor

**Q: Kan jag använda Aspose.3D för .NET med andra programmeringsspråk?**  
A: Aspose.3D är främst designat för .NET, men du kan utforska interoperabilitetsalternativ med språk som Python via .NET‑bindningar.

**Q: Var kan jag hitta detaljerad dokumentation för Aspose.3D för .NET?**  
A: Se dokumentationen [here](https://reference.aspose.com/3d/net/) för djupgående information om Aspose.3D:s funktioner och användning.

**Q: Finns det en gratis provversion av Aspose.3D för .NET?**  
A: Ja, du kan hämta din gratis provversion [here](https://releases.aspose.com/) för att utforska bibliotekets funktioner innan du köper.

**Q: Hur kan jag få teknisk support för Aspose.3D för .NET?**  
A: Besök Aspose.3D‑forumet [here](https://forum.aspose.com/c/3d/18) för att få hjälp och engagera dig i communityn.

**Q: Kan jag använda en tillfällig licens för Aspose.3D för .NET?**  
A: Ja, skaffa en tillfällig licens [here](https://purchase.aspose.com/temporary-license/) för utvärderingsändamål.

## Slutsats

Grattis! Du har framgångsrikt lärt dig hur man **create 3d scene**, applicerar linjär extrudering med anpassade skivantal och **save 3d model** som en Wavefront OBJ‑fil med Aspose.3D för .NET. Detta är bara början på din 3D‑designresa—känn dig fri att experimentera med olika profiler, skivvärden och exportformat för att låsa upp hela potentialen i **3d modeling c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-01-09  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose