---
date: 2026-03-26
description: Lär dig hur du skapar en cylinder och exporterar en OBJ‑fil med Aspose.3D
  för .NET. Denna nybörjarvänliga guide täcker 3D‑sceninställning och OBJ‑export.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Hur man skapar en cylinder med sned botten – Aspose.3D för .NET
url: /sv/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man skapar en cylinder med shear bottom – Aspose.3D för .NET

## Introduktion
Om du undrar **hur man skapar cylinder**‑objekt med ett anpassat shear bottom i en .NET‑miljö, har du hamnat på rätt ställe. I den här handledningen går vi igenom varje steg—från att sätta upp en 3‑D‑scen till att exportera den färdiga modellen som en OBJ‑fil—så att du kan förbättra dina *nybörjarskickligheter i 3D‑modellering* med **Aspose.3D för .NET**.

## Snabba svar
- **Vilken är den primära klassen för att starta en 3D-modell?** `Scene` skapar rotbehållaren för all geometri.  
- **Vilken metod exporterar modellen till OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Behöver jag en licens för testning?** En gratis provversion finns — se provlänken i FAQ.  
- **Kan jag ändra shear‑vinkeln?** Ja, modifiera `ShearBottom` med ett `Vector2`‑värde.  
- **Är detta lämpligt för nybörjare?** Absolut; API:et abstraherar låg‑nivå mesh‑hantering.

## Vad är en 3D-scen?
En *3D‑scen* är en hierarkisk behållare som rymmer alla geometriska enheter, ljus, kameror och transformationer. I Aspose.3D erbjuder `Scene`‑klassen ett rent sätt att organisera och senare exportera dina modeller.

## Varför exportera till OBJ?
OBJ är ett allmänt stödjande, textbaserat format som många 3‑D‑applikationer (Blender, Maya, Unity) kan importera. Att exportera till OBJ låter dig dela eller vidareredigera dina cylinder‑modeller utanför .NET.

## Förutsättningar
Innan vi dyker ner, se till att du har:

- Grundläggande kunskaper i C# och .NET‑utveckling.  
- **Aspose.3D för .NET** installerat – du kan ladda ner det **[här](https://releases.aspose.com/3d/net/)**.  
- En .NET‑IDE (Visual Studio, Rider eller VS Code) redo för kodning.

## Importera namnrymder
Först, importera de nödvändiga namnrymderna så att API‑typerna känns igen.

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

## Steg 1: Skapa en 3D-scen
`Scene`‑objektet fungerar som roten i din modellhierarki.

```csharp
Scene scene = new Scene();
```

## Steg 2: Skapa Cylinder 1
Vi genererar den första cylindern med en radie på 2, höjd 10 och 20 radiala segment.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Steg 3: Anpassa shear bottom för Cylinder 1
Applicera en shear‑transformation, aktivera fan‑cylinder‑generering och justera andra egenskaper för att uppnå önskad form.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Steg 4: Lägg till Cylinder 1 i scenen
Placera den första cylindern på en lämplig plats med en translations‑transform.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Steg 5: Skapa Cylinder 2
En andra cylinder skapas med samma grunddimensioner men utan anpassad shear—perfekt för en jämförelse sida‑vid‑sida.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Steg 6: Lägg till Cylinder 2 i scenen
Vi bifogar helt enkelt den andra cylindern till scen‑grafen.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Steg 7: Exportera scenen som en OBJ‑fil
Till sist sparar vi hela scenen till en OBJ‑fil så att den kan öppnas i någon standard‑3D‑visare.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Vanliga problem och lösningar
| Problem | Varför det händer | Lösning |
|---------|-------------------|--------|
| **OBJ‑filen är tom** | Scenen har ingen geometri bifogad. | Se till att båda cylindrarna läggs till i `scene.RootNode`. |
| **Shear ser felaktig ut** | `ShearBottom` förväntar sig tangenten av vinkeln. | Använd `Math.Tan(angleInRadians)` eller det angivna `0.83` för ~47,5°. |
| **Fil‑sökvägsfel** | Ogiltig eller saknad katalog. | Använd `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Vanliga frågor
### Är Aspose.3D för .NET lämplig för nybörjare?
Absolut! Aspose.3D för .NET erbjuder ett hög‑nivå API som abstraherar de matematiskt tunga delarna av 3‑D‑modellering, vilket gör det tillgängligt för utvecklare på alla kunskapsnivåer.

### Kan jag applicera olika shear‑vinklar på cylindrar?
Ja, varje `Cylinder`‑instans har sin egen `ShearBottom`‑egenskap, så du kan tilldela en unik vinkel till varje objekt.

### Finns det en provversion tillgänglig?
Ja, du kan utforska den kostnadsfria provversionen **[här](https://releases.aspose.com/)**.

### Var kan jag hitta ytterligare support?
Besök **[Aspose.3D‑forumet](https://forum.aspose.com/c/3d/18)** för gemenskapsstöd, kodexempel och diskussioner.

### Hur kan jag skaffa en tillfällig licens?
Skaffa din tillfälliga licens **[här](https://purchase.aspose.com/temporary-license/)**.

**Ytterligare Q&A**

**Q: Hur exporterar jag modellen i ett annat format, som STL?**  
A: Byt ut `FileFormat.WavefrontOBJ` mot `FileFormat.STL` i anropet `scene.Save`.

**Q: Kan jag animera cylindrarna efter skapandet?**  
A: Ja, du kan lägga till nyckel‑ram‑animationer på nod‑transformer med hjälp av `Animation`‑klasserna som tillhandahålls av Aspose.3D.

**Q: Stöder API:et .NET Core?**  
A: Biblioteket är fullt kompatibelt med .NET Core, .NET 5+ och .NET 6+.

---

**Senast uppdaterad:** 2026-03-26  
**Testad med:** Aspose.3D för .NET (senaste release)  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}