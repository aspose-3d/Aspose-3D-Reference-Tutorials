---
title: CancellationToken gebruiken
linktitle: CancellationToken gebruiken
second_title: Aspose.3D .NET-API
description: Ontdek de naadloze wereld van 3D-modellering met Aspose.3D voor .NET. Leer hoe u 3D-documenten efficiënt kunt laden en opslaan met CancellationToken.
weight: 10
url: /nl/net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# CancellationToken gebruiken

## Invoering

Welkom bij onze uitgebreide handleiding over het gebruik van Aspose.3D voor .NET om uw 3D-modellerings- en renderingprojecten te verbeteren. Aspose.3D is een krachtige bibliotheek waarmee .NET-ontwikkelaars naadloos met 3D-bestanden kunnen werken. In deze tutorial gaan we dieper in op de laad- en opslagaspecten, waarbij we ons specifiek richten op het gebruik van CancellationToken voor efficiënt beheer van asynchrone taken.

## Vereisten

Voordat we aan deze reis beginnen, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:

-  Aspose.3D voor .NET: Download en installeer de bibliotheek van[hier](https://releases.aspose.com/3d/net/).
- .NET-omgeving: Zorg ervoor dat u een compatibele .NET-ontwikkelomgeving hebt ingesteld.
- Basiskennis van C#: Bekendheid met de programmeertaal C# wordt aanbevolen.

## Naamruimten importeren

Om aan de slag te gaan, moet u ervoor zorgen dat u de benodigde naamruimten in uw project opneemt. Deze naamruimten bieden toegang tot de functionaliteiten die nodig zijn voor het manipuleren van 3D-bestanden.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Laden en opslaan - CancellationToken gebruiken

### Stap 1: Maak CancellationTokenSource

```csharp
// ExStart: CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Hier instantiëren we een CancellationTokenSource, een cruciaal onderdeel voor het beheren van annuleringen bij asynchrone bewerkingen.

### Stap 2: Initialiseer de 3D-scène

```csharp
Scene scene = new Scene();
```

Maak een exemplaar van de klasse Scene. Dit zal het canvas zijn voor uw 3D-modelleringsactiviteiten.

### Stap 3: Stel CancellationToken Timeout in

```csharp
cts.CancelAfter(1000);
```

 Stel de annuleringstime-out in met behulp van de`CancelAfter` methode. In dit voorbeeld is de time-out ingesteld op 1000 milliseconden (1 seconde).

### Stap 4: Open 3D-document

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Probeer het 3D-document binnen het opgegeven tijdsbestek te openen. De`cts.Token` parameter zorgt ervoor dat de bewerking kan worden geannuleerd als deze de ingestelde time-out overschrijdt.

### Stap 5: Importuitzondering afhandelen

In het geval van een ImportException moet u deze netjes afhandelen door te controleren of deze is veroorzaakt door een OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd: CancellationTokenSource
```

## Conclusie

Gefeliciteerd! U hebt met succes door het gebruik van Aspose.3D voor .NET met CancellationToken genavigeerd om het laden van 3D-documenten te beheren. Deze techniek zorgt voor efficiënte en tijdige importbewerkingen, waardoor de algehele prestaties van uw 3D-applicaties worden verbeterd.

## Veelgestelde vragen

### Vraag 1: Is Aspose.3D compatibel met alle 3D-bestandsformaten?

 A1: Aspose.3D ondersteunt een breed scala aan 3D-bestandsindelingen, waaronder FBX, STL, OBJ en meer. Verwijs naar de[documentatie](https://reference.aspose.com/3d/net/) voor de volledige lijst.

### Vraag 2: Hoe kan ik een tijdelijke licentie krijgen voor Aspose.3D?

 A2: Verkrijg een tijdelijke licentie door te bezoeken[deze link](https://purchase.aspose.com/temporary-license/).

### V3: Waar kan ik ondersteuning vinden voor Aspose.3D?

 A3: Neem deel aan de communitydiscussie op de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18).

### V4: Kan ik Aspose.3D gratis uitproberen voordat ik een aankoop doe?

 A4: Ja, ontdek de functies met een gratis proefversie[hier](https://releases.aspose.com/).

### V5: Wat is de nieuwste versie van Aspose.3D voor .NET?

 A5: Blijf op de hoogte door de[downloadpagina](https://releases.aspose.com/3d/net/) voor de nieuwste uitgave.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
