---
date: 2026-09-08
description: Hur man minskar storleken på 3D-modeller genom att generera ett sfärmesh
  i Java och komprimera det med Google Draco via Aspose.3D. Lär dig hela arbetsflödet
  på några minuter.
keywords:
- how to reduce 3d model size
- aspose 3d java
- draco mesh compression
- java sphere mesh
- 3d model optimization
lastmod: 2026-09-08
linktitle: Hur man minskar 3D-modellens storlek – Skapa sfärmesh i Java med Google
  Draco
og_description: Hur man minskar storleken på 3D-modeller genom att skapa ett sfärmesh
  i Java och komprimera det med Google Draco med hjälp av Aspose.3D. Få en .drc-fil
  upp till 95 % mindre på några minuter.
og_image_alt: 'Developer guide: Reduce 3d model size with Java sphere mesh and Draco
  compression'
og_title: Hur man minskar storleken på 3D-modeller med ett Java-sfärmesh och Draco
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  headline: How to reduce 3d model size with a Java sphere mesh and Draco
  type: TechArticle
- description: How to reduce 3d model size by generating a sphere mesh in Java and
    compressing it with Google Draco via Aspose.3D. Learn the full workflow in minutes.
  name: How to reduce 3d model size with a Java sphere mesh and Draco
  steps:
  - name: set up the project
    text: Create a new Java project (any IDE works) and add all Aspose.3D JARs to
      the classpath. Keep your source files in a package such as `com.example.draco`
      for clarity.
  - name: how to create sphere mesh in Java
    text: 'The `Sphere` class is Aspose.3D''s built‑in geometry generator that produces
      a triangulated mesh with a configurable radius and tessellation. > **Pro tip:**
      The `Sphere` class generates a triangulated mesh with a default radius of 1.0.
      You can pass custom radius, tessellation, or material parameters '
  - name: export the mesh to Draco format
    text: After the sphere is added to a `Scene` object, call `scene.save("sphere.drc",
      SaveFormat.Draco)`. Aspose.3D automatically selects optimal compression settings,
      but you can fine‑tune them by adjusting `DracoCompressionOptions` if you need
      the smallest possible file. `DracoCompressionOptions` lets you
  - name: verify the output
    text: Open the generated `.drc` file with a Draco viewer (e.g., three.js `DRACOLoader`)
      to ensure the geometry renders correctly. You’ll notice a dramatic reduction
      in file size—often a factor of ten or more.
  type: HowTo
