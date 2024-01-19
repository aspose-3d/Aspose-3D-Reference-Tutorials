---
title: Cilindro inferiore a taglio personalizzato
linktitle: Cilindro inferiore a taglio personalizzato
second_title: API Aspose.3D .NET
description: Impara a creare cilindri con fondo di taglio personalizzati utilizzando Aspose.3D per .NET con la nostra guida dettagliata passo passo. Migliora le tue capacità di modellazione 3D oggi!
type: docs
weight: 12
url: /it/net/working-with-cylinder/customized-shear-bottom-cylinder/
---
## introduzione
Benvenuti nella nostra guida completa sulla creazione di un cilindro con fondo di taglio personalizzato utilizzando Aspose.3D per .NET. Se stai cercando di migliorare le tue capacità di modellazione 3D e aggiungere funzionalità uniche ai tuoi progetti, sei nel posto giusto. In questo tutorial ti guideremo attraverso il processo passo dopo passo, utilizzando spiegazioni chiare e frammenti di codice.
## Prerequisiti
Prima di immergerci nel tutorial, assicurati di avere quanto segue:
- Conoscenza di base della programmazione C# e .NET.
-  Aspose.3D per la libreria .NET installata. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).
- Un ambiente di sviluppo configurato per la programmazione .NET.
## Importa spazi dei nomi
Nel codice C#, inizia importando gli spazi dei nomi necessari:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Passaggio 1: crea una scena
Inizia creando una scena 3D utilizzando Aspose.3D:
```csharp
Scene scene = new Scene();
```
## Passaggio 2: creare il cilindro 1
Genera il primo cilindro e imposta le sue proprietà:
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Passaggio 3: personalizzare il fondo di taglio per il cilindro 1
Applicare un fondo di taglio personalizzato al primo cilindro:
```csharp
cylinder1.ShearBottom = new Vector2(0, 0.83); // Taglio 47,5 gradi nel piano xy (asse z)
```
## Passaggio 4: aggiungi il cilindro 1 alla scena
Aggiungi il primo cilindro alla scena e imposta la sua traduzione:
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## Passaggio 5: creare il cilindro 2
Genera un secondo cilindro con proprietà simili:
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## Passaggio 6: aggiungi il cilindro 2 alla scena
Aggiungi il secondo cilindro alla scena senza fondo di taglio:
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## Passaggio 7: salva la scena
Salva la scena come file Wavefront OBJ nella directory dei documenti:
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## Conclusione
Congratulazioni! Hai creato con successo un cilindro inferiore di taglio personalizzato utilizzando Aspose.3D per .NET. Questo tutorial mirava a fornire una guida passo passo per utenti con diversi livelli di esperienza nella modellazione e programmazione 3D.
## Domande frequenti
### Aspose.3D per .NET è adatto ai principianti?
Assolutamente! Aspose.3D per .NET offre un'interfaccia user-friendly, rendendola accessibile sia ai principianti che agli sviluppatori esperti.
### Posso applicare angoli di taglio diversi ai cilindri?
Sì, puoi personalizzare singolarmente il fondo di taglio per ogni cilindro, permettendoti di ottenere effetti unici.
### È disponibile una versione di prova?
 Sì, puoi esplorare la versione di prova gratuita[Qui](https://releases.aspose.com/).
### Dove posso trovare ulteriore supporto?
 Visitare il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.
### Come posso ottenere una licenza temporanea?
 Ottieni la tua licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).