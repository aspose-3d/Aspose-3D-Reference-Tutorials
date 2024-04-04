---
title: Applicazione del materiale PBR alla scatola
linktitle: Applicazione del materiale PBR alla scatola
second_title: API Aspose.3D .NET
description: Esplora il mondo della grafica 3D con Aspose.3D per .NET. Crea scene coinvolgenti senza sforzo utilizzando materiali di rendering basati sulla fisica.
type: docs
weight: 10
url: /it/net/geometry-and-hierarchy/apply-pbr-material-to-box/
---
## introduzione

Benvenuti nell'affascinante mondo della grafica 3D! In questa guida passo passo, esploreremo la potente libreria Aspose.3D per .NET e impareremo come creare straordinarie scene 3D utilizzando materiali PBR (Physically Based Rendering). Aspose.3D semplifica il complesso processo della grafica 3D e apre un regno di possibilità per gli sviluppatori.

## Prerequisiti

Prima di immergerci nell'entusiasmante mondo della grafica 3D, assicuriamoci di aver impostato tutto:

### Scarica e installa Aspose.3D per .NET

 Visitare il[Aspose.3D per la documentazione .NET](https://reference.aspose.com/3d/net/) per istruzioni dettagliate sul download e l'installazione della libreria.

### Acquisisci una licenza

Per sbloccare tutto il potenziale di Aspose.3D, ottenere una licenza valida. Puoi ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/) o acquistare una licenza completa[Qui](https://purchase.aspose.com/buy).

## Importa spazi dei nomi

Innanzitutto, assicurati di importare gli spazi dei nomi necessari per sfruttare le funzionalità di Aspose.3D per .NET:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Shading;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
```

## Passaggio 1: inizializzare una scena

Inizia inizializzando una scena 3D utilizzando il seguente snippet di codice:

```csharp
Scene scene = new Scene();
```

## Passaggio 2: inizializzare il materiale PBR

Crea un oggetto materiale PBR per ottenere un rendering realistico:

```csharp
PbrMaterial mat = new PbrMaterial();
```

## Passaggio 3: impostare le proprietà del materiale

Perfeziona le proprietà del materiale, rendendolo quasi metallico e molto ruvido:

```csharp
mat.MetallicFactor = 0.9;
mat.RoughnessFactor = 0.9;
```

## Passaggio 4: crea una scatola

Genera una casella a cui verrà applicato il materiale PBR:

```csharp
var boxNode = scene.RootNode.CreateChildNode("box", new Box());
```

## Passaggio 5: applicare il materiale alla scatola

Assegna il materiale PBR al nodo scatola creato:

```csharp
boxNode.Material = mat;
```

## Passaggio 6: salva la scena 3D

Salva la scena 3D in formato STL con la directory di output desiderata:

```csharp
scene.Save("Your Output Directory" + "PBR_Material_Box_Out.stl", FileFormat.STLASCII);
```

Congratulazioni! Hai applicato con successo un materiale PBR a una scatola in una scena 3D utilizzando Aspose.3D per .NET.

## Conclusione

Avventurarsi nella grafica 3D con Aspose.3D per .NET apre le porte a infinite possibilità creative. Con la sua API intuitiva e funzionalità robuste, la creazione di scene visivamente sbalorditive diventa un'esperienza piacevole per gli sviluppatori.

## Domande frequenti

### Q1: Aspose.3D è compatibile con altri formati di file 3D?

A1: Sì, Aspose.3D supporta vari formati di file 3D, garantendo flessibilità nei tuoi progetti.

### Q2: Posso utilizzare Aspose.3D per applicazioni commerciali?

A2: Assolutamente! Aspose.3D fornisce licenze commerciali per una perfetta integrazione nelle tue applicazioni.

### Q3: È disponibile una versione di prova?

 A3: Sì, puoi esplorare le funzionalità di Aspose.3D scaricando la versione di prova gratuita[Qui](https://releases.aspose.com/).

### Q4: Dove posso trovare il supporto e le discussioni della community?

 A4: Unisciti alla comunità Aspose.3D su[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per supporto e discussioni.

### Q5: Come posso ottenere una licenza temporanea per Aspose.3D?

 A5: Puoi ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/) a fini di valutazione.