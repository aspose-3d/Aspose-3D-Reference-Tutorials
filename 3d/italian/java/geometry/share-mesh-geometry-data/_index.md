---
date: 2026-02-17
description: Scopri come convertire una mesh in FBX impostando il colore del materiale
  e condividendo i dati della geometria della mesh in Java 3D con Aspose.3D.
linktitle: Convert Mesh to FBX and Set Material Color in Java 3D
second_title: Aspose.3D Java API
title: Converti Mesh in FBX e imposta il colore del materiale in Java 3D
url: /it/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Converti Mesh in FBX e Imposta il Colore del Materiale in Java 3D

## Introduzione

Se stai creando un'applicazione 3D basata su Java, spesso avrai bisogno di riutilizzare la stessa geometria su più oggetti mantenendo un aspetto unico per ogni istanza. In questo tutorial imparerai **come convertire mesh in FBX**, condividere la geometria mesh sottostante tra diversi nodi e **impostare un colore del materiale diverso per ciascun nodo**. Alla fine avrai una scena FBX pronta per l'esportazione che potrai inserire in qualsiasi motore o visualizzatore.

## Risposte Rapide
- **Qual è l'obiettivo principale?** Convertire mesh in FBX, condividere la geometria mesh e impostare un colore del materiale distinto per ogni nodo.  
- **Quale libreria è necessaria?** Aspose.3D per Java.  
- **Come esportare il risultato?** Salva la scena come file FBX usando `FileFormat.FBX7400ASCII`.  
- **È necessaria una licenza?** È richiesta una licenza temporanea o completa per l'uso in produzione.  
- **Quale versione di Java funziona?** Qualsiasi ambiente Java 8+.

## Cos'è **convert mesh to FBX**?

`convert mesh to fbx` è il processo di prendere un oggetto mesh creato o manipolato in memoria e scriverlo nel formato file FBX, ampiamente supportato da strumenti 3D come Maya, Blender e Unity. Aspose.3D si occupa del lavoro pesante, quindi devi solo chiamare `scene.save(...)` con il `FileFormat` appropriato.

## Perché condividere i dati della geometria mesh?

Condividere la geometria riduce il consumo di memoria e velocizza il rendering perché i buffer dei vertici sottostanti vengono memorizzati una sola volta. Questa tecnica è perfetta per scene con molti oggetti duplicati — pensa a foreste, folle o architettura modulare — dove ogni istanza differisce solo per trasformazione o materiale.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di avere i seguenti prerequisiti:

- **Ambiente di sviluppo Java** – qualsiasi IDE o configurazione da riga di comando con Java 8 o superiore.  
- **Libreria Aspose.3D** – scarica l'ultimo JAR dal sito ufficiale: [here](https://releases.aspose.com/3d/java/).

## Import Packages

Inizia importando i pacchetti necessari nel tuo progetto Java. Questo passaggio è fondamentale per accedere alle funzionalità fornite dalla libreria Aspose.3D.

```java
import com.aspose.threed.*;
```

## Step 1: Initialize Scene Object (initialize scene java)

Iniziamo il processo creando un oggetto scena. Questo servirà come tela su cui si svilupperà la nostra magia 3D.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Step 2: Define Color Vectors

In questo passaggio, definiamo un array di vettori di colore che verranno applicati a diversi elementi della nostra scena 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Step 3: Create 3D Mesh Java Using Polygon Builder (create 3d mesh java)

Utilizza la classe Common per creare una mesh usando il metodo polygon builder. Questa mesh sarà la base per i nostri elementi 3D.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## How to set material color for each node?

Itera attraverso i vettori di colore, crea nodi cubo e imposta attributi come materiale, **set material color**, e traslazione. Questo è il fulcro del controllo dell'aspetto visivo di ogni istanza mesh.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## Step 5: Save the 3D Scene (save scene fbx, convert mesh to fbx)

Specifica la directory e il nome file per salvare la scena 3D nel formato file supportato, in questo caso FBX7400ASCII. Questo passaggio dimostra anche **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Common Pitfalls & Tips

- **Problemi di percorso** – Assicurati che il percorso della directory termini con un separatore di file (`/` o `\\`) prima di aggiungere il nome file.  
- **Inizializzazione della licenza** – Se dimentichi di impostare la licenza Aspose.3D prima di chiamare `scene.save`, la libreria funzionerà in modalità di prova e potrebbe inserire una filigrana.  
- **Sovrascrittura del materiale** – Riutilizzare la stessa istanza `LambertMaterial` per più nodi farà sì che tutti i nodi condividano lo stesso colore. Crea sempre un nuovo materiale per ogni iterazione, come mostrato sopra.  
- **Mesh grandi** – Per mesh con milioni di vertici, considera l'uso di `MeshBuilder` con poligoni indicizzati per mantenere gestibile la dimensione del file FBX.

## Additional Frequently Asked Questions

**D1: Posso usare Aspose.3D con altri framework Java?**  
R1: Sì, Aspose.3D è progettato per funzionare senza problemi con vari framework Java.

**D2: Ci sono opzioni di licenza disponibili per Aspose.3D?**  
R2: Sì, puoi esplorare le opzioni di licenza [here](https://purchase.aspose.com/buy).

**D3: Come posso ottenere supporto per Aspose.3D?**  
R3: Visita il [forum](https://forum.aspose.com/c/3d/18) di Aspose.3D per supporto e discussioni.

**D4: È disponibile una prova gratuita?**  
R4: Sì, puoi ottenere una prova gratuita [here](https://releases.aspose.com/).

**D5: Come posso ottenere una licenza temporanea per Aspose.3D?**  
R5: Puoi ottenere una licenza temporanea [here](https://purchase.aspose.com/temporary-license/).

## Conclusione

Congratulazioni! Hai convertito con successo **mesh in FBX**, condiviso i dati della geometria mesh tra più nodi e impostato colori di materiale individuali usando Aspose.3D per Java. Questo flusso di lavoro ti fornisce un'architettura mesh leggera e riutilizzabile che può essere esportata in qualsiasi pipeline compatibile con FBX.

---

**Last Updated:** 2026-02-17  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}