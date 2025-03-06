---
title: Nodo di trasformazione tramite matrice di trasformazione
linktitle: Nodo di trasformazione tramite matrice di trasformazione
second_title: API Aspose.3D .NET
description: Trasforma i nodi senza sforzo in scene 3D utilizzando Aspose.3D per .NET. Scopri le trasformazioni dei nodi passo dopo passo con il tutorial.
weight: 21
url: /it/net/geometry-and-hierarchy/transformation-node-matrix/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Nodo di trasformazione tramite matrice di trasformazione

## introduzione

Nel regno dinamico della grafica e delle visualizzazioni 3D, la capacità di manipolare gli oggetti all'interno di una scena è un aspetto cruciale. Aspose.3D per .NET consente agli sviluppatori di trasformare senza problemi i nodi utilizzando matrici di trasformazione, aggiungendo uno strato di creatività e controllo alle scene 3D. Questo tutorial ti guiderà passo dopo passo attraverso il processo di trasformazione di un nodo in una scena 3D.

## Prerequisiti

Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:

1.  Libreria Aspose.3D per .NET: assicurati di avere la libreria Aspose.3D installata nel tuo progetto .NET. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).

2. Ambiente di sviluppo: configura un ambiente di sviluppo .NET funzionante e, se non lo hai già fatto, crea un nuovo progetto in cui implementerai le trasformazioni.

## Importa spazi dei nomi

Inizia importando gli spazi dei nomi necessari nel tuo progetto .NET. Questi spazi dei nomi forniscono le classi e i metodi essenziali per la manipolazione delle scene 3D.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Ora che abbiamo trattato le nozioni di base, analizziamo il processo di trasformazione in una guida passo passo.

## Passaggio 1: inizializza la scena

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Inizializza l'oggetto della scena
Scene scene = new Scene();

```

In questo passaggio creiamo una nuova scena 3D vuota.

## Passaggio 2: crea mesh e collega alla scena

```csharp
// Chiama la classe Common per creare mesh utilizzando il metodo di creazione poligoni per impostare l'istanza della mesh
Mesh mesh = (new Box()).ToMesh();

// Crea un nodo contenitore per la mesh.
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Qui generiamo una mesh utilizzando il metodo di creazione poligoni e la assegniamo al nodo, stabilendo la geometria del nostro cubo.

## Passaggio 3: imposta la matrice di traduzione personalizzata

```csharp
// Imposta la matrice di traduzione personalizzata
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Definire una matrice di traduzione personalizzata per determinare la trasformazione specifica applicata al nodo. Regola i valori della matrice secondo necessità per la trasformazione desiderata.

Includi il nodo del cubo nella scena, rendendolo parte dell'ambiente 3D complessivo.

## Passaggio 4: salva la scena

```csharp
// Il percorso della directory dei documenti.
var output = "TransformationToNode.fbx";

// Salva la scena 3D nei formati di file supportati
scene.Save(output);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Specificare la directory di output e il nome file, quindi salvare la scena 3D nel formato file desiderato. In questo esempio, lo salviamo nel formato FBX7500ASCII.

## Conclusione

Congratulazioni! Hai trasformato con successo un nodo utilizzando una matrice di trasformazione in una scena 3D con Aspose.3D per .NET. Questa funzionalità apre le porte ad applicazioni 3D diverse e visivamente accattivanti.

## Domande frequenti

### Q1: Cos'è una matrice di trasformazione nella grafica 3D?

A1: Una matrice di trasformazione è una rappresentazione matematica utilizzata per applicare varie trasformazioni (traslazione, rotazione, ridimensionamento) agli oggetti nello spazio 3D.

### Q2: Posso applicare più trasformazioni a un singolo nodo?

A2: Sì, puoi combinare più trasformazioni moltiplicando le rispettive matrici e applicando il risultato al nodo.

### Q3: Esistono altri formati di file supportati per il salvataggio delle scene 3D?

 A3: Aspose.3D per .NET supporta vari formati di file, inclusi STL, GLTF, OBJ e altri. Fare riferimento al[documentazione](https://reference.aspose.com/3d/net/) per un elenco completo.

### Q4: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?

 A4: Visita il[pagina della licenza temporanea](https://purchase.aspose.com/temporary-license/)sul sito Aspose per ottenere una licenza temporanea a scopo di valutazione.

### Q5: Dove posso chiedere assistenza o connettermi con la comunità Aspose.3D?

 A5: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per porre domande, condividere esperienze e connettersi con altri sviluppatori utilizzando Aspose.3D.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