- questions:
  - answer: Yes, Aspose.3D supports OBJ, FBX, STL, GLTF, and many others, making it
      a versatile choice for **Aspose 3d export** pipelines.
    question: Is Aspose.3D compatible with different 3d file formats?
  - answer: Absolutely. Draco offers native libraries for C++, Python, and JavaScript.
      This tutorial focuses on Java, but the concepts apply across languages.
    question: Can I use Google Draco for compression in other programming languages?
  - answer: Visit the **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)**
      for full API references and more examples.
    question: Where can I find additional Aspose.3D documentation?
  - answer: Explore temporary licensing options on the **[Aspose temporary license
      page](https://purchase.aspose.com/temporary-license/)**.
    question: How do I obtain a temporary license for Aspose.3D?
  - answer: Yes, join the discussion at the **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.
    question: Is there a community forum for Aspose.3D support?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- reduce 3d model size
- Aspose.3D
- Java 3D compression
- Google Draco
- sphere mesh
title: Hur man minskar storleken på 3D-modeller med ett Java-sfärmesh och Draco
url: /sv/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hur man minskar 3d-modellens storlek med ett Java-sfärnät och Draco

## Introduktion

Om du letar efter ett snabbt sätt att **minska 3d-modellens storlek** samtidigt som du levererar högkvalitativ geometri, har du hamnat på rätt ställe. I den här handledningen går vi igenom hur man genererar ett sfärnät med **Aspose.3D for Java** och sedan komprimerar nätet med **Google Draco**. I slutet har du en färdig `.drc`‑fil som är dramatiskt mindre än originalet, vilket gör den perfekt för webbaserade visare, mobilspel eller någon Java‑applikation med begränsad bandbredd.

## Snabba svar
- **Vad täcker den här handledningen?** Skapa ett sfärnät i Java och komprimera det med Google Draco via Aspose.3D.  
- **Primärt bibliotek?** Aspose.3D for Java (används för både nätgenerering och Draco‑export).  
- **Typisk implementeringstid?** Ungefär 10‑15 minuter för en grundläggande sfär.  
- **Viktig förutsättning?** En Java‑utvecklingsmiljö med Aspose.3D‑JAR‑filerna på classpath.  
- **Resultat?** En `.drc`‑fil som **minskar 3d-modellens storlek** med upp till 95 % jämfört med ett okomprimerat nät.

## Hur man minskar 3d-modellens storlek?

`Sphere`‑klassen genererar en triangulerad sfärgeometri baserad på den angivna radien och tessellationsparametrarna. Ladda din sfär med `new Sphere(1.0, 32, 32)` och exportera den direkt till Draco med `scene.save("sphere.drc", SaveFormat.Draco)`. Metoden `scene.save` skriver den aktuella scenen till en fil i det angivna formatet. Aspose.3D hanterar konverteringen internt, så du undviker manuella kodningssteg. Draco‑exportören applicerar automatiskt geometrikvantisering och vertex‑deduplicering, vilket ger filer som ofta är 80‑95 % mindre samtidigt som den visuella kvaliteten bevaras.

## Vad betyder “reduce 3d model size” i sammanhanget av 3d‑utveckling?

**Reducing 3d model size** betyder att minska mängden geometridata som måste överföras eller lagras, utan att märkbart försämra den visuella kvaliteten. Draco uppnår detta genom att koda vertex‑positioner, normaler och andra attribut i ett mycket kompakt binärt format. När det kombineras med Aspose.3D hålls hela arbetsflödet inom Java, så du behöver inte hantera inhemska binärer.

## Varför använda Google Draco‑nätkomprimering med Aspose.3D?

Google Draco kombinerat med Aspose.3D ger en effektiv pipeline som dramatiskt minskar nätfiler samtidigt som de är enkla att integrera i Java‑projekt. Biblioteket hanterar all låg‑nivå‑kodning, så utvecklare kan fokusera på geometrisk skapelse utan att behöva hantera inhemska Draco‑binärer, vilket resulterar i snabbare utveckling och mindre resurser för webb och mobil.

- **Massiv storleksreduktion:** Draco kan minska nätdata med upp till 95 % för typiska modeller, vilket gör en 5 MB OBJ till en 0,3 MB `.drc`.  
- **Snabb avkodning vid körning:** Motorer som Unity, Unreal och three.js avkodar Draco nativt, vilket leder till snabbare laddningstider.  
- **Sömlös Java‑integration:** Aspose.3D abstraherar det inhemska Draco‑biblioteket, så du kan hålla dig i Java‑ekosystemet.  
- **All‑till‑en Aspose 3D‑export:** Samma API som du använder för att skapa geometri hanterar också exporten, vilket förenklar pipelinen.

## Förutsättningar

- **Java Development Kit (JDK)** – version 8 eller nyare.  
- **Aspose.3D for Java** – ladda ner de senaste JAR‑filerna från **[Aspose 3D Java releases page](https://releases.aspose.com/3d/java/)**.  
- **Grundläggande kunskap om Google Draco** – du använder Aspose.3D:s omslag, så ingen inhemsk Draco‑installation krävs.

## Importera paket

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Steg‑för‑steg‑guide

### Steg 1: konfigurera projektet

Skapa ett nytt Java‑projekt (valfri IDE fungerar) och lägg till alla Aspose.3D‑JAR‑filer på classpath. Håll dina källfiler i ett paket som `com.example.draco` för tydlighet.

### Steg 2: hur man skapar sfärnät i Java

`Sphere`‑klassen är Aspose.3D:s inbyggda geometrigenerator som producerar ett triangulerat nät med en konfigurerbar radie och tessellering.  

```java
import java.nio.file.Files;
import java.nio.file.Paths;
import com.aspose.threed.Sphere;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.FileFormat;

// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();

// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);

// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

> **Pro tip:** `Sphere`‑klassen genererar ett triangulerat nät med standardradien 1.0. Du kan ange anpassad radie, tessellering eller materialparametrar om du behöver en annan detaljnivå före komprimering.

### Steg 3: exportera nätet till Draco‑format

När sfären har lagts till i ett `Scene`‑objekt, anropa `scene.save("sphere.drc", SaveFormat.Draco)`. Aspose.3D väljer automatiskt optimala komprimeringsinställningar, men du kan finjustera dem genom att justera `DracoCompressionOptions` om du behöver den minsta möjliga filen. `DracoCompressionOptions` låter dig anpassa Draco‑komprimeringsinställningar såsom kvantisering och komprimeringsnivå.

### Steg 4: verifiera resultatet

Öppna den genererade `.drc`‑filen med en Draco‑visare (t.ex. three.js `DRACOLoader`) för att säkerställa att geometrin renderas korrekt. Du kommer att märka en dramatisk minskning av filstorleken — ofta en faktor tio eller mer.

## Vanliga användningsfall

| Scenario | Varför minska modellens storlek? | Hur den här handledningen hjälper |
|----------|----------------------------------|-----------------------------------|
| Webbaserade produktkonfiguratorer | Snabbare sidladdningar på långsamma anslutningar | Draco‑komprimerade `.drc`‑filer laddas på sekunder |
| Mobila AR/VR‑appar | Mindre minnesavtryck på enheter | Mindre nät håller appen responsiv |
| Molnrendrade scener | Minska bandbreddskostnader | Export med ett klick från Aspose.3D till Draco |

## Vanliga problem och lösningar

| Issue | Reason | Fix |
|-------|--------|-----|
| **`NoClassDefFoundError` för Draco‑klasser** | Aspose.3D‑JAR‑filerna finns inte på classpath | Verifiera att *alla* Aspose.3D‑JAR‑filer är inkluderade och att versionen matchar dokumentationen. |
| **Utdatafil är tom** | `MyDir` pekar på en icke‑existerande mapp | Skapa katalogen programatiskt (`Files.createDirectories(Paths.get(MyDir))`) innan filen skrivs. |
| **Komprimerat nät ser förvrängt ut** | Använder en låg komprimeringsnivå eller otillräcklig tessellering | Byt till `DracoCompressionLevel.OPTIMAL` och öka sfärens tessellering (t.ex. `new Sphere(1.0, 64, 64)`). `DracoCompressionLevel.OPTIMAL` väljer den högsta komprimeringskvaliteten för Draco‑utdata. |

## Vanliga frågor

**Q: Är Aspose.3D kompatibel med olika 3d‑filformat?**  
A: Ja, Aspose.3D stödjer OBJ, FBX, STL, GLTF och många andra, vilket gör det till ett mångsidigt val för **Aspose 3d export**‑pipelines.

**Q: Kan jag använda Google Draco för komprimering i andra programmeringsspråk?**  
A: Absolut. Draco erbjuder inhemska bibliotek för C++, Python och JavaScript. Denna handledning fokuserar på Java, men koncepten gäller för alla språk.

**Q: Var kan jag hitta ytterligare Aspose.3D‑dokumentation?**  
A: Besök **[Aspose.3D Java documentation](https://reference.aspose.com/3d/java/)** för fullständiga API‑referenser och fler exempel.

**Q: Hur får jag en tillfällig licens för Aspose.3D?**  
A: Utforska tillfälliga licensalternativ på **[Aspose temporary license page](https://purchase.aspose.com/temporary-license/)**.

**Q: Finns det ett community‑forum för Aspose.3D‑support?**  
A: Ja, gå med i diskussionen på **[Aspose.3D Forum](https://forum.aspose.com/c/3d/18)**.

## Slutsats

I den här guiden demonstrerade vi hur man **minskar 3d-modellens storlek** genom att skapa ett sfärnät i Java och sedan komprimera det med Google Draco via Aspose.3D. Genom att följa dessa koncisa steg kan du dramatiskt minska nätfiler, förbättra laddningstider och hålla dina Java‑baserade 3d‑applikationer responsiva och bandbreddseffektiva.

---

**Senast uppdaterad:** 2026-09-08  
**Testat med:** Aspose.3D for Java 24.12 (latest)  
**Författare:** Aspose

## Relaterade handledningar

- [Minska 3D-filstorlek – Komprimera scener med Aspose.3D för Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Generera ett Draco-punktmoln från sfärer med Aspose.3D för Java](/3d/java/point-clouds/generate-point-clouds-spheres-java/)
- [Lär dig hur man triangulerar nät för optimerad rendering i Java med Aspose.3D](/3d/java/geometry/triangulate-meshes-for-optimized-rendering/)

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}