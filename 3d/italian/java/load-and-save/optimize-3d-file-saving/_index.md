---
title: Ottimizza il salvataggio di file 3D in Java con Aspose.3D SaveOptions
linktitle: Ottimizza il salvataggio di file 3D in Java con Aspose.3D SaveOptions
second_title: API Java Aspose.3D
description: Scopri come ottimizzare il salvataggio di file 3D in Java con Aspose.3D SaveOptions. Migliora le prestazioni e personalizza gli output senza sforzo.
weight: 16
url: /it/java/load-and-save/optimize-3d-file-saving/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Ottimizza il salvataggio di file 3D in Java con Aspose.3D SaveOptions

## introduzione

Aspose.3D è una libreria Java ricca di funzionalità che consente agli sviluppatori di lavorare senza problemi con modelli 3D. Quando si tratta di salvare file 3D, la classe SaveOptions offre numerose impostazioni per ottimizzare l'output in base alle proprie esigenze. In questo tutorial esploreremo varie opzioni di salvataggio e come possono essere sfruttate per ottimizzare il processo.

## Prerequisiti

Prima di immergerci nel tutorial, assicurati di disporre dei seguenti prerequisiti:

-  Aspose.3D per Java: assicurati di avere la libreria Aspose.3D integrata nel tuo progetto Java. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/java/).

- Ambiente di sviluppo Java: disponi di un ambiente di sviluppo Java funzionale configurato sul tuo computer.

- Directory dei documenti: crea una directory in cui desideri salvare i file 3D e annota il suo percorso per un utilizzo successivo.

## Importa pacchetti

 Nel tuo progetto Java, importa i pacchetti necessari per lavorare con Aspose.3D. Ciò include il`Scene` classe e varie classi SaveOptions. Di seguito è riportato un esempio di base:

```java
import com.aspose.threed.*;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
```

Ora suddividiamo ogni esempio in più passaggi per dimostrare l'utilizzo di diverse SaveOptions.

## Passaggio 1: stampa graziosa in GLTF SaveOption

 IL`prettyPrintInGltfSaveOption` Il metodo consente di generare un file GLTF con contenuto JSON rientrato per la leggibilità umana.

```java
public static void prettyPrintInGltfSaveOption() throws IOException {
    // Inizializza la scena 3D
    Scene scene = new Scene(new Sphere());
    
    // Inizializza GLTFSaveOptions
    GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
    
    // Abilita una bella stampa per una migliore leggibilità
    opt.setPrettyPrint(true);
    
    // Salva scena 3D
    scene.save("Your Document Directory" + "prettyPrintInGltfSaveOption.gltf", opt);
}
```

## Passaggio 2: opzione di salvataggio HTML5

 IL`html5SaveOption` Il metodo dimostra come salvare una scena 3D come file HTML5, incluse le opzioni di personalizzazione.

```java
public static void html5SaveOption() throws IOException {
    // Inizializzare una scena
    Scene scene = new Scene();
    
    // Crea un nodo figlio con un cilindro
    Node node = scene.getRootNode().createChildNode(new Cylinder());
    
    //Imposta le proprietà per il nodo figlio
    LambertMaterial mat = new LambertMaterial();
    mat.setDiffuseColor(new Vector3(0.34, 0.59, 0.41));
    node.setMaterial(mat);
    
    // Aggiungi una luce alla scena
    Light light = new Light();
    light.setLightType(LightType.POINT);
    scene.getRootNode().createChildNode(light).getTransform().setTranslation(10, 0, 10);
    
    // Inizializza HTML5SaveOptions
    Html5SaveOptions opt = new Html5SaveOptions();
    
    // Personalizza le opzioni (ad esempio, disattiva la rete e l'interfaccia utente)
    opt.setShowGrid(false);
    opt.setShowUI(false);
    
    // Salva la scena come file HTML5
    scene.save("Your Document Directory" + "html5SaveOption.html", FileFormat.HTML5);
}
```

 Continua con suddivisioni simili per altri metodi SaveOptions come`colladaSaveOption`, `discreet3DSSaveOption`, `fbxSaveOption`, `objSaveOption`, `STLSaveOption`, `U3DSaveOption`, `glTFSaveOptions` , E`drcSaveOptions`.

## Conclusione

Seguendo questo tutorial completo, hai imparato come ottimizzare il salvataggio di file 3D in Java utilizzando Aspose.3D SaveOptions. Che tu sia interessato alla stampa di file GLTF o alla personalizzazione degli output HTML5, Aspose.3D ti fornisce gli strumenti per migliorare il tuo flusso di lavoro di grafica 3D.

## Domande frequenti

### Q1: Come posso incorporare risorse in un file glTF?

 A1: Per incorporare risorse, utilizzare il file`setEmbedAssets(true)` metodo nel`GltfSaveOptions` classe.

###  Q2: Qual è lo scopo di`setPositionBits` method in `DracoSaveOptions`?

 A2: Il`setPositionBits` Il metodo imposta i bit di quantizzazione per la posizione nell'algoritmo di compressione Draco.

### Q3: Posso esportare dati normali in un file U3D?

 A3: Sì, puoi esportare i dati normali impostando`setExportNormals(true)` nel`U3dSaveOptions` classe.

### Q4: Come posso eliminare il salvataggio dei file dei materiali in un'esportazione OBJ?

A4: Utilizzare il`setFileSystem(new DummyFileSystem())` metodo nel`ObjSaveOptions` classe per scartare i file materiali.

### Q5: esiste un modo per salvare le dipendenze in una directory locale in un file OBJ?

 A5: Sì, usa il`setFileSystem(new LocalFileSystem(MyDir))` metodo nel`ObjSaveOptions` class per salvare le dipendenze localmente.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
