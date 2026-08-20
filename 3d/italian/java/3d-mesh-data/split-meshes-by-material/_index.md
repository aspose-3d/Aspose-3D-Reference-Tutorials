---
date: 2026-05-04
description: Scopri come suddividere la mesh in modo efficiente per materiale in Java
  con Aspose.3D. Questa guida ti mostra come ridurre le chiamate di disegno e migliorare
  le prestazioni di rendering durante la suddivisione della mesh per materiale.
keywords:
- how to split mesh
- reduce draw calls
- improve rendering performance
- split mesh by material
linktitle: Come dividere una mesh per materiale in Java usando Aspose.3D
second_title: Aspose.3D Java API
title: Come dividere la mesh per materiale in Java usando Aspose.3D
url: /it/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come dividere una Mesh per Materiale in Java usando Aspose.3D

## Introduzione

Se lavori con la grafica 3D in Java, scoprirai rapidamente che l'elaborazione di mesh di grandi dimensioni può diventare un collo di bottiglia delle prestazioni, soprattutto quando una singola mesh contiene più materiali. **Imparare a dividere la mesh** per materiale ti consente di isolare ogni gruppo di poligoni specifico per materiale, permettendo un rendering più veloce, una culling più semplice e un controllo più granulare sulla gestione delle texture. In questo tutorial percorreremo i passaggi esatti per **dividere la mesh per materiale** usando la libreria Aspose.3D, con spiegazioni pratiche, consigli per ridurre le draw call e suggerimenti per migliorare le prestazioni di rendering.

## Risposte rapide
- **Cosa significa “dividere la mesh per materiale”?** Separa una singola mesh in più sotto‑mesh, ognuna contenente poligoni che condividono lo stesso materiale.  
- **Perché usare Aspose.3D?** Fornisce un'API di alto livello, cross‑platform, che astrae i formati di file a basso livello mantenendo le prestazioni.  
- **Quanto tempo richiede l'implementazione?** Circa 10–15 minuti di codifica e test.  
- **È necessaria una licenza?** È disponibile una versione di prova gratuita; è richiesta una licenza commerciale per l'uso in produzione.  
- **Quale versione di Java è supportata?** Java 8 o superiore.

## Come dividere una Mesh per Materiale – Panoramica
Dividere una mesh per materiale è essenzialmente un processo a due fasi: prima etichetti ogni poligono con un indice di materiale, poi chiedi ad Aspose.3D di separare la mesh in base a quegli indici. Il risultato è una collezione di mesh più piccole, ognuna delle quali può essere renderizzata con una singola draw call—ottimo per **ridurre le draw call** e **migliorare le prestazioni di rendering** sia su GPU desktop che mobile.

## Cos'è la Divisione di Mesh?

La divisione di mesh è il processo di suddividere una mesh 3D complessa in pezzi più piccoli e gestibili. Quando la divisione è basata sul materiale, ogni sotto‑mesh risultante contiene solo i poligoni che fanno riferimento a un singolo materiale. Questo approccio riduce le draw call, migliora le prestazioni di rendering e semplifica attività come l'applicazione di shader per materiale.

## Perché dividere una Mesh per Materiale?

- **Prestazioni:** I motori di rendering possono raggruppare le draw call per materiale, riducendo i cambi di stato della GPU.  
- **Flessibilità:** Puoi applicare effetti di post‑processing o logiche di collisione diverse per materiale.  
- **Gestione della Memoria:** Mesh più piccole sono più facili da caricare e scaricare dalla memoria, cosa cruciale per applicazioni mobile o VR.  
- **Riduzione delle Draw Call:** Meno cambi di stato consentono alla GPU di elaborare i fotogrammi più efficientemente.  
- **Miglioramento delle Prestazioni di Rendering:** L'isolamento dei materiali porta spesso a una culling e a risultati di shading migliori.

## Casi d'Uso Comuni

| Scenario | Beneficio della divisione |
|----------|---------------------------|
| **Giochi di strategia in tempo reale** | Ogni tipo di terreno può avere il proprio materiale, consentendo al motore di disegnare tutti i tappeti d'erba in un'unica chiamata. |
| **Visualizzazione architettonica** | Muri, vetro e metallo possono essere gestiti separatamente per effetti shader distinti. |
| **App AR mobili** | Ridurre le draw call aiuta a mantenere 60 fps su hardware limitato. |
| **Esperienze VR** | Un carico di lavoro GPU più basso riduce la latenza, migliorando il comfort dell'utente. |

## Prerequisiti

Prima di immergerti nel codice, assicurati di avere quanto segue:

