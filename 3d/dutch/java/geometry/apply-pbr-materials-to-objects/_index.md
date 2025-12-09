---
date: 2025-12-08
description: Leer hoe je een 3D‑scene in Java maakt, realistische PBR‑materialen toepast
  met Aspose.3D, en het 3D‑model opslaat als STL voor het renderen van 3D‑objecten
  in Java.
linktitle: Create 3D Scene Java – Apply PBR Materials with Aspose.3D
second_title: Aspose.3D Java API
title: 'Maak 3D‑scène Java: Pas PBR‑materialen toe met Aspose.3D'
url: /nl/java/geometry/apply-pbr-materials-to-objects/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Maak 3D‑scène in Java – Pas PBR‑materialen toe met Aspose.3D

## Inleiding

In deze praktische tutorial leer je **hoe je een 3D‑scène in Java maakt** en verrijk je deze met Physically Based Rendering (PBR)-materialen met behulp van de Aspose.3D-bibliotheek. Aan het einde van de gids kun je realistische oppervlakken renderen en **het 3D‑model STL opslaan** voor verder gebruik in elke 3D‑pipeline.

## Snelle antwoorden
- **Wat betekent “create 3d scene java”?** Het is het proces van het bouwen van een Scene‑object dat geometrie, lichten en camera's bevat in een Java‑applicatie.  
- **Welke bibliotheek behandelt PBR-materialen?** Aspose.3D biedt een kant‑klaar `PbrMaterial`‑klasse.  
- **Kan ik het resultaat exporteren als STL?** Ja – de `Scene.save`‑methode ondersteunt STL (ASCII en binair).  
- **Heb ik een licentie nodig voor productie?** Een permanente Aspose.3D‑licentie is vereist voor commercieel gebruik; een tijdelijke licentie werkt voor testen.  
- **Welke Java‑versie is vereist?** Elke Java 8+ runtime wordt ondersteund.

## Wat is een 3D‑scène in Java?

Een *scene* is de container die alle objecten (nodes), hun geometrie, materialen, lichten en camera's bevat. Beschouw het als het virtuele podium waarop je je 3D‑modellen plaatst. De `Scene`‑klasse van Aspose.3D biedt een nette, objectgeoriënteerde manier om dit podium programmatisch op te bouwen.

## Waarom PBR‑materialen gebruiken voor het renderen van 3D‑objecten in Java?

PBR (Physically Based Rendering) bootst de interactie van licht in de echte wereld na door parameters zoals metallic‑ en roughness‑factoren te gebruiken. Het resultaat is een overtuigender uiterlijk onder verschillende lichtomstandigheden, wat vooral waardevol is voor productvisualisatie, games of AR/VR‑ervaringen.

## Voorvereisten

Voordat we beginnen, zorg ervoor dat je het volgende hebt:

