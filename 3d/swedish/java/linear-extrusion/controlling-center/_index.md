---
date: 2026-02-20
description: Lär dig en Java‑3D‑grafikhandledning om att kontrollera centrum vid linjär
  extrudering med Aspose.3D, inklusive hur du ställer in avrundningsradie och sparar
  en OBJ‑fil i Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Java 3D‑grafikhandledning – Centrum i linjär extrudering
url: /sv/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D Graphics Tutorial – Center i Linjär Extrudering

## Introduktion

Om du bygger 3D‑visualiseringar i Java är det viktigt att behärska extruderingsmetoder. Denna **java 3d graphics tutorial** guidar dig genom att kontrollera centrum för en linjär extrudering med Aspose.3D för Java, så att du kan skapa precisa, symmetriska modeller utan extra matematik. I slutet av guiden kommer du att förstå varför `center`‑egenskapen är viktig, hur du **set rounding radius**, och hur du **save OBJ file java**‑kompatibel output.

## Snabba svar
- **Vad gör center‑egenskapen?** Den bestämmer om extruderingen är symmetrisk kring profilens ursprung.  
- **Behöver jag en licens för att köra koden?** En tillfällig licens fungerar för testning; en full licens krävs för produktion.  
- **Vilket filformat används för resultatet?** Scenen sparas som en Wavefront OBJ‑fil.  
- **Kan jag ändra antalet skivor?** Ja, använd `setSlices(int)` på `LinearExtrusion`‑objektet.  
- **Är Aspose.3D kompatibel med Java 8+?** Absolut – den stöder alla moderna Java‑versioner.

## Vad är en java 3d graphics tutorial?

En **java 3d graphics tutorial** förklarar steg för steg hur man använder Java‑bibliotek för att skapa, manipulera och rendera tredimensionella objekt. I detta fall fokuserar vi på Aspose.3D:s extruderings‑API, som omvandlar 2‑D‑profiler till fullständiga 3‑D‑nät.

## Varför använda Aspose.3D för Java?

- **High‑level API** – Ingen behov av att skriva lågnivå‑mesh‑beräkningar.  
- **Cross‑format support** – Exportera till OBJ, FBX, STL och mer.  
- **Performance‑optimized** – Hanterar stora scener effektivt.  
- **Rich documentation** – Inkluderar exempel som det nedan.

## Förutsättningar

1. **Java Development Environment** – JDK 8 eller nyare installerat.  
2. **Aspose.3D for Java** – Ladda ner biblioteket och dokumentationen [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Skapa en mapp på din maskin för att lagra genererade filer; vi kommer att referera till den som **“Your Document Directory.”**

## Importera paket

I din Java‑IDE, importera de Aspose.3D‑klasser du behöver. Detta ger kompilatorn åtkomst till extruderings‑ och scen‑byggfunktionerna.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Steg‑för‑steg guide

### Steg 1: Skapa basprofilen

Först, skapa den 2‑D‑form som ska extruderas. Här använder vi en rektangel och **set rounding radius** till 0.3, vilket mjukar upp hörnen.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Steg 2: Skapa en 3D‑scen

Ett `Scene`‑objekt fungerar som behållare för alla 3‑D‑noder, ljus och kameror.

```java
Scene scene = new Scene();
```

### Steg 3: Lägg till vänster‑ och högernoder

Vi placerar två separata noder sida vid sida så att du kan jämföra extrudering med och utan centrering.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Steg 4: Linjär extrudering – Ingen centrering (vänster nod)

Skapa extruderingen på den vänstra noden, inaktivera centrering och begränsa meshen till tre skivor för en låg‑poly‑förhandsgranskning.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Steg 5: Lägg till ett markplan för referens (vänster nod)

En tunn låda fungerar som ett visuellt golv, vilket hjälper dig att se extruderingens orientering.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Steg 6: Linjär extrudering – Centrerad (höger nod)

Upprepa nu extruderingen, den här gången aktivera `center`. Geometrin blir symmetrisk kring profilens ursprung.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Steg 7: Lägg till ett markplan för referens (höger nod)

Samma markplan för högra sidan, vilket gör jämförelsen tydlig.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Steg 8: Spara 3D‑scenen

Slutligen, exportera hela scenen till en Wavefront OBJ‑fil – ett format som enkelt kan användas i de flesta 3‑D‑redigerare.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|---------|-------------------|---------|
| **Extrusion appears offset** | `setCenter(false)` leaves the profile anchored at its corner. | Use `setCenter(true)` for symmetric results. |
| **OBJ file is empty** | Output directory path is incorrect or missing write permissions. | Verify `MyDir` points to an existing folder and the application has write access. |
| **Rounded corners look sharp** | Rounding radius is too small relative to rectangle size. | Increase the radius value (e.g., `setRoundingRadius(0.5)`). |

## Vanliga frågor

### Q1: Kan jag använda Aspose.3D för Java i kommersiella projekt?

A1: Ja, Aspose.3D för Java är tillgänglig för kommersiell användning. För licensinformation, besök [here](https://purchase.aspose.com/buy).

### Q2: Finns det en gratis provversion?

A2: Ja, du kan prova en gratis provversion av Aspose.3D för Java [here](https://releases.aspose.com/).

### Q3: Var kan jag hitta support för Aspose.3D för Java?

A3: Aspose.3D‑community‑forumet är en bra plats för att söka support och dela dina erfarenheter. Besök forumet [here](https://forum.aspose.com/c/3d/18).

### Q4: Behöver jag en tillfällig licens för testning?

A4: Ja, om du behöver en tillfällig licens för teständamål kan du skaffa en [here](https://purchase.aspose.com/temporary-license/).

### Q5: Var kan jag hitta dokumentationen?

A5: Dokumentationen för Aspose.3D för Java finns tillgänglig [here](https://reference.aspose.com/3d/java/).

## Slutsats

Genom att slutföra denna **java 3d graphics tutorial** vet du nu hur du styr centrum för en linjär extrudering, justerar rundningsradien och **save OBJ file java**‑utdata med Aspose.3D. Dessa tekniker ger dig finjusterad kontroll över mesh‑symmetri, vilket är viktigt för spel‑tillgångar, CAD‑prototyper och vetenskapliga visualiseringar. Känn dig fri att experimentera med olika profiler, antal skivor och exportformat för att utöka din 3‑D‑verktygslåda.

---

**Last Updated:** 2026-02-20  
**Tested With:** Aspose.3D for Java 24.11  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}