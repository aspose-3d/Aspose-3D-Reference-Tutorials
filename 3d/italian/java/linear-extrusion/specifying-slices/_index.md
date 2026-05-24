---
date: 2026-05-24
description: Scopri come creare un'estrusione 3D con Slices usando Aspose.3D for Java.
  Questa guida passo‑passo copre l'estrusione lineare, impostazione del raggio di
  arrotondamento e l'esportazione di OBJ.
keywords:
- create 3d extrusion java
- Aspose 3D slices
- linear extrusion Java
linktitle: Crea estrusione 3D con Slices – Aspose.3D for Java
schemas:
- author: Aspose
  dateModified: '2026-05-24'
  description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  headline: Create 3D Extrusion with Slices – Aspose.3D for Java
  type: TechArticle
- description: Learn how to create 3d extrusion with slices using Aspose.3D for Java.
    This step‑by‑step guide covers linear extrusion, set rounding radius, and exporting
    OBJ.
  name: Create 3D Extrusion with Slices – Aspose.3D for Java
  steps:
  - name: Set up the scene and define the profile
    text: '`RectangleShape` is a class that defines a 2‑D rectangle profile. First
      we create a `RectangleShape` and give it a **rounding radius** so the corners
      are smooth. `Scene` is the root container for all nodes and geometry. Then we
      initialise a new `Scene` that will hold all geometry.'
  - name: Create child node objects for each extrusion
    text: '`Node` represents an element in the scene graph that can hold geometry
      and transformations. Every piece of geometry lives under a `Node`. Here we generate
      two sibling nodes – one for a low‑slice extrusion and another for a high‑slice
      extrusion – and move the left node a little to the side so the res'
  - name: Perform linear extrusion and set slices
    text: '`LinearExtrusion` is the class that creates a solid by sweeping a profile
      linearly. `LinearExtrusion` is Aspose.3D''s class that generates a solid by
      extruding a 2‑D profile along a straight line. Using an **anonymous inner class**
      we call `setSlices` to control the smoothness. The left node gets onl'
  - name: Export OBJ – save the scene
    text: Finally we write the scene to a Wavefront OBJ file, a format widely supported
      by 3‑D editors and game engines. This demonstrates the **export OBJ Java** capability
      of Aspose.3D.
  type: HowTo
