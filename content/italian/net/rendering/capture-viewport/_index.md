---
title: Catturare le finestre nelle scene 3D
linktitle: Catturare le finestre nelle scene 3D
second_title: API Aspose.3D .NET
description: Impara a catturare straordinarie visualizzazioni 3D utilizzando Aspose.3D per .NET. Guida passo passo per eseguire il rendering delle scene con flessibilità.
type: docs
weight: 11
url: /it/net/rendering/capture-viewport/
---
## introduzione

Nel regno della grafica e della visualizzazione 3D, catturare le finestre è un'abilità essenziale che migliora la profondità e il dettaglio delle scene. Aspose.3D per .NET fornisce una soluzione solida per il rendering e la manipolazione di scene 3D. Questo tutorial ti guiderà attraverso il processo di acquisizione dei viewport nelle scene 3D utilizzando Aspose.3D, consentendoti di creare visualizzazioni straordinarie con facilità.

## Prerequisiti

Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:

-  Libreria Aspose.3D per .NET: assicurati di avere la libreria Aspose.3D installata. Puoi scaricarlo da[Qui](https://releases.aspose.com/3d/net/).

## Importa spazi dei nomi

Per iniziare, importa gli spazi dei nomi necessari nel tuo progetto .NET:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using System.Drawing;
using System.Drawing.Imaging;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
```

## Passaggio 1: caricare una scena 3D esistente

Inizia caricando una scena 3D esistente nel tuo progetto. Il seguente frammento di codice lo dimostra:

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

## Passaggio 2: crea una fotocamera

Successivamente, crea un'istanza della telecamera e impostane la posizione e il target:

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

## Passaggio 3: aggiungi l'illuminazione alla scena

Migliora la tua scena aggiungendo una fonte di luce. Lo snippet di codice seguente mostra come creare una luce puntiforme:

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

## Passaggio 4: configura il renderer e la destinazione del rendering

Imposta il renderer e crea una destinazione di rendering per catturare la scena:

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    renderer.EnableShadows = false;

    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // ... (continua nei passi successivi)
    }
}
```

## Passaggio 5: definire le finestre e il rendering

Definisci le finestre ed esegui il rendering della scena per generare immagini di output:

```csharp
Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-1viewports_out.png", ImageFormat.Png);
```

## Passaggio 6: modifica le finestre e esegui nuovamente il rendering

Modifica le finestre e renderizza nuovamente la scena, dimostrando la flessibilità di Aspose.3D:

```csharp
vp.Area = new RelativeRectangle() { ScaleWidth = 0.5f, ScaleHeight = 1 };
rt.CreateViewport(camera, new RelativeRectangle() { ScaleX = 0.5f, ScaleWidth = 0.5f, ScaleHeight = 1 });
camera.FieldOfView = 90;
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "file-2viewports_out.png", ImageFormat.Png);
```

Continua a sperimentare diverse configurazioni per ottenere gli effetti visivi desiderati.

## Conclusione

In questo tutorial, abbiamo esplorato il processo di acquisizione dei viewport nelle scene 3D utilizzando Aspose.3D per .NET. Sfruttando le sue potenti funzionalità, puoi elevare i tuoi progetti di grafica 3D a nuovi livelli, offrendo esperienze visive accattivanti.

## Domande frequenti

### Q1: Aspose.3D è compatibile con altri formati di file 3D?

A1: Sì, Aspose.3D supporta vari formati di file 3D, garantendo la compatibilità con un'ampia gamma di strumenti di progettazione.

### Q2: Posso utilizzare Aspose.3D per lo sviluppo di giochi?

A2: Sebbene Aspose.3D sia progettato principalmente per la grafica e la visualizzazione, le sue funzionalità possono integrare alcuni aspetti dello sviluppo del gioco.

### Q3: Dove posso trovare ulteriori esempi e documentazione?

 A3: Esplora il completo[Documentazione Aspose.3D](https://reference.aspose.com/3d/net/) per ulteriori esempi e informazioni dettagliate.

### Q4: È disponibile una prova gratuita?

 R4: Sì, puoi accedere a una prova gratuita[Qui](https://releases.aspose.com/).

### Q5: Come posso chiedere aiuto o partecipare alla comunità?

 A5: Unisciti alla comunità Aspose.3D su[Forum di assistenza](https://forum.aspose.com/c/3d/18) per assistenza e collaborazione.