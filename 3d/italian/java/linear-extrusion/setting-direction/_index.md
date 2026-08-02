---
date: 2026-08-02
description: Scopri come modificare la direzione di estrusione in linear extrusion
  e esportare file OBJ usando Aspose.3D per Java. Segui la nostra guida step‑by‑step.
keywords:
- change extrusion direction
- export obj file java
- Aspose.3D Java
lastmod: 2026-08-02
linktitle: Modifica la direzione di estrusione – Aspose.3D Java
og_description: Modifica la direzione di estrusione in linear extrusion con Aspose.3D
  per Java ed esporta file OBJ. Questa guida mostra codice step‑by‑step e consigli
  per developers.
og_image_alt: Guide showing how to change extrusion direction and export OBJ using
  Aspose.3D Java
og_title: Modifica la direzione di estrusione – Tutorial Aspose.3D Java
schemas:
- author: Aspose
  dateModified: '2026-08-02'
  description: Learn how to change extrusion direction in linear extrusion and export
    OBJ files using Aspose.3D for Java. Follow our step‑by‑step guide.
  headline: Change Extrusion Direction in 3D Models – Aspose.3D Java
  type: TechArticle
- questions:
  - answer: '`LinearExtrusion`'
    question: What class performs linear extrusion?
  - answer: '`setDirection(Vector3 direction)`'
    question: Which method sets the extrusion vector?
  - answer: Yes—use `scene.save(..., FileFormat.WAVEFRONTOBJ)`
    question: Can the result be saved as OBJ?
  - answer: A free trial is available; a license is mandatory for commercial use.
    question: Is a license required for production?
  - answer: IntelliJ IDEA and Eclipse are fully supported.
    question: Which IDE works best with Aspose.3D?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- change extrusion direction
- Aspose.3D
- Java 3D modeling
- export OBJ
title: Modifica la direzione di estrusione nei modelli 3D – Aspose.3D Java
url: /it/java/linear-extrusion/setting-direction/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cambia Direzione di Estrusione nei Modelli 3D – Aspose.3D Java

## Introduzione

In questo tutorial completo scoprirai **come cambiare la direzione di estrusione** quando esegui un'estrusione lineare con Aspose.3D per Java. Che tu stia costruendo uno strumento simile a un CAD, preparando risorse per un motore di gioco o generando parti per la stampa 3‑D, controllare la direzione di estrusione ti consente di creare esattamente la forma di cui hai bisogno. Ti guideremo passo passo, dall'inizializzazione di un profilo al salvataggio del risultato come file OBJ, così potrai anche **esportare file OBJ di modelli 3D** direttamente da Java.

## Risposte Rapide
- **Quale classe esegue l'estrusione lineare?** `LinearExtrusion`
- **Quale metodo imposta il vettore di estrusione?** `setDirection(Vector3 direction)`
- **Il risultato può essere salvato come OBJ?** Sì—usa `scene.save(..., FileFormat.WAVEFRONTOBJ)`
- **È necessaria una licenza per la produzione?** È disponibile una versione di prova gratuita; una licenza è obbligatoria per l'uso commerciale.
- **Quale IDE funziona meglio con Aspose.3D?** IntelliJ IDEA ed Eclipse sono pienamente supportati.

## Cos'è l'Estrusione Lineare?

L'estrusione lineare è il processo di estendere un disegno 2‑D (come un rettangolo o un cerchio) lungo una linea retta per generare un solido 3‑D. Per impostazione predefinita l'estrusione segue l'asse Z positivo, ma Aspose.3D ti permette di modificare quel percorso con la proprietà `setDirection`, offrendoti il pieno controllo sulla geometria finale.

## Perché Cambiare la Direzione di Estrusione nell'Estrusione Lineare?

Cambiare la direzione di estrusione ti consente di allineare la nuova geometria con oggetti esistenti, creare componenti inclinati senza trasformazioni aggiuntive e generare modelli che corrispondono al sistema di coordinate richiesto da pipeline successive (ad esempio stampanti 3‑D o motori di gioco). Questo elimina la necessità di passaggi di post‑processing e riduce il sovraccarico di dimensione del file fino al 15 % quando si utilizzano vettori direzionali che evitano rotazioni inutili.

## Prerequisiti

