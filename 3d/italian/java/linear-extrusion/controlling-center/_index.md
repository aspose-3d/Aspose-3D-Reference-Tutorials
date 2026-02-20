---
date: 2026-02-20
description: Impara un tutorial di grafica 3D Java sul controllo del centro nell'estrusione
  lineare con Aspose.3D, inclusi come impostare il raggio di arrotondamento e salvare
  il file OBJ in Java.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Tutorial di grafica 3D Java – Centro nell'estrusione lineare
url: /it/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Tutorial Java 3D Graphics – Centro nell'estrusione lineare

## Introduzione

Se stai creando visualizzazioni 3D in Java, padroneggiare le tecniche di estrusione è fondamentale. Questo **java 3d graphics tutorial** ti guida nel controllare il centro di un'estrusione lineare usando Aspose.3D per Java, così potrai realizzare modelli precisi e simmetrici senza calcoli aggiuntivi. Alla fine di questa guida comprenderai perché la proprietà `center` è importante, come **impostare il raggio di arrotondamento** e come **salvare un file OBJ** compatibile con Java.

## Risposte rapide
- **Cosa fa la proprietà center?** Determina se l'estrusione è simmetrica attorno all'origine del profilo.  
- **È necessaria una licenza per eseguire il codice?** Una licenza temporanea è sufficiente per i test; una licenza completa è richiesta per la produzione.  
- **Quale formato di file viene usato per il risultato?** La scena viene salvata come file Wavefront OBJ.  
- **Posso modificare il numero di slice?** Sì, usa `setSlices(int)` sull'oggetto `LinearExtrusion`.  
- **Aspose.3D è compatibile con Java 8+?** Assolutamente sì – supporta tutte le versioni moderne di Java.

## Che cos'è un java 3d graphics tutorial?

Un **java 3d graphics tutorial** spiega passo‑passo come utilizzare le librerie Java per creare, manipolare e renderizzare oggetti tridimensionali. In questo caso, ci concentriamo sull'API di estrusione di Aspose.3D, che trasforma profili 2‑D in mesh 3‑D complete.

## Perché usare Aspose.3D per Java?

- **API di alto livello** – Nessuna necessità di scrivere calcoli di mesh a basso livello.  
- **Supporto multi‑formato** – Esporta in OBJ, FBX, STL e molto altro.  
- **Ottimizzato per le prestazioni** – Gestisce scene di grandi dimensioni in modo efficiente.  
- **Documentazione ricca** – Include esempi come quello qui sotto.

## Prerequisiti

Prima di iniziare, assicurati di avere:

1. **Ambiente di sviluppo Java** – JDK 8 o versioni successive installate.  
2. **Aspose.3D per Java** – Scarica la libreria e la documentazione [qui](https://reference.aspose.com/3d/java/).  
3. **Directory dei documenti** – Crea una cartella sul tuo computer per memorizzare i file generati; la chiameremo **“Your Document Directory.”**

## Importare i pacchetti

Nel tuo IDE Java, importa le classi Aspose.3D necessarie. Questo fornisce al compilatore l'accesso alle funzionalità di estrusione e costruzione della scena.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Guida passo‑passo

### Passo 1: Configurare il profilo di base

Per prima cosa, crea la forma 2‑D che verrà estrusa. Qui usiamo un rettangolo e **impostiamo il raggio di arrotondamento** a 0,3, che smussa gli angoli.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Passo 2: Creare una scena 3D

Un oggetto `Scene` funge da contenitore per tutti i nodi 3‑D, le luci e le telecamere.

```java
Scene scene = new Scene();
```

### Passo 3: Aggiungere nodi sinistro e destro

Inseriremo due nodi separati affiancati così da poter confrontare l'estrusione con e senza centratura.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 4: Estrusione lineare – Nessun centro (nodo sinistro)

Crea l'estrusione sul nodo sinistro, disabilita la centratura e limita la mesh a tre slice per una preview low‑poly.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Passo 5: Aggiungere un piano di riferimento (nodo sinistro)

Una scatola sottile funge da pavimento visivo, aiutandoti a vedere l'orientamento dell'estrusione.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Passo 6: Estrusione lineare – Centrata (nodo destro)

Ora ripeti l'estrusione, questa volta abilitando `center`. La geometria sarà simmetrica attorno all'origine del profilo.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Passo 7: Aggiungere un piano di riferimento (nodo destro)

Stesso piano di riferimento per il lato destro, per rendere il confronto chiaro.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Passo 8: Salvare la scena 3D

Infine, esporta l'intera scena in un file Wavefront OBJ – un formato facilmente utilizzabile nella maggior parte degli editor 3‑D.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| **L'estrusione appare spostata** | `setCenter(false)` lascia il profilo ancorato al suo angolo. | Usa `setCenter(true)` per risultati simmetrici. |
| **Il file OBJ è vuoto** | Il percorso della directory di output è errato o mancano i permessi di scrittura. | Verifica che `MyDir` punti a una cartella esistente e che l'applicazione abbia i permessi di scrittura. |
| **Gli angoli arrotondati appaiono netti** | Il raggio di arrotondamento è troppo piccolo rispetto alle dimensioni del rettangolo. | Aumenta il valore del raggio (es. `setRoundingRadius(0.5)`). |

## Domande frequenti

### Q1: Posso usare Aspose.3D per Java in progetti commerciali?

A1: Sì, Aspose.3D per Java è disponibile per uso commerciale. Per i dettagli sulla licenza, visita [qui](https://purchase.aspose.com/buy).

### Q2: È disponibile una versione di prova gratuita?

A2: Sì, puoi provare gratuitamente Aspose.3D per Java [qui](https://releases.aspose.com/).

### Q3: Dove posso trovare supporto per Aspose.3D per Java?

A3: Il forum della community di Aspose.3D è un ottimo posto per chiedere supporto e condividere esperienze. Visita il forum [qui](https://forum.aspose.com/c/3d/18).

### Q4: È necessaria una licenza temporanea per i test?

A4: Sì, se ti serve una licenza temporanea per scopi di test, puoi ottenerla [qui](https://purchase.aspose.com/temporary-license/).

### Q5: Dove posso trovare la documentazione?

A5: La documentazione per Aspose.3D per Java è disponibile [qui](https://reference.aspose.com/3d/java/).

## Conclusione

Completato questo **java 3d graphics tutorial**, ora sai come controllare il centro di un'estrusione lineare, regolare il raggio di arrotondamento e **salvare un file OBJ** compatibile con Java usando Aspose.3D. Queste tecniche ti offrono un controllo dettagliato sulla simmetria della mesh, fondamentale per asset di gioco, prototipi CAD e visualizzazioni scientifiche. Sentiti libero di sperimentare con profili diversi, numeri di slice e formati di esportazione per ampliare il tuo toolbox 3‑D.

---

**Ultimo aggiornamento:** 2026-02-20  
**Testato con:** Aspose.3D per Java 24.11  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}