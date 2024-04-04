---
title: Conversione di materiale da non PBR a PBR
linktitle: Conversione di materiale da non PBR a PBR
second_title: API Aspose.3D .NET
description: Esplora Aspose.3D per .NET converti materiali non PBR in PBR senza sforzo. Tutorial completo e API potente.
type: docs
weight: 16
url: /it/net/loading-and-saving/gltf/non-pbr-to-pbr-material-conversion/
---
## introduzione

Benvenuti in questa guida passo passo sull'utilizzo di Aspose.3D per .NET per convertire materiali non PBR (rendering basato fisicamente) in materiali PBR. Aspose.3D è una potente API che consente agli sviluppatori di lavorare senza problemi con i formati di file 3D nelle loro applicazioni .NET.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di possedere i seguenti prerequisiti:

-  Aspose.3D per .NET: assicurati di avere la libreria Aspose.3D per .NET installata. È possibile trovare il collegamento per il download[Qui](https://releases.aspose.com/3d/net/).

- Comprensione di base di C#: questo tutorial presuppone che tu abbia una conoscenza di base della programmazione C#.

- IDE (ambiente di sviluppo integrato): scegli il tuo IDE preferito per lo sviluppo .NET, come Visual Studio.

## Importa spazi dei nomi

Nel codice C#, inizia importando gli spazi dei nomi necessari:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Passaggio 1: inizializza una nuova scena 3D

Inizia creando una nuova scena 3D utilizzando il seguente codice:

```csharp
// ExStart:Non_PBRtoPBRMaterial
// inizializzare una nuova scena 3D
var scene = new Scene();
```

## Passaggio 2: crea un oggetto 3D

Successivamente, crea un oggetto 3D, ad esempio una scatola:

```csharp
var box = new Box();
scene.RootNode.CreateChildNode("box1", box).Material = new PhongMaterial() { DiffuseColor = new Vector3(1, 0, 1) };
```

## Passaggio 3: configurare la conversione del materiale

Imposta le opzioni di conversione del materiale per la conversione da non PBR a PBR:

```csharp
GltfSaveOptions options = new GltfSaveOptions(FileFormat.GLTF2);
options.MaterialConverter = delegate (Material material)
{
    PhongMaterial phongMaterial = (PhongMaterial)material;
    return new PbrMaterial() { Albedo = new Vector3(phongMaterial.DiffuseColor.x, phongMaterial.DiffuseColor.y, phongMaterial.DiffuseColor.z) };
};
```

## Passaggio 4: salva nel formato GLTF 2.0

Salva la scena convertita in formato GLTF 2.0:

```csharp
scene.Save("Your Output Directory" + "Non_PBRtoPBRMaterial_Out.gltf", options);
// ExEnd:Non_PBRtoPBRMaterial
```

Ripeti questi passaggi secondo necessità per il tuo caso d'uso specifico, assicurandoti che ogni dettaglio sia configurato correttamente.

## Conclusione

Congratulazioni! Hai imparato con successo come convertire materiali non PBR in PBR utilizzando Aspose.3D per .NET. Questo potente strumento apre infinite possibilità per la manipolazione della grafica 3D nelle tue applicazioni .NET.

## Domande frequenti

### Q1: Aspose.3D è compatibile con tutti i formati di file 3D?

A1: Sì, Aspose.3D supporta un'ampia gamma di formati di file 3D, offrendo flessibilità nei tuoi progetti.

### Q2: Posso utilizzare Aspose.3D per applicazioni commerciali?

 A2: Assolutamente! Aspose.3D è un prodotto commerciale e puoi acquistarlo[Qui](https://purchase.aspose.com/buy).

### Q3: Ho bisogno di una licenza temporanea per i test?

 R3: Sì, puoi ottenere una licenza temporanea a scopo di test[Qui](https://purchase.aspose.com/temporary-license/).

### Q4: Dove posso trovare supporto per Aspose.3D?

 A4: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.

### Q5: È disponibile una prova gratuita?

 R5: Sì, puoi esplorare una versione di prova gratuita[Qui](https://releases.aspose.com/).