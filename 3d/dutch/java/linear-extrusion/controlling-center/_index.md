---
title: Controlecentrum in lineaire extrusie met Aspose.3D voor Java
linktitle: Controlecentrum in lineaire extrusie met Aspose.3D voor Java
second_title: Aspose.3D Java-API
description: Ontdek de wereld van 3D-graphics in Java met Aspose.3D. Beheers moeiteloos het midden in lineaire extrusie.
weight: 11
url: /nl/java/linear-extrusion/controlling-center/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlecentrum in lineaire extrusie met Aspose.3D voor Java

## Invoering

In de wereld van 3D-graphics en Java-programmeren speelt het besturen van het centrum bij lineaire extrusie een cruciale rol bij het bereiken van de gewenste effecten in uw projecten. Aspose.3D voor Java biedt een krachtige toolkit om dergelijke taken naadloos uit te voeren. In deze tutorial duiken we in het proces van het besturen van het centrum in lineaire extrusie met behulp van Aspose.3D voor Java, waarbij we elke stap opsplitsen om een soepel en uitgebreid begrip te garanderen.

## Vereisten

Voordat we aan dit zelfstudietraject beginnen, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

1. Java-ontwikkelomgeving: Zorg ervoor dat er een Java-ontwikkelomgeving op uw computer is geïnstalleerd.

2.  Aspose.3D voor Java: Download en installeer de Aspose.3D-bibliotheek. U kunt de bibliotheek en de bijbehorende documentatie vinden[hier](https://reference.aspose.com/3d/java/).

3. Documentmap: maak een map om uw Java-documenten op te slaan. Laten we het 'Uw documentenmap' noemen.

## Pakketten importeren

Importeer in uw Java-ontwikkelomgeving de benodigde pakketten voor Aspose.3D. Dit zorgt ervoor dat uw code toegang heeft tot de functionaliteiten van de bibliotheek.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Stap 1: Stel het basisprofiel in

Initialiseer het te extruderen basisprofiel. In dit voorbeeld gebruiken we een rechthoekige vorm met een afrondingsstraal van 0,3.

```java
// Het pad naar de documentenmap.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Stap 2: Maak een 3D-scène

Leg de basis van uw 3D-wereld door een scène te creëren.

```java
Scene scene = new Scene();
```

## Stap 3: Maak linker- en rechterknooppunten

Creëer linker- en rechterknooppunten binnen uw scène. Deze knooppunten dienen als canvas voor uw 3D-objecten.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Stap 4: Lineaire extrusie met centrale eigenschap

Voer lineaire extrusie uit op het linkerknooppunt zonder centrering en stel het aantal plakjes in op 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Stap 5: Stel het grondvlak in ter referentie

Verbeter de visuele weergave door een grondvlak aan het linkerknooppunt toe te voegen.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Stap 6: Lineaire extrusie met centrale eigenschap (rechterknooppunt)

Voer lineaire extrusie uit op het rechterknooppunt, centreer deze keer de extrusie, en stel het aantal plakjes opnieuw in op 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Stap 7: Stel het grondvlak in ter referentie (rechterknooppunt)

Voeg, net als bij het linkerknooppunt, ter referentie een grondvlak toe aan het rechterknooppunt.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Stap 8: Sla de 3D-scène op

Sla uw 3D-scène op in Wavefront OBJ-formaat.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusie

Het besturen van het centrum in lineaire extrusie met Aspose.3D voor Java opent opwindende mogelijkheden in de ontwikkeling van 3D-graphics. Door deze stapsgewijze handleiding te volgen, heeft u geleerd hoe u de eigenschap center kunt manipuleren, zodat u de gewenste visuele effecten in uw Java-projecten kunt bereiken.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor Java gebruiken in commerciële projecten?

 A1: Ja, Aspose.3D voor Java is beschikbaar voor commercieel gebruik. Ga voor licentiegegevens naar[hier](https://purchase.aspose.com/buy).

### Vraag 2: Is er een gratis proefversie beschikbaar?

 A2: Ja, u kunt een gratis proefversie van Aspose.3D voor Java uitproberen[hier](https://releases.aspose.com/).

### V3: Waar kan ik ondersteuning vinden voor Aspose.3D voor Java?

 A3: Het Aspose.3D-communityforum is een geweldige plek om ondersteuning te zoeken en uw ervaringen te delen. Bezoek het forum[hier](https://forum.aspose.com/c/3d/18).

### Vraag 4: Heb ik een tijdelijke licentie nodig om te testen?

A4: Ja, als u een tijdelijke licentie nodig heeft voor testdoeleinden, kunt u deze verkrijgen[hier](https://purchase.aspose.com/temporary-license/).

### Vraag 5: Waar kan ik de documentatie vinden?

 A5: De documentatie voor Aspose.3D voor Java is beschikbaar[hier](https://reference.aspose.com/3d/java/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
