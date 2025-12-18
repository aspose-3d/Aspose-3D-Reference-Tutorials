---
date: 2025-12-18
description: Lär dig hur du extruderar former i Java med Aspose.3D, skapar en 3D-scen
  och exporterar Wavefront OBJ-filer utan ansträngning.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Hur man extruderar en form i Java med Aspose.3D linjär extrusion
url: /sv/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Utföra linjär extrudering i Aspose.3D för Java

## Introduktion

Välkommen till denna omfattande handledning om **how to extrude shape** i Aspose.3D för Java! Om du vill förbättra dina 3D-modelleringskunskaper med Java är du på rätt plats. Vi guidar dig genom att skapa en 3D-scen, utföra linjär extrudering och exportera resultatet som en Wavefront OBJ‑fil — allt med tydliga, steg‑för‑steg kodexempel.

## Snabba svar
- **What is linear extrusion?** Att förlänga en 2D-profil längs en rak bana för att skapa ett 3D‑solid.  
- **Which library handles this in Java?** Aspose.3D för Java.  
- **Can I export to OBJ?** Ja, med Wavefront OBJ‑exportfunktionen.  
- **Do I need a license for development?** En gratis provversion fungerar för testning; en licens krävs för produktion.  
- **What Java version is required?** Java 1.6 eller senare.

## Vad är “how to extrude shape”?

Linjär extrudering är en grundläggande teknik i **3d modeling java** som förvandlar en platt profil — som en rektangel — till ett volymetriskt objekt genom att dra den över ett definierat avstånd. Denna metod används ofta för att skapa mekaniska delar, arkitektoniska element och dekorativa modeller.

## Varför använda Aspose.3D för linjär extrudering?

- **Full control** över geometri (skivor, vridning, offset).  
- **Seamless integration** med Java‑projekt — inga inhemska beroenden.  
- **Built‑in exporters** för populära format, inklusive Wavefront OBJ, vilket gör det enkelt att **generate 3d model**‑filer för efterföljande pipelines.

## Förutsättningar

Innan du dyker ner i handledningen, se till att du har följande förutsättningar på plats:

1. **Java Development Environment** – ett JDK (1.6 eller nyare) och din favorit‑IDE.  
2. **Aspose.3D Library** – ladda ner och installera biblioteket från den officiella sidan **[here](https://releases.aspose.com/3d/java/)**.

## Importera paket

När du har konfigurerat din utvecklingsmiljö och installerat Aspose.3D‑biblioteket, importera det nödvändiga paketet:

```java
import com.aspose.threed.*;
```

### Steg 1: Ange dokumentkatalog

Definiera mappen där de genererade filerna ska sparas:

```java
String MyDir = "Your Document Directory";
```

> Detta säkerställer att **generate 3d model**‑operationen skriver OBJ‑filen till en känd plats.

### Steg 2: Initiera basform

Skapa en rektangel som kommer att fungera som extruderingsprofil:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Du kan justera avrundningsradien för att få rundade hörn eller sätta den till `0` för en perfekt rektangel.

### Steg 3: Utför linjär extrudering

Nu extruderar vi rektangeln längs Z‑axeln, lägger till skivor, aktiverar centrering och applicerar en vridning med ett offset:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Extrusion length** – `10` enheter.  
- **Slices** – `100` för slät geometri.  
- **Twist** – `360°` skapar en full rotation.  
- **Twist offset** – flyttar vridningsursprunget till `(10, 0, 0)`.

### Steg 4: Skapa 3D-scen

Skapa en scenbehållare och lägg till extruderingen som ett barn‑nod. Detta steg **creates 3d scene** som kan hålla flera objekt:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Steg 5: Spara 3D-scen

Exportera scenen till en Wavefront OBJ‑fil. Detta demonstrerar **wavefront obj export** och **save 3d obj**‑funktioner:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Efter att ha kört koden hittar du `LinearExtrusion.obj` i den katalog du angav, redo att öppnas i någon 3D‑visare eller vidare bearbetas.

## Vanliga problem och lösningar

| Problem | Orsak | Lösning |
|---------|-------|---------|
| OBJ‑filen är tom | Sökvägen till utdatamappen är felaktig eller ej skrivbar | Verifiera att `MyDir` pekar på en befintlig mapp med skrivrättigheter. |
| Vridning inte tillämpad | `setCenter(true)` utelämnad | Se till att centrering är aktiverad eller justera `setTwistOffset`‑värden. |
| Kompileringsfel på `LinearExtrusion` | Använder en äldre Aspose.3D‑version | Uppdatera till den senaste Aspose.3D‑utgåvan. |

## Vanliga frågor

**Q: Är Aspose.3D kompatibel med alla Java‑versioner?**  
A: Aspose.3D fungerar med Java 1.6 och senare.

**Q: Kan jag använda Aspose.3D för kommersiella projekt?**  
A: Ja, kommersiell användning är tillåten med en giltig licens. Du kan skaffa en **[here](https://purchase.aspose.com/buy)**.

**Q: Var kan jag få support om jag stöter på problem?**  
A: Besök **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** för gemenskapshjälp eller köp en **[temporary license](https://purchase.aspose.com/temporary-license/)** för premium‑support.

**Q: Vilka andra 3D‑modelleringsfunktioner erbjuder Aspose.3D?**  
A: Biblioteket inkluderar mesh‑manipulation, Boolean‑operationer, textur‑mappning och mer. Se hela listan **[here](https://reference.aspose.com/3d/java/)**.

**Q: Finns det en gratis provversion tillgänglig?**  
A: Ja, du kan ladda ner en provversion **[here](https://releases.aspose.com/)**.

## Slutsats

Du har nu lärt dig **how to extrude shape** med Aspose.3D för Java, skapat en 3D‑scen och exporterat resultatet som en Wavefront OBJ‑fil. Denna teknik öppnar dörren till ett brettktrum av **3d modeling java**‑projekt — från enkla delar till komplexa sammansättningar. Utforska ytterligare funktioner som Boolean‑operationer eller textur‑mappning för att ytterligare berika dina modeller.

**Senast uppdaterad:** 2025-12-18  
**Testad med:** Aspose.3D 24.11 för Java  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## MÅLNYCKELORD:

**Primär nyckelord (HÖGSTA PRIORITET):**  
how to extrude shape  

**Sekundära nyckelord (STÖDJANDE):**  
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj