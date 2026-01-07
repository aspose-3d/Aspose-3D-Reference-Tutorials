---
date: 2026-01-07
description: Lär dig hur du lägger till ett markplan när du utför linjär extrusion
  med Aspose.3D för .NET och exporterar Wavefront OBJ‑filer. Bemästra centrering och
  förankringstekniker i 3‑D‑modellering.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Lägg till markplan och centrum i linjär extrudering
url: /sv/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lägg till markplan och centrering i linjär extrusion

## Introduktion

Välkommen till denna omfattande guide för att bemästra linjär extrusion med Aspose.3D för .NET. Om du vill **lägga till markplan** till dina modeller och **exportera Wavefront OBJ**‑filer samtidigt som extrusionen hålls centrerad, är du på rätt plats. I den här handledningen går vi igenom tekniken för linjär extrusion, med särskilt fokus på centrering och hur ett markplan hjälper dig att visualisera resultatet tydligare.

## Snabba svar
- **Vad innebär “add ground plane”?** Det ger en visuell referens som gör det enkelt att se var extrusionen sitter på X‑Z‑planet.  
- **Vilket format används för att exportera modellen?** Scenen sparas som en Wavefront OBJ‑fil (`FileFormat.WavefrontOBJ`).  
- **Behöver jag en licens för att köra koden?** En gratis provversion fungerar för utveckling; en permanent licens krävs för produktion.  
- **Kan jag ändra extrusionens längd?** Ja – ändra den andra parametern i `LinearExtrusion`.  
- **Är centrering valfri?** Att sätta `Center = true` centrerar extrusionen kring profilen; `false` justerar den till ena sidan.

## Förutsättningar

Innan vi påbörjar denna spännande resa, se till att du har följande förutsättningar på plats:

- Grundläggande förståelse för programmeringsspråket C#.  
- Visual Studio installerat på din maskin.  
- Aspose.3D för .NET‑biblioteket, som du kan ladda ner från den [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Se till att du har åtkomst till den [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) för referens under hela handledningen.

## Importera namnrymder

För att komma igång, låt oss importera de nödvändiga namnrymderna. Dessa kommer att lägga grunden för vårt 3D‑modellering mästerverk.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Steg 1: Initiera basprofilen

Vi börjar med att definiera en rektangulär profil som ska extruderas. `RoundingRadius` lägger till en subtil avrundning på hörnen.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Steg 2: Skapa en 3D‑scen

Ett `Scene`‑objekt fungerar som behållare för all geometri, ljus och kameror.

```csharp
Scene scene = new Scene();
```

## Steg 3: Skapa vänstra och högra noder

Två syskon‑noder skapas under roten. En kommer att demonstrera extrusion **utan** centrering, den andra **med** centrering. Vi flyttar också den vänstra noden så att de två exemplen inte överlappar.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Steg 4: Utför linjär extrusion på vänster nod (utan centrering)

Här extruderar vi profilen utan centrering. Observera flaggan `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Steg 5: Lägg till markplan för referens (vänster nod)

Att lägga till en tunn låda fungerar som ett **markplan** så att du tydligt kan se hur extrusionen sitter på basen.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Steg 6: Utför linjär extrusion på högre nod (med centrering)

Nu extruderar vi samma profil men aktiverar centrering. Geometrin kommer att placeras symmetriskt runt profilens ursprung.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Steg 7: Lägg till markplan för referens (högre nod)

Ett andra markplan läggs till i den högra noden för att hålla den visuella jämförelsen konsekvent.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Steg 8: Exportera Wavefront OBJ‑fil

Slutligen **exporterar vi Wavefront OBJ** så att resultatet kan öppnas i någon standard 3‑D‑visare.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Varför lägga till ett markplan?

Att lägga till ett markplan ger dig en omedelbar visuell ledtråd om extrusionens höjd och justering. Det är särskilt användbart när du behöver jämföra centrerade vs. icke‑centrerade resultat, som demonstreras i den här handledningen.

## Vanliga problem & tips

- **Markplanet syns inte:** Se till att planens tjocklek (`0.01` i `Box`‑konstruktorn) är tillräckligt liten för att inte dölja extrusionen men tillräckligt stor för att renderas.  
- **Export misslyckas:** Verifiera att målkatalogen finns och att du har skrivbehörighet.  
- **Centrerad extrusion verkar förskjuten:** Dubbelkolla `Center`‑egenskapen; `true` centrerar profilen, `false` justerar den till ena sidan.

## Vanliga frågor

### Q1: Kan jag använda Aspose.3D för .NET med andra programmeringsspråk?

A1: Aspose.3D stödjer främst .NET‑språk som C# och VB.NET.

### Q2: Var kan jag hitta support för frågor relaterade till Aspose.3D?

A2: Besök [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) för dedikerad support och diskussioner.

### Q3: Finns det en gratis provversion för Aspose.3D för .NET?

A3: Ja, du kan komma åt den gratis provversionen [här](https://releases.aspose.com/).

### Q4: Hur kan jag skaffa en tillfällig licens för Aspose.3D för .NET?

A4: Du kan skaffa en tillfällig licens [här](https://purchase.aspose.com/temporary-license/).

### Q5: Var kan jag köpa licensen för Aspose.3D för .NET?

A5: Köp din licens [här](https://purchase.aspose.com/buy).

### Q6: Kan jag exportera scenen till andra format än OBJ?

A6: Ja, Aspose.3D stödjer många format som STL, FBX och GLTF. Ändra helt enkelt `FileFormat`‑enum‑värdet i `Save`‑metoden.

### Q7: Hur ändrar jag antalet skivor i extrusionen?

A7: Justera `Slices`‑egenskapen i `LinearExtrusion`‑konstruktorn för att kontrollera mesh‑densiteten.

---

**Senast uppdaterad:** 2026-01-07  
**Testad med:** Aspose.3D for .NET latest version  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}