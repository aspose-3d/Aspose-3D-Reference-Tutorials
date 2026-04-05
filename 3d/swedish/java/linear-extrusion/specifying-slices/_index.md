---
date: 2026-02-22
description: Lär dig hur du skapar 3D‑extrudering med skivor med Aspose.3D för Java.
  Denna steg‑för‑steg‑guide täcker linjär extrudering, att sätta avrundningsradie
  och export av OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Skapa 3D-extrudering med skivor – Aspose.3D för Java
url: /sv/java/linear-extrusion/specifying-slices/
weight: 13
---

}} etc.

Also keep shortcodes unchanged.

Proceed.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Skapa 3D‑extrudering med skivor – Aspose.3D för Java

## Introduktion

Om du behöver **skapa 3d extrusion**‑objekt som ser släta och precisa ut, är kontrollen av antalet skivor nyckeln. I den här handledningen går vi igenom hur du anger skivor när du utför en linjär extrudering med Aspose.3D för Java. Du får se varför antalet skivor spelar roll, hur du ställer in en avrundningsradie och hur du exporterar resultatet som en OBJ‑fil som kan användas i vilken 3D‑pipeline som helst.

## Snabba svar
- **Vad styr “skivor”?** Antalet mellansteg‑tvärsnitt som används för att approximera extruderingsytan.  
- **Vilken metod sätter antalet skivor?** `LinearExtrusion.setSlices(int)`  
- **Kan jag ändra avrundningsradien på profilen?** Ja, via `RectangleShape.setRoundingRadius(double)`  
- **Vilket filformat används i detta exempel?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Behöver jag en licens för att köra koden?** En gratis provversion fungerar för utvärdering; en kommersiell licens krävs för produktion.

## Vad är en linjär extrudering med skivor?

Linjär extrudering tar en 2‑D‑profil (t.ex. en rektangel) och sträcker den längs en rak linje för att bilda ett 3‑D‑solid. Genom att specificera **skivor** talar du om för Aspose.3D hur många mellansteg som ska genereras, vilket direkt påverkar slätheten på kurvade kanter såsom en avrundad rektangel.

## Varför använda Aspose.3D för Java för att skapa 3d extrusion?

* **Full kontroll** – Du kan justera antalet skivor, avrundningsradie och exportformat programatiskt.  
* **Plattformsoberoende** – Fungerar i alla Java‑miljöer utan inhemska beroenden.  
* **Exportflexibilitet** – Spara direkt till OBJ, FBX, STL och många andra format.

## Förutsättningar

1. **Java Development Kit** – JDK 8 eller högre installerat.  
2. **Aspose.3D för Java** – Ladda ner biblioteket från den officiella sidan [här](https://releases.aspose.com/3d/java/).  
3. En IDE eller textredigerare du föredrar.

## Importera paket

Lägg till Aspose.3D‑namnutrymmet i ditt projekt så att du kan komma åt 3‑D‑modellklasserna.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Steg‑för‑steg‑guide

### Steg 1: Ställ in scenen och definiera profilen

Först skapar vi en `RectangleShape` och ger den en **avrundningsradie** så att hörnen blir släta. Sedan initierar vi en ny `Scene` som kommer att hålla all geometri.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Steg 2: **Skapa barn‑node**‑objekt för varje extrudering

Varje geometridel lever under en `Node`. Här genererar vi två syskon‑noder – en för en låg‑skiv‑extrudering och en för en hög‑skiv‑extrudering – och flyttar den vänstra noden lite åt sidan så att resultaten blir enkla att jämföra.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Steg 3: Utför linjär extrudering och **ställ in skivor**

Nu skapar vi faktiskt **3d extrusion**‑objekt. `LinearExtrusion`‑konstruktorn tar profilen och extruderingsdjupet. Med en **anonymous inner class** anropar vi `setSlices` för att kontrollera slätheten. Den vänstra noden får bara 2 skivor (grov), medan den högra noden får 10 skivor (slät).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Steg 4: **Exportera OBJ** – spara scenen

Till sist skriver vi scenen till en Wavefront OBJ‑fil, ett format som är brett stödjat av 3‑D‑redigerare och spelmotorer. Detta demonstrerar **export obj java**‑kapaciteten i Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Vanliga problem och lösningar

| Problem | Varför det händer | Lösning |
|-------|----------------|-----|
| **Extruderingen ser platt ut** | Antalet skivor är satt till 1 eller 0 | Se till att `setSlices` anropas med ett värde ≥ 2. |
| **Avrundade hörn ser hackiga ut** | Avrundningsradien är för liten i förhållande till antalet skivor | Öka antingen radien eller antalet skivor för mjukare kurvor. |
| **Filen hittas inte vid sparning** | `MyDir` pekar på en icke‑existerande mapp | Skapa katalogen i förväg eller använd en absolut sökväg. |

## Vanliga frågor

**Q: Hur kan jag ladda ner Aspose.3D för Java?**  
A: Du kan ladda ner biblioteket [här](https://releases.aspose.com/3d/java/).

**Q: Var kan jag hitta dokumentationen för Aspose.3D?**  
A: Se dokumentationen [här](https://reference.aspose.com/3d/java/).

**Q: Finns det en gratis provversion?**  
A: Ja, du kan utforska en gratis provversion [här](https://releases.aspose.com/).

**Q: Hur får jag support för Aspose.3D?**  
A: Besök support‑forumet [här](https://forum.aspose.com/c/3d/18).

**Q: Kan jag köpa en tillfällig licens?**  
A: Ja, en tillfällig licens kan erhållas [här](https://purchase.aspose.com/temporary-license/).

---

**Senast uppdaterad:** 2026-02-22  
**Testat med:** Aspose.3D för Java 24.11 (senaste vid skrivtillfället)  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}