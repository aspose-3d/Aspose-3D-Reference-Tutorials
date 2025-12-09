---
date: 2025-12-09
description: Lär dig hur du lägger till en barnnod, placerar 3D-objekt och sparar
  scenen som OBJ medan du skapar anpassade fläktcylindrar med Aspose.3D för Java.
language: sv
linktitle: Adding Child Node for Fan Cylinders with Aspose.3D Java
second_title: Aspose.3D Java API
title: Lägg till barnnod för att bygga fläktcylindrar med Aspose.3D för Java
url: /java/cylinders/creating-fan-cylinders/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Lägg till barnnod för att bygga fläktcylindrar med Aspose.3D för Java

## Introduktion

Redo att **add child node** till en 3‑D-scen och skapa iögonfallande fläktcylindrar? I den här handledningen går vi igenom varje steg—från att sätta upp scenen, positionera 3D-objekt, till slut att **save scene as OBJ**—med Aspose.3D för Java. Oavsett om du finjusterar en spelresurs eller bygger en snabb prototyp, ger koncepten här dig solid kontroll över dina 3‑D-modeller.

## Snabba svar
- **Vad gör “add child node”?** Det infogar ett nytt objekt i scengrafen och ärver transformationer från sin förälder.  
- **Hur kan jag positionera ett 3D-objekt?** Genom att applicera en translation (eller rotation/skala) på nodens transform.  
- **Vilket filformat används för export?** Exemplet sparar modellen som en Wavefront OBJ-fil.  
- **Behöver jag en licens för att köra koden?** En gratis provversion fungerar för utvärdering; en licens krävs för produktion.  
- **Vilken IDE fungerar bäst?** Alla Java-IDE:er (IntelliJ IDEA, Eclipse, VS Code) som stödjer JDK 8+.

## Vad är “add child node” i Aspose.3D?
Att lägga till en barnnod innebär att skapa en ny nod under en befintlig förälder i scenhierarkin. Barnet ärver förälderns koordinatsystem, vilket gör det enkelt att **position 3d object** instanser relativt varandra.

## Varför lägga till en barnnod när man bygger fläktcylindrar?
- **Modulär design:** Varje cylinder (fläkt eller icke‑fläkt) finns i sin egen nod, vilket förenklar senare redigeringar.  
- **Transformärvning:** Flytta, rotera eller skala föräldern så följer alla barn automatiskt.  
- **Renare scengraf:** Förbättrar läsbarhet och felsökning av komplexa modeller.

## Prerequisites

- **Java Development Kit (JDK)** – ladda ner från den [officiella webbplatsen](https://www.oracle.com/java/technologies/javase-downloads.html).  
- **Aspose.3D for Java** – hämta det senaste biblioteket från [nedladdningslänken](https://releases.aspose.com/3d/java/).

## Importera paket

Begin by importing the necessary packages into your Java project. This step is crucial for accessing the functionalities provided by Aspose.3D.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg 1: Skapa en scen

Först skapar vi en tom 3‑D-scen som kommer att hysa alla våra objekt.

```java
// ExStart:2
// Create a Scene
Scene scene = new Scene();
// ExEnd:2
```

## Steg 2: Skapa en fläktcylinder

Därefter bygger vi en cylinder som kommer att renderas som en fläkt (delvis svep).

```java
// ExStart:3
// Create a cylinder with fan
Cylinder fan = new Cylinder(2, 2, 10, 20, 1, false);
fan.setGenerateFanCylinder(true);
fan.setThetaLength(MathUtils.toRadian(270.0));
// ExEnd:3
```

## Steg 3: Lägg till barnnod & positionera 3D‑objekt

Nu **add child node** till scenen och **position the 3d object** genom att sätta dess translation. Här blir fläktcylindern en del av scengrafen.

```java
// ExStart:4
// Create ChildNode and set translation
scene.getRootNode().createChildNode(fan).getTransform().setTranslation(10, 0, 0);
// ExEnd:4
```

## Steg 4: Skapa en icke‑fläktcylinder

För att visa Aspose.3D:s flexibilitet skapar vi också en vanlig cylinder utan fläkt och lägger till den som en annan barnnod.

```java
// ExStart:5
// Create a cylinder without a fan
Cylinder nonfan = new Cylinder(2, 2, 10, 20, 1, false);
// Create ChildNode
scene.getRootNode().createChildNode(nonfan);
// ExEnd:5
```

## Steg 5: Spara scenen som OBJ

Till sist **save scene as OBJ** så att du kan visa resultatet i någon standard 3‑D‑visare.

```java
// ExStart:6
// Save scene
scene.save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

Grattis! Du har framgångsrikt **added child node**, positionerat dina objekt och exporterat modellen.

## Vanliga problem & tips

| Problem | Lösning |
|-------|----------|
| **File not found** när du sparar | Se till att mål katalogen finns och att du har skrivbehörighet. |
| **Cylinder appears flat** | Verifiera radie- och höjdvärden; Aspose.3D förväntar sig enheter i samma skala. |
| **Fan slice looks incomplete** | Justera `ThetaLength` (i radianer) för att täcka önskad vinkel. |
| **Scene not visible in viewer** | Bekräfta att OBJ-filen sparades med tillhörande `.mtl` (material) fil om det behövs. |

## Vanliga frågor

**Q:** *Är Aspose.3D kompatibel med andra Java‑bibliotek för 3D‑modellering?*  
**A:** Ja, Aspose.3D fungerar tillsammans med andra Java 3‑D‑bibliotek, så att du kan kombinera funktioner efter behov.

**Q:** *Kan jag anpassa utseendet på de genererade fläktcylindrarna ytterligare?*  
**A:** Absolut. Du kan applicera material, texturer och belysning med hjälp av `Material` och `Light`‑klasserna.

**Q:** *Var kan jag hitta ytterligare support eller hjälp för Aspose.3D?*  
**A:** Besök [Aspose.3D‑forumet](https://forum.aspose.com/c/3d/18) för gemenskapsstöd och officiella svar.

**Q:** *Finns det en gratis provversion av Aspose.3D?*  
**A:** Ja, du kan utforska Aspose.3D med en [gratis provversion](https://releases.aspose.com/) innan du köper.

**Q:** *Hur kan jag skaffa en tillfällig licens för Aspose.3D?*  
**A:** Skaffa en tillfällig licens [här](https://purchase.aspose.com/temporary-license/) för testning och utveckling.

## Slutsats

I den här guiden demonstrerade vi hur man **add child node**, **position 3d object** och **save scene as OBJ** samtidigt som man skapar anpassade fläktcylindrar med Aspose.3D för Java. Dessa byggstenar ger dig flexibiliteten att konstruera komplexa 3‑D‑hierarkier och exportera dem för vilken efterföljande arbetsflöde som helst.

---

**Senast uppdaterad:** 2025-12-09  
**Testad med:** Aspose.3D 24.12 for Java  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}