---
title: Opzioni di caricamento personalizzate
linktitle: Opzioni di caricamento personalizzate
second_title: API Aspose.3D .NET
description: Esplora Aspose.3D per .NET, la soluzione definitiva per il caricamento e il salvataggio senza interruzioni dei modelli 3D.
type: docs
weight: 15
url: /it/net/loading-and-saving/custom-load-options/
---
## introduzione

Benvenuti nel mondo di Aspose.3D per .NET, una potente libreria che consente agli sviluppatori di lavorare senza problemi con file 3D. In questo tutorial, approfondiremo le complessità del caricamento e del salvataggio dei modelli 3D, concentrandoci sulle opzioni di caricamento personalizzate. Che tu sia uno sviluppatore esperto o un nuovo arrivato, questa guida ti guiderà attraverso il processo passo dopo passo, assicurandoti di sfruttare tutto il potenziale di Aspose.3D per .NET.

## Prerequisiti

Prima di intraprendere questo viaggio, assicurati di disporre dei seguenti prerequisiti:

-  Aspose.3D per .NET: assicurati di avere la libreria installata. Puoi scaricarlo[Qui](https://releases.aspose.com/3d/net/).

- Directory dei documenti: crea una directory per archiviare i file del modello 3D.

Ora che hai gli elementi essenziali, tuffiamoci nell'emozionante mondo della manipolazione dei modelli 3D!

## Importa spazi dei nomi

Per prima cosa, importiamo gli spazi dei nomi necessari. Questo porrà le basi per il nostro viaggio nel regno Aspose.3D.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## Caricamento e salvataggio: opzioni di caricamento personalizzate

### Passaggio 1: caricamento dei file Discreet3DS

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //Imposta opzioni personalizzate
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carica il file con le opzioni di caricamento
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### Passaggio 2: caricamento dei file OBJ

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //Imposta opzioni personalizzate
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carica il file con le opzioni di caricamento
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### Passaggio 3: caricamento dei file STL

```csharp
private static void STLLoadOption()
{
    // Il percorso della directory dei documenti.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //Imposta opzioni personalizzate
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carica il file con le opzioni di caricamento
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### Passaggio 4: caricamento dei file U3D

```csharp
private static void U3DLoadOption()
{
    // Il percorso della directory dei documenti.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //Imposta opzioni personalizzate
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //Carica il file con le opzioni di caricamento
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### Passaggio 5: caricamento dei file glTF

```csharp
private static void glTFLoadOptions()
{
    // Il percorso della directory dei documenti.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //Imposta opzioni personalizzate
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### Passaggio 6: caricamento dei file PLY

```csharp
private static void PlyLoadOptions()
{
    // Il percorso della directory dei documenti.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //Imposta opzioni personalizzate
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### Passaggio 7: caricamento dei file FBX

```csharp
private static void FBXLoadOptions()
{
    // Il percorso della directory dei documenti.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //Imposta opzioni personalizzate
    scene.Open("test.FBX", opt);

    // Proprietà di output definite in GlobalSettings nel file FBX
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## Conclusione

Congratulazioni! Hai navigato con successo attraverso l'intricato mondo del caricamento e del salvataggio di modelli 3D utilizzando Aspose.3D per .NET. Questo tutorial ha trattato vari formati di file e le relative opzioni di caricamento personalizzate, consentendoti di manipolare facilmente le risorse 3D.

## Domande frequenti

### Q1: Aspose.3D per .NET è adatto ai principianti?

R1: Assolutamente! Aspose.3D per .NET fornisce un'interfaccia user-friendly, rendendola accessibile agli sviluppatori di tutti i livelli.

### Q2: Posso utilizzare Aspose.3D per progetti commerciali?

A2: Sì, Aspose.3D per .NET viene fornito con una licenza commerciale, che ti consente di utilizzarlo nei tuoi progetti.

### Q3: Esistono limitazioni sui formati di file supportati?

 A3: Aspose.3D per .NET supporta un'ampia gamma di formati di file 3D popolari, inclusi OBJ, STL, FBX e altri. Fare riferimento al[documentazione](https://reference.aspose.com/3d/net/) per un elenco completo.

### Q4: È disponibile una versione di prova?

A4: Sì, puoi esplorare le funzionalità di Aspose.3D per .NET scaricando il file[prova gratuita](https://releases.aspose.com/).

### Q5: Dove posso cercare supporto per Aspose.3D per .NET?

 A5: Visita il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per il sostegno e l'assistenza della comunità.