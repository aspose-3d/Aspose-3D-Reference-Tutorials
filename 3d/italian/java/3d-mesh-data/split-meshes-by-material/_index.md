---
date: 2026-01-27
description: Scopri come suddividere la mesh in modo efficiente per materiale in Java
  con Aspose.3D. Questa guida ti mostra come ridurre le chiamate di disegno e migliorare
  le prestazioni di rendering durante la suddivisione della mesh per materiale.
linktitle: How to Split Mesh by Material in Java Using Aspose.3D
second_title: Aspose.3D Java API
title: Come dividere la mesh per materiale in Java usando Aspose.3D
url: /it/java/3d-mesh-data/split-meshes-by-material/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come dividere una mesh per materiale in Java usando Aspose.3D

## Introduzione

Se lavori con la grafica 3D in Java, scoprirai rapidamente che l'elaborazione di mesh di grandi dimensioni può diventare un collo di bottiglia delle prestazioni, soprattutto quando una singola mesh contiene più materiali. **Imparare a dividere una mesh** per materiale ti consente di isolare ogni gruppo di poligoni specifico per materiale, permettendo un rendering più veloce, una culling più semplice e un controllo più granulare sulla gestione delle texture. In questo tutorial percorreremo i passaggi esatti per **dividere una mesh per materiale** usando la libreria Aspose.3D, con spiegazioni pratiche, consigli per ridurre le draw call e suggerimenti per migliorare le prestazioni di rendering.

## Risposte rapide
- **Che cosa significa “split mesh by material”?** Separa una singola mesh in più sub‑mesh, ognuna contenente poligoni che condividono lo stesso materiale.
- **Perché usare Aspose.3D?** Fornisce un'API di alto livello, cross‑platform, che astrae i formati di file a basso livello mantenendo le prestazioni.
- **Quanto tempo richiede l'implementazione?** Circa 10–15 minuti di codifica e test.
- **È necessaria una licenza?** È disponibile una versione di prova gratuita; è richiesta una licenza commerciale per l'uso in produzione.
- **Quale versione di Java è supportata?** Java 8 o.

## Cos'è la divisione della mesh?

La divisione della mesh è il processo di suddividere una mesh 3D complessa in parti più piccole e gestibili. Quando la divisione è basata sul materiale, ogni sub‑mesh risultante contiene solo i poligoni che fanno riferimento a un singolo materiale. Questo approccio riduce le draw call, migliora le prestazioni di rendering e semplifica attività come l'applicazione di shader per materiale.

## Perché dividere la mesh per materiale?

- **Prestazioni:** I motori di rendering possono raggruppare le draw call per materiale, riducendo i cambi di stato della GPU.
- **Flessibilità:** Puoi applicare diversi effetti di post‑processing o logiche di collisione per materiale.
- **Gestione della memoria:** Mesh più piccole sono più facili da caricare e scaricare dalla memoria, cosa cruciale per applicazioni mobile o VR.
- **Draw call ridotte:** Meno cambi di stato significano che la GPU può elaborare i fotogrammi più efficientemente.
- **Prestazioni di rendering migliorate:** Isolare i materiali porta spesso a risultati migliori di culling e shading.

## Prerequisiti

Prima di immergerci nel codice, assicurati di avere quanto segue:

