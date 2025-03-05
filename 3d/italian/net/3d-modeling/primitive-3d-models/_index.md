---
title: Creazione di modelli 3D primitivi
linktitle: Creazione di modelli 3D primitivi
second_title: API Aspose.3D .NET
description: Esplora il mondo della modellazione 3D con Aspose.3D per .NET. Crea straordinari modelli primitivi senza sforzo.
type: docs
weight: 10
url: /it/net/3d-modeling/primitive-3d-models/
---
## introduzione

Benvenuti nell'entusiasmante mondo della modellazione 3D con Aspose.3D per .NET! In questo tutorial completo, esploreremo il processo di creazione di modelli 3D primitivi utilizzando Aspose.3D in modo passo passo. Che tu sia uno sviluppatore esperto o un principiante curioso, questa guida ti aiuterà a sfruttare la potenza di Aspose.3D per creare elementi 3D visivamente sorprendenti per i tuoi progetti.

## Prerequisiti

Prima di immergerci nell'affascinante regno della modellazione 3D, assicurati di possedere i seguenti prerequisiti:

-  Aspose.3D per .NET: scarica e installa la libreria Aspose.3D per .NET da[Link per scaricare](https://releases.aspose.com/3d/net/).

- Ambiente di sviluppo: configura un ambiente di sviluppo .NET, garantendo la compatibilità con Aspose.3D.

Ora che hai gli elementi essenziali, iniziamo il nostro viaggio per creare modelli 3D primitivi passo dopo passo.

## Importa spazi dei nomi

Inizia importando gli spazi dei nomi necessari per accedere alle funzionalità fornite da Aspose.3D:

```csharp
using System;
using System.IO;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Animation;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
```

Con questi spazi dei nomi in atto, sei pronto per liberare la potenza di Aspose.3D nella tua applicazione .NET.

## Passaggio 1: inizializzare un oggetto scena

```csharp
//Inizializza un oggetto Scene
Scene scene = new Scene();
```

Crea un nuovo oggetto scena, che funge da tela per il tuo capolavoro 3D.

## Passaggio 2: crea un modello di scatola

```csharp
// Crea un modello di scatola
scene.RootNode.CreateChildNode("box", new Box());
```

Aggiungi un modello di scatola alla radice della tua scena. Personalizza le dimensioni e le proprietà della scatola secondo la tua visione creativa.

## Passaggio 3: creare un modello di cilindro

```csharp
// Creare un modello Cilindro
scene.RootNode.CreateChildNode("cylinder", new Cylinder());
```

Migliora la tua scena introducendo un modello di cilindro. Regola i suoi parametri per ottenere la forma e le dimensioni desiderate.

## Passaggio 4: salva il disegno in formato FBX

```csharp
// Salva il disegno nel formato FBX
var output = "Your Output Directory" + "test.fbx";
scene.Save(output, FileFormat.FBX7500ASCII);
```

Salva il tuo capolavoro 3D nel formato FBX. Scegli una directory di output e un nome file adatti per la tua creazione.

## Passaggio 5: Visualizza il messaggio di successo

```csharp
// Visualizza il messaggio di successo
Console.WriteLine("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
```

Festeggia il tuo risultato! La scena viene creata con successo da modelli 3D primitivi e il file viene salvato.

## Conclusione

 Congratulazioni! Hai creato con successo straordinari modelli 3D utilizzando Aspose.3D per .NET. Questa guida copre le nozioni di base, ma le possibilità sono illimitate. Esplorare la[documentazione](https://reference.aspose.com/3d/net/) per funzionalità e tecniche più avanzate.

## Domande frequenti

### Q1: posso utilizzare Aspose.3D per .NET con altri linguaggi di programmazione?

A1: Aspose.3D supporta principalmente .NET, ma sono disponibili altre versioni per Java e altre piattaforme.

### Q2: È disponibile una prova gratuita?

 A2: Sì, puoi esplorare le funzionalità di Aspose.3D con a[prova gratuita](https://releases.aspose.com/).

### Q3: Dove posso trovare supporto per Aspose.3D per .NET?

 A3: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il supporto e le discussioni della comunità.

### Q4: Come posso ottenere una licenza temporanea?

 A4: È possibile ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).

### Q5: Sono disponibili tutorial di esempio?

 A5: Sì, esplora ulteriori tutorial ed esempi nella sezione[documentazione](https://reference.aspose.com/3d/net/).