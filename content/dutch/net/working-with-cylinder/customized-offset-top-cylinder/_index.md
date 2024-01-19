---
title: Aangepaste offset-topcilinder
linktitle: Aangepaste offset-topcilinder
second_title: Aspose.3D .NET-API
description: Ontdek de wonderen van 3D-graphics met Aspose.3D voor .NET. Leer moeiteloos op maat gemaakte offset-topcilinders maken. Verbeter nu uw codeerervaring!
type: docs
weight: 11
url: /nl/net/working-with-cylinder/customized-offset-top-cylinder/
---
## Invoering
Welkom in de wereld van 3D grafische manipulatie met Aspose.3D voor .NET! In deze zelfstudie begeleiden we u bij het maken van een aangepaste offset-topcilinder met behulp van Aspose.3D, een krachtige bibliotheek voor het werken met 3D-scènes, objecten en formaten in .NET-toepassingen.
## Vereisten
Voordat we ingaan op de tutorial, zorg ervoor dat je aan de volgende vereisten voldoet:
- Basiskennis van de programmeertaal C#.
- Visual Studio is op uw computer geïnstalleerd.
- Aspose.3D voor .NET-bibliotheek gedownload en waarnaar wordt verwezen in uw project.
Laten we nu aan de slag gaan met de stapsgewijze handleiding!
## Naamruimten importeren
Zorg er eerst voor dat u de benodigde naamruimten in uw C#-code importeert:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Stap 1: Maak een scène
```csharp
// Creëer een scène
Scene scene = new Scene();
```
Hiermee wordt een nieuwe 3D-scène geïnitialiseerd met behulp van Aspose.3D.
## Stap 2: Initialiseer de cilinder
```csharp
// Initialiseer de cilinder
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Hier maken we een cilinder met specifieke parameters zoals straal, hoogte en plakjes.
## Stap 3: Stel OffsetTop in voor de eerste cilinder
```csharp
// OffsetTop instellen
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Hiermee wordt een aangepaste offset-top voor de eerste cilinder ingesteld.
## Stap 4: Creëer ChildNode voor de eerste cilinder
```csharp
// Maak een ChildNode
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
We voegen de eerste cilinder als een kindknooppunt aan de scène toe en passen de positie ervan aan.
## Stap 5: Initialiseer de tweede cilinder
```csharp
//Initialiseer de tweede cilinder zonder aangepaste OffsetTop
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Een tweede cilinder wordt geïnitialiseerd zonder een aangepaste offset-top.
## Stap 6: Creëer ChildNode voor de tweede cilinder
```csharp
// Maak een ChildNode
scene.RootNode.CreateChildNode(cylinder2);
```
We voegen de tweede cilinder als een kindknooppunt aan de scène toe.
## Stap 7: Sla de scène op
```csharp
// Redden
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Hierdoor wordt de 3D-scène, inclusief de aangepaste offset-topcilinder, opgeslagen in het Wavefront OBJ-formaat.
Nu hebt u met succes een aangepaste offset-topcilinder gemaakt met Aspose.3D voor .NET!
## Conclusie
In deze zelfstudie hebben we de basisbeginselen van het werken met Aspose.3D voor .NET onderzocht om een aangepaste offset-topcilinder te maken. Deze bibliotheek biedt eindeloze mogelijkheden voor manipulatie van 3D-afbeeldingen binnen uw .NET-toepassingen.
## Veelgestelde vragen
### Vraag: Waar kan ik de documentatie voor Aspose.3D voor .NET vinden?
 A: De documentatie is beschikbaar[hier](https://reference.aspose.com/3d/net/).
### Vraag: Hoe kan ik Aspose.3D downloaden voor .NET?
 EEN: Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).
### Vraag: Is er een gratis proefversie beschikbaar voor Aspose.3D voor .NET?
 A: Ja, u kunt een gratis proefperiode krijgen[hier](https://releases.aspose.com/).
### Vraag: Waar kan ik ondersteuning krijgen voor Aspose.3D voor .NET?
 A: Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) Voor ondersteuning.
### Vraag: Kan ik een tijdelijke licentie verkrijgen voor Aspose.3D voor .NET?
 A: Ja, u kunt een tijdelijke licentie krijgen[hier](https://purchase.aspose.com/temporary-license/).