- questions:
  - answer: You can download the library [here](https://releases.aspose.com/3d/java/).
    question: How can I download Aspose.3D for Java?
  - answer: Refer to the documentation [here](https://reference.aspose.com/3d/java/).
    question: Where can I find the documentation for Aspose.3D?
  - answer: Yes, you can explore a free trial [here](https://releases.aspose.com/).
    question: Is there a free trial available?
  - answer: Visit the support forum [here](https://forum.aspose.com/c/3d/18).
    question: How can I get support for Aspose.3D?
  - answer: Yes, a temporary license can be obtained [here](https://purchase.aspose.com/temporary-license/).
    question: Can I purchase a temporary license?
  type: FAQPage
second_title: Aspose.3D Java API
title: Crea estrusione 3D con Slices – Aspose.3D for Java
url: /it/java/linear-extrusion/specifying-slices/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crea estrusione 3D con fette – Aspose.3D per Java

## Introduzione

Se hai bisogno di **creare estrusioni 3d** oggetti che appaiano lisci e precisi, controllare il numero di fette è fondamentale. In questo tutorial vedremo come specificare le fette durante un'estrusione lineare con Aspose.3D per Java. Scoprirai perché il conteggio delle fette è importante, come impostare un raggio di arrotondamento e come esportare il risultato come file OBJ che può essere usato in qualsiasi pipeline 3‑D.

## Risposte rapide
- **Cosa controlla “slices”?** Il numero di sezioni trasversali intermedie utilizzate per approssimare la superficie dell'estrusione.  
- **Quale metodo imposta il conteggio delle fette?** `LinearExtrusion.setSlices(int)`  
- **Posso modificare il raggio di arrotondamento del profilo?** Sì, tramite `RectangleShape.setRoundingRadius(double)`  
- **Quale formato file è usato in questo esempio?** Wavefront OBJ (`FileFormat.WAVEFRONTOBJ`)  
- **Ho bisogno di una licenza per eseguire il codice?** Una prova gratuita è sufficiente per la valutazione; è necessaria una licenza commerciale per la produzione.

`LinearExtrusion.setSlices(int)` imposta quante fette intermedie genererà l'estrusione.  
`RectangleShape.setRoundingRadius(double)` definisce il raggio d'angolo di un profilo rettangolare.

## Come creare estrusione 3d Java con fette?

Carica il tuo profilo 2‑D, scegli un conteggio di fette, imposta il raggio di arrotondamento e chiama `save` – l'intero flusso di lavoro si riduce a poche righe. Aspose.3D per Java gestisce automaticamente la creazione della geometria, l'interpolazione delle fette e l'esportazione OBJ, così puoi concentrarti sulla qualità visiva anziché sui calcoli di mesh a basso livello.

## Cos'è un'estrusione lineare con fette?

Un'estrusione lineare con fette trasforma una forma 2‑D piatta in un solido 3‑D spazzolando lungo una linea retta mentre genera un numero configurabile di sezioni trasversali intermedie. Il conteggio delle fette influisce direttamente sulla fluidità con cui vengono renderizzate le curve, come gli angoli arrotondati.

## Perché usare Aspose.3D per Java per creare estrusioni 3d?

Aspose.3D offre **controllo programmatico completo** su ogni parametro di estrusione, supporta **oltre 50 formati di input e output** (inclusi OBJ, FBX, STL e GLTF) e può elaborare **modelli di centinaia di pagine** senza caricare l'intero file in memoria. Funziona su qualsiasi piattaforma abilitata a Java, non richiede DLL native e garantisce risultati deterministici su Windows, Linux e macOS.

## Prerequisiti

1. **Java Development Kit** – JDK 8 o superiore installato.  
2. **Aspose.3D for Java** – Scarica la libreria dal sito ufficiale [qui](https://releases.aspose.com/3d/java/).  
3. Un IDE o un editor di testo a tua scelta.

## Importa pacchetti

Aggiungi lo spazio dei nomi Aspose.3D al tuo progetto per poter accedere alle classi di modellazione 3‑D.

```java
import com.aspose.threed.*;

import java.io.IOException;
```

## Guida passo‑passo

### Passo 1: Configura la scena e definisci il profilo

`RectangleShape` è una classe che definisce un profilo rettangolare 2‑D.  
Prima creiamo un `RectangleShape` e gli assegniamo un **raggio di arrotondamento** affinché gli angoli siano lisci.  
`Scene` è il contenitore radice per tutti i nodi e la geometria.  
Quindi inizializziamo una nuova `Scene` che conterrà tutta la geometria.

```java
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
Scene scene = new Scene();
```

### Passo 2: Crea oggetti nodo figlio per ogni estrusione

`Node` rappresenta un elemento nel grafo della scena che può contenere geometria e trasformazioni.  
Ogni pezzo di geometria vive sotto un `Node`. Qui generiamo due nodi fratelli – uno per un'estrusione a poche fette e un altro per un'estrusione ad alte fette – e spostiamo leggermente il nodo sinistro di lato affinché i risultati siano facili da confrontare.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Passo 3: Esegui l'estrusione lineare e imposta le fette

`LinearExtrusion` è la classe che crea un solido spazzolando un profilo linearmente.  
`LinearExtrusion` è la classe di Aspose.3D che genera un solido estrudendo un profilo 2‑D lungo una linea retta. Utilizzando una **classe interna anonima** chiamiamo `setSlices` per controllare la fluidità. Il nodo sinistro ottiene solo 2 fette (grossolane), mentre il nodo destro ne ottiene 10 (lisce).

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(2);}});
right.createChildNode(new LinearExtrusion(profile, 2) {{setSlices(10);}});
```

### Passo 4: Esporta OBJ – salva la scena

Infine scriviamo la scena in un file Wavefront OBJ, un formato ampiamente supportato da editor 3‑D e motori di gioco. Questo dimostra la capacità di **esportazione OBJ Java** di Aspose.3D.

```java
scene.save(MyDir + "SlicesInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| **L'estrusione appare piatta** | Il conteggio delle fette è impostato a 1 o 0 | Assicurati che `setSlices` sia chiamato con un valore ≥ 2. |
| **Gli angoli arrotondati appaiono seghettati** | Il raggio di arrotondamento è troppo piccolo rispetto al conteggio delle fette | Aumenta il raggio o il conteggio delle fette per curve più lisce. |
| **File non trovato durante il salvataggio** | `MyDir` punta a una cartella inesistente | Crea la directory in anticipo o usa un percorso assoluto. |

## Domande frequenti

**D: Come posso scaricare Aspose.3D per Java?**  
R: Puoi scaricare la libreria [qui](https://releases.aspose.com/3d/java/).

**D: Dove posso trovare la documentazione per Aspose.3D?**  
R: Consulta la documentazione [qui](https://reference.aspose.com/3d/java/).

**D: È disponibile una prova gratuita?**  
R: Sì, puoi provare una versione di prova gratuita [qui](https://releases.aspose.com/).

**D: Come posso ottenere supporto per Aspose.3D?**  
R: Visita il forum di supporto [qui](https://forum.aspose.com/c/3d/18).

**D: Posso acquistare una licenza temporanea?**  
R: Sì, una licenza temporanea può essere ottenuta [qui](https://purchase.aspose.com/temporary-license/).

---

**Ultimo aggiornamento:** 2026-05-24  
**Testato con:** Aspose.3D per Java 24.11 (ultima versione al momento della scrittura)  
**Autore:** Aspose

## Tutorial correlati

- [Crea estrusione 3D Java con Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Come impostare la direzione nell'estrusione lineare con Aspose.3D per Java](/3d/java/linear-extrusion/setting-direction/)
- [Crea scena 3D con torsione nell'estrusione lineare – Aspose.3D per Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}