---
date: 2026-04-29
description: Leer hoe u de grootte van een 3D‑model kunt verkleinen door een bolvormige
  mesh te maken in Java en deze te comprimeren met Google Draco via Aspose.3D – essentieel
  voor Aspose 3D‑export.
keywords:
- reduce 3d model size
- aspose 3d export
- compress 3d mesh java
linktitle: Hoe maak je een bolmesh in Java – 3D‑meshes comprimeren met Google Draco
second_title: Aspose.3D Java API
title: 'Verminder 3D-modelgrootte: Maak een bolvormige mesh in Java met Draco'
url: /nl/java/3d-mesh-data/compress-meshes-google-draco/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Verminder 3D-modelgrootte: Maak een bolvormig mesh in Java met Draco

## Inleiding

Als je op zoek bent naar een snelle manier om **3D-modelgrootte te verkleinen** terwijl je toch hoogwaardige geometrie levert, ben je hier aan het juiste adres. In deze tutorial lopen we door het genereren van een bolvormig mesh met **Aspose.3D for Java** en vervolgens het comprimeren van dat mesh met **Google Draco**. Aan het einde heb je een kant-en-klare `.drc`‑file die dramatisch kleiner is dan het origineel, waardoor het perfect is voor web‑gebaseerde viewers, mobiele games of elke Java‑applicatie met beperkte bandbreedte.

## Snelle antwoorden

- **Waar gaat deze tutorial over?** Een bolvormig mesh maken in Java en dit comprimeren met Google Draco via Aspose.3D.  
- **Primaire bibliotheek?** Aspose.3D for Java (gebruikt voor zowel mesh‑creatie als Draco‑export).  
- **Typische implementatietijd?** Ongeveer 10‑15 minuten voor een basisbol.  
- **Belangrijke voorwaarde?** Een Java‑ontwikkelomgeving met de Aspose.3D‑JARs op de classpath.  
- **Resultaat?** Een `.drc`‑file die **3D-modelgrootte verkleint** tot wel 90 % ten opzichte van een niet‑gecomprimeerd mesh.

## Wat betekent “reduce 3D model size” in de context van 3D-ontwikkeling?

Het verkleinen van de 3D-modelgrootte betekent het verminderen van de hoeveelheid geometrie‑data die moet worden overgedragen of opgeslagen, zonder merkbaar verlies van visuele kwaliteit. Draco bereikt dit door vertex‑posities, normals en andere attributen te coderen in een zeer compact binair formaat. In combinatie met Aspose.3D blijft de volledige workflow binnen Java, zodat je geen native binaries hoeft te beheren.

## Waarom Google Draco‑meshcompressie gebruiken met Aspose.3D?

- **Massieve grootte‑reductie:** Draco kan mesh‑data tot 90 % verminderen ten opzichte van formaten zoals OBJ of STL.  
- **Snelle runtime‑decodering:** Engines zoals Unity, Unreal en three.js decoderen Draco native, wat leidt tot snellere laadtijden.  
- **Naadloze Java‑integratie:** Aspose.3D abstraheert de native Draco‑bibliotheek, zodat je binnen het Java‑ecosysteem kunt blijven.  
- **Alles‑in‑één Aspose 3D‑export:** Dezelfde API die je gebruikt om geometrie te maken, verwerkt ook de export, waardoor de pipeline wordt vereenvoudigd.

## Vereisten

