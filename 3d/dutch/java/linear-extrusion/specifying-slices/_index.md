---
date: 2026-02-22
description: Leer hoe je 3D‑extrusie met slices maakt met Aspose.3D voor Java. Deze
  stapsgewijze handleiding behandelt lineaire extrusie, het instellen van de afrondingsradius
  en het exporteren van OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Maak 3D-extrusie met slices – Aspose.3D voor Java
url: /nl/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3D Extrusie met Slices – Aspose.3D voor Java

## Introduction

Als je **3d extrusion maken** objecten wilt maken die er glad en precies uitzien, is het beheersen van het aantal slices de sleutel. In deze tutorial lopen we stap voor stap door hoe je slices specificeert tijdens een lineaire extrusie met Aspose.3D voor Java. Je zult zien waarom het aantal slices belangrijk is, hoe je een afrondingsstraal instelt, en hoe je het resultaat exporteert als een OBJ‑bestand dat in elke 3D‑pipeline kan worden gebruikt.

## Quick Answers
- **Wat regelt “slices”?** Het aantal tussenliggende doorsneden dat wordt gebruikt om het extrusieoppervlak te benaderen.  
- **Welke methode stelt het aantal slices in?** `LinearExtrusion.setSlices(int)`  
- **Kan ik de afrondingsstraal van het profiel wijzigen?** Ja, via `RectangleShape.setRoundingRadius(double)`  
- **Welk bestandsformaat wordt in dit voorbeeld gebruikt?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Heb ik een licentie nodig om de code uit te voeren?** Een gratis proefversie werkt voor evaluatie; een commerciële licentie is vereist voor productie.

## Wat is een lineaire extrusie met slices?

Lineaire extrusie neemt een 2‑D‑profiel (bijvoorbeeld een rechthoek) en strekt het uit langs een rechte lijn om een 3‑D‑solid te vormen. Door **slices** op te geven, vertel je Aspose.3D hoeveel tussenstappen er moeten worden gegenereerd, wat direct de gladheid van gebogen randen beïnvloedt, zoals bij een afgeronde rechthoek.

## Waarom Aspose.3D voor Java gebruiken om 3d extrusie te maken?

* **Volledige controle** – Je kunt het aantal slices, de afrondingsstraal en het exportformaat programmatisch aanpassen.  
* **Cross‑platform** – Werkt in elke Java‑omgeving zonder native afhankelijkheden.  
* **Exportflexibiliteit** – Direct opslaan naar OBJ, FBX, STL en vele andere formaten.

## Vereisten

1. **Java Development Kit** – JDK 8 of hoger geïnstalleerd.  
2. **Aspose.3D for Java** – Download de bibliotheek van de officiële site [hier](https://releases.aspose.com/3d/java/).  
3. Een IDE of teksteditor naar keuze.

## Importeer pakketten

Voeg de Aspose.3D‑namespace toe aan je project zodat je toegang hebt tot de 3‑D‑modelleerklassen.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Stapsgewijze gids

### Stap 1: Stel de scene in en definieer het profiel

Eerst maken we een `RectangleShape` aan en geven we het een **afrondingsstraal** zodat de hoeken glad zijn. Vervolgens initialiseren we een nieuwe `Scene` die alle geometrie zal bevatten.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Stap 2: **Maak child node** objecten voor elke extrusie

Elk stuk geometrie bevindt zich onder een `Node`. Hier genereren we twee sibling‑nodes – één voor een low‑slice extrusie en een andere voor een high‑slice extrusie – en verplaatsen we de linker node een beetje naar de zijkant zodat de resultaten gemakkelijk te vergelijken zijn.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Stap 3: Voer lineaire extrusie uit en **stel slices in**

Nu maken we daadwerkelijk **3d extrusion** objecten. De `LinearExtrusion`‑constructor neemt het profiel en de extrusiediepte. Met een **anonieme inner class** roepen we `setSlices` aan om de gladheid te regelen. De linker node krijgt slechts 2 slices (grof), terwijl de rechter node 10 slices krijgt (glad).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Stap 4: **Export OBJ** – sla de scene op

Tot slot schrijven we de scene naar een Wavefront OBJ‑bestand, een formaat dat breed wordt ondersteund door 3‑D‑editors en game‑engines. Dit toont de **export obj java**‑functionaliteit van Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| **Extrusie lijkt plat** | Slice count set to 1 or 0 | Ensure `setSlices` is called with a value ≥ 2. |
| **Afgeronde hoeken zien er gekarteld uit** | Rounding radius too small relative to slice count | Increase either the radius or the slice count for smoother curves. |
| **Bestand niet gevonden bij opslaan** | `MyDir` points to a non‑existent folder | Create the directory beforehand or use an absolute path. |

## Veelgestelde vragen

**Q: Hoe kan ik Aspose.3D voor Java downloaden?**  
A: Je kunt de bibliotheek downloaden [hier](https://releases.aspose.com/3d/java/).

**Q: Waar kan ik de documentatie voor Aspose.3D vinden?**  
A: Raadpleeg de documentatie [hier](https://reference.aspose.com/3d/java/).

**Q: Is er een gratis proefversie beschikbaar?**  
A: Ja, je kunt een gratis proefversie verkennen [hier](https://releases.aspose.com/).

**Q: Hoe kan ik ondersteuning krijgen voor Aspose.3D?**  
A: Bezoek het supportforum [hier](https://forum.aspose.com/c/3d/18).

**Q: Kan ik een tijdelijke licentie aanschaffen?**  
A: Ja, een tijdelijke licentie kan worden verkregen [hier](https://purchase.aspose.com/temporary-license/).

---

**Laatst bijgewerkt:** 2026-02-22  
**Getest met:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}