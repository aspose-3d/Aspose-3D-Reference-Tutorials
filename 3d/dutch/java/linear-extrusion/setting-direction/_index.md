---
date: 2026-02-22
description: Leer hoe je de richting instelt bij lineaire extrusie en een 3D‑model
  OBJ exporteert met Aspose.3D voor Java. Volg onze stapsgewijze handleiding.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Hoe de richting in lineaire extrusie instellen met Aspose.3D voor Java
url: /nl/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Hoe richt je de richting in bij lineaire extrusie met Aspose.3D voor Java

## Introductie

In deze uitgebreide tutorial ontdek je **hoe je de richting instelt** bij het uitvoeren van een lineaire extrusie met Aspose.3D voor Java. Of je nu een CAD‑achtige tool bouwt of geometrie genereert voor een game‑engine, het controleren van de extrusierichting stelt je in staat precies de vorm te maken die je nodig hebt. We lopen elke stap door, van het initialiseren van een profiel tot het opslaan van het resultaat als een OBJ‑bestand, zodat je ook **3d‑model‑obj**‑bestanden direct vanuit Java kunt **exporteren**.

## Snelle antwoorden
- **Wat is de primaire klasse voor lineaire extrusie?** `LinearExtrusion`
- **Welke methode bepaalt de extrusierichting?** `setDirection(Vector3 direction)`
- **Kan ik het resultaat exporteren als OBJ?** Ja, met `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **Heb ik een licentie nodig voor ontwikkeling?** Een gratis proefversie is beschikbaar; een licentie is vereist voor productie.
- **Welke Java‑IDE werkt het beste?** IntelliJ IDEA of Eclipse worden beide volledig ondersteund.

## Wat is lineaire extrusie?

Lineaire extrusie neemt een 2‑D‑profiel (zoals een rechthoek of cirkel) en strekt het uit langs een rechte lijn om een 3‑D‑solid te creëren. Standaard volgt de extrusie de positieve Z‑as, maar Aspose.3D laat je dat pad wijzigen met de eigenschap `setDirection`.

## Waarom de richting instellen bij lineaire extrusie?

Het instellen van een aangepaste richting is nuttig wanneer:
- Je geometrie wilt uitlijnen met bestaande objecten in een scène.
- Je schuine of hoekige onderdelen wilt maken zonder extra transformaties.
- Je modellen exporteert die moeten overeenkomen met een specifiek coördinatensysteem (bijv. voor 3‑D‑printen of game‑engines).

## Vereisten

Voordat we beginnen, zorg dat je het volgende hebt:

- Basiskennis van Java.
- Aspose.3D‑bibliotheek geïnstalleerd. Je kunt deze downloaden van [hier](https://releases.aspose.com/3d/java/).
- Een IDE zoals Eclipse of IntelliJ IDEA.

## Importpakketten

Importeer eerst de namespaces die de kern‑3‑D‑klassen en hulptype leveren.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Basisprofiel initialiseren

Maak de vorm die geëxtrudeerd zal worden. In dit voorbeeld gebruiken we een `RectangleShape` met een kleine afrondingsstraal om de randen een gladde look te geven.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Stap 2: Een scène maken

Een `Scene`‑object fungeert als container voor alle 3‑D‑nodes, lichten, camera's en materialen.

```java
Scene scene = new Scene();
```

## Stap 3: Nodes maken

Voeg twee kind‑nodes toe aan de scène‑root—één voor de linkse extrusie en één voor de rechtse extrusie. De rechter‑node wordt vertaald zodat de twee objecten niet overlappen.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 4: Lineaire extrusie uitvoeren op de linkse node

Extrudeer het profiel op de linkse node met de standaard Z‑asrichting. We voegen ook een volledige 360°‑draaiing toe en verhogen het aantal slices voor een vloeiender mesh.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Stap 5: Lineaire extrusie uitvoeren op de rechtse node met richting

Hier **stellen we de richting in**. Door een aangepaste `Vector3` door te geven aan `setDirection`, volgt de extrusie de vector (0.3, 0.2, 1), waardoor een schuine vorm ontstaat.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Stap 6: 3D‑scène opslaan

Exporteer tenslotte de scène naar het Wavefront OBJ‑formaat. Deze stap laat zien hoe je **obj‑bestand‑java**‑projecten kunt **opslaan** en maakt het eenvoudig om het resultaat in elke 3‑D‑viewer te bekijken.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Veelvoorkomende problemen en oplossingen

| Probleem | Waarom het gebeurt | Oplossing |
|----------|--------------------|-----------|
| OBJ‑bestand lijkt leeg | Het profiel is niet toegevoegd aan een node | Zorg ervoor dat `createChildNode` wordt aangeroepen op een geldige node |
| Richting lijkt niet veranderd | `setDirection` werd aangeroepen nadat de extrusie al was geconstrueerd | Stel de richting in binnen de `LinearExtrusion`‑initializer zoals getoond |
| Mesh met lage resolutie | `setSlices`‑waarde is te laag | Verhoog het aantal slices (bijv. 100 of meer) |

## Conclusie

Je weet nu **hoe je de richting instelt** bij een lineaire extrusie, hoe je twist‑ en slice‑instellingen kunt aanpassen, en hoe je **3d‑model‑obj**‑bestanden kunt **exporteren** met Aspose.3D voor Java. Deze technieken geven je fijne controle over geometriecreatie en maken het eenvoudig om 3‑D‑assets in grotere pipelines te integreren.

## FAQ's

### Q1: Kan ik Aspose.3D gebruiken met andere programmeertalen?

A1: Aspose.3D ondersteunt verschillende programmeertalen, waaronder .NET en Java.

### Q2. Is er een gratis proefversie beschikbaar voor Aspose.3D?

A2: Ja, je kunt de functies van Aspose.3D verkennen met een gratis proefversie [hier](https://releases.aspose.com/).

### Q3: Waar vind ik gedetailleerde documentatie voor Aspose.3D voor Java?

A3: De uitgebreide documentatie is beschikbaar [hier](https://reference.aspose.com/3d/java/).

### Q4: Hoe kan ik ondersteuning krijgen voor Aspose.3D?

A4: Bezoek het [Aspose.3D‑forum](https://forum.aspose.com/c/3d/18) voor hulp of vragen.

### Q5: Zijn tijdelijke licenties beschikbaar voor Aspose.3D?

A5: Ja, je kunt een tijdelijke licentie verkrijgen [hier](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Laatst bijgewerkt:** 2026-02-22  
**Getest met:** Aspose.3D voor Java (laatste release)  
**Auteur:** Aspose