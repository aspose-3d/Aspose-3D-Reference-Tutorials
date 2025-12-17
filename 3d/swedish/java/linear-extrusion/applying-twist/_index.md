---
date: 2025-12-17
description: Lär dig hur du skapar en vriden 3D-modell med Aspose.3D för Java med
  linjär extrudering och vridning samt exporterar en OBJ‑fil i Java. Följ vår steg‑för‑steg‑guide.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Skapa vriden 3D-modell – Tillämpa vridning i linjär extrudering med Aspose.3D
  för Java
url: /sv/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Applicering av Twist i Linjär Extrudering med Aspose.3D för Java

## Introduktion

Välkommen till denna steg‑för‑steg‑handledning om **hur man skapar en vriden 3D-modell** genom att applicera en twist under linjär extrudering med Aspose.3D för Java. Oavsett om du bygger arkitektoniska visualiseringar, spelresurser eller ingenjörsprototyper, kan en twist ge din geometri ett dynamiskt, spiralformat utseende med bara några rader kod.

## Snabba svar
- **Vad betyder “twist” i extrudering?** Det roterar profilen runt extruderingsaxeln när formen förlängs.  
- **Vilken API-klass hanterar twist?** `LinearExtrusion` tillhandahåller metoden `setTwist`.  
- **Behöver jag en licens för att köra exemplet?** En gratis provversion fungerar för utvärdering; en kommersiell licens krävs för produktion.  
- **Kan jag exportera resultatet som OBJ?** Ja, använd `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Vilken Java-version krävs?** Java 8 eller senare stöds fullt ut.

## Förutsättningar

Innan du dyker ner i handledningen, se till att du har följande förutsättningar på plats:

- Java‑utvecklingsmiljö: Se till att du har Java installerat på ditt system.  
- Aspose.3D‑bibliotek: Ladda ner och installera Aspose.3D‑biblioteket för Java från [download link](https://releases.aspose.com/3d/java/).  
- Dokumentation: Se [Aspose.3D documentation](https://reference.aspose.com/3d/java/) för omfattande vägledning.

## Importera paket

Innan du påbörjar kodningsprocessen, importera de nödvändiga paketen till ditt Java‑projekt. Här är ett exempel på hur du gör detta:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Ange dokumentkatalog

Först, definiera var den genererade 3D‑filen ska sparas.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Initiera basprofil

Nästa steg, skapa formen som ska extruderas. I detta exempel använder vi en rektangel med en liten avrundningsradie.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Skapa en scen

`Scene`‑objektet fungerar som behållare för alla 3D‑noder.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Skapa noder

Lägg till två barnnoder i scenen – en kommer att förbli rak, den andra får twist.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Linjär extruderings‑twist

Nu utför vi **linjär extruderings‑twist** på båda noderna. Den vänstra noden får en 0° twist (rak), medan den högra noden får en 90° twist, vilket skapar en spiralformad geometri. Vi ställer också in antalet skivor för att säkerställa en jämn geometri.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Exportera OBJ‑fil Java

Till sist, spara scenen i det allmänt stödda OBJ‑formatet. Detta demonstrerar **export OBJ file Java**‑funktionen i Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Varför detta är viktigt

Att skapa en vriden 3D‑modell ger dig en kraftfull visuell effekt utan att behöva externa modelleringsverktyg. Det är särskilt användbart för:

- **Mekaniska delar** som kräver helixfunktioner (t.ex. fjädrar, skruvar).  
- **Artistiska designer** där en subtil spiral ger visuellt intresse.  
- **Spelresurser** som drar nytta av låg‑poly, procedurgenererad geometri.

## Vanliga problem & tips

| Problem | Lösning |
|---------|----------|
| Twist visas platt eller saknas | Se till att `setSlices` är tillräckligt hög (t.ex. 100) för jämn rotation. |
| OBJ‑filen öppnas inte i visaren | Verifiera att utsökvägen (`MyDir`) är korrekt och att filen har skrivrättigheter. |
| Oväntad skalning | Kontrollera enhetssystemet för din källprofil; Aspose.3D arbetar i meter som standard. |

## Vanliga frågor

**Q: Kan jag använda Aspose.3D för Java för att arbeta med andra 3D‑filformat?**  
A: Ja, Aspose.3D stöder ett brett sortiment av format såsom FBX, STL, 3MF och fler.

**Q: Var kan jag hitta support för Aspose.3D för Java?**  
A: Besök [Aspose.3D forum](https://forum.aspose.com/c/3d/18) för communityhjälp och officiell assistans.

**Q: Finns det en gratis provversion tillgänglig?**  
A: Ja, du kan ladda ner en provversion från [här](https://releases.aspose.com/).

**Q: Hur får jag en tillfällig licens för testning?**  
A: Skaffa en tillfällig licens från [tillfällig licenssida](https://purchase.aspose.com/temporary-license/).

**Q: Var kan jag köpa en full licens?**  
A: Köp Aspose.3D för Java från [köpsida](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Senast uppdaterad:** 2025-12-17  
**Testad med:** Aspose.3D 24.11 för Java  
**Författare:** Aspose  

---