---
title: Exporteren naar PLY-formaat als puntenwolk
linktitle: Exporteren naar PLY-formaat als puntenwolk
second_title: Aspose.3D .NET-API
description: Ontdek de wereld van 3D-modellering met Aspose.3D voor .NET. Leer moeiteloos modellen naar PLY-formaat te exporteren. Breng uw projecten naar een hoger niveau met verbluffende beelden.
weight: 16
url: /nl/net/loading-and-saving/ply/export-to-ply-point-cloud/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Exporteren naar PLY-formaat als puntenwolk

## Invoering
In de dynamische wereld van 3D-modellering en -ontwikkeling onderscheidt Aspose.3D voor .NET zich als een krachtige toolkit. Deze tutorial leidt u door het proces van het exporteren van 3D-modellen naar PLY-indeling als een puntenwolk met behulp van Aspose.3D voor .NET. Als u klaar bent om uw projecten te verbeteren met verbluffende beelden, volg dan mee en ontgrendel het volledige potentieel van deze veelzijdige bibliotheek.
## Vereisten
Voordat u in de zelfstudie duikt, moet u ervoor zorgen dat u aan de volgende vereisten voldoet:
-  Aspose.3D voor .NET: Download en installeer de bibliotheek van de[downloadpagina](https://releases.aspose.com/3d/net/).
- Ontwikkelomgeving: Stel de .NET-ontwikkelomgeving van uw voorkeur in, zoals Visual Studio.
## Naamruimten importeren
Om aan de slag te gaan met Aspose.3D voor .NET importeert u de benodigde naamruimten in uw project:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Stap 1: Maak een 3D-model
Begin met het maken van een 3D-model dat u als puntenwolk wilt exporteren. Laten we bijvoorbeeld een bol maken:
```csharp
Sphere sphere = new Sphere();
```
## Stap 2: Definieer de exportinstellingen
Geef de exportinstellingen op, inclusief het bestandsformaat (PLY) en schakel de puntenwolkexport in:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## Stap 3: Stel het exportpad in
Bepaal de map waarin u het geëxporteerde PLY-bestand wilt opslaan:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## Stap 4: Coderen en exporteren
 Maak gebruik van de`Encode` methode om het 3D-model naar PLY-formaat te exporteren:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## Conclusie
Gefeliciteerd! U hebt met succes een 3D-model naar PLY-indeling geëxporteerd als een puntenwolk met Aspose.3D voor .NET. Dit opent eindeloze mogelijkheden voor het integreren van meeslepende beelden in uw toepassingen.

## Veelgestelde vragen
### 1. Is Aspose.3D compatibel met alle .NET-frameworks?
Aspose.3D ondersteunt verschillende .NET-frameworks, waardoor compatibiliteit binnen een breed scala aan ontwikkelomgevingen wordt gegarandeerd.
### 2. Kan ik Aspose.3D gebruiken voor commerciële projecten?
 Absoluut! Aspose.3D biedt flexibele licentieopties, inclusief commercieel gebruik. Bekijk de[aankooppagina](https://purchase.aspose.com/buy) voor details.
### 3. Hoe kan ik ondersteuning krijgen voor Aspose.3D?
 Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) om verbinding te maken met de gemeenschap en hulp te krijgen van experts.
### 4. Is er een gratis proefperiode beschikbaar?
 Ja, verken de functies met een[gratis proefperiode](https://releases.aspose.com/) voordat u een toezegging doet.
### 5. Hoe verkrijg ik een tijdelijke licentie?
 Ga voor tijdelijke licentieopties naar[deze link](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