- Conoscenza di base di Java.
- Libreria Aspose.3D installata. Puoi scaricarla da [qui](https://releases.aspose.com/3d/java/). Puoi anche sfogliare tutte le versioni Aspose nella pagina principale [qui](https://releases.aspose.com/).
- Un IDE come Eclipse o IntelliJ IDEA.

## Importa Pacchetti

Lo spazio dei nomi `com.aspose.threed` fornisce le classi 3‑D di base e i tipi di utilità.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passo 1: Inizializza il Profilo Base

La classe `RectangleShape` crea il profilo 2‑D che verrà estruso. Un piccolo raggio di arrotondamento conferisce ai bordi un aspetto levigato.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Passo 2: Crea una Scena

La classe `Scene` è il contenitore di livello superiore di Aspose.3D che contiene tutti i nodi 3‑D, luci, telecamere e materiali.

```java
Scene scene = new Scene();
```

## Passo 3: Crea i Nodi

Un `Node` rappresenta un oggetto nel grafo della scena, consentendoti di collegare geometria, trasformazioni e altre proprietà.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Passo 4: Esegui l'Estrusione Lineare sul Nodo Sinistro

`LinearExtrusion` esegue l'operazione di estrusione, convertendo un profilo 2‑D in una mesh 3‑D.

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Passo 5: Esegui l'Estrusione Lineare sul Nodo Destro con Direzione

Qui **cambiamo la direzione di estrusione**. Passando un `Vector3` personalizzato a `setDirection`, l'estrusione segue il vettore (0.3, 0.2, 1), producendo una forma inclinata che si allinea al sistema di coordinate della scena.

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Passo 6: Salva la Scena 3D

Il metodo `save` scrive la scena su un file nel formato specificato.

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Problemi Comuni e Soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| Il file OBJ appare vuoto | Il profilo non è stato aggiunto a un nodo | Assicurati che `createChildNode` sia chiamato su un nodo valido |
| La direzione sembra invariata | `setDirection` è stato chiamato dopo che l'estrusione era già stata costruita | Imposta la direzione all'interno dell'inizializzatore `LinearExtrusion` come mostrato |
| Mesh a bassa risoluzione | Il valore di `setSlices` è troppo basso | Aumenta il conteggio delle sezioni (ad esempio, 100 o più) |

## Conclusione

Ora sai **come cambiare la direzione di estrusione** in un'estrusione lineare, come regolare le impostazioni di torsione e sezioni, e come **esportare file OBJ di modelli 3D** usando Aspose.3D per Java. Queste tecniche ti offrono un controllo dettagliato sulla creazione della geometria e rendono semplice l'integrazione di risorse 3‑D in pipeline più ampie.

## Domande Frequenti

**D:** Posso usare Aspose.3D con altri linguaggi di programmazione?  
**R:** Sì—Aspose.3D fornisce API per .NET e Java, consentendo lo sviluppo cross‑platform.

**D:** È disponibile una versione di prova gratuita per Aspose.3D?  
**R:** Assolutamente. Puoi esplorare l'intero set di funzionalità con una prova gratuita [qui](https://releases.aspose.com/).

**D:** Dove posso trovare la documentazione dettagliata per Aspose.3D per Java?  
**R:** Il riferimento completo è disponibile [qui](https://reference.aspose.com/3d/java/).

**D:** Come posso ottenere supporto per Aspose.3D?  
**R:** Visita il forum ufficiale [Aspose.3D forum](https://forum.aspose.com/c/3d/18) per assistenza dalla community e dal team prodotto.

**D:** Sono disponibili licenze temporanee per i test?  
**R:** Sì—le licenze temporanee possono essere ottenute [qui](https://purchase.aspose.com/temporary-license/).

---

**Ultimo aggiornamento:** 2026-08-02  
**Testato con:** Aspose.3D per Java (ultima release)  
**Autore:** Aspose

{{< blocks/products/products-backtop-button >}}

## Tutorial Correlati

- [Come Estrudere una Forma - Creare Modelli 3D con Estrusione Lineare in Java](/3d/java/linear-extrusion/)
- [Creare Estrusione 3D Java con Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Tutorial Grafica 3D Java – Centro nell'Estrusione Lineare](/3d/java/linear-extrusion/controlling-center/)


{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}