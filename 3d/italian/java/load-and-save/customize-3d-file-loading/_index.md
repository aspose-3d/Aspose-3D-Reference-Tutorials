---
date: 2026-02-25
description: Scopri come invertire il sistema di coordinate e personalizzare l'importazione
  3D usando Aspose.3D LoadOptions in Java. Guida passo‑passo per 3DS, OBJ, STL, U3D,
  glTF, PLY, X e, facoltativamente, FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Capovolgi il sistema di coordinate – Personalizza il caricamento di file 3D
  in Java con Aspose.3D
url: /it/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Inverti il Sistema di Coordinate – Personalizza il Caricamento di File 3D in Java con Aspose.3D

Nel panorama in continua evoluzione del design e dello sviluppo 3D, **invertire il sistema di coordinate** durante l'importazione dei modelli è una necessità comune. Che tu stia convertendo asset da un sistema destro a uno sinistro o debba allineare i modelli alle convenzioni degli assi del tuo motore, Aspose.3D per Java ti offre un controllo fine. Questo tutorial ti guida su come **personalizzare l'importazione 3D** usando `LoadOptions` di Aspose.3D, coprendo i formati più popolari come 3DS, OBJ, STL, U3D, glTF, PLY, X e, facoltativamente, FBX.

## Risposte Rapide
- **Cosa fa “invertire il sistema di coordinate”?** Scambia gli assi X/Y/Z per corrispondere alla convenzione di coordinate di destinazione.  
- **Quali formati supportano l’inversione?** Tutti i principali formati (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) espongono l’opzione `setFlipCoordinateSystem`.  
- **Ho bisogno di librerie aggiuntive?** Solo il JAR di Aspose.3D per Java; non sono richiesti convertitori esterni.  
- **Posso caricare i materiali contemporaneamente?** Sì—usa `setEnableMaterials(true)` per i file OBJ.  
- **È necessaria una licenza per la produzione?** È necessaria una licenza valida di Aspose.3D per le distribuzioni non‑trial.

## Cos’è “invertire il sistema di coordinate”?
Invertire il sistema di coordinate cambia l’orientamento degli assi utilizzati dal modello importato. Questo è essenziale quando il file sorgente utilizza una mano diversa (destra vs. sinistra) rispetto al tuo motore di rendering, evitando che i modelli appaiano specchiati o invertiti.

## Perché personalizzare l’importazione 3D?
Personalizzare l’importazione ti consente di:
- Conservare le trasformazioni di animazione (`setApplyAnimationTransform`).  
- Correggere la gestione dei colori (`setGammaCorrectedColor`).  
- Risolvere i percorsi delle risorse esterne tramite `getLookupPaths()`.  
- Ottimizzare l’uso della memoria caricando solo ciò di cui hai bisogno.

## Prerequisiti

- Conoscenza di base della programmazione Java.  
- Java Development Kit (JDK) installato.  
- Libreria Aspose.3D per Java scaricata. Puoi ottenerla [qui](https://releases.aspose.com/3d/java/).  
- Familiarità con i formati di file 3D come 3DS, OBJ, STL, U3D, glTF, PLY, X e FBX.

## Import Packages

Nel tuo progetto Java, assicurati di importare i pacchetti Aspose.3D necessari:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Come personalizzare l’importazione 3D con LoadOptions

Di seguito trovi snippet di codice passo‑passo che mostrano come abilitare l’opzione **invertire il sistema di coordinate** per ciascun formato supportato. Gli snippet sono pronti per essere copiati nel tuo progetto; sostituisci semplicemente `"Your Document Directory"` con il percorso reale delle tue risorse.

### Passo 1: Personalizza il Caricamento di File 3DS

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

### Passo 2: Personalizza il Caricamento di File OBJ

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Passo 3: Personalizza il Caricamento di File STL

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Passo 4: Personalizza il Caricamento di File U3D

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Passo 5: Personalizza il Caricamento di File glTF

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Passo 6: Personalizza il Caricamento di File PLY

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Passo 7: Personalizza il Caricamento di File X

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Passo 8: Personalizza il Caricamento di File FBX (Facoltativo)

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

## Problemi Comuni e Soluzioni
- **Il modello appare specchiato dopo il caricamento** – Verifica che `setFlipCoordinateSystem(true)` sia impostato per il formato corretto.  
- **I materiali mancano** – Per i file OBJ, assicurati `setEnableMaterials(true)` e che i file di materiale (.mtl) siano presenti in uno dei percorsi di lookup.  
- **Le coordinate di texture sono capovolte** – Per glTF, potresti aver bisogno di `setFlipTexCoordV(true)` oltre all’inversione degli assi.  
- **Errori di file non trovato** – Aggiungi la directory contenente le risorse esterne (texture, file ausiliari) a `loadOpts.getLookupPaths()`.

## Conclusione

Sfruttando `LoadOptions` di Aspose.3D, puoi **invertire il sistema di coordinate** e **personalizzare l’importazione 3D** per praticamente tutti i principali formati. Questo livello di controllo elimina la necessità di script di post‑processing e garantisce che i tuoi asset vengano renderizzati correttamente al primo tentativo.

## Domande Frequenti

### Q1: Dove posso trovare la documentazione di Aspose.3D per Java?
A1: La documentazione è disponibile [qui](https://reference.aspose.com/3d/java/).

### Q2: Come posso scaricare Aspose.3D per Java?
A2: Puoi scaricarlo [qui](https://releases.aspose.com/3d/java/).

### Q3: È disponibile una versione di prova gratuita?
A3: Sì, puoi accedere alla prova gratuita [qui](https://releases.aspose.com/).

### Q4: Dove posso ottenere supporto per Aspose.3D per Java?
A4: Visita il forum di supporto [qui](https://forum.aspose.com/c/3d/18).

### Q5: Ho bisogno di una licenza temporanea per i test?
A5: Sì, ottieni una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-25  
**Tested With:** Aspose.3D for Java 24.11 (latest)  
**Author:** Aspose