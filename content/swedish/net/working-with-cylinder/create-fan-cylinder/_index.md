---
title: Skapar fläktcylinder
linktitle: Skapar fläktcylinder
second_title: Aspose.3D .NET API
description: Lås upp en värld av 3D-design med Aspose.3D för .NET! Skapa fantastiska fläkt- och icke-fläktcylindrar utan ansträngning. Ladda ner din testversion nu.
type: docs
weight: 10
url: /sv/net/working-with-cylinder/create-fan-cylinder/
---
## Introduktion
Välkommen till en värld av 3D-modellering och visualisering med Aspose.3D för .NET! I den här steg-för-steg-guiden kommer vi att utforska hur man skapar en fängslande fläktcylinder med Aspose.3D för .NET. Aspose.3D är ett kraftfullt bibliotek som ger omfattande möjligheter för att arbeta med 3D-innehåll i .NET-applikationer.
## Förutsättningar
Innan vi dyker in i den spännande världen av 3D-modellering, se till att du har följande förutsättningar:
- En grundläggande förståelse för .NET-programmering.
- Visual Studio installerat på din dator.
-  Aspose.3D för .NET-bibliotek, som du kan ladda ner[här](https://releases.aspose.com/3d/net/).
- Ett genuint intresse av att släppa loss din kreativitet genom 3D-design.
## Importera namnområden
Låt oss kicka igång genom att importera de nödvändiga namnrymden för att göra Aspose.3D-funktionalitet tillgänglig i ditt .NET-projekt.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importera Aspose.3D-namnrymder
```
Nu när vi alla är klara, låt oss dela upp processen för att skapa en fläktcylinder i hanterbara steg.
## Steg 1: Skapa en scen
```csharp
// Skapa en scen
Scene scene = new Scene();
```
Börja med att initiera en ny 3D-scen. Detta fungerar som duken där vår fläktcylinder kommer till liv.
## Steg 2: Skapa en fläktcylinder
```csharp
// Skapa en cylinder
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Definiera egenskaperna för din fläktcylinder, ange parametrar som radie, höjd och upplösning.
## Steg 3: Anpassa fläktcylinderegenskaper
```csharp
// Ställ in GenerateFanCylinder på sant
fan.GenerateFanCylinder = true;
// Ställ in ThetaLength
fan.ThetaLength = MathUtils.ToRadian(270);
```
Skräddarsy din fläktcylinder genom att aktivera genereringen av fläktdelen och justera vinkelsvepet med ThetaLength.
## Steg 4: Placera fläktcylindern i scenen
```csharp
// Skapa ChildNode
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Lägg till fläktcylindern som en barnnod till scenens rotnod och placera den i 3D-utrymmet.
## Steg 5: Skapa en icke-fläktcylinder
```csharp
// Skapa en cylinder utan fläkt
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Utforska flexibiliteten hos Aspose.3D genom att skapa en cylinder utan fläktdelen.
## Steg 6: Anpassa egenskaper för icke-fläktcylinder
```csharp
// Ställ in GenerateFanCylinder på false
nonfan.GenerateFanCylinder = false;
// Ställ in ThetaLength
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Särskilj den icke-fläktcylindern genom att inaktivera genereringen av fläktdelen.
## Steg 7: Placera icke-fläktcylindern i scenen
```csharp
// Skapa ChildNode
scene.RootNode.CreateChildNode(nonfan);
```
Lägg på liknande sätt till cylindern utan fläkt som en barnnod till scenens rotnod.
## Steg 8: Spara scenen
```csharp
// Spara scen
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Spara ditt mästerverk i önskat format och plats. Nu har du skapat en fläkt och en icke-fläktcylinder med Aspose.3D för .NET!
## Slutsats
Grattis till att du har slutfört den här praktiska guiden till 3D-modellering med Aspose.3D för .NET! Du har släppt lös din kreativitet i den digitala sfären och skapat fläkt- och icke-fläktcylindrar med lätthet.
## Vanliga frågor
### Kan jag använda Aspose.3D för .NET med andra .NET-ramverk?
Ja, Aspose.3D är kompatibel med olika .NET-ramverk, vilket ger mångsidighet i dina utvecklingsprojekt.
### Finns det en gratis testversion tillgänglig för Aspose.3D för .NET?
 Ja, du kan utforska en gratis provperiod[här](https://releases.aspose.com/).
### Var kan jag hitta detaljerad dokumentation för Aspose.3D för .NET?
 Dokumentationen finns tillgänglig[här](https://reference.aspose.com/3d/net/).
### Hur kan jag få support för Aspose.3D för .NET?
 Besök supportforumet[här](https://forum.aspose.com/c/3d/18) för hjälp från samhället och Aspose-experter.
### Finns tillfälliga licenser tillgängliga för Aspose.3D för .NET?
 Ja, tillfälliga licenser kan erhållas[här](https://purchase.aspose.com/temporary-license/).