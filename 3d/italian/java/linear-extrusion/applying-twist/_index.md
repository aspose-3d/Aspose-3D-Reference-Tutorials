---
date: 2025-12-17
description: Scopri come creare un modello 3D attorcigliato usando Aspose.3D per Java
  con estrusione lineare torcente ed esportare il file OBJ in Java. Segui la nostra
  guida passo passo.
linktitle: Applying Twist in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Crea modello 3D attorcigliato – Applicare la torsione nell'estrusione lineare
  con Aspose.3D per Java
url: /it/java/linear-extrusion/applying-twist/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Applicare la torsione nell'estrusione lineare con Aspose.3D per Java

## Introduzione

Benvenuti a questo tutorial passo‑paso su **come creare un modello 3D torcente** applicando una torsione durante l'estrusione lineare con Aspose.3D per Java. Che stiate realizzando visualizzazioni architettoniche, asset per giochi o prototipi ingegneristici, aggiungere una torsione può conferire alla vostra geometria un aspetto dinamico e a spirale con poche righe di codice.

## Risposte rapide
- **Che cosa significa “twist” (torsione) nell'estrusione?** Ruota il profilo attorno all'asse di estrusione man mano che la forma viene allungata.  
- **Quale classe API gestisce la torsione?** `LinearExtrusion` fornisce il metodo `setTwist`.  
- **È necessaria una licenza per eseguire l'esempio?** Una versione di prova gratuita è sufficiente per la valutazione; per la produzione è richiesta una licenza commerciale.  
- **Posso esportare il risultato come OBJ?** Sì, usa `scene.save(..., FileFormat.WAVEFRONTOBJ)`.  
- **Quale versione di Java è richiesta?** Java 8 o successive sono pienamente supportate.

## Prerequisiti

Prima di immergervi nel tutorial, assicuratevi di avere i seguenti prerequisiti:

- **Ambiente di sviluppo Java:** assicuratevi di avere Java installato sul vostro sistema.  
- **Libreria Aspose.3D:** scaricate e installate la libreria Aspose.3D per Java dal [download link](https://releases.aspose.com/3d/java/).  
- **Documentazione:** consultate la [documentazione Aspose.3D](https://reference.aspose.com/3d/java/) per una guida completa.

## Importare i pacchetti

Prima di iniziare a scrivere il codice, importate i pacchetti necessari nel vostro progetto Java. Ecco un esempio di come farlo:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Impostare la directory del documento

Definite innanzitutto dove verrà salvato il file 3D generato.

```java
// ExStart:SetDocumentDirectory
String MyDir = "Your Document Directory";
// ExEnd:SetDocumentDirectory
```

## Inizializzare il profilo di base

Successivamente, create la forma che verrà estrusa. In questo esempio utilizziamo un rettangolo con un piccolo raggio di arrotondamento.

```java
// ExStart:InitializeBaseProfile
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
// ExEnd:InitializeBaseProfile
```

## Creare una scena

Un oggetto `Scene` funge da contenitore per tutti i nodi 3D.

```java
// ExStart:CreateScene
Scene scene = new Scene();
// ExEnd:CreateScene
```

## Creare i nodi

Aggiungete due nodi figlio alla scena – uno rimarrà dritto, l'altro riceverà la torsione.

```java
// ExStart:CreateNodes
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
// ExEnd:CreateNodes
```

## Torsione nell'estrusione lineare

Ora eseguiamo la **torsione nell'estrusione lineare** su entrambi i nodi. Il nodo sinistro ottiene una torsione di 0° (dritto), mentre il nodo destro ottiene una torsione di 90°, creando una forma a spirale. Impostiamo anche il numero di slice per garantire una geometria fluida.

```java
// ExStart:LinearExtrusionWithTwist
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(0); setSlices(100); }});
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(90); setSlices(100); }});
// ExEnd:LinearExtrusionWithTwist
```

## Esportare file OBJ Java

Infine, salvate la scena nel formato OBJ, ampiamente supportato. Questo dimostra la capacità di **esportare file OBJ Java** di Aspose.3D.

```java
// ExStart:Save3DScene
scene.save(MyDir + "TwistInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
// ExEnd:Save3DScene
```

## Perché è importante

Creare un modello 3D torcente vi offre un effetto visivo potente senza la necessità di strumenti di modellazione esterni. È particolarmente utile per:

- **Componenti meccanici** che richiedono caratteristiche elicoidali (ad es., molle, viti).  
- **Design artistici** dove una leggera spirale aggiunge interesse visivo.  
- **Asset di gioco** che beneficiano di geometria low‑poly generata proceduralmente.

## Problemi comuni e suggerimenti

| Problema | Soluzione |
|----------|-----------|
| La torsione appare piatta o assente | Assicuratevi che `setSlices` sia sufficientemente alto (es., 100) per una rotazione fluida. |
| Il file OBJ non si apre nel visualizzatore | Verificate che il percorso di output (`MyDir`) sia corretto e che il file abbia i permessi di scrittura. |
| Scala inattesa | Controllate il sistema di unità del profilo di origine; Aspose.3D utilizza i metri per impostazione predefinita. |

## Domande frequenti

**D: Posso usare Aspose.3D per Java per lavorare con altri formati di file 3D?**  
R: Sì, Aspose.3D supporta una vasta gamma di formati come FBX, STL, 3MF e molti altri.

**D: Dove posso trovare supporto per Aspose.3D per Java?**  
R: Visitate il [forum Aspose.3D](https://forum.aspose.com/c/3d/18) per assistenza della community e supporto ufficiale.

**D: È disponibile una versione di prova gratuita?**  
R: Sì, potete scaricare una versione di prova da [qui](https://releases.aspose.com/).

**D: Come ottengo una licenza temporanea per i test?**  
R: Ottenete una licenza temporanea dalla [pagina della licenza temporanea](https://purchase.aspose.com/temporary-license/).

**D: Dove posso acquistare una licenza completa?**  
R: Acquistate Aspose.3D per Java dalla [pagina di acquisto](https://purchase.aspose.com/buy).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2025-12-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose