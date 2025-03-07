---
title: Trasformazione del nodo per quaternione
linktitle: Trasformazione del nodo per quaternione
second_title: API Aspose.3D .NET
description: Impara a trasformare i nodi 3D con quaternioni utilizzando Aspose.3D per .NET. Guida passo passo per principianti.
weight: 20
url: /it/net/geometry-and-hierarchy/transformation-node-quaternion/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Trasformazione del nodo per quaternione

## introduzione

Benvenuti in una guida passo passo sulla trasformazione di un nodo tramite quaternione in scene 3D utilizzando Aspose.3D per .NET. In questo tutorial esploreremo le potenti funzionalità di Aspose.3D per .NET e seguiremo il processo di aggiunta di trasformazioni a un nodo 3D utilizzando i quaternioni.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di disporre dei seguenti prerequisiti:

-  Aspose.3D per .NET: assicurati di avere la libreria Aspose.3D installata. Puoi scaricarlo da[pagina di rilascio](https://releases.aspose.com/3d/net/).

- Ambiente di sviluppo: configura il tuo ambiente di sviluppo .NET con gli strumenti e le configurazioni necessarie.

- Comprensione di base dei concetti 3D: sarà utile la familiarità con la grafica e i concetti 3D.

## Importa spazi dei nomi

Nel tuo progetto .NET, includi gli spazi dei nomi richiesti per Aspose.3D:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

## Passaggio 1: inizializzare l'oggetto scena

```csharp
// ExStart:AddTransformationToNodeByQuaternion
// Inizializza l'oggetto della scena
Scene scene = new Scene();
```

## Passaggio 2: inizializzare l'oggetto classe nodo

```csharp
// Inizializza l'oggetto della classe Node
Node cubeNode = new Node("cube");
```

## Passaggio 3: crea mesh utilizzando Polygon Builder

```csharp
// Chiama la classe Common per creare mesh utilizzando il metodo di creazione poligoni per impostare l'istanza della mesh
Mesh mesh = Common.CreateMeshUsingPolygonBuilder();
```

## Passaggio 4: puntare il nodo sulla geometria della mesh

```csharp
// Nodo punto alla geometria Mesh
cubeNode.Entity = mesh;
```

## Passaggio 5: impostare la rotazione utilizzando Quaternion

```csharp
// Imposta la rotazione
cubeNode.Transform.Rotation = Quaternion.FromRotation(new Vector3(0, 1, 0), new Vector3(0.3, 0.5, 0.1));            
```

## Passaggio 6: impostare la traduzione

```csharp
// Imposta la traduzione
cubeNode.Transform.Translation = new Vector3(0, 0, 20);            
```

## Passaggio 7: aggiungi il cubo alla scena

```csharp
// Aggiungi il cubo alla scena
scene.RootNode.ChildNodes.Add(cubeNode);
```

## Passaggio 8: salva la scena 3D

```csharp
// Il percorso della directory dei documenti.
var output = "Your Output Directory" + "TransformationToNode.fbx";

// Salva la scena 3D nei formati di file supportati
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByQuaternion
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

## Conclusione

 Congratulazioni! Hai imparato con successo come trasformare un nodo tramite quaternione in scene 3D utilizzando Aspose.3D per .NET. Esplora ulteriori funzionalità e possibilità facendo riferimento a[documentazione](https://reference.aspose.com/3d/net/).

## Domande frequenti

### Q1: Cos'è un quaternione nella grafica 3D?

R1: I quaternioni sono entità matematiche utilizzate per rappresentare le rotazioni nello spazio 3D.

### Q2: Come posso scaricare Aspose.3D per .NET?

 A2: È possibile scaricare la libreria da[pagina di rilascio](https://releases.aspose.com/3d/net/).

### Q3: È disponibile una prova gratuita per Aspose.3D per .NET?

 R3: Sì, puoi ottenere una prova gratuita da[Qui](https://releases.aspose.com/).

### Q4: Dove posso trovare supporto per Aspose.3D per .NET?

 A4: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per supporto e discussioni.

### Q5: Come posso ottenere una licenza temporanea per Aspose.3D?

 A5: ottieni una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
