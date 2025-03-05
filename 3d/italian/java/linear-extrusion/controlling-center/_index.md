---
title: Centro di controllo nell'estrusione lineare con Aspose.3D per Java
linktitle: Centro di controllo nell'estrusione lineare con Aspose.3D per Java
second_title: API Java Aspose.3D
description: Esplora il mondo della grafica 3D in Java con Aspose.3D. Controlla il centro nell'estrusione lineare senza sforzo.
type: docs
weight: 11
url: /it/java/linear-extrusion/controlling-center/
---
## introduzione

Nel mondo della grafica 3D e della programmazione Java, il controllo del centro nell'estrusione lineare gioca un ruolo cruciale per ottenere gli effetti desiderati nei tuoi progetti. Aspose.3D per Java fornisce un potente toolkit per gestire tali attività senza problemi. In questo tutorial, approfondiremo il processo di controllo del centro nell'estrusione lineare utilizzando Aspose.3D per Java, analizzando ogni passaggio per garantire una comprensione fluida e completa.

## Prerequisiti

Prima di intraprendere questo viaggio tutorial, assicurati di disporre dei seguenti prerequisiti:

1. Ambiente di sviluppo Java: assicurati di avere un ambiente di sviluppo Java configurato sul tuo computer.

2.  Aspose.3D per Java: scarica e installa la libreria Aspose.3D. Potete trovare la biblioteca e la sua documentazione[Qui](https://reference.aspose.com/3d/java/).

3. Directory dei documenti: crea una directory per archiviare i tuoi documenti Java. Chiamiamola "La tua directory dei documenti".

## Importa pacchetti

Nel tuo ambiente di sviluppo Java, importa i pacchetti necessari per Aspose.3D. Ciò garantisce che il tuo codice abbia accesso alle funzionalità fornite dalla libreria.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passaggio 1: impostare il profilo di base

Inizializzare il profilo di base da estrudere. In questo esempio utilizzeremo una forma rettangolare con un raggio di arrotondamento di 0,3.

```java
// Il percorso della directory dei documenti.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Passaggio 2: crea una scena 3D

Costruisci le fondamenta del tuo mondo 3D creando una scena.

```java
Scene scene = new Scene();
```

## Passaggio 3: crea i nodi sinistro e destro

Stabilisci i nodi sinistro e destro all'interno della scena. Questi nodi fungono da tela per i tuoi oggetti 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Passaggio 4: estrusione lineare con proprietà Center

Esegui l'estrusione lineare sul nodo sinistro senza centrare e imposta il numero di fette su 3.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Passaggio 5: impostare il piano terra come riferimento

Migliora la rappresentazione visiva aggiungendo un piano terra al nodo sinistro.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Passo 6: Estrusione lineare con proprietà Center (nodo destro)

Esegui l'estrusione lineare sul nodo destro, questa volta centrando l'estrusione e imposta nuovamente il numero di fette su 3.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Passaggio 7: impostare il piano terra come riferimento (nodo destro)

Similmente al nodo sinistro, aggiungi un piano terra al nodo destro come riferimento.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Passaggio 8: salva la scena 3D

Salva la tua scena 3D in formato Wavefront OBJ.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusione

Il controllo del centro nell'estrusione lineare con Aspose.3D per Java apre interessanti possibilità nello sviluppo di grafica 3D. Seguendo questa guida passo passo, hai imparato come manipolare la proprietà center, consentendoti di ottenere gli effetti visivi desiderati nei tuoi progetti Java.

## Domande frequenti

### Q1: Posso utilizzare Aspose.3D per Java in progetti commerciali?

 A1: Sì, Aspose.3D per Java è disponibile per uso commerciale. Per i dettagli sulla licenza, visitare[Qui](https://purchase.aspose.com/buy).

### Q2: È disponibile una prova gratuita?

 A2: Sì, puoi esplorare una prova gratuita di Aspose.3D per Java[Qui](https://releases.aspose.com/).

### Q3: Dove posso trovare supporto per Aspose.3D per Java?

 A3: Il forum della community Aspose.3D è un ottimo posto per cercare supporto e condividere le tue esperienze. Visita il forum[Qui](https://forum.aspose.com/c/3d/18).

### Q4: Ho bisogno di una licenza temporanea per i test?

R4: Sì, se hai bisogno di una licenza temporanea a scopo di test, puoi ottenerne una[Qui](https://purchase.aspose.com/temporary-license/).

### Q5: Dove posso trovare la documentazione?

 A5: La documentazione per Aspose.3D per Java è disponibile[Qui](https://reference.aspose.com/3d/java/).