---
title: Personalizza il caricamento di file 3D in Java con Aspose.3D LoadOptions
linktitle: Personalizza il caricamento di file 3D in Java con Aspose.3D LoadOptions
second_title: API Java Aspose.3D
description: Migliora il caricamento dei tuoi file 3D in Java con LoadOptions personalizzabili Aspose.3D. Scopri la personalizzazione passo passo per 3DS, OBJ, STL, U3D, glTF, PLY, X e FBX opzionale.
weight: 12
url: /it/java/load-and-save/customize-3d-file-loading/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Personalizza il caricamento di file 3D in Java con Aspose.3D LoadOptions

## introduzione

Nel panorama in continua evoluzione della progettazione e dello sviluppo 3D, la gestione efficiente dei formati di file 3D è fondamentale. Aspose.3D per Java fornisce una potente soluzione per personalizzare il caricamento di vari formati di file 3D. Questo tutorial ti guiderà attraverso il processo di personalizzazione del caricamento di file 3D in Java utilizzando LoadOptions di Aspose.3D.

## Prerequisiti

Prima di immergerti nel processo di personalizzazione, assicurati di avere quanto segue:

- Conoscenza di base della programmazione Java.
- Kit di sviluppo Java (JDK) installato.
-  Aspose.3D per la libreria Java scaricata. Puoi ottenerlo[Qui](https://releases.aspose.com/3d/java/).
- Familiarità con formati di file 3D come 3DS, OBJ, STL, U3D, glTF, PLY, X e FBX.

## Importa pacchetti

Nel tuo progetto Java, assicurati di importare i pacchetti Aspose.3D necessari:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Personalizza il caricamento dei file 3D

### Passaggio 1: personalizza il caricamento dei file 3DS

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Passaggio 2: personalizzare il caricamento del file OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Passaggio 3: personalizzare il caricamento del file STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Passaggio 4: personalizzare il caricamento dei file U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Passaggio 5: personalizzare il caricamento del file glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Passaggio 6: personalizzare il caricamento del file PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Passaggio 7: personalizzare il caricamento dei file X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Passaggio 8: personalizzare il caricamento dei file FBX (facoltativo)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Conclusione

La personalizzazione del caricamento di file 3D in Java con LoadOptions di Aspose.3D consente agli sviluppatori di adattare il processo di importazione a requisiti specifici. Che si tratti di regolare le trasformazioni di animazione, di invertire i sistemi di coordinate o di gestire dipendenze esterne, Aspose.3D offre la flessibilità necessaria per un'integrazione perfetta.

## Domande frequenti

### Q1: Dove posso trovare la documentazione Aspose.3D per Java?

 A1: La documentazione è disponibile[Qui](https://reference.aspose.com/3d/java/).

### Q2: Come posso scaricare Aspose.3D per Java?

 A2: Puoi scaricarlo[Qui](https://releases.aspose.com/3d/java/).

### Q3: È disponibile una prova gratuita?

 R3: Sì, puoi accedere alla prova gratuita[Qui](https://releases.aspose.com/).

### Q4: Dove posso ottenere supporto per Aspose.3D per Java?

 R4: Visita il forum di supporto[Qui](https://forum.aspose.com/c/3d/18).

### Q5: Ho bisogno di una licenza temporanea per i test?

 A5: Sì, ottieni una licenza temporanea[Qui](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
