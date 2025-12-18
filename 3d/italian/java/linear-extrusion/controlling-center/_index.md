---
date: 2025-12-18
description: Scopri come aggiungere un piano di base e impostare la proprietà center
  nell'estrusione lineare usando Aspose.3D per Java, con esempi di codice passo passo.
linktitle: Controlling Center in Linear Extrusion with Aspose.3D for Java
second_title: Aspose.3D Java API
title: Come aggiungere il piano di terra e il centro di controllo nell'estrusione
  lineare con Aspose.3D per Java
url: /it/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Controlling Center in Linear Extrusion with Aspose.3D for Java

## Introduction

Quando si creano scene 3D in Java, la possibilità di **aggiungere un piano di riferimento** e di impostare con precisione la **proprietà center** su un'estrusione lineare può fare la differenza tra un prototipo piatto e una visualizzazione rifinita. In questo tutorial percorreremo l’intero processo di controllo del centro dell’estrusione e di aggiunta di un piano di riferimento usando Aspose.3D per Java. Vedrai perché è importante, come configurarlo e otterrai un esempio di codice pronto all’uso che potrai adattare ai tuoi progetti.

## Quick Answers
- **Cosa fa “add ground plane”?** Crea una geometria di riferimento sottile che ti aiuta a vedere la posizione dell’estrusione rispetto agli assi del mondo.  
- **Come imposto il centro di un’estrusione lineare?** Usa il metodo `setCenter(boolean)` sull’oggetto `LinearExtrusion`.  
- **È necessaria una licenza per eseguire il campione?** Una licenza temporanea è sufficiente per i test; una licenza completa è richiesta per la produzione.  
- **Quale formato di file viene usato per il salvataggio?** L’esempio salva in Wavefront OBJ (`.obj`).  
- **Quale versione di Java è richiesta?** Java 8 o successive sono sufficienti.

## What is “add ground plane” in a 3D scene?

Aggiungere un piano di riferimento significa inserire una geometria rettangolare sottile (spesso un box con spessore minimo) che giace sul piano X‑Z. Funziona come un pavimento visivo, facilitando la valutazione dell’altezza e dell’allineamento degli altri oggetti, soprattutto quando si sperimentano i centri di estrusione.

## Why set the center property on a linear extrusion?

Per impostazione predefinita, un’estrusione lineare parte dall’origine del profilo. Impostare la proprietà center (`setCenter(true)`) sposta il profilo in modo che l’estrusione sia centrata attorno all’origine, utile per design simmetrici o quando è necessario un allineamento coerente tra più oggetti.

## Prerequisites

Prima di intraprendere questo tutorial, assicurati di avere i seguenti prerequisiti:

1. **Java Development Environment** – Verifica di avere un ambiente di sviluppo Java configurato sulla tua macchina.  
2. **Aspose.3D for Java** – Scarica e installa la libreria Aspose.3D. Puoi trovare la libreria e la sua documentazione [qui](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Crea una cartella per memorizzare i tuoi documenti Java. Chiamiamola “Your Document Directory”.

## Import Packages

Nel tuo ambiente di sviluppo Java, importa i pacchetti necessari per Aspose.3D. Questo garantisce che il tuo codice abbia accesso alle funzionalità offerte dalla libreria.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Step 1: Set Up the Base Profile

Inizializza il profilo di base da estrudere. In questo esempio, useremo una forma rettangolare con raggio di arrotondamento pari a 0.3.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Step 2: Create a 3D Scene

Costruisci le fondamenta del tuo mondo 3D creando una scena.

```java
Scene scene = new Scene();
```

## Step 3: Create Left and Right Nodes

Stabilisci i nodi sinistro e destro all’interno della scena. Questi nodi fungono da tela per i tuoi oggetti 3D.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Step 4: Linear Extrusion with Center Property (Left Node)

Esegui un’estrusione lineare sul nodo sinistro **senza centrare** e imposta il numero di slice a 3. Nota la chiamata `setCenter(false)` – è qui che **impostiamo la proprietà center** a *false*.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

## Step 5: Add Ground Plane for Reference (Left Node)

Migliora la rappresentazione visiva **aggiungendo un piano di riferimento** al nodo sinistro. Il box sottile funge da pavimento così da poter vedere chiaramente l’altezza dell’estrusione.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

## Step 6: Linear Extrusion with Center Property (Right Node)

Ora esegui l’estrusione lineare sul nodo destro, questa volta **centrando l’estrusione**. La chiamata `setCenter(true)` dimostra come **impostare la proprietà center** a *true*.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

## Step 7: Add Ground Plane for Reference (Right Node)

Proprio come per il lato sinistro, aggiungi un piano di riferimento al nodo destro per mantenere una base visiva coerente.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

## Step 8: Save the 3D Scene

Salva la tua scena 3D in formato Wavefront OBJ così da poterla visualizzare con qualsiasi visualizzatore 3D standard.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Common Issues and Solutions

| Issue | Why It Happens | Fix |
|-------|----------------|-----|
| Ground plane not visible | Box thickness is too small for the viewer’s scale. | Increase the thickness (first parameter of `Box`) or zoom out in the viewer. |
| Extrusion appears offset | `setCenter` value not set as intended. | Double‑check the boolean passed to `setCenter`. |
| File not saved | Incorrect directory path or missing write permissions. | Verify `MyDir` points to an existing folder with write access. |

## Frequently Asked Questions

**Q1: Posso usare Aspose.3D per Java in progetti commerciali?**  
A1: Sì, Aspose.3D per Java è disponibile per uso commerciale. Per i dettagli sulla licenza, visita [qui](https://purchase.aspose.com/buy).

**Q2: È disponibile una versione di prova gratuita?**  
A2: Sì, puoi provare gratuitamente Aspose.3D per Java [qui](https://releases.aspose.com/).

**Q3: Dove posso trovare per Aspose.3D per Java?**  
A3: Il forum della community di Aspose.3D è un ottimo posto per chiedere supporto e condividere esperienze. Visita il forum [qui](https://forum.aspose.com/c/3d/18).

**Q4: È necessaria una licenza temporanea per i test?**  
A4: Sì, se ti serve una licenza temporanea per scopi di test, puoi ottenerla [qui](https://purchase.aspose.com/temporary-license/).

**Q5: Dove posso trovare la documentazione?**  
A5: La documentazione per Aspose.3D per Java è disponibile [qui](https://reference.aspose.com3d/java/).

## Conclusion

Controllare il centro in un’estrusione lineare **e** imparare a **aggiungere un piano di riferimento** con Aspose.3D per Java apre interessanti possibilità nello sviluppo di grafica 3D. Seguendo i passaggi sopra, ora disponi di un modello riutilizzabile per creare estrusioni centrate, piani di riferimento visivi e esportare il risultato in OBJ. Sentiti libero di sperimentare con profili diversi, numeri di slice e trasformazioni per adattarli alle esigenze del tuo progetto.

---

**Last Updated:** 2025-12-18  
**Tested With:** Aspose.3D 24.11 for Java (latest at time of writing)  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}