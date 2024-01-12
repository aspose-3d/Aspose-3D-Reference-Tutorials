---
title: Creazione del cilindro della ventola
linktitle: Creazione del cilindro della ventola
second_title: API Aspose.3D .NET
description: Sblocca il mondo della progettazione 3D con Aspose.3D per .NET! Crea straordinari cilindri con ventola e senza ventola senza sforzo. Scarica subito la tua versione di prova.
type: docs
weight: 10
url: /it/net/working-with-cylinder/create-fan-cylinder/
---
## introduzione
Benvenuti nel mondo della modellazione e visualizzazione 3D con Aspose.3D per .NET! In questa guida passo passo, esploreremo come creare un accattivante cilindro della ventola utilizzando Aspose.3D per .NET. Aspose.3D è una potente libreria che fornisce ampie funzionalità per lavorare con contenuti 3D nelle applicazioni .NET.
## Prerequisiti
Prima di immergerci nell'entusiasmante mondo della modellazione 3D, assicurati di possedere i seguenti prerequisiti:
- Una conoscenza di base della programmazione .NET.
- Visual Studio installato sul tuo computer.
-  Libreria Aspose.3D per .NET, che puoi scaricare[Qui](https://releases.aspose.com/3d/net/).
- Un genuino interesse nel liberare la tua creatività attraverso la progettazione 3D.
## Importa spazi dei nomi
Cominciamo importando gli spazi dei nomi necessari per rendere disponibile la funzionalità Aspose.3D nel tuo progetto .NET.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Importa spazi dei nomi Aspose.3D
```
Ora che è tutto pronto, suddividiamo il processo di creazione di un cilindro della ventola in passaggi gestibili.
## Passaggio 1: crea una scena
```csharp
// Crea una scena
Scene scene = new Scene();
```
Inizia inizializzando una nuova scena 3D. Questo funge da tela su cui il nostro cilindro della ventola prenderà vita.
## Passaggio 2: creare un cilindro della ventola
```csharp
// Crea un cilindro
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
Definisci le caratteristiche del tuo cilindro ventilatore, specificando parametri come raggio, altezza e risoluzione.
## Passaggio 3: personalizzare le proprietà del cilindro della ventola
```csharp
// Imposta GenerateFanCylinder su true
fan.GenerateFanCylinder = true;
// Imposta la lunghezza Theta
fan.ThetaLength = MathUtils.ToRadian(270);
```
Personalizza il cilindro della ventola abilitando la generazione della parte della ventola e regolando lo spostamento angolare utilizzando ThetaLength.
## Passaggio 4: posizionare il cilindro della ventola nella scena
```csharp
// Crea nodo figlio
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
Aggiungi il cilindro della ventola come nodo figlio al nodo radice della scena e posizionalo nello spazio 3D.
## Passaggio 5: creare un cilindro senza ventola
```csharp
// Crea un cilindro senza ventola
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
Esplora la flessibilità di Aspose.3D creando un cilindro senza la parte della ventola.
## Passaggio 6: personalizzare le proprietà del cilindro non ventola
```csharp
// Imposta GenerateFanCylinder su false
nonfan.GenerateFanCylinder = false;
// Imposta la lunghezza Theta
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
Distinguere il cilindro non ventola disabilitando la generazione della parte ventola.
## Passaggio 7: posizionare il cilindro senza ventola nella scena
```csharp
// Crea nodo figlio
scene.RootNode.CreateChildNode(nonfan);
```
Allo stesso modo, aggiungi il cilindro non fan come nodo figlio al nodo radice della scena.
## Passaggio 8: salva la scena
```csharp
// Salva scena
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
Salva il tuo capolavoro nel formato e nella posizione desiderati. Ora hai creato con successo una ventola e un cilindro non ventola utilizzando Aspose.3D per .NET!
## Conclusione
Congratulazioni per aver completato questa guida pratica alla modellazione 3D con Aspose.3D per .NET! Hai liberato la tua creatività nel regno digitale, realizzando con facilità cilindri a ventola e non.
## Domande frequenti
### Posso utilizzare Aspose.3D per .NET con altri framework .NET?
Sì, Aspose.3D è compatibile con vari framework .NET, offrendo versatilità nei tuoi progetti di sviluppo.
### È disponibile una prova gratuita per Aspose.3D per .NET?
 Sì, puoi esplorare una prova gratuita[Qui](https://releases.aspose.com/).
### Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?
 La documentazione è disponibile[Qui](https://reference.aspose.com/3d/net/).
### Come posso ottenere supporto per Aspose.3D per .NET?
 Visita il forum di supporto[Qui](https://forum.aspose.com/c/3d/18) per l'aiuto della comunità e degli esperti Aspose.
### Sono disponibili licenze temporanee per Aspose.3D per .NET?
 Sì, è possibile ottenere licenze temporanee[Qui](https://purchase.aspose.com/temporary-license/).