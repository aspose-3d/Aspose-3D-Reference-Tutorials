---
date: 2025-12-06
description: Leer hoe u FBX‑bestanden opslaat en scène‑informatie opvraagt met Aspose.3D
  voor Java. Deze stapsgewijze handleiding behandelt het instellen van de toepassingsnaam,
  het definiëren van meeteenheden en het exporteren van de scène naar FBX.
language: nl
linktitle: How to Save FBX and Retrieve 3D Scene Info in Java
second_title: Aspose.3D Java API
title: Hoe FBX op te slaan en 3D‑scène‑informatie op te halen in Java
url: /java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe FBX op te slaan en 3D‑scène‑informatie op te halen in Java

## Inleiding

Als je op zoek bent naar een duidelijke, praktische gids over **hoe fbx**‑bestanden op te slaan terwijl je bruikbare metadata uit je 3D‑scènes haalt, ben je hier aan het juiste adres. In deze tutorial lopen we elke stap door met behulp van de **Aspose.3D Java**‑bibliotheek: van het maken van een scène, **het instellen van de toepassingsnaam**, **het definiëren van meeteenheden**, tot het uiteindelijk **exporteren van de scène naar FBX**. Aan het einde heb je een kant‑klaar FBX‑bestand dat de asset‑informatie bevat die je nodig hebt voor downstream‑pijplijnen.

## Snelle antwoorden
- **Wat is het primaire doel?** Een FBX‑bestand opslaan dat aangepaste asset‑informatie bevat.  
- **Welke bibliotheek wordt gebruikt?** Aspose.3D for Java.  
- **Heb ik een licentie nodig?** Een gratis proefversie werkt voor ontwikkeling; een commerciële licentie is vereist voor productie.  
- **Kan ik de meeteenheden wijzigen?** Ja – gebruik `setUnitName` en `setUnitScaleFactor`.  
- **Waar wordt de output opgeslagen?** Naar het pad dat je opgeeft in `scene.save(...)`.

## Vereisten

Voordat we beginnen, zorg dat je het volgende hebt:

- Een stevige kennis van de basis‑Java‑syntaxis.  
- **Aspose.3D for Java** gedownload en toegevoegd aan je project (je kunt het verkrijgen via de officiële) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Je favoriete Java‑IDE (IntelliJ IDEA, Eclipse, NetBeans, enz.) correct geconfigureerd.

## Importpakketten

Importeer in je Java‑bronbestand de Aspose.3D‑klassen die scène‑beheer en bestandsformaatondersteuning bieden.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Pro tip:** Houd de importlijst minimaal om onnodige afhankelijkheden te vermijden en de compile‑tijden te verbeteren.

## Wat is het proces voor het opslaan van een FBX‑bestand?

Hieronder vind je een beknopte, stap‑voor‑stap walkthrough die laat zien **hoe je asset‑informatie** aan een scène toevoegt en vervolgens **de scène exporteert naar FBX**.

### Stap 1: Initialiseer een 3D‑scène

Maak eerst een leeg `Scene`‑object. Dit wordt de container voor alle geometrie, lichten, camera’s en asset‑metadata.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Stap 2: Stel toepassings‑ en leveranciersinformatie in

Het toevoegen van aangepaste metadata helpt downstream‑tools de bron van het bestand te identificeren. Hier **stellen we de toepassingsnaam** en leverancier in via het `AssetInfo`‑object.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Waarom dit belangrijk is:** Veel pijplijnen filteren of taggen assets op basis van de oorspronkelijke applicatie, waardoor deze stap essentieel is voor grote projecten.

### Stap 3: Definieer meeteenheden

Aspose.3D laat je het eenheidssysteem specificeren dat je scène gebruikt. In dit voorbeeld gebruiken we een oude Egyptische eenheid genaamd “pole” met een aangepaste schaalfactor.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Tip:** Pas `unitScaleFactor` aan om overeen te komen met de werkelijke grootte van je modellen; 1.0 vertegenwoordigt een 1‑op‑1‑mapping met de gekozen eenheid.

### Stap 4: Exporteer scène naar FBX

