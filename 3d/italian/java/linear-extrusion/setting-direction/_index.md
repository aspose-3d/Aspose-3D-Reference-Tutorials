---
date: 2026-02-22
description: Scopri come impostare la direzione nell'estrusione lineare ed esportare
  il modello 3D in formato OBJ usando Aspose.3D per Java. Segui la nostra guida passo‑passo.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Come impostare la direzione nell'estrusione lineare con Aspose.3D per Java
url: /it/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come impostare la direzione nell'estrusione lineare con Aspose.3D per Java

## Introduzione

In questo tutorial completo scoprirai **come impostare la direzione** quando esegui un'estrusione lineare con Aspose.3D per Java. Che tu stia costruendo uno strumento simile a un CAD o generando geometria per un motore di gioco, controllare la direzione dell'estrusione ti permette di creare esattamente la forma di cui hai bisogno. Ti guideremo passo passo, dall'inizializzazione di un profilo al salvataggio del risultato come file OBJ, così potrai anche **esportare file obj di modelli 3d** direttamente da Java.

## Risposte rapide
- **Qual è la classe principale per l'estrusione lineare?** `LinearExtrusion`
- **Quale metodo definisce la direzione dell'estrusione?** `setDirection(Vector3 direction)`
- **Posso esportare il risultato come OBJ?** Sì, usando `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **È necessaria una licenza per lo sviluppo?** È disponibile una versione di prova gratuita; è richiesta una licenza per la produzione.
- **Quale IDE Java funziona meglio?** IntelliJ IDEA o Eclipse sono entrambi pienamente supportati.

## Cos'è l'estrusione lineare?

L'estrusione lineare prende un profilo 2‑D (come un rettangolo o un cerchio) e lo estende lungo una linea retta per creare un solido 3‑D. Per impostazione predefinita l'estrusione segue l'asse Z positivo, ma Aspose.3D ti consente di modificare quel percorso con la proprietà `setDirection`.

## Perché impostare la direzione nell'estrusione lineare?

Impostare una direzione personalizzata è utile quando:
- Allinei la geometria con oggetti esistenti in una scena.
- Crei parti inclinate o angolate senza passaggi di trasformazione aggiuntivi.
- Esporti modelli che devono corrispondere a un sistema di coordinate specifico (ad esempio, per la stampa 3‑D o i motori di gioco).

## Prerequisiti

Prima di iniziare, assicurati di avere:

- Conoscenze di base di Java.
- Libreria Aspose.3D installata. Puoi scaricarla da [qui](https://releases.aspose.com/3d/java/).
- Un IDE come Eclipse o IntelliJ IDEA.

## Importare i pacchetti

Per prima cosa, importa gli spazi dei nomi che forniscono le classi 3‑D di base e i tipi di utilità.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passo 1: Inizializzare il profilo di base

Crea la forma che verrà estrusa. In questo esempio usiamo un `RectangleShape` con un piccolo raggio di arrotondamento per dare ai bordi un aspetto liscio.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Passo 2: Creare una scena

Un oggetto `Scene` funge da contenitore per tutti i nodi 3‑D, luci, telecamere e materiali.

```java
Scene scene = new Scene();
```

## Passo 3: Creare i nodi

Aggiungi due nodi figlio alla radice della scena — uno per l'estrusione a sinistra e uno per l'estrusione a destra. Il nodo destro è traslato in modo che i due oggetti non si sovrappongano.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Passo 4: Eseguire l'estrusione lineare sul nodo sinistro

Estrudi il profilo sul nodo sinistro usando la direzione predefinita dell'asse Z. Aggiungiamo anche una torsione completa di 360° e aumentiamo il conteggio delle sezioni per una mesh più liscia.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Passo 5: Eseguire l'estrusione lineare sul nodo destro con direzione

Qui è dove **impostiamo la direzione**. Passando un `Vector3` personalizzato a `setDirection`, l'estrusione segue il vettore (0.3, 0.2, 1), producendo una forma inclinata.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Passo 6: Salvare la scena 3D

Infine, esporta la scena nel formato Wavefront OBJ. Questo passaggio dimostra come **salvare file obj java** e rende facile visualizzare il risultato in qualsiasi visualizzatore 3‑D.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| Il file OBJ appare vuoto | Il profilo non è stato aggiunto a un nodo | Assicurati che `createChildNode` sia chiamato su un nodo valido |
| La direzione sembra invariata | `setDirection` è stato chiamato dopo che l'estrusione era già stata costruita | Imposta la direzione all'interno dell'inizializzatore `LinearExtrusion` come mostrato |
| Mesh a bassa risoluzione | Il valore di `setSlices` è troppo basso | Aumenta il conteggio delle sezioni (ad esempio, 100 o più) |

## Conclusione

Ora sai **come impostare la direzione** in un'estrusione lineare, come regolare le impostazioni di torsione e sezioni, e come **esportare file obj di modelli 3d** usando Aspose.3D per Java. Queste tecniche ti offrono un controllo dettagliato sulla creazione della geometria e rendono semplice integrare asset 3‑D in pipeline più ampie.

## FAQ

### Q1: Posso usare Aspose.3D con altri linguaggi di programmazione?

A1: Aspose.3D supporta vari linguaggi di programmazione, tra cui .NET e Java.

### Q2. È disponibile una versione di prova gratuita per Aspose.3D?

A2: Sì, puoi esplorare le funzionalità di Aspose.3D con una prova gratuita [qui](https://releases.aspose.com/).

### Q3: Dove posso trovare la documentazione dettagliata per Aspose.3D per Java?

A3: La documentazione completa è disponibile [qui](https://reference.aspose.com/3d/java/).

### Q4: Come posso ottenere supporto per Aspose.3D?

A4: Visita il [forum Aspose.3D](https://forum.aspose.com/c/3d/18) per qualsiasi assistenza o domanda.

### Q5: Sono disponibili licenze temporanee per Aspose.3D?

A5: Sì, puoi ottenere una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ultimo aggiornamento:** 2026-02-22  
**Testato con:** Aspose.3D per Java (ultima release)  
**Autore:** Aspose