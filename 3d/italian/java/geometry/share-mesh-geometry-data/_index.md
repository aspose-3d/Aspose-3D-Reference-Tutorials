---
date: 2025-12-12
description: Impara come impostare il colore del materiale mentre condividi i dati
  della geometria della mesh e salvi la scena come FBX in Java 3D usando Aspose.3D.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Imposta il colore del materiale e condividi i dati della geometria della mesh
  in Java 3D con Aspose.3D
url: /it/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Impostare il colore del materiale e condividere i dati della geometria mesh in Java 3D con Aspose.3D

## Introduzione

Intraprendere un viaggio nel mondo di Java 3D con Aspose.3D apre una serie di possibilità per creare visualizzazioni sorprendenti ed esperienze immersive. In questo tutorial, ti guideremo attraverso **come condividere i dati mesh** in Java 3D usando Aspose.3D, e ti mostreremo esattamente **come impostare il colore del materiale** per ogni istanza mesh. Segui attentamente ogni passaggio e, al termine, sarai in grado di scambiare dati mesh tra più nodi controllando i colori ed esportando in FBX.

## Risposte rapide
- **Qual è l'obiettivo principale?** Impostare il colore del materiale per ogni nodo e condividere i dati della geometria mesh.  
- **Quale libreria è necessaria?** Aspose.3D per Java.  
- **Come esportare il risultato?** Salvare la scena come file FBX (FBX7400ASCII).  
- **È necessaria una licenza?** È richiesta una licenza temporanea o completa per l'uso in produzione.  
- **Quale versione di Java funziona?** Qualsiasi ambiente Java 8+.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di avere i seguenti prerequisiti:

- **Ambiente di sviluppo Java:** Assicurati di avere un ambiente di sviluppo Java configurato sul tuo sistema.  
- **Libreria Aspose.3D:** Scarica e installa la libreria Aspose.3D. Puoi trovare la libreria [qui](https://releases.aspose.com/3d/java/).

## Importare i pacchetti

Inizia importando i pacchetti necessari nel tuo progetto Java. Questo passaggio è fondamentale per accedere alle funzionalità offerte dalla libreria Aspose.3D.

```java
import com.aspose.threed.*;
```

## Passo 1: Inizializzare l'oggetto Scene (initialize scene java)

Avviamo il processo inizializzando un oggetto scene. Questo servirà da tela dove si svolgerà la magia 3D.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Passo 2: Definire i vettori di colore

In questo passaggio definiamo un array di vettori di colore che verranno applicati ai diversi elementi della nostra scena 3D.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## Passo 3: Creare una mesh 3D Java usando Polygon Builder (create 3d mesh java)

Utilizza la classe Common per creare una mesh usando il metodo polygon builder. Questa mesh sarà la base per i nostri elementi 3D.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## Come impostare il colore del materiale per ogni nodo?

Itera attraverso i vettori di colore, crea nodi cubo e imposta attributi come materiale, **set material color**, e traslazione. Questo è il cuore del controllo dell'aspetto visivo di ogni istanza mesh.

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

## Passo 5: Salvare la scena 3D (save scene fbx, convert mesh to fbx)

Specifica la directory e il nome file per salvare la scena 3D nel formato supportato, in questo caso FBX7400ASCII. Questo passaggio dimostra anche **convert mesh to FBX**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## Conclusione

Congratulazioni! Hai impostato con successo il **colore del materiale**, condiviso i dati della geometria mesh tra più nodi e esportato il risultato come file FBX usando Aspose.3D per Java. Questo apre infinite possibilità per creare applicazioni 3D visivamente spettacolari e interattive.

## FAQ

### Q1: Posso usare Aspose.3D con altri framework Java?
A1: Sì, Aspose.3D è progettato per funzionare senza problemi con vari framework Java.

### Q2: Sono disponibili opzioni di licenza per Aspose.3D?
A2: Sì, puoi esplorare le opzioni di licenza [qui](https://purchase.aspose.com/buy).

### Q3: Come posso ottenere supporto per Aspose.3D?
A3: Visita il [forum](https://forum.aspose.com/c/3d/18) di Aspose.3D per supporto e discussioni.

### Q4: È disponibile una prova gratuita?
A4: Sì, puoi ottenere una prova gratuita [qui](https://releases.aspose.com/).

### Q5: Come posso ottenere una licenza temporanea per Aspose.3D?
A5: Puoi ottenere una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

## Domande frequenti aggiuntive

**D: Posso esportare la scena in altri formati oltre FBX?**  
A: Sì, Aspose.3D supporta OBJ, STL, 3MF e altri. Basta cambiare l'enum `FileFormat` nella chiamata `save`.

**D: E se devo cambiare il materiale dopo che la scena è stata creata?**  
A: Recupera il nodo, modifica il suo `LambertMaterial` (ad es., `setDiffuseColor`) e salva nuovamente la scena.

**D: La libreria gestisce mesh grandi in modo efficiente?**  
A: Aspose.3D utilizza strutture dati ottimizzate; tuttavia, per mesh estremamente grandi considera lo streaming o la suddivisione della scena.

**D: Esiste un modo per animare il cambiamento di colore?**  
A: Sì, puoi animare le proprietà del materiale usando l'API `AnimationController`.

---

**Last Updated:** 2025-12-12  
**Tested With:** Aspose.3D 24.11 for Java  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}