- **Java Development Kit (JDK)** – versie 8 of nieuwer.  
- **Aspose.3D for Java** – download de nieuwste JARs van de officiële pagina [hier](https://releases.aspose.com/3d/java/).  
- **Basic familiarity with Google Draco** – je gebruikt de wrapper van Aspose.3D, dus geen native Draco‑installatie is vereist.

## Pakketten importeren

```java
import com.aspose.threed.DracoCompressionLevel;
import com.aspose.threed.DracoSaveOptions;
import com.aspose.threed.FileFormat;
import com.aspose.threed.Sphere;


import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

## Stapsgewijze handleiding

### Stap 1: Het project opzetten

Maak een nieuw Java‑project (elke IDE werkt) en voeg alle Aspose.3D‑JARs toe aan de classpath. Plaats je bronbestanden in een package zoals `com.example.draco` voor duidelijkheid.

### Stap 2: Hoe een bolvormig mesh maken in Java

```java
// ExStart:Encode3DMeshinGoogleDraco
// The path to the documents directory.
String MyDir = "Your Document Directory";

// Create a sphere
Sphere sphere = new Sphere();
```

> **Pro tip:** De `Sphere`‑klasse genereert een getrianguleerd mesh met een standaardstraal van 1.0. Je kunt een aangepaste straal, tessellatie of materiaaleigenschappen doorgeven als je vóór compressie een ander detailniveau nodig hebt.

### Stap 3: Hoe een mesh comprimeren met Google Draco

```java
// Encode the sphere to Google Draco raw data using optimal compression level.
DracoSaveOptions opt = new DracoSaveOptions();
opt.setCompressionLevel(DracoCompressionLevel.OPTIMAL);
byte[] b = FileFormat.DRACO.encode(sphere.toMesh(), opt);
```

Het instellen van het compressieniveau op `OPTIMAL` levert de grootste grootte‑reductie op terwijl de visuele getrouwheid behouden blijft, waardoor je direct **3D-modelgrootte verkleint**.

### Stap 4: Het gecomprimeerde mesh opslaan

```java
// Save the raw bytes to file
Files.write(Paths.get(MyDir, "SphereMeshtoDRC_Out.drc"), b);
// ExEnd:Encode3DMeshinGoogleDraco
```

De resulterende `SphereMeshtoDRC_Out.drc` kan naar clients worden gestreamd, opgeslagen in een CDN, of direct worden geladen door elke Draco‑compatibele engine.

## Veelvoorkomende gebruikssituaties

| Scenario | Waarom modelgrootte verkleinen? | Hoe deze tutorial helpt |
|----------|----------------------------------|--------------------------|
| Web‑gebaseerde productconfigurators | Snellere paginaladingen bij trage verbindingen | Draco‑gecomprimeerde `.drc`‑bestanden laden in seconden |
| Mobiele AR/VR‑apps | Kleiner geheugenverbruik op apparaten | Kleinere meshes houden de app responsief |
| Cloud‑gerenderde scènes | Bandbreedtekosten verlagen | Export met één klik van Aspose.3D naar Draco |

## Veelvoorkomende problemen en oplossingen

| Issue | Reason | Fix |
|-------|--------|-----|
| **`NoClassDefFoundError` voor Draco‑klassen** | Aspose.3D‑JARs niet op de classpath | Controleer of *alle* Aspose.3D‑JAR‑bestanden zijn opgenomen en of de versie overeenkomt met de documentatie. |
| **Uitvoerbestand is leeg** | `MyDir` wijst naar een niet‑bestaande map | Maak de map programmatisch aan (`Files.createDirectories(Paths.get(MyDir))`) voordat je het bestand schrijft. |
| **Gecomprimeerd mesh ziet er vervormd uit** | Een laag compressieniveau of onvoldoende tessellatie gebruiken | Schakel over naar `DracoCompressionLevel.OPTIMAL` en verhoog de tessellatie van de bol (bijv. `new Sphere(1.0, 64, 64)`). |

## Veelgestelde vragen

**Q: Is Aspose.3D compatibel met verschillende 3D‑bestandsformaten?**  
A: Ja, Aspose.3D ondersteunt OBJ, FBX, STL, GLTF en vele anderen, waardoor het een veelzijdige keuze is voor **Aspose 3D export**‑pipelines.

**Q: Kan ik Google Draco gebruiken voor compressie in andere programmeertalen?**  
A: Absoluut. Draco biedt native bibliotheken voor C++, Python en JavaScript. Deze tutorial richt zich op Java, maar de concepten zijn toepasbaar in alle talen.

**Q: Waar kan ik extra Aspose.3D‑documentatie vinden?**  
A: Bezoek de [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) voor volledige API‑referenties en meer voorbeelden.

**Q: Hoe krijg ik een tijdelijke licentie voor Aspose.3D?**  
A: Bekijk tijdelijke licentie‑opties [hier](https://purchase.aspose.com/temporary-license/).

**Q: Is er een community‑forum voor Aspose.3D‑ondersteuning?**  
A: Ja, neem deel aan de discussie op het [Aspose.3D Forum](https://forum.aspose.com/c/3d/18).

## Conclusie

In deze gids hebben we laten zien hoe je **3D-modelgrootte verkleint** door een bolvormig mesh te maken in Java en dit vervolgens te comprimeren met Google Draco via Aspose.3D. Door deze beknopte stappen te volgen kun je mesh‑bestanden drastisch verkleinen, laadtijden verbeteren en je Java‑gebaseerde 3D‑applicaties responsief en bandbreedte‑vriendelijk houden.

---

**Laatst bijgewerkt:** 2026-04-29  
**Getest met:** Aspose.3D for Java 24.12 (latest)  
**Auteur:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}