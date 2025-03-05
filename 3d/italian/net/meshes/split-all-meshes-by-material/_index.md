---
title: Divisione di tutte le mesh della scena per materiale
linktitle: Divisione di tutte le mesh della scena per materiale
second_title: API Aspose.3D .NET
description: Scopri come dividere le mesh 3D per materiale utilizzando Aspose.3D per .NET. Segui la nostra guida passo passo per un'organizzazione e una gestione efficiente dei modelli 3D.
type: docs
weight: 21
url: /it/net/meshes/split-all-meshes-by-material/
---
## introduzione
Benvenuti in questa guida passo passo sulla divisione di tutte le mesh di una scena 3D in base al materiale utilizzando Aspose.3D per .NET. Se lavori con modelli 3D e desideri organizzare in modo efficiente le tue mesh in base ai materiali, questo tutorial fa per te. Aspose.3D è una potente libreria .NET che fornisce una gamma di funzionalità per lavorare con file 3D, rendendola una scelta eccellente per gli sviluppatori.
## Prerequisiti
Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:
- Conoscenza base del linguaggio di programmazione C#.
- Visual Studio installato sul tuo computer.
-  Aspose.3D per la libreria .NET. Puoi scaricarlo da[Qui](https://releases.aspose.com/3d/net/).
- Un file 3D di input (ad esempio "test.fbx") che desideri dividere.
## Importa spazi dei nomi
Inizia importando gli spazi dei nomi necessari nel tuo progetto C#:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```
## Passaggio 1: caricare il file 3D
```csharp
// Il percorso della directory dei documenti.
string input = RunExamples.GetDataFilePath("test.fbx");
// Carica un file 3D
Scene scene = new Scene(input);
```
 In questo passaggio, carichiamo il file 3D utilizzando Aspose.3D`Scene` classe.
## Passaggio 2: dividere tutte le mesh
```csharp
// Dividi tutte le mesh
PolygonModifier.SplitMesh(scene, SplitMeshPolicy.CloneData);
```
 Qui usiamo il`SplitMesh` metodo da`PolygonModifier` classe per dividere tutte le mesh in base al materiale.
## Passaggio 3: salva la scena divisa
```csharp
// Salvare il file
var output = "Your Output Directory" + "test-splitted.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```
Salva la scena modificata in un nuovo file per conservare le modifiche.
## Passaggio 4: Visualizza il messaggio di successo
```csharp
// Visualizza il messaggio di successo
Console.WriteLine("\nSplitting all meshes of a scene per material successfully.\nFile saved at " + output);
```
Stampa un messaggio di successo indicando che l'operazione è stata completata con successo.
## Conclusione
Congratulazioni! Hai imparato con successo come dividere tutte le mesh di una scena 3D per materiale utilizzando Aspose.3D per .NET. Questa può essere una tecnica preziosa per organizzare e gestire modelli 3D complessi.
## Domande frequenti
### 1. Posso utilizzare Aspose.3D per .NET con altri linguaggi di programmazione?
Aspose.3D è progettato principalmente per .NET, ma fornisce l'interoperabilità con altri linguaggi tramite collegamenti linguistici .NET.
### 2. È disponibile una versione di prova?
 Sì, puoi accedere alla versione di prova gratuita[Qui](https://releases.aspose.com/).
### 3. Dove posso trovare ulteriori esempi e documentazione?
 Esplora la documentazione completa su[Documentazione Aspose.3D](https://reference.aspose.com/3d/net/).
### 4. Come posso ottenere supporto per Aspose.3D?
 Visitare il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.
### 5. Posso ottenere una licenza temporanea?
 Sì, puoi ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).