1. **Java‑ontwikkelomgeving** – JDK 8 of nieuwer geïnstalleerd.  
2. **Aspose.3D‑bibliotheek** – Download de nieuwste JAR van de [download link](https://releases.aspose.com/3d/java/).  
3. **Documentatie** – Maak je vertrouwd met de API via de officiële [documentation](https://reference.aspose.com/3d/java/).  
4. **Tijdelijke licentie (optioneel)** – Als je geen permanente licentie hebt, verkrijg dan een [temporary license](https://purchase.aspose.com/temporary-license/) voor testen.

## Importeer pakketten

Voeg de Aspose.3D‑namespace toe aan je Java‑bronbestand:

```java
import com.aspose.threed.*;
```

## Stap 1: Initialiseer een scene

Maak de scene die zal fungeren als het canvas voor je geometrie en materialen.

```java
// ExStart:InitializeScene
String MyDir = "Your Document Directory";
Scene scene = new Scene();
// ExEnd:InitializeScene
```

> **Pro tip:** Houd `MyDir` gericht op een schrijfbare map; anders zal de `save`‑aanroep mislukken.

## Stap 2: Initialiseer een PBR‑materiaal

Configureer een PBR‑materiaal met metallic‑ en roughness‑waarden die een bijna‑metallisch uiterlijk geven.

```java
// ExStart:InitializePBRMaterial
PbrMaterial mat = new PbrMaterial();
mat.setMetallicFactor(0.9);
mat.setRoughnessFactor(0.9);
// ExEnd:InitializePBRMaterial
```

> **Waarom deze waarden?** Een hoge metallic‑factor (≈ 0.9) laat het oppervlak zich gedragen als metaal, terwijl een hoge roughness (≈ 0.9) subtiele diffusie toevoegt, waardoor een perfecte spiegelafwerking wordt voorkomen.

## Stap 3: Maak een 3D‑object en pas het materiaal toe

Hier genereren we een eenvoudige doosgeometrie, koppelen we deze aan de root‑node van de scene, en wijzen we het PBR‑materiaal toe dat we zojuist hebben gemaakt.

```java
// ExStart:Create3DObject
Node boxNode = scene.getRootNode().createChildNode("box", new Box());
boxNode.setMaterial(mat);
// ExEnd:Create3DObject
```

> **Veelvoorkomende valkuil:** Het vergeten om het materiaal op de node in te stellen laat het object achter met de standaard (niet‑PBR) weergave.

## Stap 4: Sla de 3D‑scene op (STL‑export)

Exporteer de volledige scene — inclusief de met PBR‑verbeterde doos — naar een STL‑bestand. STL is een breed ondersteund formaat voor 3‑D‑printen en snelle visuele controles.

```java
// ExStart:Save3DScene
scene.save(MyDir + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
// ExEnd:Save3DScene
```

Je kunt ook `FileFormat.STLBINARY` kiezen als een kleinere bestandsgrootte vereist is.

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarschijnlijke oorzaak | Oplossing |
|----------|--------------------------|-----------|
| **Bestand niet opgeslagen** | `MyDir` wijst naar een niet‑bestaande map of heeft geen schrijfrechten | Controleer of de map bestaat en dat je Java‑proces schrijfrechten heeft |
| **Materiaal ziet er plat uit** | Metallic/Roughness‑waarden zijn ingesteld op 0 | Verhoog `setMetallicFactor` en/of `setRoughnessFactor` |
| **STL‑bestand kan niet worden geopend** | Verkeerde bestandsformaat‑vlag (ASCII vs Binair) voor de viewer | Gebruik de juiste `FileFormat`‑enum voor je doelviewer |

## Veelgestelde vragen

**Q: Kan ik Aspose.3D gebruiken voor commerciële projecten?**  
A: Ja. Koop een commerciële licentie op de [purchase page](https://purchase.aspose.com/buy).

**Q: Hoe krijg ik ondersteuning voor Aspose.3D?**  
A: Word lid van de community op het [Aspose.3D forum](https://forum.aspose.com/c/3d/18) voor gratis hulp, of open een supportticket met een geldige licentie.

**Q: Is er een gratis proefversie beschikbaar?**  
A: Absoluut. Download een proefversie van de [free trial page](https://releases.aspose.com/).

**Q: Waar vind ik gedetailleerde documentatie voor Aspose.3D?**  
A: Alle API‑referenties zijn beschikbaar op de officiële [documentation](https://reference.aspose.com/3d/java/).

**Q: Hoe verkrijg ik een tijdelijke licentie voor testen?**  
A: Vraag er een aan via de [temporary license link](https://purchase.aspose.com/temporary-license/).

## Conclusie

Je hebt nu **een 3D‑scene in Java gemaakt**, een realistisch PBR‑materiaal toegepast, en het resultaat geëxporteerd als een STL‑bestand met Aspose.3D. Deze workflow biedt je een solide basis voor het bouwen van rijkere visualisaties, het voorbereiden van assets voor 3‑D‑printen, of het invoeren van modellen in game‑engines.

---

**Laatst bijgewerkt:** 2025-12-08  
**Getest met:** Aspose.3D 24.12 (latest)  
**Auteur:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}