---
date: 2025-12-18
description: Scopri come creare una scena 3D e salvare un file OBJ usando Aspose.3D
  per Java. Segui la nostra guida passo‑passo per la direzione di estrusione lineare.
linktitle: Setting Direction in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Crea scena 3D – Imposta direzione di estrusione Aspose.3D Java
url: /it/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crea Scena 3D – Imposta Direzione di Estrusione Aspose.3D Java

## Introduzione

In questo tutorial imparerai **come creare scene 3d** oggetti e controllare la direzione di estrusione con Aspose.3D per Java. Che tu stia creando visualizzazioni architettoniche, prototipi di prodotto o asset per giochi, padroneggiare l'estrusione lineare ti offre la flessibilità di modellare forme complesse rapidamente. Ti guideremo passo passo, dall'aggiunta di nodi in Java a **esportare file obj di modello 3d**, così potrai vedere il risultato immediatamente.

## Risposte Rapide
- **Cosa significa “create 3d scene”?** Significa inizializzare un oggetto Aspose.3D `Scene` che conterrà tutta la geometria, le luci e le telecamere.  
- **Come imposto la direzione di estrusione?** Usa il metodo `setDirection(Vector3)` su un'istanza `LinearExtrusion`.  
- **Quale formato devo usare per l'esportazione?** Il formato OBJ (`FileFormat.WAVEFRONTOBJ`) è ampiamente supportato per i flussi di lavoro 3‑D.  
- **È necessaria una licenza per Aspose.3D?** Una prova gratuita funziona per lo sviluppo; è necessaria una licenza commerciale per la produzione.  
- **Posso aggiungere più nodi in Java?** Sì—usa `scene.getRootNode().createChildNode()` per aggiungere quanti oggetti desideri.

## Cos'è un flusso di lavoro “create 3d scene”?

Un flusso di lavoro **create 3d scene** inizia con un oggetto `Scene` vuoto, aggiunge geometria (come profili estrusi), la posiziona con trasformazioni e infine salva la scena in un formato file come OBJ. Questo modello è la spina dorsale della maggior parte delle applicazioni 3‑D costruite con Aspose.3D.

## Perché impostare la direzione di estrusione?

Impostare la direzione di estrusione ti consente di inclinare, ruotare o distorcere la forma mentre viene estrusa, dandoti il controllo sulla geometria finale senza ulteriori post‑processi. È particolarmente utile per:

- Creare colonne conica o tubi di forma personalizzata.  
- Allineare le estrusioni con assi non standard in parti meccaniche.  
- Generare forme artistiche per effetti visivi.

## Prerequisiti

- Conoscenza di base di Java.  
- Libreria Aspose.3D installata – scaricala da [here](https://releases.aspose.com/3d/java/).  
- Un IDE come Eclipse o IntelliJ IDEA.

## Importa Pacchetti

Per prima cosa, importa le classi Aspose.3D necessarie:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passo 1: Inizializza Profilo Base

Crea il profilo 2‑D che verrà estruso. In questo esempio usiamo un rettangolo arrotondato:

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

> **Consiglio:** Regola il raggio di arrotondamento per controllare quanto affilate o morbide appaiono gli angoli del rettangolo prima dell'estrusione.

## Passo 2: Crea una Scena

Ora **creiamo una scena 3d** che ospiterà i nostri oggetti:

```java
Scene scene = new Scene();
```

## Passo 3: Aggiungi Nodi Java – Posizionamento degli Oggetti

Aggiungeremo due nodi figlio (sinistro e destro) al nodo radice della scena e sposteremo leggermente quello sinistro di lato:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Passo 4: Come estrudere – Nodo Sinistro (direzione predefinita)

Estrudi il profilo sul nodo sinistro usando la direzione predefinita dell'asse Z. Impostiamo anche una torsione completa di 360° e aumentiamo il conteggio delle sezioni per la fluidità:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Passo 5: Come impostare la direzione – Nodo Destro

Qui **impostiamo la direzione** fornendo un `Vector3` personalizzato. Questo inclina l'estrusione verso il vettore (0.3, 0.2, 1):

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Passo 6: Salva file OBJ – Esporta modello 3D

Infine, **salviamo il file obj** per vedere il risultato in qualsiasi visualizzatore 3‑D:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Quando apri il file OBJ generato, vedrai due rettangoli estrusi: uno con la direzione predefinita e l'altro inclinato secondo il vettore impostato.

## Problemi Comuni e Soluzioni

| Problema | Motivo | Correzione |
|----------|--------|------------|
| Il file OBJ appare vuoto | Scena non salvata o percorso errato | Verifica che `MyDir` punti a una cartella scrivibile e che il nome del file termini con `.obj`. |
| L'estrusione sembra piatta | `setSlices` troppo basso | Aumenta `setSlices` (es., 200) per una geometria più fluida. |
| La direzione sembra invariata | Vettore non normalizzato | Usa un `Vector3` normalizzato o regola i valori per riflettere l'inclinazione desiderata. |

## Domande Frequenti

### Q1: Posso usare Aspose.3D con altri linguaggi di programmazione?
A1: Aspose.3D supporta vari linguaggi, inclusi .NET e Java.

### Q2: È disponibile una prova gratuita per Aspose.3D?
A2: Sì, puoi esplorare le funzionalità di Aspose.3D con una prova gratuita [here](https://releases.aspose.com/).

### Q3: Dove posso trovare la documentazione dettagliata per Aspose.3D per Java?
A3: La documentazione completa è disponibile [here](https://reference.aspose.com/3d/java/).

### Q4: Come posso ottenere supporto per Aspose.3D?
A4: Visita il [Aspose.3D forum](https://forum.aspose.com/c/3d/18) per qualsiasi assistenza o domanda.

### Q5: Sono disponibili licenze temporanee per Aspose.3D?
A5: Sì, puoi ottenere una licenza temporanea [here](https://purchase.aspose.com/temporary-license/).

---

**Ultimo Aggiornamento:** 2025-12-18  
**Testato Con:** Aspose.3D 24.11 per Java  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}