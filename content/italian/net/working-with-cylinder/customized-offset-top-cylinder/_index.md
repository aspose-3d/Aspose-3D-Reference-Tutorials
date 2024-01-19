---
title: Cilindro superiore offset personalizzato
linktitle: Cilindro superiore offset personalizzato
second_title: API Aspose.3D .NET
description: Esplora le meraviglie della grafica 3D con Aspose.3D per .NET. Impara a creare cilindri superiori offset personalizzati senza sforzo. Migliora la tua esperienza di codifica adesso!
type: docs
weight: 11
url: /it/net/working-with-cylinder/customized-offset-top-cylinder/
---
## introduzione
Benvenuti nel mondo della manipolazione della grafica 3D con Aspose.3D per .NET! In questo tutorial ti guideremo attraverso il processo di creazione di un cilindro superiore offset personalizzato utilizzando Aspose.3D, una potente libreria per lavorare con scene, oggetti e formati 3D nelle applicazioni .NET.
## Prerequisiti
Prima di immergerci nel tutorial, assicurati di avere i seguenti prerequisiti:
- Conoscenza base del linguaggio di programmazione C#.
- Visual Studio installato sul tuo computer.
- Libreria Aspose.3D per .NET scaricata e referenziata nel tuo progetto.
Ora iniziamo con la guida passo passo!
## Importa spazi dei nomi
Innanzitutto, assicurati di importare gli spazi dei nomi necessari nel tuo codice C#:
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
```csharp
// Crea una scena
Scene scene = new Scene();
```
Questo inizializza una nuova scena 3D usando Aspose.3D.
## Passaggio 2: inizializzare il cilindro
```csharp
// Inizializza il cilindro
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
Qui creiamo un cilindro con parametri specifici come raggio, altezza e sezioni.
## Passaggio 3: impostare OffsetTop per il primo cilindro
```csharp
// Imposta OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
Ciò imposta un offset superiore personalizzato per il primo cilindro.
## Passaggio 4: crea ChildNode per il primo cilindro
```csharp
// Crea nodo figlio
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
Aggiungiamo il primo cilindro come nodo figlio alla scena, regolandone la posizione.
## Passaggio 5: inizializzare il secondo cilindro
```csharp
//Inizializza il secondo cilindro senza OffsetTop personalizzato
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
Un secondo cilindro viene inizializzato senza un offset superiore personalizzato.
## Passaggio 6: crea ChildNode per il secondo cilindro
```csharp
// Crea nodo figlio
scene.RootNode.CreateChildNode(cylinder2);
```
Aggiungiamo il secondo cilindro come nodo figlio alla scena.
## Passaggio 7: salva la scena
```csharp
// Salva
scene.Save("Your Document Directory" + "CustomizedOffsetTopCylinder.obj", FileFormat.WavefrontOBJ);
```
Ciò salva la scena 3D, incluso il cilindro superiore con offset personalizzato, nel formato Wavefront OBJ.
Ora hai creato con successo un cilindro superiore offset personalizzato utilizzando Aspose.3D per .NET!
## Conclusione
In questo tutorial, abbiamo esplorato le basi del lavoro con Aspose.3D per .NET per creare un cilindro superiore offset personalizzato. Questa libreria apre infinite possibilità per la manipolazione della grafica 3D all'interno delle tue applicazioni .NET.
## Domande frequenti
### D: Dove posso trovare la documentazione per Aspose.3D per .NET?
 R: La documentazione è disponibile[Qui](https://reference.aspose.com/3d/net/).
### D: Come posso scaricare Aspose.3D per .NET?
 R: Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).
### D: È disponibile una prova gratuita per Aspose.3D per .NET?
 R: Sì, puoi ottenere una prova gratuita[Qui](https://releases.aspose.com/).
### D: Dove posso ottenere supporto per Aspose.3D per .NET?
 R: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per supporto.
### D: Posso ottenere una licenza temporanea per Aspose.3D per .NET?
 R: Sì, puoi ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).