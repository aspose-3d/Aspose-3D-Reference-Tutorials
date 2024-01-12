---
title: Rendering della scena in una mappa cubica con sei facce
linktitle: Rendering della scena in una mappa cubica con sei facce
second_title: API Aspose.3D .NET
description: Crea straordinarie mappe cubiche con Aspose.3D per .NET. Segui la nostra guida passo passo per trasformare le scene 3D in accattivanti mappe cubiche a sei facce.
type: docs
weight: 14
url: /it/net/rendering/render-scene-cubemap/
---
## introduzione
Benvenuti in questa guida passo passo sul rendering di una scena in una mappa cubica con sei facce utilizzando Aspose.3D per .NET. In questo tutorial ti guideremo attraverso il processo di creazione di una straordinaria mappa cubica eseguendo il rendering di una scena 3D. Aspose.3D è una potente API .NET che semplifica la manipolazione della grafica 3D e con questa guida potrai sfruttare le sue capacità per creare accattivanti mappe cubiche.
## Prerequisiti
Prima di immergerci nel tutorial, assicurati di disporre dei seguenti prerequisiti:
- Una conoscenza pratica dello sviluppo C# e .NET.
- Aspose.3D per .NET installato. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).
- Un file di scena 3D in formato GLB (ad esempio "VirtualCity.glb") per il rendering.
## Importa spazi dei nomi
Inizia importando gli spazi dei nomi necessari per Aspose.3D nel tuo codice C#:
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
## Passaggio 1: caricare la scena
Carica il file della scena 3D utilizzando il seguente codice:
```csharp
Scene scene = new Scene(RunExamples.GetDataFilePath("VirtualCity.glb"));
```
## Passaggio 2: crea fotocamera e luci
Crea una telecamera e due luci per illuminare la scena:
```csharp
Camera cam = new Camera(ProjectionType.Perspective)
{
    NearPlane = 0.1,
    FarPlane = 200,
    RotationMode = RotationMode.FixedDirection
};
scene.RootNode.CreateChildNode(cam).Transform.Translation = new Vector3(5, 6, 0);
scene.RootNode.CreateChildNode(new Light() { LightType = LightType.Point }).Transform.Translation = new Vector3(-10, 7, -10);
scene.RootNode.CreateChildNode(new Light()
{
    Color = new Vector3(Color.CadetBlue)
}).Transform.Translation = new Vector3(49, 0, 49);
```
## Passaggio 3: crea il renderer e la destinazione del rendering
Crea un renderer e una destinazione di rendering della mappa cubica con texture di profondità:
```csharp
using (var renderer = Renderer.CreateRenderer())
{
    IRenderTexture rt = renderer.RenderFactory.CreateCubeRenderTexture(new RenderParameters(false), 512, 512);
    rt.CreateViewport(cam, RelativeRectangle.FromScale(0, 0, 1, 1));
    renderer.Render(rt);
    ITextureCubemap cubemap = rt.Targets[0] as ITextureCubemap;
```
## Passaggio 4: salva i volti della mappa cubica
Salva ogni faccia della mappa cubica su disco con i nomi di file specificati:
```csharp
CubeFaceData<string> fileNames = new CubeFaceData<string>()
{
    Right = "Your Output Directory" + "right.png",
    Left = "Your Output Directory" + "left.png",
    Back = "Your Output Directory" + "back.png",
    Front = "Your Output Directory" + "front.png",
    Bottom = "Your Output Directory" + "bottom.png",
    Top = "Your Output Directory" + "top.png"
};
cubemap.Save(fileNames, ImageFormat.Png);
```
## Conclusione
Congratulazioni! Hai eseguito con successo il rendering di una scena 3D in una mappa cubica utilizzando Aspose.3D per .NET. Esplora ulteriori opzioni di personalizzazione e migliora i tuoi progetti di grafica 3D con questa potente API.
## Domande frequenti
### D: Posso utilizzare Aspose.3D per .NET con altri formati di file 3D?
Sì, Aspose.3D supporta vari formati di file 3D, offrendo flessibilità ai tuoi progetti.
### D: Come posso ottenere supporto per Aspose.3D?
 Visitare il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.
### D: È disponibile una prova gratuita?
 Sì, puoi accedere alla prova gratuita[Qui](https://releases.aspose.com/).
### D: Posso eseguire il rendering di scene con animazioni utilizzando Aspose.3D?
Assolutamente! Aspose.3D supporta il rendering di scene 3D animate.
### D: Dove posso trovare la documentazione dettagliata?
 Fare riferimento al[Documentazione Aspose.3D](https://reference.aspose.com/3d/net/) per informazioni approfondite.