---
date: 2026-01-07
description: Lär dig hur du linjärt extruderar en 2D‑profil och exporterar 3D‑modellen
  OBJ med Aspose.3D för .NET. Denna tutorial om linjär extrusion guidar dig steg för
  steg.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Hur man linjär extruderar med Aspose.3D för .NET
url: /sv/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man Linear Extrude med Aspose.3D för .NET

## Introduction

Välkommen till vår **linear extrusion tutorial**! I den här guiden kommer du att upptäcka **how to linear extrude** en 2‑D‑profil och förvandla den till ett fullt utvecklat 3‑D‑objekt med Aspose.3D för .NET. Oavsett om du bygger en CAD‑liknande applikation eller bara behöver **export 3d model obj**‑filer för vidare bearbetning, kommer den här steg‑för‑steg‑genomgången att ge dig förtroendet att lägga till kraftfull geometrisk skapande i dina projekt.

## Quick Answers
- **What is linear extrusion?** Att förlänga en 2‑D‑form längs en rak bana för att skapa ett 3‑D‑solid.  
- **Which library do we use?** Aspose.3D för .NET.  
- **Do I need a license?** En temporär licens fungerar för testning; en full licens krävs för produktion.  
- **Can I export to OBJ?** Ja – den slutgiltiga scenen sparas som en Wavefront OBJ‑fil.  
- **How many lines of code?** Under 30 rader C# plus förklarande kommentarer.

## What is Linear Extrusion?

Linear extrusion tar en platt profil (t.ex. en rektangel eller cirkel) och sveper den längs en rak linje, med möjlighet att lägga till vridningar, skalning eller förskjutningar. Resultatet blir ett solid som kan renderas, redigeras eller exporteras för användning i andra 3‑D‑verktyg.

## Why Use Aspose.3D for Linear Extrusion?

* **Zero‑dependency:** Ingen extern CAD‑kärna behövs.  
* **Full .NET support:** Fungerar med .NET Framework, .NET Core och .NET 5/6+.  
* **Export flexibility:** Spara direkt till OBJ, STL, FBX och många andra format.  
* **Rich API:** Styr skivor, vridning och förskjutningar med bara några få egenskaper.

## Prerequisites

Innan du börjar, se till att du har:

1. **Aspose.3D installed** – ladda ner det från [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – följ installationsguiden [here](https://reference.aspose.com/3d/net/).  
3. En .NET‑utvecklingsmiljö (Visual Studio, VS Code eller Rider) med de nödvändiga namnrymderna refererade.

## Import Namespaces

Inkludera de nödvändiga namnrymderna för att låsa upp Aspose.3D‑funktionaliteten:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Dessa namnrymder ger dig åtkomst till `Scene`, `LinearExtrusion`, `RectangleShape` och hjälparklasser som `Vector3`.

## Performing Linear Extrusion

Nedan är hela arbetsflödet. Varje steg förklaras i klartext innan motsvarande kodblock, så att du kan följa med utan att gissa vad koden gör.

### Step 1: Initialize the Base Profile

Först skapar du den 2‑D‑form som ska extruderas. I det här exemplet använder vi en rektangel med en liten avrundningsradie.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Varför detta är viktigt:* Profilen definierar tvärsnittet på det slutgiltiga 3‑D‑objektet. Justera `RoundingRadius`, bredd eller höjd för att få olika silhuetter.

### Step 2: Apply Linear Extrusion

Nu sveper vi profilen 10 enheter längs Z‑axeln, lägger till 100 skivor för jämnhet, centrerar geometrin och applicerar en full 360°‑vridning med ett förskjutningsvärde.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Proffstips:* Lek med `Slices` för att balansera prestanda mot visuell kvalitet, och experimentera med `Twist` för spiral‑effekter.

### Step 3: Create a Scene

Ett `Scene` fungerar som behållare för alla 3‑D‑entiteter – tänk på det som en målarduk.

```csharp
Scene scene = new Scene();
```

### Step 4: Add the Extrusion to the Scene

Fäst den extruderade geometrin på scenens rot‑nod så att den blir en del av den renderbara hierarkin.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Step 5: Save the 3‑D Model

Till sist exporterar du scenen till en allmänt stödd OBJ‑fil. Detta demonstrerar **export 3d model obj**‑kapaciteten i Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

När du öppnar den resulterande `LinearExtrusion.obj` i någon 3‑D‑visare kommer du att se ett vridet rektangulärt prisma – exakt vad koden beskriver.

## Common Pitfalls & Tips

| Problem | Varför det händer | Hur man åtgärdar |
|-------|----------------|------------|
| **Profile not visible** | Glömt att lägga till extrusionen i scenen. | Se till att `CreateChildNode` anropas. |
| **Twist looks flat** | `Slices` för lågt, vilket ger grov geometri. | Öka `Slices` (t.ex. 200) för en mjukare vridning. |
| **Export fails** | Utdatamappen finns inte eller saknar skrivbehörighet. | Använd `RunExamples.GetOutputFilePath` eller skapa katalogen manuellt. |
| **Unexpected scaling** | `Center` satt till `false` förskjuter geometrin. | Sätt `Center = true` om du inte behöver ett offset. |

## Frequently Asked Questions

### Q1: Is Aspose.3D suitable for beginners?

A1: Absolut! Aspose.3D erbjuder ett användarvänligt API, och den här tutorialen guidar dig genom grunderna i linear extrusion.

### Q2: Can I use Aspose.3D for commercial projects?

A2: Ja, Aspose.3D har licensalternativ för både personligt och kommersiellt bruk. Se [here](https://purchase.aspose.com/buy) för detaljer.

### Q3: How can I get temporary licenses for testing?

A3: Besök [this link](https://purchase.aspose.com/temporary-license/) för att skaffa temporära licenser för teständamål.

### Q4: Where can I find community support?

A4: Gå med i [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) för att ansluta till en livlig community och få hjälp.

### Q5: Is there a free trial available?

A5: Självklart! Ladda ner den kostnadsfria provversionen [here](https://releases.aspose.com/) för att uppleva Aspose.3D:s funktioner på egen hand.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D 24.11 för .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**
how to linear extrude

**Secondary Keywords (SUPPORTING):**
export 3d model obj, linear extrusion tutorial

**Keyword Integration Strategy:**
1. Primary keyword: Use 3-5 times (title, meta, first paragraph, H2 heading, body)
2. Secondary keywords: Use 1-2 times each (headings, body text)
3. All keywords must be integrated naturally - prioritize readability over keyword count
4. If a keyword doesn't fit naturally, use a semantic variation or skip it