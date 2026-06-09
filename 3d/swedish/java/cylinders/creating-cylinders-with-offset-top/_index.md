---
date: 2026-04-08
description: Lär dig hur du skapar en cylinder med förskjuten topp i Aspose.3D för
  Java, lägger till ett barnnod i Java, ställer in förskjuten topp, genererar en 3D-modell
  och exporterar OBJ med en tillfällig Aspose‑licens.
keywords:
- aspose temporary license
- generate 3d model
- add child node java
- java export obj
- set offset top
linktitle: Aspose tillfällig licens – Skapa cylinder med förskjuten topp (Java)
second_title: Aspose.3D Java API
title: Aspose tillfällig licens – Skapa cylinder med förskjuten topp (Java)
url: /sv/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aspose Tillfällig Licens – Skapa Cylinder med Förskjuten Topp (Java)

## Introduktion

Om du vill **create cylinder** objekt med en anpassad förskjuten topp i en Java‑baserad 3D‑scen, gör Aspose.3D processen enkel. I den här handledningen går vi igenom varje steg—från att sätta upp scenen till att exportera den färdiga modellen som en OBJ‑fil—så att du kan integrera cylinder med förskjuten topp i dina applikationer med förtroende. I slutet av guiden kommer du också att förstå hur en **aspose temporary license** låter dig utvärdera dessa funktioner utan ett fullständigt köp.

## Snabba svar
- **Vilket bibliotek används?** Aspose.3D for Java  
- **Kan jag förskjuta toppen på en cylinder?** Yes, using `setOffsetTop`  
- **Hur lägger jag till en child node i Java?** Call `createChildNode` on the root node  
- **Vilket format kan jag exportera till?** Wavefront OBJ (`java export obj`)  
- **Behöver jag en licens för testning?** An **aspose temporary license** is available for evaluation  

## Vad är Aspose Tillfällig Licens?

En **aspose temporary license** är en kort‑siktig, gratis utvärderingsnyckel som låser upp hela funktionsuppsättningen av Aspose.3D för Java under utveckling och testning. Den tar bort utvärderingsvattenmärken och låter dig generera 3D‑modelfiler, såsom OBJ, STL eller FBX, exakt som en betald licens skulle göra.

## Varför använda Aspose.3D för Java?

- **High‑level API:** Ingen behov av att hantera låg‑nivå mesh‑data.  
- **Cross‑platform:** Fungerar i alla JVM‑kompatibla miljöer.  
- **Built‑in exporters:** Spara direkt till OBJ, STL, FBX och mer.  
- **Extensible:** Lägg enkelt till child nodes, tillämpa transformationer och integrera med andra Java‑bibliotek.  

## Förutsättningar

- **Java Development Kit (JDK)** – en kompatibel version installerad.  
- **Aspose.3D for Java library** – ladda ner den senaste JAR‑filen från den officiella sidan [here](https://releases.aspose.com/3d/java/).  
- En IDE efter eget val (Eclipse, IntelliJ IDEA, NetBeans, etc.).  

## Importera paket

Först, importera de klasser vi behöver. Placera dessa satser högst upp i din Java‑fil:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Steg‑för‑steg guide

### Steg 1: Skapa en Java 3D‑scen

En **java 3d scene** fungerar som behållare för alla 3D‑objekt.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Steg 2: Initiera Cylinder med Förskjuten Topp

Här svarar vi på **how to create cylinder** med en anpassad offset. Konstruktorn definierar radie, höjd, skivor, staplar och om cylindern är sluten. Därefter förskjuter vi toppen med `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Steg 3: Lägg till Child Node Java – Fäst den Första Cylindern

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Steg 4: Initiera en Andra Cylinder (Ingen Offset)

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Steg 5: Lägg till Child Node Java – Fäst den Andra Cylindern

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Steg 6: Java Export OBJ – Spara scenen som OBJ

Till sist **java export obj** hela scenen (båda cylindrarna) som en Wavefront OBJ‑fil, som är brett stöd av 3D‑verktyg.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

När du kör programmet hittar du `CustomizedOffsetTopCylinder.obj` i den angivna katalogen, redo att öppnas i Blender, Maya eller någon annan OBJ‑kompatibel visare.

## Hur man genererar 3D‑modell och exporterar OBJ i Java

Kombinationen av `Scene.save(..., FileFormat.WAVEFRONTOBJ)` och **aspose temporary license** låter dig **generate 3d model** filer snabbt, utan att behöva externa konverterare. Detta är särskilt praktiskt under prototypframtagning eller när du delar resurser med designers.

## Verkliga användningsfall

- **Architectural visualisation:** Offset‑top cylinders modellerar pelare som smalnar av mot taket.  
- **Mechanical parts:** Skapa kolvar eller kugghus där den övre ytan avsiktligt är förskjuten.  
- **Game assets:** Producera varierade pelarformer i farten, vilket minskar behovet av handgjorda mesh‑ar.  

## Vanliga problem och lösningar

| Problem | Orsak | Lösning |
|-------|--------|-----|
| **OBJ-filen är tom** | Scenen sparades inte korrekt eller fel sökväg. | Verifiera att målkatalogen finns och att du har skrivrättigheter. |
| **Offset har inte tillämpats** | Använder en äldre version av Aspose.3D. | Uppdatera till den senaste biblioteket där `setOffsetTop` stöds. |
| **Child node är inte synlig** | Transformationen har inte tillämpats. | Se till att du anropar `getTransform().setTranslation` efter att ha skapat child node. |

## Vanliga frågor

**Q: Är Aspose.3D kompatibel med olika Java‑IDEer?**  
A: Ja, det fungerar sömlöst med Eclipse, IntelliJ IDEA, NetBeans och andra IDEer.

**Q: Kan jag applicera texturer på de skapade 3D‑objekten?**  
A: Absolut! Använd `Material`‑klassen för att tilldela texturer och ytegenskaper.

**Q: Finns det licensalternativ för Aspose.3D?**  
A: Olika licensmodeller finns tillgängliga; du kan utforska dem [here](https://purchase.aspose.com/buy).

**Q: Hur kan jag få hjälp eller dela erfarenheter?**  
A: Gå med i Aspose.3D‑communityforum [here](https://forum.aspose.com/c/3d/18) för support och diskussion.

**Q: Finns en tillfällig licens tillgänglig för testning?**  
A: Ja, en **aspose temporary license** kan erhållas för utvärdering [here](https://purchase.aspose.com/temporary-license/).

---

**Senast uppdaterad:** 2026-04-08  
**Testad med:** Aspose.3D for Java 24.12 (latest)  
**Författare:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}