---
date: 2026-02-25
description: Lär dig hur du skapar 3D‑extrudering i Java med Aspose.3D och exporterar
  OBJ‑fil i Java, vilket levererar högkvalitativa 3D‑modeller i Java‑applikationer.
linktitle: Create 3D Extrusion Java with Aspose.3D
second_title: Aspose.3D Java API
title: Skapa 3D‑extrudering i Java med Aspose.3D
url: /sv/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Skapa 3D Extrusion Java med Aspose.3D

## Introduktion

Om du behöver **create 3d extrusion java** snabbt och pålitligt, har du hamnat på rätt handledning. Under de kommande minuterna går vi igenom hur du genererar en linjär extrusion, anpassar dess geometri och **export obj file java** med Aspose.3D-biblioteket. Oavsett om du bygger ett CAD‑liknande verktyg, en spel‑tillgångspipeline eller någon Java‑baserad 3‑D‑arbetsflöde, ger den här guiden dig en solid, produktionsklar grund.

## Snabba svar
- **What does “linear extrusion” mean?** Det sveper en 2‑D-profil längs en rak linje för att bilda en 3‑D-solidd.  
- **Which library handles the extrusion?** Aspose.3D for Java tillhandahåller ett hög‑nivå API.  
- **Can I export the result as OBJ?** Ja – handledningen avslutas med `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Do I need a license for development?** En gratis provversion fungerar för lärande; en kommersiell licens krävs för produktion.  
- **What Java version is supported?** Java 1.6 och senare.

## Vad är Create 3D Extrusion Java?
Att skapa en 3D‑extrusion i Java innebär att ta en enkel 2‑D-form (som en rektangel) och utvidga den till den tredje dimensionen. Det resulterande meshet kan sparas i vanliga format som OBJ, som många 3‑D‑redigerare förstår.

## Varför använda Aspose.3D för linjär extrusion?
- **Pure Java API** – inga inhemska beroenden, perfekt för plattformsoberoende projekt.  
- **Rich geometry controls** – avrundning, vridning, skivor och offset exponeras alla via enkla egenskaper.  
- **Direct export** – spara till OBJ, STL, FBX och mer utan extra konverterare.  
- **Enterprise‑grade support** – licensiering, dokumentation och community‑forum är lätt tillgängliga.

## Förutsättningar

Innan du börjar, se till att du har:

1. **Java Development Environment** – JDK 1.6+ installerad och konfigurerad.  
2. **Aspose.3D Library** – Ladda ner den senaste JAR‑filen från den officiella webbplatsen [here](https://releases.aspose.com/3d/java/).

## Importera paket

Lägg till det centrala Aspose.3D‑namnutrymmet i din Java‑källfil:

```java
import com.aspose.threed.*;
```

## Steg 1: Ange dokumentkatalog

Definiera var de genererade filerna ska skrivas:

```java
String MyDir = "Your Document Directory";
```

> **Pro tip:** Använd en absolut sökväg eller en konfigurerbar egenskap så att utdataplatsen fungerar i olika miljöer.

## Steg 2: Initiera basform

Skapa en rektangel som kommer att fungera som extrusionsprofil. Avrundningsradien mjukar upp hörnen:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Du kan experimentera med `setRoundingRadius` för att få en mer cirkulär eller skarpare profil.

## Steg 3: Utför linjär extrusion

Nu omvandlar vi 2‑D-rektangeln till ett 3‑D‑objekt. Konstruktorn tar profilen och extrusionsdjupet (10 enheter i detta fall). Ytterligare egenskaper finjusterar meshet:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Slices** – styr hur mjuk extruderingen är.  
- **Center** – placerar geometrin kring origo.  
- **Twist** – roterar profilen längs extrusionsaxeln (här en full 360°).  
- **TwistOffset** – flyttar vridningspivoten, vilket demonstrerar hur man skapar spiraler.

## Steg 4: Skapa 3D‑scen

Ett `Scene` är behållaren för alla 3‑D‑objekt. Att lägga till extruderingen som ett barnnod gör den till en del av scen‑grafen:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

## Steg 5: Spara 3D‑scen

Slutligen, exportera scenen till en Wavefront OBJ‑fil – ett format som är brett stöd av 3‑D‑redigerare, spelmotorer och utskrifts‑pipelines:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Efter att ha kört koden hittar du **LinearExtrusion.obj** i den katalog du angav, redo att öppnas i Blender, Maya eller någon annan OBJ‑kompatibel visare.

## Vanliga problem och lösningar

| Symptom | Trolig orsak | Åtgärd |
|---------|--------------|--------|
| `FileNotFoundException` when saving | `MyDir` finns inte eller saknar skrivbehörighet | Skapa mappen i förväg eller använd en absolut sökväg med rätt behörigheter. |
| OBJ appears empty in viewer | Ingen geometri lades till i scenen | Verifiera att `LinearExtrusion`‑objektet är korrekt instansierat och bifogat till rot‑noden. |
| Twist looks wrong | Felaktiga `TwistOffset`‑värden | Justera `Vector3`‑koordinaterna; kom ihåg att offseten appliceras före vridningsrotationen. |

## Vanliga frågor

### Q1: Är Aspose.3D kompatibel med alla Java‑versioner?
A1: Aspose.3D är designad för att fungera med Java 1.6 och senare versioner.

### Q2: Kan jag använda Aspose.3D för kommersiella projekt?
A2: Ja, Aspose.3D kan användas både för personliga och kommersiella projekt. Kontrollera licensdetaljerna [here](https://purchase.aspose.com/buy).

### Q3: Hur kan jag få support för Aspose.3D?
A3: Besök [Aspose.3D forum](https://forum.aspose.com/c/3d/18) för community‑support eller överväg att köpa en [temporary license](https://purchase.aspose.com/temporary-license/) för premium‑support.

### Q4: Finns det andra 3D‑modelleringsegenskaper i Aspose.3D?
A4: Absolut! Utforska den omfattande dokumentationen [here](https://reference.aspose.com/3d/java/) för en komplett lista över funktioner och exempel.

### Q5: Finns det en gratis provversion av Aspose.3D?
A5: Ja, du kan få åtkomst till en gratis provversion [here](https://releases.aspose.com/).

## Slutsats

Du vet nu hur du **create 3d extrusion java** med Aspose.3D, anpassar dess geometri och **export obj file java** för vidare användning. Experimentera med olika profiler, vridningar och exportformat för att passa dina specifika projektbehov. När du är redo, utforska andra Aspose.3D‑funktioner såsom mesh‑manipulation, texturkartläggning och animation för att ytterligare berika dina Java‑baserade 3‑D‑applikationer.

---

**Senast uppdaterad:** 2026-02-25  
**Testad med:** Aspose.3D 24.12 för Java  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}