- Conoscenza di base della programmazione Java.  
- Libreria Aspose.3D per Java installata (scaricabile dal [sito Aspose](https://releases.aspose.com/3d/java/)).  
- Un IDE come IntelliJ IDEA, Eclipse o VS Code configurato per lo sviluppo Java.

## Importare i Pacchetti

Per prima cosa, importa le classi Aspose.3D necessarie e eventuali utility Java standard di cui avrai bisogno:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Guida passo‑passo

Di seguito trovi una panoramica concisa di ogni passaggio, con spiegazioni prima dei blocchi di codice così sai esattamente cosa sta accadendo.

### Passo 1: Creare una Mesh di un Cubo

Iniziamo con una primitiva geometrica semplice—un cubo—così possiamo vedere chiaramente come ogni faccia (piano) ottenga il proprio materiale in seguito.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Passo 2: Creare un Elemento Materiale

Un `VertexElementMaterial` memorizza gli indici di materiale per ogni poligono. Collegandolo alla mesh, possiamo controllare quale materiale usa ogni faccia.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Passo 3: Specificare Indici di Materiale Diversi

Qui assegniamo un indice di materiale unico a ciascuno dei sei piani del cubo. L'ordine dell'array corrisponde all'ordine dei poligoni generati dalla primitiva `Box`.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Passo 4: Dividere la Mesh in Sotto‑Mesh

Chiamando `PolygonModifier.splitMesh` con `SplitMeshPolicy.CLONE_DATA` si crea una nuova sotto‑mesh per ogni indice di materiale distinto, preservando i dati dei vertici originali.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Passo 5: Aggiornare gli Indici di Materiale e Dividere Nuovamente

Per dimostrare una strategia di divisione diversa, raggruppiamo ora i primi tre piani sotto il materiale 0 e i restanti tre sotto il materiale 1, quindi dividiamo usando `COMPACT_DATA` per eliminare i vertici inutilizzati.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Passo 6: Confermare il Successo

Un semplice messaggio sulla console ti informa che l'operazione è stata completata senza errori.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Ridurre le Draw Call e Migliorare le Prestazioni di Rendering

Trasformando ogni materiale nella propria mesh, permetti alla pipeline grafica di emettere una singola draw call per materiale anziché una per poligono. Questa riduzione delle draw call si traduce direttamente in frame rate più fluidi, soprattutto su hardware di fascia bassa. Inoltre, la politica `COMPACT_DATA` rimuove i vertici inutilizzati, riducendo ulteriormente la larghezza di banda della memoria e aiutando la GPU a renderizzare in modo più efficiente.

## Problemi Comuni e Soluzioni

| Problema | Perché succede | Correzione |
|----------|----------------|------------|
| **Le sotto‑mesh contengono vertici duplicati** | L'uso di `CLONE_DATA` copia tutti i dati dei vertici per ogni sotto‑mesh. | Passa a `COMPACT_DATA` quando desideri deduplicare i vertici condivisi. |
| **Assegnazione di materiale errata** | La lunghezza dell'array di indici non corrisponde al numero di poligoni. | Verifica il numero di poligoni (ad esempio, un cubo ha 6) e fornisci un array di indici corrispondente. |

## Domande Frequenti

**Q: Aspose.3D è compatibile con altre librerie Java 3D?**  
A: Sì, Aspose.3D può coesistere con librerie come Java 3D o jMonkeyEngine, permettendoti di importare/esportare mesh tra di esse.

**Q: Questa tecnica può essere applicata a modelli complessi con centinaia di materiali?**  
A: Assolutamente. Le stesse chiamate API funzionano indipendentemente dalla complessità della mesh; basta assicurarsi che l'array di indici rifletta correttamente la disposizione dei materiali.

**Q: Dove posso trovare la documentazione completa di Aspose.3D per Java?**  
A: Visita la [documentazione ufficiale di Aspose.3D Java](https://reference.aspose.com/3d/java/) per riferimenti API dettagliati ed esempi aggiuntivi.

**Q: È disponibile una versione di prova gratuita per Aspose.3D per Java?**  
A: Sì, puoi scaricare una versione di prova dalla [pagina Releases di Aspose](https://releases.aspose.com/).

**Q: Come posso ottenere supporto se riscontro problemi?**  
A: Il forum della community Aspose ([forum Aspose.3D](https://forum.aspose.com/c/3d/18)) è un ottimo luogo per porre domande e ricevere aiuto sia dal team Aspose sia da altri sviluppatori.

## Conclusione

Ora disponi di un metodo completo e pronto per la produzione per **dividere la mesh per materiale** usando Aspose.3D in Java. Applicando questa tecnica otterrai meno draw call, un uso della memoria più efficiente e un rendering più fluido su una vasta gamma di dispositivi. Sentiti libero di sperimentare con le diverse opzioni di `SplitMeshPolicy` o di integrare le sotto‑mesh risultanti nel tuo pipeline di rendering.

---

**Ultimo aggiornamento:** 2026-05-04  
**Testato con:** Aspose.3D per Java 24.11  
**Autore:** Aspose

---

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}