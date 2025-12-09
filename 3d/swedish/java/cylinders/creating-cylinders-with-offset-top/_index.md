---
date: 2025-12-05
description: Lär dig hur du skapar cylindermodeller med förskjutna toppar i Aspose.3D
  för Java, lägger till barnnod Java‑steg och exporterar 3D-modellens OBJ‑filer enkelt.
linktitle: How to Create Cylinder with Offset Top in Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hur man skapar en cylinder med förskjuten topp i Aspose.3D för Java
url: /sv/java/cylinders/creating-cylinders-with-offset-top/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Så skapar du cylinder med förskjuten topp i Aspose.3D för Java

## Introduktion

Om du vill **how to create cylinder** objekt med en anpassad förskjuten topp i en Java‑baserad 3D‑scen, gör Aspose.3D processen enkel. I den här handledningen går vi igenom varje steg—från att sätta upp scenen till att exportera den slutliga modellen som en OBJ‑fil—så att du kan integrera cylinder med förskjuten topp i dina applikationer med förtroende.

## Snabba svar
- **Vilket bibliotek används?** Aspose.3D for Java  
- **Kan jag förskjuta toppen på en cylinder?** Ja, med `setOffsetTop`  
- **Hur lägger jag till en child node i Java?** Anropa `createChildNode` på rot‑noden  
- **Vilket format kan jag exportera till?** Wavefront OBJ (`export 3d model obj`)  
- **Behöver jag en licens för testning?** En tillfällig licens finns tillgänglig för utvärdering  

## Vad är “how to create cylinder” med en förskjuten topp?

Att skapa en cylinder med en förskjuten topp betyder att den övre cirkulära ytan förskjuts i förhållande till basen, vilket gör att du kan modellera avsmalnande eller asymmetriska former utan manuell vertex‑manipulation. Aspose.3D tillhandahåller en dedikerad konstruktor och en `OffsetTop`‑egenskap för att uppnå detta på bara några kodrader.

## Varför använda Aspose.3D för Java?

- **High‑level API:** Ingen behov av att hantera låg‑nivå mesh‑data.  
- **Cross‑platform:** Fungerar i alla JVM‑kompatibla miljöer.  
- **Built‑in exporters:** Spara direkt till OBJ, STL, FBX och mer.  
- **Extensible:** Lägg enkelt till child nodes, applicera transformationer och integrera med andra Java‑bibliotek.

## Förutsättningar

Innan vi börjar, se till att du har:

- **Java Development Kit (JDK)** – en kompatibel version installerad.  
- **Aspose.3D for Java library** – ladda ner den senaste JAR‑filen från den officiella sidan [here](https://releases.aspose.com/3d/java/).  
- En IDE efter ditt val (Eclipse, IntelliJ IDEA, NetBeans, etc.).

## Importera paket

Först, importera de klasser vi behöver. Placera dessa satser högst upp i din Java‑fil:

```java
import com.aspose.threed.Cylinder;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
import com.aspose.threed.Vector3;


import java.io.IOException;
```

## Steg‑för‑steg‑guide

### Steg 1: Skapa en scen

En scen fungerar som behållare för alla 3D‑objekt.

```java
// ExStart:1
// Create a scene
Scene scene = new Scene();
// ExEnd:1
```

### Steg 2: Initiera cylinder med förskjuten topp

Här svarar vi på **how to create cylinder** med en anpassad förskjutning. Konstruktorn definierar radie, höjd, slices, stacks och om cylindern är sluten. Därefter förskjuter vi toppen med `setOffsetTop`.

```java
// ExStart:2
// Initialize cylinder
Cylinder cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
// Set OffsetTop
cylinder1.setOffsetTop(new Vector3(5, 3, 0));
// ExEnd:2
```

### Steg 3: Hur man **add child node Java** – Fäst den första cylindern

Vi skapar en child node under scenens rot‑node och flyttar cylindern till önskad plats.

```java
// ExStart:3
// Create ChildNode
scene.getRootNode().createChildNode(cylinder1).getTransform().setTranslation(10, 0, 0);
// ExEnd:3
```

### Steg 4: Initiera en andra cylinder (utan förskjutning)

För jämförelse lägger vi till en vanlig cylinder utan förskjutning.

```java
// ExStart:4
// Initialize second cylinder without customized OffsetTop
Cylinder cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
// ExEnd:4
```

### Steg 5: Hur man **add child node Java** – Fäst den andra cylindern

```java
// ExStart:5
// Create ChildNode
scene.getRootNode().createChildNode(cylinder2);
// ExEnd:5
```

### Steg 6: Hur man **export 3d model OBJ** – Spara scenen

Till sist exporterar vi hela scenen (båda cylindrarna) som en Wavefront OBJ‑fil, som är brett stöd av 3D‑verktyg.

```java
// ExStart:6
// Save
scene.save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:6
```

När du kör programmet hittar du `CustomizedOffsetTopCylinder.obj` i den angivna katalogen, redo att öppnas i Blender, Maya eller någon annan OBJ‑kompatibel visare.

## Vanliga problem och lösningar

| Problem | Orsak | Lösning |
|-------|--------|-----|
| **OBJ‑filen är tom** | Scenen sparades inte korrekt eller fel sökväg. | Verifiera att mål‑katalogen finns och att du har skrivrättigheter. |
| **Förskjutning tillämpas inte** | Använder en äldre version av Aspose.3D. | Uppdatera till den senaste versionen där `setOffsetTop` stöds. |
| **Child node syns inte** | Transformationen har inte tillämpats. | Se till att du anropar `getTransform().setTranslation` efter att ha skapat child node. |

## Vanliga frågor

**Q: Är Aspose.3D kompatibel med olika Java‑IDEer?**  
A: Ja, det fungerar sömlöst med Eclipse, IntelliJ IDEA, NetBeans och andra IDEer.

**Q: Kan jag applicera texturer på de skapade 3D‑objekten?**  
A: Absolut! Använd `Material`‑klassen för att tilldela texturer och ytegenskaper.

**Q: Finns det licensalternativ för Aspose.3D?**  
A: Olika licensmodeller finns tillgängliga; du kan utforska dem [here](https://purchase.aspose.com/buy).

**Q: Hur kan jag få hjälp eller dela erfarenheter?**  
A: Gå med i Aspose.3D‑community‑forumet [here](https://forum.aspose.com/c/3d/18) för support och diskussion.

**Q: Finns en tillfällig licens tillgänglig för testning?**  
A: Ja, en tillfällig licens kan erhållas för utvärdering [here](https://purchase.aspose.com/temporary-license/).

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---
**Last Updated:** 2025-12-05  
**Tested With:** Aspose.3D for Java 24.12 (latest)  
**Author:** Aspose