---
title: Offset torsione nell'estrusione lineare
linktitle: Offset torsione nell'estrusione lineare
second_title: API Aspose.3D .NET
description: Esplora la magia di Aspose.3D per .NET con la nostra guida passo passo su Twist Offset nell'estrusione lineare. Migliora i tuoi progetti 3D senza sforzo.
type: docs
weight: 15
url: /it/net/3d-modeling/linear-extrusion/twist-offset-in-linear-extrusion/
---
## introduzione

Benvenuti nel mondo di Aspose.3D per .NET, una libreria versatile che consente agli sviluppatori di gestire facilmente la manipolazione 3D. In questo tutorial, approfondiremo una delle funzionalità più interessanti: il "Twist Offset nell'estrusione lineare". Se sei pronto per migliorare le tue capacità di programmazione 3D, tuffiamoci subito!

## Prerequisiti

Prima di intraprendere questo entusiasmante viaggio, assicurati di possedere i seguenti prerequisiti:

-  Aspose.3D per .NET Library: scarica e installa la libreria da[pagina di rilascio](https://releases.aspose.com/3d/net/).

- Il tuo ambiente di sviluppo: assicurati che il tuo ambiente di sviluppo sia configurato e pronto per essere utilizzato.

## Importa spazi dei nomi

Inizia importando gli spazi dei nomi necessari per accedere alle funzionalità fornite da Aspose.3D per .NET. Nel tuo codice, questo potrebbe essere simile a:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Ora, suddividiamo l'esempio in passaggi gestibili per padroneggiare l'offset di torsione nell'estrusione lineare:

## Passaggio 1: inizializzare il profilo di base

Inizia creando un profilo di base, qui esemplificato da una forma rettangolare con un raggio di arrotondamento specificato.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passaggio 2: crea una scena

Genera una scena 3D per ospitare i tuoi nodi e le tue forme.

```csharp
Scene scene = new Scene();
```

## Passaggio 3: crea nodi

Costruisci nodi all'interno della scena, sia a sinistra che a destra.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(18, 0, 0);
```

## Passaggio 4: estrusione lineare sul nodo sinistro

Esegui l'estrusione lineare sul nodo sinistro utilizzando la proprietà twist e slice.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Passaggio 5: estrusione lineare sul nodo destro con offset di torsione

Sul nodo destro, esegui l'estrusione lineare utilizzando le proprietà torsione, offset torsione e fette.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, TwistOffset = new Vector3(3, 0, 0) });
```

## Passaggio 6: salva la scena 3D

Salva la scena 3D nella directory di output desiderata, specificando il formato file come WavefrontOBJ.

```csharp
scene.Save("Your Output Directory" + "TwistOffsetInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Congratulazioni! Hai implementato con successo Twist Offset nell'estrusione lineare utilizzando Aspose.3D per .NET.

## Conclusione

In questo tutorial, abbiamo esplorato le potenti funzionalità di Aspose.3D per .NET, concentrandoci in particolare su Twist Offset nell'estrusione lineare. Con queste nuove competenze, sei ben attrezzato per infondere dinamismo nei tuoi progetti 3D.

## Domande frequenti

### Q1: posso utilizzare Aspose.3D per .NET con altri linguaggi di programmazione?

A1: Aspose.3D supporta principalmente i linguaggi .NET, ma Aspose fornisce librerie simili per Java e altre piattaforme.

### Q2: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?

 A2: Visita[questo link](https://purchase.aspose.com/temporary-license/)acquisire una licenza temporanea a scopo di test.

### Q3: Esiste un forum della community per Aspose.3D per .NET?

 A3: Assolutamente! Unisciti alla comunità su[Aspose.3D Forum](https://forum.aspose.com/c/3d/18) per interagire con altri sviluppatori e chiedere assistenza.

### Q4: Sono disponibili ulteriori esempi e documentazione?

 A4: Esplora il[documentazione](https://reference.aspose.com/3d/net/) per guide ed esempi esaustivi.

### Q5: Dove posso acquistare Aspose.3D per .NET?

 A5: Vai a[questo link](https://purchase.aspose.com/buy) per effettuare un acquisto e sbloccare tutto il potenziale di Aspose.3D.