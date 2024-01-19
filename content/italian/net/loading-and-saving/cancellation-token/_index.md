---
title: Caricamento e salvataggio utilizzo di CancellationToken
linktitle: Caricamento e salvataggio utilizzo di CancellationToken
second_title: API Aspose.3D .NET
description: Esplora il mondo senza soluzione di continuità della modellazione 3D con Aspose.3D per .NET. Impara a caricare e salvare documenti 3D in modo efficiente utilizzando CancellationToken.
type: docs
weight: 10
url: /it/net/loading-and-saving/cancellation-token/
---
## introduzione

Benvenuti nella nostra guida completa sull'utilizzo di Aspose.3D per .NET per migliorare i vostri progetti di modellazione e rendering 3D. Aspose.3D è una potente libreria che consente agli sviluppatori .NET di lavorare senza problemi con file 3D. In questo tutorial approfondiremo gli aspetti di caricamento e salvataggio, concentrandoci in particolare sull'utilizzo di CancellationToken per una gestione efficiente delle attività asincrone.

## Prerequisiti

Prima di intraprendere questo viaggio, assicurati di possedere i seguenti prerequisiti:

-  Aspose.3D per .NET: scarica e installa la libreria da[Qui](https://releases.aspose.com/3d/net/).
- Ambiente .NET: assicurati di avere configurato un ambiente di sviluppo .NET compatibile.
- Conoscenza di base di C#: si consiglia la familiarità con il linguaggio di programmazione C#.

## Importa spazi dei nomi

Per iniziare, assicurati di includere gli spazi dei nomi necessari nel tuo progetto. Questi spazi dei nomi forniranno l'accesso alle funzionalità necessarie per la manipolazione dei file 3D.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Caricamento e salvataggio: utilizzo di CancellationToken

### Passaggio 1: crea CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Qui creiamo un'istanza di CancellationTokenSource, un componente cruciale per la gestione della cancellazione nelle operazioni asincrone.

### Passaggio 2: inizializza la scena 3D

```csharp
Scene scene = new Scene();
```

Crea un'istanza della classe Scene. Questa sarà la tela per le tue attività di modellazione 3D.

### Passaggio 3: imposta il timeout del token Cancellation

```csharp
cts.CancelAfter(1000);
```

 Impostare il timeout di cancellazione utilizzando`CancelAfter` metodo. In questo esempio, il timeout è impostato su 1000 millisecondi (1 secondo).

### Passaggio 4: apri il documento 3D

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

 Tentare di aprire il documento 3D entro l'intervallo di tempo specificato. IL`cts.Token`Il parametro garantisce che l'operazione possa essere annullata se supera il timeout impostato.

### Passaggio 5: gestire l'eccezione di importazione

In caso di ImportException, gestiscila con garbo controllando se è stata causata da OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Conclusione

Congratulazioni! Hai completato con successo il processo di utilizzo di Aspose.3D per .NET con CancellationToken per gestire il caricamento di documenti 3D. Questa tecnica garantisce operazioni di importazione efficienti e tempestive, migliorando le prestazioni complessive delle tue applicazioni 3D.

## Domande frequenti

### Q1: Aspose.3D è compatibile con tutti i formati di file 3D?

 A1: Aspose.3D supporta un'ampia gamma di formati di file 3D, inclusi FBX, STL, OBJ e altri. Fare riferimento al[documentazione](https://reference.aspose.com/3d/net/) per l'elenco completo.

### Q2: Come posso ottenere una licenza temporanea per Aspose.3D?

 A2: Ottieni una licenza temporanea visitando[questo link](https://purchase.aspose.com/temporary-license/).

### Q3: Dove posso trovare supporto per Aspose.3D?

 A3: Partecipa alla discussione della community su[Forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Posso provare Aspose.3D gratuitamente prima dell'acquisto?

 R4: Sì, esplora le funzionalità con una prova gratuita disponibile[Qui](https://releases.aspose.com/).

### Q5: Qual è l'ultima versione di Aspose.3D per .NET?

 A5: Rimani aggiornato controllando il[pagina di download](https://releases.aspose.com/3d/net/) per l'ultima versione.