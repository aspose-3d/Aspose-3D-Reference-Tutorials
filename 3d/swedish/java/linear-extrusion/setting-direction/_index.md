---
date: 2025-12-18
description: Lär dig hur du skapar en 3D-scen och sparar en OBJ-fil med Aspose.3D
  för Java. Följ vår steg‑för‑steg‑guide för linjär extruderingsriktning.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Skapa 3D-scen – Ange extruderingsriktning Aspose.3D Java
url: /sv/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Skapa 3D-scen – Ställ in extruderingsriktning Aspose.3D Java

## Introduction

I den här handledningen kommer du att lära dig **hur man skapar 3d-scen**-objekt och kontrollera extruderingsriktningen med Aspose.3D för Java. Oavsett om du bygger arkitektoniska visualiseringar, produktprototyper eller spelresurser, ger behärskning av linjär extrusion dig flexibiliteten att snabbt modellera komplexa former. Vi går igenom varje steg, från att lägga till noder i Java till **exportera 3d-modell obj**-filer, så att du kan se resultatet omedelbart.

## Quick Answers
- **Vad betyder “create 3d scene”?** Det betyder att initiera ett Aspose.3D `Scene`-objekt som kommer att innehålla all geometri, ljus och kameror.  
- **Hur ställer jag in extruderingsriktning?** Använd metoden `setDirection(Vector3)` på en `LinearExtrusion`-instans.  
- **Vilket format ska jag använda för export?** OBJ-formatet (`FileFormat.WAVEFRONTOBJ`) stöds brett för 3‑D‑arbetsflöden.  
- **Behöver jag en licens för Aspose.3D?** En gratis provversion fungerar för utveckling; en kommersiell licens krävs för produktion.  
- **Kan jag lägga till fler noder i Java?** Ja—använd `scene.getRootNode().createChildNode()` för att lägga till så många objekt som behövs.

## What is a “create 3d scene” workflow?

Ett **create 3d scene**-arbetsflöde börjar med ett tomt `Scene`-objekt, lägger till geometri (som extruderade profiler), placerar den med transformationer och sparar slutligen scenen till ett filformat som OBJ. Detta mönster är ryggraden i de flesta 3‑D‑applikationer byggda med Aspose.3D.

## Why set extrusion direction?

Att ställa in extruderingsriktningen låter dig luta, rotera eller skeva formen medan den extruderas, vilket ger dig kontroll över den slutliga geometrin utan extra efterbehandling. Det är särskilt användbart för:

- Att skapa avsmalnande kolonner eller specialformade rör.  
- Att aligna extrusioner med icke‑standardaxlar i mekaniska delar.  
- Att generera konstnärliga former för visuella effekter.

## Prerequisites

Innan vi dyker ner, se till att du har:

- Grundläggande kunskaper i Java.  
- Aspose.3D‑biblioteket installerat – ladda ner det från [here](https://releases.aspose.com/3d/java/).  
- En IDE som Eclipse eller IntelliJ IDEA.

## Import Packages

Först, importera de nödvändiga Aspose.3D-klasserna:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Initialize Base Profile

Skapa den 2‑D-profil som ska extruderas. I detta exempel använder vi en avrundad rektangel:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Proffstips:** Justera avrundningsradien för att kontrollera hur skarpa eller mjuka rektangelhörnen ser ut innan extrusion.

## Step 2: Create a Scene

Nu **skapar vi 3d scene** som kommer att hysa våra objekt:

```java
Scene scene = new Scene();
```

## Step 3: Add Nodes Java – Positioning the Objects

Vi kommer att lägga till två barnnoder (vänster och höger) till scenens rot‑node och flytta den vänstra lite åt sidan:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: How to extrude – Left Node (default direction)

Extrudera profilen på den vänstra noden med standard Z‑axelriktning. Vi sätter också en full 360° vridning och ökar antalet skivor för jämnhet:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Step 5: How to set direction – Right Node

Här **ställer vi in riktning** genom att tillhandahålla en anpassad `Vector3`. Detta lutar extrusionen mot vektorn (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Step 6: Save OBJ file – Export 3D model

Till sist **sparar vi obj‑fil** för att se resultatet i någon 3‑D‑visare:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

När du öppnar den genererade OBJ‑filen kommer du att se två extruderade rektanglar: en med standardriktning och en lutad enligt den vektor vi angav.

## Common Issues and Solutions

| Problem | Orsak | Lösning |
|-------|--------|-----|
| OBJ‑filen är tom | Scenen sparades inte eller sökvägen är felaktig | Verifiera att `MyDir` pekar på en skrivbar mapp och att filnamnet slutar med `.obj`. |
| Extrusionen ser platt ut | `setSlices` är för lågt | Öka `setSlices` (t.ex. 200) för jämnare geometri. |
| Riktningen verkar oförändrad | Vektorn är inte normaliserad | Använd en normaliserad `Vector3` eller justera värdena för att återspegla önskad lutning. |

## Frequently Asked Questions

### Q1: Kan jag använda Aspose.3D med andra programmeringsspråk?
A1: Aspose.3D stödjer olika språk, inklusive .NET och Java.

### Q2: Finns det en gratis provversion av Aspose.3D?
A2: Ja, du kan utforska funktionerna i Aspose.3D med en gratis provversion [here](https://releases.aspose.com/).

### Q3: Var kan jag hitta detaljerad dokumentation för Aspose.3D för Java?
A3: Den omfattande dokumentationen finns tillgänglig [here](https://reference.aspose.com/3d/java/).

### Q4: Hur kan jag få support för Aspose.3D?
A4: Besök [Aspose.3D forum](https://forum.aspose.com/c/3d/18) för hjälp eller frågor.

### Q5: Finns tillfälliga licenser för Aspose.3D?
A5: Ja, du kan skaffa en tillfällig licens [here](https://purchase.aspose.com/temporary-license/).

---

**Senast uppdaterad:** 2025-12-18  
**Testad med:** Aspose.3D 24.11 för Java  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}