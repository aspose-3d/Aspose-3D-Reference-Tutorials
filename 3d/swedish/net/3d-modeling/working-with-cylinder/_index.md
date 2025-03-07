---
title: Anpassad skjuvcylinder
linktitle: Anpassad skjuvcylinder
second_title: Aspose.3D .NET API
description: Lär dig att skapa skräddarsydda skjuvbottencylindrar med Aspose.3D för .NET med vår detaljerade steg-för-steg-guide. Lyft dina färdigheter i 3D-modellering idag!
weight: 12
url: /sv/net/3d-modeling/working-with-cylinder/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Anpassad skjuvcylinder

## Introduktion
Välkommen till vår omfattande guide för att skapa en anpassad cylinder med Aspose.3D för .NET. Om du vill förbättra dina färdigheter i 3D-modellering och lägga till unika funktioner till dina projekt, är du på rätt plats. I den här handledningen går vi igenom processen steg för steg, med hjälp av tydliga förklaringar och kodavsnitt.
## Förutsättningar
Innan vi dyker in i handledningen, se till att du har följande:
- Grundläggande förståelse för C# och .NET programmering.
-  Aspose.3D för .NET-biblioteket installerat. Du kan ladda ner den[här](https://releases.aspose.com/3d/net/).
- En utvecklingsmiljö inrättad för .NET-programmering.
## Importera namnområden
Börja med att importera de nödvändiga namnrymden i din C#-kod:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Steg 1: Skapa en scen
Börja med att skapa en 3D-scen med Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Steg 2: Skapa cylinder 1
Generera den första cylindern och ställ in dess egenskaper:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Steg 3: Anpassa skjuvbotten för cylinder 1
Applicera en anpassad klippbotten på den första cylindern:
```csharp
//Skjuvning 47,5 grader i xy-planet (z-axeln)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Ställ in GenerateFanCylinder på sant
cylinder1.GenerateFanCylinder = true;
// Ställ in ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Ställ in OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Steg 4: Lägg till Cylinder 1 till scenen
Lägg till den första cylindern till scenen och ställ in dess översättning:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Steg 5: Skapa Cylinder 2
Skapa en andra cylinder med liknande egenskaper:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Steg 6: Lägg till Cylinder 2 till scenen
Lägg till den andra cylindern till scenen utan anpassade parametrar:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Steg 7: Spara scenen
Spara scenen som en Wavefront OBJ-fil i din dokumentkatalog:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Slutsats
Grattis! Du har framgångsrikt skapat en anpassad skjuvbottencylinder med Aspose.3D för .NET. Denna handledning syftade till att tillhandahålla en steg-för-steg-guide för användare med olika nivåer av expertis inom 3D-modellering och programmering.
## Vanliga frågor
### Är Aspose.3D för .NET lämplig för nybörjare?
Absolut! Aspose.3D för .NET erbjuder ett användarvänligt gränssnitt, vilket gör det tillgängligt för både nybörjare och erfarna utvecklare.
### Kan jag använda olika klippvinklar på cylindrar?
Ja, du kan anpassa skjuvbotten för varje cylinder individuellt, vilket gör att du kan uppnå unika effekter.
### Finns det en testversion tillgänglig?
 Ja, du kan utforska den kostnadsfria testversionen[här](https://releases.aspose.com/).
### Var kan jag hitta ytterligare support?
 Besök[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) för samhällsstöd och diskussioner.
### Hur kan jag få en tillfällig licens?
 Skaffa din tillfälliga licens[här](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
