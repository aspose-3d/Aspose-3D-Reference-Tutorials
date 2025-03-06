---
title: Centro nell'estrusione lineare
linktitle: Centro nell'estrusione lineare
second_title: API Aspose.3D .NET
description: Esplora il mondo della modellazione 3D con Aspose.3D per .NET. Centrare le tecniche di estrusione lineare, creare design straordinari e liberare la tua creatività.
weight: 10
url: /it/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Centro nell'estrusione lineare

## introduzione

Benvenuti in questa guida completa sulla padronanza dell'estrusione lineare utilizzando Aspose.3D per .NET. Se stai cercando di migliorare le tue capacità di modellazione 3D e creare estrusioni straordinarie, sei nel posto giusto. In questo tutorial approfondiremo la tecnica dell'estrusione lineare, concentrandoci in particolare sull'aspetto della centratura per portare i tuoi progetti a un livello completamente nuovo.

## Prerequisiti

Prima di intraprendere questo entusiasmante viaggio, assicurati di possedere i seguenti prerequisiti:

- Conoscenza base del linguaggio di programmazione C#.
- Visual Studio installato sul tuo computer.
-  Aspose.3D per la libreria .NET, che puoi scaricare da[Documentazione Aspose.3D .NET](https://reference.aspose.com/3d/net/).
-  Assicurati di avere accesso a[Documentazione Aspose.3D .NET](https://reference.aspose.com/3d/net/) come riferimento durante il tutorial.

## Importa spazi dei nomi

Per iniziare, importiamo gli spazi dei nomi necessari. Questi getteranno le basi per il nostro capolavoro di modellazione 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Passaggio 1: inizializzare il profilo di base

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passaggio 2: crea una scena 3D

```csharp
Scene scene = new Scene();
```

## Passaggio 3: crea i nodi sinistro e destro

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Passaggio 4: eseguire l'estrusione lineare sul nodo sinistro

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Passaggio 5: impostare il piano terra come riferimento

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Passaggio 6: eseguire l'estrusione lineare sul nodo destro

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Passaggio 7: impostare il piano terra come riferimento (nodo destro)

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Passaggio 8: salva la scena 3D

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Conclusione

Congratulazioni! Hai padroneggiato con successo l'arte dell'estrusione lineare con centratura utilizzando Aspose.3D per .NET. Sentiti libero di sperimentare diversi parametri ed esplorare le vaste possibilità offerte da questa tecnica.

## Domande frequenti

### Q1: posso utilizzare Aspose.3D per .NET con altri linguaggi di programmazione?

A1: Aspose.3D supporta principalmente linguaggi .NET come C# e VB.NET.

### Q2: Dove posso trovare supporto per le query relative ad Aspose.3D?

 A2: Visita il[Aspose.3D Forum](https://forum.aspose.com/c/3d/18) per supporto e discussioni dedicate.

### Q3: È disponibile una prova gratuita per Aspose.3D per .NET?

 R3: Sì, puoi accedere alla prova gratuita[Qui](https://releases.aspose.com/).

### Q4: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?

 A4: È possibile acquisire una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).

### Q5: Dove posso acquistare la licenza Aspose.3D per .NET?

 A5: Acquista la tua licenza[Qui](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
