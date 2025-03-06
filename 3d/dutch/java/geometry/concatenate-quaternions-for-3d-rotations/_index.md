---
title: Voeg quaternions samen voor 3D-rotaties in Java met Aspose.3D
linktitle: Voeg quaternions samen voor 3D-rotaties in Java met Aspose.3D
second_title: Aspose.3D Java-API
description: Leer hoe u quaternionen aaneenschakelt voor 3D-rotaties in Java met behulp van Aspose.3D. Volg onze stapsgewijze handleiding voor naadloze animatietransformaties.
weight: 11
url: /nl/java/geometry/concatenate-quaternions-for-3d-rotations/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Voeg quaternions samen voor 3D-rotaties in Java met Aspose.3D

## Invoering

Quaternion-aaneenschakeling is een fundamenteel concept in 3D-graphics, waardoor u meerdere rotatietransformaties naadloos kunt combineren. Aspose.3D vereenvoudigt dit proces in Java en biedt een efficiënte en intuïtieve manier om quaternion-bewerkingen af te handelen. In deze zelfstudie begeleiden we u bij het aaneenschakelen van quaternionen en het toepassen ervan op 3D-objecten met behulp van Aspose.3D.

## Vereisten

Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

- Basiskennis van Java-programmeren.
- Aspose.3D voor Java geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/java/).

## Pakketten importeren

Zorg ervoor dat u de benodigde pakketten importeert om de Aspose.3D-functionaliteiten te benutten. Neem de volgende regels op in uw Java-code:

```java
import com.aspose.threed.*;
```

Laten we nu de voorbeeldcode in meerdere stappen opsplitsen om een uitgebreide tutorial te maken:

## Stap 1: Stel de scène in

```java
Scene scene = new Scene();
```

## Stap 2: Definieer quaternionen

```java
Quaternion q1 = Quaternion.fromEulerAngle(Math.PI * 0.5, 0, 0);
Vector3.X_AXIS.x = 3;
Quaternion q2 = Quaternion.fromAngleAxis(-Math.PI * 0.5, Vector3.X_AXIS);
```

## Stap 3: Quaternionen aaneenschakelen

```java
Quaternion q3 = q1.concat(q2);
```

## Stap 4: Maak 3 cilinders

```java
Node cylinder = scene.getRootNode().createChildNode("cylinder-q1", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q1);
cylinder.getTransform().setTranslation(new Vector3(-5, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q2", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q2);
cylinder.getTransform().setTranslation(new Vector3(0, 2, 0));
```

```java
cylinder = scene.getRootNode().createChildNode("cylinder-q3", new Cylinder(0.1, 1, 2));
cylinder.getTransform().setRotation(q3);
cylinder.getTransform().setTranslation(new Vector3(5, 2, 0));
```

## Stap 5: Opslaan in bestand

```java
MyDir = MyDir + "test_out.fbx";
scene.save(MyDir, FileFormat.FBX7400ASCII);
// ExEnd:Quaternionen samenvoegen
```

## Stap 6: Succesbericht afdrukken

```java
System.out.println("\nQuaternions concatenated successfully.\nFile saved at " + MyDir);
```

## Conclusie

Door deze tutorial te volgen, heb je geleerd hoe je quaternionen aaneenschakelt voor 3D-rotaties in Java met behulp van Aspose.3D. Experimenteer met verschillende quaternioncombinaties om diverse en nauwkeurige rotaties in uw 3D-projecten te bereiken.

## Veelgestelde vragen

### V1: Kan ik Aspose.3D voor Java gratis gebruiken?

 A1: Aspose.3D biedt een[gratis proefperiode](https://releases.aspose.com/) zodat u de functies ervan kunt verkennen. Voor langdurig gebruik kunt u overwegen een[licentie](https://purchase.aspose.com/buy).

### V2: Waar kan ik uitgebreide documentatie voor Aspose.3D vinden?

 A2: De[documentatie](https://reference.aspose.com/3d/java/) biedt gedetailleerde informatie en voorbeelden om u op weg te helpen.

### Vraag 3: Hoe kan ik ondersteuning zoeken voor Aspose.3D?

 A3: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om vragen te stellen, ervaringen te delen en hulp te krijgen van de gemeenschap.

### V4: Zijn er tijdelijke licenties beschikbaar voor Aspose.3D?

 A4: Ja, u kunt een[tijdelijke licentie](https://purchase.aspose.com/temporary-license/) voor test- en evaluatiedoeleinden.

### Vraag 5: Welke bestandsformaten worden ondersteund voor het opslaan van 3D-scènes?

A5: Aspose.3D ondersteunt verschillende formaten en u kunt scènes opslaan in FBX-formaat, zoals gedemonstreerd in deze tutorial.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
