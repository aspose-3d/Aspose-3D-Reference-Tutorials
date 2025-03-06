---
title: Applicazione dell'effetto lente fisheye con Aspose.3D per .NET
linktitle: Applicazione dell'effetto lente fisheye alla scena 3D
second_title: API Aspose.3D .NET
description: Migliora le tue scene 3D con Aspose.3D per .NET! Scopri come applicare un accattivante effetto lente fisheye passo dopo passo. Scarica ora!
weight: 12
url: /it/net/rendering/fisheye-lens-effect-3d-scene/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Applicazione dell'effetto lente fisheye con Aspose.3D per .NET

## introduzione
Stai cercando di migliorare l'attrattiva visiva delle tue scene 3D? Immergiti nell'affascinante mondo degli effetti delle lenti fisheye con Aspose.3D per .NET. Questo tutorial ti guiderà passo dopo passo su come applicare un effetto lente fisheye alle tue scene 3D, donando loro una prospettiva unica e accattivante.
## Prerequisiti
Prima di iniziare, assicurati di disporre dei seguenti prerequisiti:
-  Aspose.3D per .NET: assicurati di avere la libreria Aspose.3D per .NET installata. In caso contrario, puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).
-  Scena 3D di esempio: lavoreremo con un file di scena 3D di esempio (VirtualCity.glb). Puoi utilizzare la tua scena o scaricare l'esempio dal file[Documentazione Aspose.3D](https://reference.aspose.com/3d/net/).
## Importa spazi dei nomi
Nel tuo progetto .NET, includi gli spazi dei nomi necessari per accedere alle funzionalità Aspose.3D. Aggiungi i seguenti spazi dei nomi all'inizio del codice:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Render;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
```
## Passaggio 1: carica la scena 3D
Carica il file della scena 3D nel tuo progetto utilizzando il seguente codice:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Passaggio 2: imposta la fotocamera e le luci
Crea una telecamera e luci per migliorare gli aspetti visivi della tua scena. Regola parametri come NearPlane, FarPlane e RotationMode secondo necessità:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light() { Color = new Vector3(Color.CadetBlue) }).Transform.Translation = new Vector3(49, 0, 49);
```
## Passaggio 3: creazione del renderer e delle destinazioni di rendering
Imposta il renderer e crea destinazioni di rendering per la mappa cubica e la texture 2D:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    IRenderTexture final = renderer.RenderFactory.CreateRenderTexture(new RenderParameters(false, 32, 0, 0), 1024, 1024);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
```
## Passaggio 4: applica l'effetto lente fisheye
Esegui la post-elaborazione dell'effetto lente fisheye sulla mappa cubica renderizzata:
```csharp
PostProcessing fisheye = renderer.GetPostProcessing("fisheye");
fisheye.FindProperty("fov").Value = 360.0;
fisheye.Input = rt.Targets[0];
renderer.Execute(fisheye, final);
((ITexture2D)final.Targets[0]).Save("Your Output Directory" + "fisheye.png", ImageFormat.Png);
```
## Conclusione
Congratulazioni! Hai applicato con successo un effetto lente fisheye alla scena 3D utilizzando Aspose.3D per .NET. Sperimenta scene e parametri diversi per liberare la tua creatività.
## Domande frequenti
### Posso applicare l'effetto fisheye a qualsiasi scena 3D?
Sì, puoi applicare l'effetto fisheye a qualsiasi scena 3D. Assicurati che la scena sia caricata e illuminata correttamente per ottenere risultati ottimali.
### Qual è il significato di regolare il campo visivo (fov) a 360 gradi?
Un campo visivo di 360 gradi garantisce una proiezione sferica completa, creando uno straordinario effetto fisheye.
### Come posso personalizzare l'illuminazione nella mia scena 3D?
È possibile regolare le proprietà delle luci, come posizione, tipo e colore, per ottenere gli effetti di luce desiderati.
### Esiste un limite alla dimensione della scena 3D che può essere elaborata?
La dimensione della scena 3D è limitata principalmente dalle risorse di sistema. Assicurati che il tuo hardware sia in grado di gestire le dimensioni della scena.
### Posso utilizzare un formato di output diverso anziché PNG per il risultato dell'effetto fisheye?
Sì, puoi modificare il codice per salvare l'output in diversi formati di immagine in base alle tue esigenze.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
