---
title: Esportazione di scene 3D in formato AMF compresso
linktitle: Esportazione di scene 3D in formato AMF compresso
second_title: API Aspose.3D .NET
description: Scopri come esportare scene 3D in formato AMF compresso utilizzando Aspose.3D per .NET. Migliora le tue capacità di sviluppo con questa guida passo passo.
type: docs
weight: 11
url: /it/net/3d-scene/export-scene-compressed-amf/
---
## introduzione

Nel mondo dinamico della modellazione e del rendering 3D, efficienza e flessibilità sono fondamentali. Aspose.3D per .NET consente agli sviluppatori di esportare senza problemi scene 3D nel formato compresso AMF (Additive Manufacturing File), garantendo dimensioni di file ottimali senza compromettere la qualità. Questo tutorial ti guiderà attraverso il processo passo dopo passo, rendendo facile sia ai principianti che agli sviluppatori esperti sfruttare le funzionalità di Aspose.3D per .NET.

## Prerequisiti

Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:

- Conoscenza di base dei concetti di modellazione 3D
- Visual Studio installato sul tuo computer
-  Aspose.3D per la libreria .NET. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/)
- Il desiderio di migliorare le tue capacità di sviluppo 3D!

## Importa spazi dei nomi

Nel tuo progetto, assicurati di importare gli spazi dei nomi necessari per sfruttare la funzionalità di Aspose.3D per .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Passaggio 1: carica una scena 3D

Inizia caricando una scena 3D utilizzando Aspose.3D per .NET. Crea un oggetto scena e aggiungi entità come scatole:

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## Passaggio 2: trasformazione in scala

Successivamente, applica una trasformazione di scala a un'altra casella nella scena:

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(5, 5, 5);
```

## Passaggio 3: impostare gli angoli di Eulero

Imposta gli angoli di Eulero per la trasformazione:

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## Passaggio 4: crea nodi secondari

Continua a costruire la scena creando nodi figlio:

```csharp
scene.RootNode.CreateChildNode();
scene.RootNode.CreateChildNode().CreateChildNode(box);
scene.RootNode.CreateChildNode().CreateChildNode(box);
```

## Passaggio 5: salva il file AMF compresso

Infine, salva la scena 3D in un file AMF compresso nella directory di output desiderata:

```csharp
scene.Save("Your Output Directory" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## Conclusione

Congratulazioni! Hai esportato con successo una scena 3D in un formato AMF compresso utilizzando Aspose.3D per .NET. Questa potente libreria apre un mondo di possibilità per gli sviluppatori 3D, consentendo loro di creare modelli efficienti e visivamente sorprendenti.

## Domande frequenti

### Q1: Aspose.3D è compatibile con i più diffusi software di modellazione 3D?

R1: Aspose.3D supporta vari formati di file, rendendolo compatibile con i più diffusi strumenti di modellazione 3D.

### Q2: Posso abilitare la compressione per altri formati di file oltre a AMF?

A2: Sì, Aspose.3D fornisce opzioni per abilitare la compressione per vari formati di file.

### Q3: Aspose.3D è adatto sia ai principianti che agli sviluppatori avanzati?

A3: Assolutamente! Aspose.3D offre semplicità per i principianti e funzionalità avanzate per sviluppatori esperti.

### Q4: Esistono limitazioni sulle dimensioni delle scene 3D che possono essere esportate?

A4: Aspose.3D è progettato per gestire scene di varia complessità e non esistono limiti di dimensione rigorosi.

### Q5: Dove posso trovare ulteriore supporto e discussioni nella community?

 A5: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per supporto e discussioni.