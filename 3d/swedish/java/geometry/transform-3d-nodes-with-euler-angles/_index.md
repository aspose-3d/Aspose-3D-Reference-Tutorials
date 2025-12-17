---
date: 2025-12-13
description: Lär dig hur du använder Aspose 3D Java för att transformera 3D‑noder.
  Den här guiden visar hur du använder Eulervinklar, lägger till 3D‑rotation och ställer
  in translation i Java.
linktitle: Aspose 3D Java – Transform 3D Nodes with Euler Angles
second_title: Aspose.3D Java API
title: Aspose 3D Java – Transformera 3D‑noder med Eulervinklar
url: /sv/java/geometry/transform-3d-nodes-with-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Transformera 3D-noder med Euler-vinklar i Java med Aspose.3D

## Introduktion

I den här handledningen kommer du att upptäcka **hur du använder aspose 3d java** för att transformera 3D-noder genom att applicera Euler-vinklar. I slutet av guiden kommer du att kunna lägga till rotation 3d, ange translation java och skapa dynamiska scener som reagerar på realtidsdata.

## Snabba svar
- **Vilket bibliotek hanterar 3D-transformationer i Java?** Aspose 3D for Java.  
- **Vilken metod sätter rotation med Euler-vinklar?** `setEulerAngles()` på nodens transform.  
- **Hur flyttar jag en nod i rymden?** Använd `setTranslation()` med en `Vector3`.  
- **Behöver jag en licens för produktion?** Ja, en kommersiell Aspose 3D-licens krävs.  
- **Kan jag exportera till FBX?** Absolut – `scene.save(..., FileFormat.FBX7500ASCII)` fungerar direkt.

## Förutsättningar

Innan vi dyker ner i handledningen, se till att du har följande förutsättningar på plats:

- Grundläggande kunskap i Java-programmering.  
- Java Development Kit (JDK) installerat på din maskin.  
- Aspose.3D-biblioteket, som du kan hämta från [Aspose.3D Java-dokumentation](https://reference.aspose.com/3d/java/).

## Importera paket

Börja med att importera de nödvändiga paketen i ditt Java-projekt. Se till att Aspose.3D-biblioteket är korrekt tillagt i din classpath. Om du ännu inte har laddat ner det, kan du hitta nedladdningslänken [här](https://releases.aspose.com/3d/java/).

```java
import com.aspose.threed.*;
```

## aspose 3d java – Arbeta med Euler-vinklar

### Steg 1. Initiera scen och nod

Först, skapa en scen och en nod som kommer att hålla den geometri du vill transformera.

```java
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();

// Initialize Node class object
Node cubeNode = new Node("cube");
```

### Steg 2. Skapa mesh och ange geometri

Därefter, generera ett enkelt mesh (en kub i detta fall) och fäst det på noden.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();

// Point node to the Mesh geometry
cubeNode.setEntity(mesh);
```

## Lägg till 3D-rotation till en nod

### Steg 3. Ange Euler-vinklar och translation

Nu applicerar vi rotationen med Euler-vinklar och flyttar även noden till en synlig position.

```java
// Euler angles
cubeNode.getTransform().setEulerAngles(new Vector3(0.3, 0.1, -0.5));

// Set translation
cubeNode.getTransform().setTranslation(new Vector3(0, 0, 20));
```

## Ange translation Java – Positionering av noden

Steget ovan visar **set translation java** i praktiken: noden flyttas 20 enheter längs Z‑axeln så att du kan se den efter rendering.

## Steg 4. Lägg till nod i scenen

Fäst den transformerade noden till scenens rot-nod.

```java
// Add cube to the scene
scene.getRootNode().getChildNodes().add(cubeNode);
```

## Steg 5. Spara 3D-scen

Slutligen, exportera scenen till en FBX-fil (eller något annat stödd format).

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByEulerAngles
System.out.println("\nTransformation added successfully to node.\nFile saved at " + MyDir);
```

Se till att ersätta `"Your Document Directory"` med den lämpliga sökvägen på din maskin.

## Slutsats

Grattis! Du har framgångsrikt transformerat 3D-noder med Euler-vinklar i Java med **aspose 3d java**. Experimentera med olika vinklar och translationer för att skapa dynamiska och engagerande 3D-scener.

## Vanliga frågor

**Q: Vad är skillnaden mellan Euler-vinklar och kvaternionrotation?**  
A: Euler-vinklar är intuitiva (pitch, yaw, roll) men kan drabbas av gimbal lock, medan kvaternioner undviker detta problem och är bättre för jämna interpolationer.

**Q: Kan jag kedja flera transformationer på samma nod?**  
A: Ja. Anropa `setEulerAngles`, `setTranslation` och `setScale` i vilken ordning som helst; biblioteket sammansätter dem till en enda transformmatris.

**Q: Är det möjligt att exportera till andra format som OBJ eller STL?**  
A: Absolut. Ersätt `FileFormat.FBX7500ASCII` med `FileFormat.OBJ` eller `FileFormat.STL` i anropet `scene.save`.

**Q: Hur applicerar jag samma rotation på flera noder samtidigt?**  
A: Skapa en föräldranod, applicera rotationen på föräldern och lägg till barnnoder under den. Alla barn ärver transformationen.

**Q: Behöver jag anropa några städningsmetoder efter sparning?**  
A: Java:s skräpsamlare hanterar de flesta resurser, men du kan explicit anropa `scene.dispose()` om du arbetar med stora scener i en långvarig applikation.

---

**Senast uppdaterad:** 2025-12-13  
**Testad med:** Aspose.3D 23.12 för Java  
**Författare:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}