---
title: Applicazione di effetti visivi nelle finestre 3D
linktitle: Applicazione di effetti visivi nelle finestre 3D
second_title: API Aspose.3D .NET
description: Esplora il mondo della visualizzazione 3D con Aspose.3D per .NET. Impara ad applicare effetti visivi accattivanti alle tue scene utilizzando tutorial passo passo. Migliora i tuoi progetti con pixelazione, scala di grigi, rilevamento dei bordi ed effetti di sfocatura.
type: docs
weight: 10
url: /it/net/3d-viewports/apply-visual-effects/
---
## introduzione

Migliorare l'attrattiva visiva delle scene 3D è un aspetto cruciale della creazione di esperienze coinvolgenti. Aspose.3D per .NET fornisce un potente set di strumenti per applicare effetti visivi alle finestre 3D. In questo tutorial esamineremo il processo di applicazione di vari effetti a una scena 3D, tra cui pixelizzazione, scala di grigi, rilevamento dei bordi e sfocatura.

## Prerequisiti

Prima di immergerti nel tutorial, assicurati di avere quanto segue:

- Una conoscenza pratica dello sviluppo C# e .NET.
-  Aspose.3D per la libreria .NET installata. Puoi scaricarlo da[Qui](https://releases.aspose.com/3d/net/).
- Un file di scena 3D (ad esempio, "scene.obj") per la sperimentazione.

## Importa spazi dei nomi

Per iniziare, importa gli spazi dei nomi necessari per Aspose.3D e altre dipendenze. Aggiungi le seguenti righe al tuo codice:

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

```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("scene.obj"));
```

 Carica la tua scena 3D utilizzando`Scene` classe.

## Passaggio 2: crea una fotocamera

```csharp
Camera camera = new Camera();
scene.RootNode.CreateChildNode("camera", camera).Transform.Translation = new Vector3(2, 44, 66);
camera.LookAt = new Vector3(50, 12, 0);
```

Crea un'istanza della telecamera e impostane la posizione e il target.

## Passaggio 3: aggiungi luce alla scena

```csharp
scene.RootNode.CreateChildNode("light", new Light() { Color = new Vector3(Color.White), LightType = LightType.Point }).Transform.Translation = new Vector3(26, 57, 43);
```

Introdurre l'illuminazione per migliorare gli effetti visivi.

## Passaggio 4: crea un renderer e una destinazione di rendering

```csharp
using (var renderer = Renderer.CreateRenderer())
{
    // Configura le impostazioni del renderer
    renderer.EnableShadows = false;

    // Crea una destinazione di rendering
    using (IRenderTexture rt = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(), 1, 1024, 1024))
    {
        // Configura vista
        Viewport vp = rt.CreateViewport(camera, new RelativeRectangle() { ScaleWidth = 1, ScaleHeight = 1 });

        // Renderizza la scena in texture
        renderer.Render(rt);

        // Salva la texture renderizzata in un file
        ((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "Original_viewport_out.png", ImageFormat.Png);

        // Continua con gli effetti di post-elaborazione...
    }
}
```

Crea un renderer e una destinazione di rendering per catturare la scena.

## Passaggio 5: applica gli effetti di post-elaborazione

### Passaggio 5.1 Effetto pixel

```csharp
// Crea un effetto pixel
PostProcessing pixelation = renderer.GetPostProcessing("pixelation");
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_pixelation_out.png", ImageFormat.Png);
```

Applica l'effetto pixel e salva il risultato.

### Passaggio 5.2 Effetto scala di grigi

```csharp
// Crea un effetto in scala di grigi
PostProcessing grayscale = renderer.GetPostProcessing("grayscale");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale_out.png", ImageFormat.Png);
```

Applica l'effetto scala di grigi e salva il risultato.

### Passaggio 5.3 Combina effetti

```csharp
// Combina effetti di scala di grigi e pixel
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(grayscale);
renderer.PostProcessings.Add(pixelation);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_grayscale+pixelation_out.png", ImageFormat.Png);
```

Combina più effetti per risultati unici.

### Passaggio 5.4 Effetto rilevamento bordi

```csharp
// Crea un effetto di rilevamento dei bordi
PostProcessing edgedetection = renderer.GetPostProcessing("edge-detection");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(edgedetection);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_edgedetection_out.png", ImageFormat.Png);
```

Applica l'effetto di rilevamento dei bordi e salva il risultato.

### Passaggio 5.5 Effetto sfocatura

```csharp
// Crea un effetto sfocato
PostProcessing blur = renderer.GetPostProcessing("blur");
renderer.PostProcessings.Clear();
renderer.PostProcessings.Add(blur);
renderer.Render(rt);
((ITexture2D)rt.Targets[0]).Save("Your Output Directory" + "VisualEffect_blur_out.png", ImageFormat.Png);
```

Applica l'effetto sfocato e salva il risultato.

## Conclusione

Sperimentare gli effetti visivi nelle finestre 3D aggiunge profondità e creatività alle tue scene. Aspose.3D per .NET semplifica questo processo, offrendo una gamma di effetti di post-elaborazione per elevare i tuoi progetti.

## Domande frequenti

### Q1: Posso applicare più effetti contemporaneamente?

R1: Sì, puoi combinare diversi effetti di post-elaborazione per risultati unici e complessi.

### Q2: Come posso regolare l'intensità degli effetti visivi?

R2: Ogni effetto può avere parametri che puoi modificare per controllarne l'intensità. Fare riferimento alla documentazione per dettagli specifici.

### Q3: Aspose.3D è adatto allo sviluppo di giochi?

R3: Sebbene Aspose.3D sia progettato principalmente per la modellazione e il rendering 3D, può essere utilizzato in alcuni aspetti dello sviluppo del gioco.

### Q4: Sono disponibili ulteriori effetti di post-elaborazione?

A4: Aspose.3D fornisce una varietà di effetti di post-elaborazione integrati ed è possibile creare effetti personalizzati utilizzando la libreria.

### Q5: Posso utilizzare Aspose.3D per progetti commerciali?

 A5: Sì, puoi utilizzare Aspose.3D per scopi commerciali. Fare riferimento al[pagina di acquisto](https://purchase.aspose.com/buy) per i dettagli sulla licenza.