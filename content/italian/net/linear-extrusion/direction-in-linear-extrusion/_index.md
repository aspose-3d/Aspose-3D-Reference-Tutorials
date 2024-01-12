---
title: Direzione nell'estrusione lineare
linktitle: Direzione nell'estrusione lineare
second_title: API Aspose.3D .NET
description: Sblocca il mondo della modellazione 3D con Aspose.3D per .NET. Impara la direzione dell'estrusione lineare, stimola la creatività e crea applicazioni coinvolgenti senza sforzo.
type: docs
weight: 11
url: /it/net/linear-extrusion/direction-in-linear-extrusion/
---
## introduzione

Nel dinamico mondo dello sviluppo software, la creazione di modelli 3D immersivi è un'abilità indispensabile. Aspose.3D per .NET fornisce agli sviluppatori un robusto set di strumenti per sfruttare il potenziale della modellazione 3D nelle loro applicazioni. In questo tutorial, approfondiremo l'intrigante mondo dell'estrusione lineare ed esploreremo le sfumature della funzione "Direzione nell'estrusione lineare".

## Prerequisiti

Prima di intraprendere questo entusiasmante viaggio, assicurati di possedere i seguenti prerequisiti:

-  Aspose.3D per .NET: scarica e installa la libreria da[Documentazione Aspose.3D .NET](https://reference.aspose.com/3d/net/).

- Ambiente di sviluppo: assicurati di avere configurato un ambiente di sviluppo .NET funzionante.

## Importa spazi dei nomi

Nel tuo progetto .NET, importa gli spazi dei nomi necessari per accedere alla funzionalità di Aspose.3D. Aggiungi le seguenti righe all'inizio del tuo codice:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Passaggio 1: inizializzare il profilo di base

Inizia inizializzando il profilo di base da estrudere. In questo esempio creiamo una forma rettangolare con un raggio di arrotondamento di 0,3.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passaggio 2: crea una scena 3D

Costruisci le basi per il tuo capolavoro 3D creando una scena.

```csharp
Scene scene = new Scene();
```

## Passaggio 3: crea nodi

Genera nodi all'interno della scena per rappresentare diversi componenti del tuo ambiente 3D.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(8, 0, 0);
```

## Passaggio 4: estrusione lineare senza direzione

 Eseguire l'estrusione lineare sul nodo sinistro utilizzando il`Twist` E`Slices` proprietà.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100 });
```

## Passaggio 5: estrusione lineare con direzione

 Estendi le capacità di estrusione incorporando il`Direction` proprietà nel nodo destro.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 10) { Twist = 360, Slices = 100, Direction = new Vector3(0.3, 0.2, 1) });
```

## Passaggio 6: salva la scena 3D

 Conserva la tua creazione salvando la scena 3D. Sostituire`"Your Output Directory"` con la directory desiderata.

```csharp
scene.Save("Your Output Directory" + "DirectionInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

Congratulazioni! Hai implementato con successo l'estrusione lineare con Aspose.3D per .NET, esplorando sia l'approccio tradizionale che quello direzionale.

## Conclusione

In questo tutorial, abbiamo navigato nell'affascinante regno della modellazione 3D utilizzando Aspose.3D per .NET. L'estrusione lineare, con e senza direzione, apre infinite possibilità agli sviluppatori che cercano di creare applicazioni visivamente sorprendenti. Con Aspose.3D, la potenza della modellazione 3D è a portata di mano.

## Domande frequenti

### Q1: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?

 A1: Visita[Richiedi licenza temporanea](https://purchase.aspose.com/temporary-license/) per ottenere una licenza temporanea.

### Q2: Dove posso trovare supporto per Aspose.3D?

 A2: Unisciti a[Aspose.3D Forum](https://forum.aspose.com/c/3d/18) cercare assistenza e connettersi con la comunità.

### Q3: È disponibile una prova gratuita?

 R3: Sì, esplora le funzionalità con una prova gratuita su[Rilasci Aspose.3D](https://releases.aspose.com/).

### Q4: Come posso acquistare Aspose.3D per .NET?

 A4: Passare a[Aspose Pagina di acquisto](https://purchase.aspose.com/buy) per le opzioni di licenza e i dettagli di acquisto.

### Q5: Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?

 A5: Fare riferimento al completo[Documentazione Aspose.3D .NET](https://reference.aspose.com/3d/net/) per informazioni approfondite.