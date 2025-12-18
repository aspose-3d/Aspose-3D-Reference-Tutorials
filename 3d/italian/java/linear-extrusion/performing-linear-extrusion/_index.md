---
date: 2025-12-18
description: Impara come estrudere forme in Java usando Aspose.3D, crea una scena
  3D ed esporta file Wavefront OBJ senza sforzo.
linktitle: How to Extrude Shape in Java with Aspose.3D Linear Extrusion
second_title: Aspose.3D Java API
title: Come estrudere una forma in Java con Aspose.3D estrusione lineare
url: /it/java/linear-extrusion/performing-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Eseguire l'estrusione lineare in Aspose.3D per Java

## Introduzione

Benvenuti a questo tutorial completo su **how to extrude shape** in Aspose.3D per Java! Se desideri migliorare le tue competenze di modellazione 3D usando Java, sei nel posto giusto. Ti guideremo nella creazione di una scena 3D, nell'esecuzione dell'estrusione lineare e nell'esportazione del risultato come file Wavefront OBJ—tutto con esempi di codice chiari, passo dopo passo.

## Risposte rapide
- **Che cos'è l'estrusione lineare?** Estendere un profilo 2D lungo un percorso rettilineo per creare un solido 3D.  
- **Quale libreria gestisce questo in Java?** Aspose.3D for Java.  
- **Posso esportare in OBJ?** Sì, usando la funzionalità di esportazione Wavefront OBJ.  
- **È necessaria una licenza per lo sviluppo?** Una versione di prova gratuita funziona per i test; è necessaria una licenza per la produzione.  
- **Quale versione di Java è richiesta?** Java 1.6 o successiva.

## Che cos'è “how to extrude shape”?
L'estrusione lineare è una tecnica fondamentale nella **3d modeling java** che trasforma un profilo piatto — come un rettangolo — in un oggetto volumetrico tirandolo lungo una distanza definita. Questo metodo è ampiamente usato per creare parti meccaniche, elementi architettonici e modelli decorativi.

## Perché usare Aspose.3D per l'estrusione lineare?
- **Controllo completo** sulla geometria (fette, torsione, offset).  
- **Integrazione senza soluzione di continuità** con progetti Java—senza dipendenze native.  
- **Esportatori integrati** per formati popolari, incluso Wavefront OBJ, rendendo facile **generate 3d model** file per pipeline successive.

## Prerequisiti

Prima di immergerti nel tutorial, assicurati di avere i seguenti prerequisiti:

1. **Ambiente di sviluppo Java** – un JDK (1.6 o più recente) e il tuo IDE preferito.  
2. **Libreria Aspose.3D** – scarica e installa la libreria dal sito ufficiale **[here](https://releases.aspose.com/3d/java/)**.

## Importare i pacchetti

Una volta configurato l'ambiente di sviluppo e installata la libreria Aspose.3D, importa il pacchetto necessario:

```java
import com.aspose.threed.*;
```

### Passo 1: Impostare la directory del documento

Definisci la cartella in cui verranno salvati i file generati:

```java
String MyDir = "Your Document Directory";
```

> Questo garantisce che l'operazione **generate 3d model** scriva il file OBJ in una posizione nota.

### Passo 2: Inizializzare la forma di base

Crea un rettangolo che servirà da profilo di estrusione:

```java
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

Puoi regolare il raggio di arrotondamento per ottenere angoli arrotondati o impostarlo a `0` per un rettangolo perfetto.

### Passo 3: Eseguire l'estrusione lineare

Ora estrudiamo il rettangolo lungo l'asse Z, aggiungiamo fette, abilitiamo il centraggio e applichiamo una torsione con offset:

```java
LinearExtrusion extrusion = new LinearExtrusion(profile, 10) {{ setSlices(100); setCenter(true); setTwist(360); setTwistOffset(new Vector3(10, 0, 0));}};
```

- **Lunghezza dell'estrusione** – `10` unità.  
- **Fette** – `100` per una geometria liscia.  
- **Torsione** – `360°` crea una rotazione completa.  
- **Offset della torsione** – sposta l'origine della torsione a `(10, 0, 0)`.

### Passo 4: Creare una scena 3D

Crea un contenitore di scena e aggiungi l'estrusione come nodo figlio. Questo passo **creates 3d scene** che può contenere più oggetti:

```java
Scene scene = new Scene();
scene.getRootNode().createChildNode(extrusion);
```

### Passo 5: Salvare la scena 3D

Esporta la scena in un file Wavefront OBJ. Questo dimostra le capacità di **wavefront obj export** e **save 3d obj**:

```java
scene.save(MyDir +  "LinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

Dopo aver eseguito il codice, troverai `LinearExtrusion.obj` nella directory specificata, pronto per essere aperto in qualsiasi visualizzatore 3D o ulteriormente elaborato.

## Problemi comuni e soluzioni

| Problema | Motivo | Soluzione |
|----------|--------|-----------|
| Il file OBJ è vuoto | Il percorso della directory di output è errato o non scrivibile | Verifica che `MyDir` punti a una cartella esistente con permessi di scrittura. |
| Torsione non applicata | `setCenter(true)` omesso | Assicurati che il centraggio sia abilitato o regola i valori di `setTwistOffset`. |
| Errore di compilazione su `LinearExtrusion` | Uso di una versione più vecchia di Aspose.3D | Aggiorna all'ultima versione di Aspose.3D. |

## Domande frequenti

**Q: È Aspose.3D compatibile con tutte le versioni di Java?**  
A: Aspose.3D works with Java 1.6 and later.

**Q: Posso usare Aspose.3D per progetti commerciali?**  
A: Sì, l'uso commerciale è consentito con una licenza valida. Puoi ottenerla **[here](https://purchase.aspose.com/buy)**.

**Q: Dove posso ottenere supporto se incontro problemi?**  
A: Visita il **[Aspose.3D forum](https://forum.aspose.com/c/3d/18)** per aiuto della community o acquista una **[temporary license](https://purchase.aspose.com/temporary-license/)** per supporto premium.

**Q: Quali altre funzionalità di modellazione 3D offre Aspose.3D?**  
A: La libreria include manipolazione di mesh, operazioni booleane, mappatura delle texture e altro. Vedi l'elenco completo **[here](https://reference.aspose.com/3d/java/)**.

**Q: È disponibile una versione di prova gratuita?**  
A: Sì, puoi scaricare una versione di prova **[here](https://releases.aspose.com/)**.

## Conclusione

Ora hai imparato **how to extrude shape** usando Aspose.3D per Java, creato una scena 3D ed esportato il risultato come file Wavefront OBJ. Questa tecnica apre la porta a una vasta gamma di progetti **3d modeling java**—da parti semplici ad assemblaggi complessi. Esplora funzionalità aggiuntive come operazioni booleane o mappatura delle texture per arricchire ulteriormente i tuoi modelli.

---

**Ultimo aggiornamento:** 2025-12-18  
**Testato con:** Aspose.3D 24.11 for Java  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

## TARGET KEYWORDS:

**Primary Keyword (HIGHEST PRIORITY):**
how to extrude shape

**Secondary Keywords (SUPPORTING):**
create 3d scene, 3d modeling java, generate 3d model, wavefront obj export, save 3d obj