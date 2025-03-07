---
title: Impostazione della direzione nell'estrusione lineare con Aspose.3D per Java
linktitle: Impostazione della direzione nell'estrusione lineare con Aspose.3D per Java
second_title: API Java Aspose.3D
description: Padroneggia l'estrusione lineare con Aspose.3D per Java! Segui la nostra guida per una programmazione 3D senza interruzioni. Scaricalo ora per un'esperienza accattivante.
weight: 12
url: /it/java/linear-extrusion/setting-direction/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Impostazione della direzione nell'estrusione lineare con Aspose.3D per Java

## introduzione

Benvenuti nella nostra guida passo passo sull'impostazione della direzione nell'estrusione lineare utilizzando Aspose.3D per Java. Aspose.3D è una potente libreria Java che consente agli sviluppatori di lavorare senza problemi con file e scene 3D. In questo tutorial ci concentreremo sul compito specifico di impostare la direzione nell'estrusione lineare, migliorando la tua competenza nella programmazione 3D.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di disporre dei seguenti prerequisiti:

- Conoscenza base del linguaggio di programmazione Java.
-  Libreria Aspose.3D installata. Puoi scaricarlo da[Qui](https://releases.aspose.com/3d/java/).
- Un ambiente di sviluppo integrato (IDE) per Java, come Eclipse o IntelliJ.

## Importa pacchetti

Assicurati di importare i pacchetti necessari per avviare il tuo progetto:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Passaggio 1: inizializza il profilo di base

 Inizia inizializzando il profilo di base da estrudere. In questo esempio usiamo a`RectangleShape` con raggio di arrotondamento 0,3:

```java
// Il percorso della directory dei documenti.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

## Passaggio 2: crea una scena

Successivamente, crea una scena 3D per contenere gli oggetti estrusi:

```java
Scene scene = new Scene();
```

## Passaggio 3: crea nodi

Crea nodi sinistro e destro all'interno della scena:

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

## Passaggio 4: eseguire l'estrusione lineare sul nodo sinistro

 Eseguire l'estrusione lineare sul nodo sinistro utilizzando il`LinearExtrusion`classe con parametri specificati come twist e slice:

```java
left.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); }});
```

## Passaggio 5: eseguire l'estrusione lineare sul nodo destro con direzione

 Eseguire l'estrusione lineare sul nodo destro, introducendo il`setDirection` proprietà per definire la direzione di estrusione:

```java
right.createChildNode(new LinearExtrusion(profile, 10) {{ setTwist(360); setSlices(100); setDirection(new Vector3(0.3, 0.2, 1));}});
```

## Passaggio 6: salva la scena 3D

Salva la scena 3D nel formato file desiderato. In questo esempio, lo salviamo come file Wavefront OBJ:

```java
scene.save(MyDir + "DirectionInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Conclusione

Congratulazioni! Hai imparato con successo come impostare la direzione nell'estrusione lineare utilizzando Aspose.3D per Java. Questo tutorial migliora le tue abilità nella programmazione 3D e apre nuove possibilità per progetti creativi.

## Domande frequenti

### Q1: Posso utilizzare Aspose.3D con altri linguaggi di programmazione?

A1: Aspose.3D supporta vari linguaggi di programmazione, tra cui .NET e Java.

### Q2. È disponibile una prova gratuita per Aspose.3D?

 A2: Sì, puoi esplorare le funzionalità di Aspose.3D con una prova gratuita[Qui](https://releases.aspose.com/).

### Q3: Dove posso trovare la documentazione dettagliata per Aspose.3D per Java?

 A3: La documentazione completa è disponibile[Qui](https://reference.aspose.com/3d/java/).

### Q4: Come posso ottenere supporto per Aspose.3D?

 A4: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per qualsiasi assistenza o domanda.

### Q5: Sono disponibili licenze temporanee per Aspose.3D?

 R5: Sì, puoi ottenere una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
