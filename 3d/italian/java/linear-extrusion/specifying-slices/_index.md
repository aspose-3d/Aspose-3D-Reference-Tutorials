---
date: 2026-02-22
description: Scopri come creare estrusioni 3D con fette usando Aspose.3D per Java.
  Questa guida passo passo copre l'estrusione lineare, l'impostazione del raggio di
  arrotondamento e l'esportazione in OBJ.
linktitle: Create 3D Extrusion with Slices – Aspose.3D for Java
second_title: Aspose.3D Java API
title: Crea estrusione 3D con fette – Aspose.3D per Java
url: /it/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crea estrusione 3D con fette – Aspose.3D per Java

## Introduction

Se hai bisogno di **creare estrusione 3D** oggetti che appaiono lisci e precisi, controllare il numero di fette è fondamentale. In questo tutorial vedremo come specificare le fette durante un'estrusione lineare con Aspose.3D per Java. Vedrai perché il conteggio delle fette è importante, come impostare un raggio di arrotondamento e come esportare il risultato in un file OBJ che può essere usato in qualsiasi pipeline 3D.

## Quick Answers
- **Cosa controllano le “fette”?** Il numero di sezioni trasversali intermedie usate per approssimare la superficie dell'estrusione.  
- **Quale metodo imposta il conteggio delle fette?** `LinearExtrusion.setSlices(int)`  
- **Posso modificare il raggio di arrotondamento del profilo?** Sì, tramite `RectangleShape.setRoundingRadius(double)`  
- **Quale formato file è usato in questo esempio?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Ho bisogno di una licenza per eseguire il codice?** Una versione di prova gratuita è sufficiente per la valutazione; è necessaria una licenza commerciale per la produzione.

## What is a linear extrusion with slices?

L'estrusione lineare prende un profilo 2‑D (come un rettangolo) e lo allunga lungo una linea retta per formare un solido 3‑D. Specificando le **fette**, si indica ad Aspose.3D quanti passaggi intermedi generare, influenzando direttamente la fluidità dei bordi curvi, come un rettangolo arrotondato.

## Why use Aspose.3D for Java to create 3d extrusion?

* **Controllo completo** – Puoi regolare il conteggio delle fette, il raggio di arrotondamento e il formato di esportazione programmaticamente.  
* **Cross‑platform** – Funziona su qualsiasi ambiente abilitato a Java senza dipendenze native.  
* **Flessibilità di esportazione** – Salva direttamente in OBJ, FBX, STL e molti altri formati.

## Prerequisites

1. **Java Development Kit** – JDK 8 o versioni successive installate.  
2. **Aspose.3D for Java** – Scarica la libreria dal sito ufficiale [qui](https://releases.aspose.com/3d/java/).  
3. Un IDE o editor di testo a tua scelta.

## Import Packages

Aggiungi lo spazio dei nomi Aspose.3D al tuo progetto così potrai accedere alle classi di modellazione 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Step‑by‑Step Guide

### Step 1: Set up the scene and define the profile

Per prima cosa creiamo un `RectangleShape` e gli assegniamo un **raggio di arrotondamento** così gli angoli sono lisci. Poi inizializziamo una nuova `Scene` che conterrà tutta la geometria.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Step 2: **Create child node** objects for each extrusion

Ogni elemento di geometria vive sotto un `Node`. Qui generiamo due nodi fratelli – uno per un'estrusione a poche fette e un altro per un'estrusione ad alte fette – e spostiamo il nodo sinistro leggermente di lato così i risultati sono facili da confrontare.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Step 3: Perform linear extrusion and **set slices**

Ora creiamo effettivamente gli oggetti **crea estrusione 3d**. Il costruttore `LinearExtrusion` accetta il profilo e la profondità di estrusione. Usando una **classe interna anonima** chiamiamo `setSlices` per controllare la fluidità. Il nodo sinistro ottiene solo 2 fette (grossolane), mentre il nodo destro ne ottiene 10 (lisce).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Step 4: **Export OBJ** – save the scene

Infine scriviamo la scena in un file Wavefront OBJ, un formato ampiamente supportato da editor 3‑D e motori di gioco. Questo dimostra la capacità di **export obj java** di Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Problema | Perché accade | Soluzione |
|-------|----------------|-----|
| **L'estrusione appare piatta** | Il conteggio delle fette è impostato a 1 o 0 | Assicurati che `setSlices` sia chiamato con un valore ≥ 2. |
| **Gli angoli arrotondati appaiono a scalini** | Raggio di arrotondamento troppo piccolo rispetto al conteggio delle fette | Aumenta il raggio o il conteggio delle fette per curve più lisce. |
| **File non trovato durante il salvataggio** | `MyDir` punta a una cartella inesistente | Crea la directory in anticipo o usa un percorso assoluto. |

## Frequently Asked Questions

**D: Come posso scaricare Aspose.3D per Java?**  
R: Puoi scaricare la libreria [qui](https://releases.aspose.com/3d/java/).

**D: Dove posso trovare la documentazione per Aspose.3D?**  
R: Consulta la documentazione [qui](https://reference.aspose.com/3d/java/).

**D: È disponibile una versione di prova gratuita?**  
R: Sì, puoi provare la versione gratuita [qui](https://releases.aspose.com/).

**D: Come posso ottenere supporto per Aspose.3D?**  
R: Visita il forum di supporto [qui](https://forum.aspose.com/c/3d/18).

**D: Posso acquistare una licenza temporanea?**  
R: Sì, è possibile ottenere una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

---

**Ultimo aggiornamento:** 2026-02-22  
**Testato con:** Aspose.3D for Java 24.11 (latest at time of writing)  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}