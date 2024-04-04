---
title: Aangepaste schuifbodemcilinder
linktitle: Aangepaste schuifbodemcilinder
second_title: Aspose.3D .NET-API
description: Leer hoe u aangepaste schuifbodemcilinders kunt maken met Aspose.3D voor .NET met onze gedetailleerde stapsgewijze handleiding. Verbeter vandaag nog uw vaardigheden op het gebied van 3D-modelleren!
type: docs
weight: 12
url: /nl/net/3d-modeling/working-with-cylinder/
---
## Invoering
Welkom bij onze uitgebreide handleiding over het maken van een aangepaste cilinder met Aspose.3D voor .NET. Als u uw vaardigheden op het gebied van 3D-modelleren wilt verbeteren en unieke functies aan uw projecten wilt toevoegen, bent u hier aan het juiste adres. In deze tutorial leiden we u stap voor stap door het proces, aan de hand van duidelijke uitleg en codefragmenten.
## Vereisten
Voordat we ingaan op de tutorial, zorg ervoor dat je over het volgende beschikt:
- Basiskennis van programmeren in C# en .NET.
-  Aspose.3D voor .NET-bibliotheek geïnstalleerd. Je kunt het downloaden[hier](https://releases.aspose.com/3d/net/).
- Een ontwikkelomgeving opgezet voor .NET-programmering.
## Naamruimten importeren
Begin in uw C#-code met het importeren van de benodigde naamruimten:
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
Begin met het maken van een 3D-scène met Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Stap 2: Maak cilinder 1
Genereer de eerste cilinder en stel de eigenschappen ervan in:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Stap 3: Pas de afschuifbodem voor cilinder 1 aan
Breng een aangepaste schuifbodem aan op de eerste cilinder:
```csharp
//Afschuiving 47,5 graden in het xy-vlak (z-as)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Stel GenerateFanCylinder in op true
cylinder1.GenerateFanCylinder = true;
// Stel Thetalengte in
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// OffsetTop instellen
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## Stap 4: Voeg cilinder 1 toe aan de scène
Voeg de eerste cilinder toe aan de scène en stel de vertaling in:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Stap 5: Maak cilinder 2
Genereer een tweede cilinder met vergelijkbare eigenschappen:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Stap 6: Voeg cilinder 2 toe aan de scène
Voeg de tweede cilinder toe aan de scène zonder aangepaste parameters:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Stap 7: Sla de scène op
Sla de scène op als een Wavefront OBJ-bestand in uw documentmap:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusie
Gefeliciteerd! U hebt met succes een aangepaste schuifbodemcilinder gemaakt met Aspose.3D voor .NET. Deze tutorial was bedoeld om een stapsgewijze handleiding te bieden voor gebruikers met verschillende niveaus van expertise op het gebied van 3D-modellering en -programmering.
## Veel Gestelde Vragen
### Is Aspose.3D voor .NET geschikt voor beginners?
Absoluut! Aspose.3D voor .NET biedt een gebruiksvriendelijke interface, waardoor het toegankelijk is voor zowel beginners als ervaren ontwikkelaars.
### Kan ik verschillende schuifhoeken toepassen op cilinders?
Ja, u kunt de schuifbodem voor elke cilinder afzonderlijk aanpassen, waardoor u unieke effecten kunt bereiken.
### Is er een proefversie beschikbaar?
 Ja, u kunt de gratis proefversie verkennen[hier](https://releases.aspose.com/).
### Waar kan ik aanvullende ondersteuning vinden?
 Bezoek de[Aspose.3D-forum](https://forum.aspose.com/c/3d/18) voor gemeenschapsondersteuning en discussies.
### Hoe kan ik een tijdelijke licentie verkrijgen?
 Haal uw tijdelijke licentie[hier](https://purchase.aspose.com/temporary-license/).