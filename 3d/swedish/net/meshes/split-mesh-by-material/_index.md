---
title: Dela mesh efter material
linktitle: Dela mesh efter material
second_title: Aspose.3D .NET API
description: Lär dig att dela 3D-maskor efter material med Aspose.3D för .NET. Förbättra scenens organisation och effektivitet. Steg-för-steg-guide för utvecklare.
weight: 22
url: /sv/net/meshes/split-mesh-by-material/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Dela mesh efter material

## Introduktion
Välkommen till denna omfattande handledning om att dela ett nät efter material med Aspose.3D för .NET! Om du är en utvecklare som arbetar med 3D-grafik och vill hantera och manipulera mesh effektivt, är du på rätt plats. I den här guiden kommer vi att utforska processen att dela upp ett nät baserat på material, en avgörande uppgift för att skapa olika och visuellt tilltalande 3D-scener.
## Förutsättningar
Innan du dyker in i handledningen, se till att du har följande förutsättningar på plats:
-  Aspose.3D för .NET: Se till att du har Aspose.3D-biblioteket installerat i ditt .NET-projekt. Om inte kan du ladda ner den från[släpper](https://releases.aspose.com/3d/net/) sida.
- Grundläggande kunskap om 3D-grafik: Bekanta dig med grundläggande koncept för 3D-grafik för att förstå nyanserna av mesh-manipulation.
- Utvecklingsmiljö: Sätt upp en lämplig .NET-utvecklingsmiljö, som Visual Studio.
## Importera namnområden
Börja med att importera de nödvändiga namnområdena för att komma åt Aspose.3D-funktionaliteten. Inkludera följande i början av din kod:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
Låt oss nu dela upp exemplet i flera steg:
## Steg 1: Skapa ett Box Mesh
```csharp
// Skapa ett nät av en låda (som består av 6 plan)
Mesh box = (new Box()).ToMesh();
```
Här initierar vi ett nät som representerar en låda med sex plan med Aspose.3D.
## Steg 2: Lägg till material till nätet
```csharp
// Skapa ett materialelement på detta nät
VertexElementMaterial mat = (VertexElementMaterial)box.CreateElement(VertexElementType.Material, MappingMode.Polygon, ReferenceMode.Index);
// Ange olika materialindex för varje plan
mat.Indices.AddRange(new int[] { 0, 1, 2, 3, 4, 5 });
```
Detta steg innefattar att lägga till ett materialelement till nätet och tilldela distinkta materialindex till varje plan.
## Steg 3: Dela nätet efter material (CloneData Policy)
```csharp
// Dela upp det i 6 undermaskor, varje plan blir ett undernät
Mesh[] planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CloneData);
```
Här delar vi nätet i sex undernät baserat på de angivna materialen, med hjälp av CloneData-policyn.
## Steg 4: Uppdatera materialindex för kompakta data
```csharp
mat.Indices.Clear();
mat.Indices.AddRange(new int[] { 0, 0, 0, 1, 1, 1 });
```
Uppdatera materialindex för att förbereda för nästa uppdelning med CompactData-policyn.
## Steg 5: Dela nätet efter material (CompactData Policy)
```csharp
// Dela upp den i 2 undermaskor, som var och en innehåller specifika plan
planes = PolygonModifier.SplitMesh(box, SplitMeshPolicy.CompactData);
```
Nu delar vi nätet i två undernät, grupperar plan baserat på material och använder CompactData-policyn.
## Slutsats
Grattis! Du har framgångsrikt lärt dig hur man delar upp ett nät efter material med Aspose.3D för .NET. Denna teknik är viktig för att effektivt hantera komplexa 3D-scener.
## Vanliga frågor
### F: Kan jag tillämpa den här tekniken på anpassade maskor?
Absolut! Så länge ditt nät har definierat material kan du använda detta tillvägagångssätt.
### F: Hur skiljer sig CloneData-policyn från CompactData-policyn?
CloneData-policyn säkerställer att varje sub-mesh delar samma kontrollpunktsinformation, medan CompactData-policyn ger varje sub-mesh sin egen kontrollpunktsinformation.
### F: Finns det prestandaöverväganden när du använder den här metoden?
I allmänhet kan CloneData-policyn ha något bättre prestanda på grund av delad kontrollpunktsinformation.
### F: Kan jag visualisera resultatet av mesh-delning?
Ja, du kan rendera och visualisera de resulterande sub-maskorna med Aspose.3D-renderingsfunktioner.
### F: Är Aspose.3D lämplig för spelutveckling?
Även om Aspose.3D främst används för modellering och rendering, kan den integreras i spelutvecklingspipelines för specifika uppgifter.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