- Conoscenza di base della programmazione Java.
- Libreria Aspose.3D per Java installata (scaricabile dal [sito Aspose](https://releases.aspose.com/3d/java/)).
- Un IDE come IntelliJ IDEA, Eclipse o VS Code configurato per lo sviluppo Java.

## Importare i pacchetti

Per prima cosa, importa le classi Aspose.3D necessarie e eventuali utility Java standard di cui avrai bisogno:

```java
import com.aspose.threed.*;

import java.util.Arrays;
```

## Guida passo‑passo

Di seguito trovi una panoramica concisa di ogni passaggio, con spiegazioni precedenti ai blocchi di codice in modo da sapere esattamente cosa sta accadendo.

### Passo 1: Creare una mesh di un cubo

Iniziamo con una primitiva geometrica semplice — un cubo — così da poter vedere chiaramente come ogni faccia (piano) ottenga il proprio materiale in seguito.

```java
// ExStart:SplitMeshbyMaterial

// Create a mesh of a box (composed of 6 planes)
Mesh box = (new Box()).toMesh();
```

### Passo 2: Creare un elemento Materiale

Un `VertexElementMaterial` memorizza gli indici di materiale per ogni poligono. Collegandolo alla mesh, possiamo controllare quale materiale usa ogni faccia.

```java
// Create a material element on the box mesh
VertexElementMaterial mat = (VertexElementMaterial) box.createElement(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX);
```

### Passo 3: Specificare indici di materiale diversi

Qui assegniamo un indice di materiale unico a ciascuno dei sei piani del cubo. L'ordine dell'array corrisponde all'ordine dei poligoni generati dalla primitiva `Box`.

```java
// Specify different material indices for each plane
mat.setIndices(new int[]{0, 1, 2, 3, 4, 5});
```

### Passo 4: Dividere la mesh in sub‑mesh

Chiamando `PolygonModifier.splitMesh` con `SplitMeshPolicy.CLONE_DATA` si crea una nuova sub‑mesh per ogni indice di materiale distinto, preservando i dati originali dei vertici.

```java
// Split the mesh into 6 sub-meshes, each plane becoming a sub-mesh
Mesh[] planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.CLONE_DATA);
```

### Passo 5: Aggiornare gli indici di materiale e dividere nuovamente

Per dimostrare una strategia di divisione diversa, raggruppiamo ora i primi tre piani sotto il materiale 0 e i restanti tre sotto il materiale 1, quindi dividiamo usando `COMPACT_DATA` per eliminare i vertici non utilizzati.

```java
// Update material indices and split into 2 sub-meshes
mat.getIndices().clear();
mat.setIndices(new int[]{0, 0, 0, 1, 1, 1});
planes = PolygonModifier.splitMesh(box, SplitMeshPolicy.COMPACT_DATA);
```

### Passo 6: Confermare il successo

Un semplice messaggio sulla console ti informa che l'operazione è stata completata senza errori.

```java
// Display success message
System.out.println("\nSplitting a mesh by specifying the material successfully.");
// ExEnd:SplitMeshbyMaterial
```

## Ridurre le draw call e migliorare le prestazioni di rendering

Trasformando ogni materiale nella propria mesh, abiliti la pipeline grafica a emettere una singola draw call per materiale anziché una per poligono. Questa riduzione delle draw call si traduce direttamente in frame rate più fluidi, soprattutto su hardware di fascia bassa. Inoltre, la politica `COMPACT_DATA` rimuove i vertici inutilizzati, riducendo ulteriormente la larghezza di banda della memoria e aiutando la GPU a renderizzare in modo più efficiente.

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| **Le sub‑mesh contengono vertici duplicati** | L'uso di `CLONE_DATA` copia tutti i dati dei vertici per ogni sub‑mesh. | Passa a `COMPACT_DATA` quando desideri che i vertici condivisi vengano deduplicati. |
| **Assegnazione materiale errata** | La lunghezza dell'array di indici non corrisponde al numero di poligoni. | Verifica il numero di poligoni (ad esempio, un cubo ne ha 6) e fornisci un array di indici corrispondente. |

## Domande frequenti

**D: Aspose.3D è compatibile con altre librerie Java 3D?**  
R: Sì, Aspose.3D può coesistere con librerie come Java 3D o jMonkeyEngine, consentendo di importare/esportare mesh tra di esse.

**D: Questa tecnica può essere applicata a modelli complessi con centinaia di materiali?**  
R: Assolutamente. Le stesse chiamate API funzionano indipendentemente dalla complessità della mesh; basta assicurarsi che l'array di indici rifletta correttamente la disposizione dei materiali.

**D: Dove posso trovare la documentazione completa di Aspose.3D per Java?**  
R: Visita la documentazione ufficiale [Aspose.3D Java documentation](https://reference.aspose.com/3d/java/) per riferimenti API dettagliati ed esempi aggiuntivi.

**D: È disponibile una versione di prova gratuita per Aspose.3D per Java?**  
R: Sì, puoi scaricare una versione di prova dalla [pagina Aspose Releases](https://releases.aspose.com/).

**D: Come posso ottenere supporto se incontro problemi?**  
R: Il forum della community Aspose ([Aspose.3D forum](https://forum.aspose.com/c/3d/18)) è un ottimo posto per porre domande e ricevere aiuto sia dal team Aspose sia da altri sviluppatori.

---

**Ultimo aggiornamento:** 2026-01-27  
**Testato con:** Aspose.3D for Java 24.11  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}