---
title: Creazione di una scena con texture incorporata
linktitle: Creazione di una scena con texture incorporata
second_title: API Aspose.3D .NET
description: Crea affascinanti scene 3D con texture incorporate utilizzando Aspose.3D per .NET. Segui la nostra guida passo passo per risultati sorprendenti.
type: docs
weight: 10
url: /it/net/materials/create-scene-embedded-texture/
---
## introduzione
Benvenuti nell'emozionante mondo della grafica 3D con Aspose.3D per .NET! In questo tutorial completo, ti guideremo attraverso il processo di creazione di straordinarie scene 3D con texture incorporate utilizzando Aspose.3D, una libreria potente e versatile per sviluppatori .NET.
## Prerequisiti
Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:
- Una conoscenza di base della programmazione C# e .NET.
- Visual Studio installato sul tuo computer.
- Libreria Aspose.3D per .NET, che puoi scaricare[Qui](https://releases.aspose.com/3d/net/).
- Familiarità con i concetti di grafica 3D e creazione di scene.
## Importa spazi dei nomi
Inizia importando gli spazi dei nomi necessari nel tuo progetto. Questi spazi dei nomi forniranno gli strumenti e le funzionalità necessarie per la manipolazione della grafica 3D.
```csharp
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
```
## Passaggio 1: creazione di una scena
Inizia creando una nuova scena 3D utilizzando Aspose.3D per .NET. Questo servirà come tela per il tuo capolavoro 3D.
```csharp
// Crea un file FBX con texture incorporate
Scene scene = new Scene();
```
## Passaggio 2: creazione di una texture incorporata
Ora aggiungiamo un tocco visivo alla scena incorporando una texture. Creeremo una texture con contenuto personalizzato e le assegneremo un nome file.
```csharp
// Crea una texture incorporata
Texture tex = new Texture()
{
    Content = CreateTextureContent(),
    //Il nome del file è obbligatorio se viene utilizzata la texture incorporata.
    FileName = "test.png"
};
tex.SetProperty("TexProp", "value");
```
## Passaggio 3: creazione di un materiale
Successivamente, crea un materiale per i tuoi oggetti 3D, incorporando la texture creata in precedenza e le proprietà personalizzate.
```csharp
// Crea un materiale con proprietà personalizzate
LambertMaterial mat = new LambertMaterial("my-mat");
mat.SetTexture(Material.MapDiffuse, tex);
mat.SetProperty("MyProp", 1.0);
```
## Passaggio 4: creazione di un oggetto 3D
Ora diamo vita alla tua scena aggiungendo un oggetto 3D. In questo esempio utilizzeremo un toro e applicheremo il materiale appena creato.
```csharp
// Crea un toro con applicato il materiale creato in precedenza
scene.RootNode.CreateChildNode(new Torus()).Material = mat;
```
## Passaggio 5: salvataggio della scena
Infine, salva il tuo capolavoro in un file. In questo esempio, lo salveremo in formato FBX.
```csharp
// Salva la scena in un file
scene.Save(RunExamples.GetOutputFilePath(@"test.fbx"), FileFormat.FBX7500ASCII);
```
Congratulazioni! Hai creato con successo una scena 3D con trame incorporate utilizzando Aspose.3D per .NET.
## Codice sorgente CreateTextureContent
```csharp
        private static byte[] CreateTextureContent()
        {
            using (var bitmap = new Bitmap(256, 256))
            {
                using (var g = Graphics.FromImage(bitmap))
                {
                    g.Clear(Color.White);
                    LinearGradientBrush brush = new LinearGradientBrush(new Rectangle(0, 0, 128, 128), Color.Moccasin,
                        Color.ForestGreen, 45);
                    using (var font = new Font(FontFamily.GenericSerif, 40))
                    {
                        g.DrawString("Aspose.3D", font, brush, Point.Empty);
                    }
                }
                using (var ms = new MemoryStream())
                {
                    bitmap.Save(ms, ImageFormat.Png);
                    return ms.ToArray();
                }
            }
        }
```
## Conclusione
In questo tutorial, abbiamo esplorato le basi della creazione di scene 3D visivamente sbalorditive con trame incorporate utilizzando Aspose.3D per .NET. Armati di questa conoscenza, puoi liberare la tua creatività e creare accattivanti applicazioni 3D.

## Domande frequenti

### D: Posso utilizzare Aspose.3D per .NET con altri linguaggi di programmazione?
R: Aspose.3D è progettato principalmente per .NET, ma sono disponibili librerie simili per altri linguaggi.
### D: Come posso applicare animazioni alle mie scene 3D?
R: Aspose.3D fornisce funzionalità di animazione; fare riferimento alla documentazione per istruzioni dettagliate.
### D: È disponibile una versione di prova per Aspose.3D per .NET?
 R: Sì, puoi scaricare la versione di prova[Qui](https://releases.aspose.com/).
### D: Dove posso trovare ulteriore supporto e risorse?
 R: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.
### D: Posso utilizzare Aspose.3D per progetti commerciali?
 R: Sì, puoi acquistare una licenza[Qui](https://purchase.aspose.com/buy).