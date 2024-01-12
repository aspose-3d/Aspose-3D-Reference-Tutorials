---
title: Conversione di mesh sferiche in mesh triangolari con layout di memoria personalizzato
linktitle: Conversione di mesh sferiche in mesh triangolari con layout di memoria personalizzato
second_title: API Aspose.3D .NET
description: Esplora Aspose.3D per .NET e converti facilmente Sphere Mesh in Triangle Mesh con layout di memoria personalizzato. Segui la nostra guida passo passo per un'integrazione perfetta.
type: docs
weight: 15
url: /it/net/objects/convert-sphere-mesh-triangle-memory-layout/
---
## introduzione
Stai cercando di sfruttare la potenza di Aspose.3D per .NET per convertire una Mesh sferica in una Mesh triangolare con un layout di memoria personalizzato? Questa guida passo passo ti guiderà attraverso il processo, rendendolo facile da seguire anche per i principianti. Alla fine di questo tutorial, avrai una solida conoscenza di come ottenere questo risultato utilizzando Aspose.3D per .NET.
## Prerequisiti
Prima di immergerti nel tutorial, assicurati di disporre dei seguenti prerequisiti:
- Conoscenza base della programmazione .NET.
- Aspose.3D per la libreria .NET installata. Puoi scaricarlo da[Pagina di download di Aspose.3D per .NET](https://releases.aspose.com/3d/net/).
- Conoscenza del linguaggio di programmazione C#.
## Importa spazi dei nomi
Nel tuo progetto C#, assicurati di importare gli spazi dei nomi necessari per sfruttare la funzionalità Aspose.3D:
```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System.Runtime.InteropServices;
```
## Passaggio 1: inizializza l'oggetto scena
```csharp
// Inizializza l'oggetto della scena
Scene scene = new Scene();
```
## Passaggio 2: inizializzare l'oggetto classe nodo
```csharp
// Inizializza l'oggetto della classe Node
Node cubeNode = new Node("sphere");
```
## Passaggio 3: convertire la Mesh sferica in TriMesh tipizzata
```csharp
Mesh sphere = (new Sphere()).ToMesh();
var myMesh = TriMesh<MyVertex>.FromMesh(sphere);
```
## Passaggio 4: ottieni i dati dei vertici nella struttura personalizzata
```csharp
MyVertex[] vertex = myMesh.VerticesToTypedArray();
```
## Passaggio 5: ottieni indici a 32 e 16 bit
```csharp
int[] indices32bit;
ushort[] indices16bit;
myMesh.IndicesToArray(out indices32bit);
myMesh.IndicesToArray(out indices16bit);
```
## Passaggio 6: scrivere i dati dei vertici e degli indici nel flusso di memoria
```csharp
using (MemoryStream ms = new MemoryStream())
{
    myMesh.WriteVerticesTo(ms);
    myMesh.Write16bIndicesTo(ms);
    myMesh.Write32bIndicesTo(ms);
}
```
## Passaggio 7: puntare il nodo sulla geometria della mesh
```csharp
cubeNode.Entity = sphere;
```
## Passaggio 8: aggiungi nodo alla scena
```csharp
scene.RootNode.ChildNodes.Add(cubeNode);
```
## Passaggio 9: salva la scena 3D
```csharp
string output = "Your Output Directory" + "SphereToTriangleMeshCustomMemoryLayoutScene.fbx";
scene.Save(output, FileFormat.FBX7400ASCII);
```
## Passaggio 10: visualizzare i risultati
```csharp
Console.WriteLine("Indices = {0}, Actual vertices = {1}, vertices before merging = {2}", myMesh.IndicesCount, myMesh.VerticesCount, myMesh.UnmergedVerticesCount);
Console.WriteLine("Total bytes of vertices in memory {0}bytes", myMesh.VerticesSizeInBytes);
Console.WriteLine("\nConverted a Sphere mesh to a triangle mesh with a custom memory layout of the vertex successfully.\nFile saved at " + output);
```
## Conclusione
Congratulazioni! Hai convertito con successo una mesh sferica in una mesh triangolare con un layout di memoria personalizzato utilizzando Aspose.3D per .NET. Questa potente libreria fornisce un modo semplice per manipolare oggetti 3D nelle tue applicazioni .NET.
## Domande frequenti
### D: Posso utilizzare Aspose.3D per .NET con altri framework .NET?
R: Sì, Aspose.3D per .NET è compatibile con vari framework .NET.
### D: Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?
 R: Fare riferimento a[Aspose.3D per la documentazione .NET](https://reference.aspose.com/3d/net/) per informazioni approfondite.
### D: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?
 Una visita[questo link](https://purchase.aspose.com/temporary-license/) per ottenere una licenza temporanea.
### D: Sono disponibili progetti di esempio per Aspose.3D per .NET?
 A: Esplora la documentazione di Aspose.3D per .NET e[Repositorio GitHub](https://github.com/aspose-3d/Aspose.3D-for-.NET) per progetti campione.
### D: Esiste una comunità attiva per Aspose.3D per il supporto .NET?
 R: Sì, unisciti a[Aspose.3D per il forum .NET](https://forum.aspose.com/c/3d/18) per ottenere assistenza dalla comunità.