Nu de asset‑informatie is toegevoegd, slaan we de scène op als een FBX‑bestand. De optie `FileFormat.FBX7500ASCII` produceert een mens‑leesbare ASCII FBX, wat handig is voor debugging.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
// ExEnd:AddAssetInformationToScene
```

> **Onthoud:** Vervang `"Your Document Directory"` door een absoluut pad of een pad relatief ten opzichte van de werkmap van je project.

### Stap 5: Print succes‑bericht

Een eenvoudige console‑output bevestigt dat de bewerking geslaagd is en vertelt je waar het bestand is weggeschreven.

```java
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
```

## Veelvoorkomende gebruiksscenario's

- **Game‑asset‑pijplijnen** – embed creator‑informatie direct in FBX‑bestanden voor versie‑tracking.  
- **Architecturale visualisatie** – sla projectspecifieke eenheden op om schaalfouten te voorkomen bij import in render‑engines.  
- **Geautomatiseerde rapportage** – genereer FBX‑bestanden on‑the‑fly met metadata die downstream‑analyse‑tools kunnen lezen.

## Probleemoplossing & Tips

| Probleem | Oplossing |
|----------|-----------|
| **Bestand niet gevonden na opslaan** | Controleer of `MyDir` naar een bestaande map wijst en of je applicatie schrijfrechten heeft. |
| **Eenheden lijken onjuist in externe viewer** | Controleer `unitScaleFactor` opnieuw; sommige viewers verwachten meters als basiseenheid. |
| **Asset‑metadata ontbreekt** | Zorg ervoor dat je `scene.getAssetInfo()` **vóór** het opslaan aanroept; wijzigingen na `save()` worden niet bewaard. |

## Veelgestelde vragen

### Q1: Is Aspose.3D compatibel met alle Java‑IDE’s?

A1: Ja, Aspose.3D is ontworpen om naadloos te werken met alle grote Java‑IDE’s.

### Q2: Kan ik Aspose.3D gebruiken voor commerciële projecten?

A2: Absoluut. Aspose.3D biedt commerciële licenties voor ontwikkelaars, zodat je voldoet aan de licentie‑vereisten.

### Q3: Waar vind ik extra ondersteuning voor Aspose.3D?

A3: Voor vragen of hulp, bezoek het [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Is er een gratis proefversie beschikbaar voor Aspose.3D?

A4: Ja, je kunt de functionaliteit verkennen met een gratis proefversie beschikbaar [hier](https://releases.aspose.com/).

### Q5: Hoe kan ik een tijdelijke licentie voor Aspose.3D verkrijgen?

A5: Haal een tijdelijke licentie voor testdoeleinden [hier](https://purchase.aspose.com/temporary-license/).

## Veelgestelde vragen (Gedetailleerd)

**Q: Hoe wijzig ik het uitvoerformaat naar binaire FBX?**  
A: Vervang `FileFormat.FBX7500ASCII` door `FileFormat.FBX7500` bij het aanroepen van `scene.save(...)`.

**Q: Kan ik aangepaste, door de gebruiker gedefinieerde metadata toevoegen naast de ingebouwde asset‑velden?**  
A: Ja, gebruik `scene.getUserData().add("Key", "Value")` om extra sleutel‑waarde‑paren in te sluiten.

**Q: Ondersteunt Aspose.3D andere exportformaten zoals OBJ of GLTF?**  
A: Ja. Verander simpelweg de `FileFormat`‑enum naar `OBJ` of `GLTF2` indien nodig.

**Q: Welke Java‑versie is vereist?**  
A: Aspose.3D for Java ondersteunt Java 8 en hoger.

**Q: Is het mogelijk een bestaand FBX‑bestand te laden, de asset‑info te wijzigen en opnieuw op te slaan?**  
A: Absoluut. Laad het bestand met `new Scene("input.fbx")`, wijzig `scene.getAssetInfo()`, en sla vervolgens op.

---

**Laatst bijgewerkt:** 2025-12-06  
**Getest met:** Aspose.3D for Java 24.11  
**Auteur:** Aspose

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
