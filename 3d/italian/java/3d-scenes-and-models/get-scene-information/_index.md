---
date: 2026-09-08
description: Scopri come definire le unità ed esportare una scena in FBX con Java
  usando Aspose.3D. Questa guida passo‑passo mostra come impostare il nome dell'applicazione,
  le unità di misura e recuperare le informazioni della scena 3D.
keywords:
- how to define units
- export scene to fbx
- how to set application name
- define measurement units
lastmod: 2026-09-08
linktitle: Come salvare FBX e recuperare le informazioni della scena 3D in Java
og_description: Scopri come definire le unità ed esportare una scena in FBX con Java
  usando Aspose.3D. La guida copre l'impostazione del nome dell'applicazione, le unità
  di misura e il recupero delle informazioni della scena 3D in pochi passaggi.
og_image_alt: Guide showing how to define units and export a 3D scene to FBX using
  Aspose.3D Java
og_title: Come definire le unità ed esportare la scena in FBX con Java
schemas:
- author: Aspose
  dateModified: '2026-09-08'
  description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  headline: How to define units and export scene to FBX in Java
  type: TechArticle
- description: Learn how to define units and export a scene to FBX in Java using Aspose.3D.
    This step‑by‑step guide shows setting the application name, measurement units,
    and retrieving 3D scene information.
  name: How to define units and export scene to FBX in Java
  steps:
  - name: initialize a 3D scene
    text: The `Scene` class is Aspose.3D's top‑level container that represents an
      entire 3D scene, including geometry, lights, cameras, and metadata. First, create
      an empty `Scene` object. This will be the container for all geometry, lights,
      cameras, and asset metadata.
  - name: define measurement units
    text: The unit system determines the real‑world scale of the scene; Aspose.3D
      lets you specify a unit name and a scale factor relative to meters. In this
      example we use an ancient Egyptian unit called “pole” with a custom scale factor.
      > **Tip:** Adjust `unitScaleFactor` to match the real‑world size of yo
  - name: export scene to FBX
    text: Now that the asset information is attached, we save the scene as an FBX
      file. The `FileFormat.FBX7500ASCII` option produces a human‑readable ASCII FBX,
      which is handy for debugging. > **Remember:** Replace `"Your Document Directory"`
      with an absolute path or a path relative to your project's working
  type: HowTo
- questions:
  - answer: Replace `FileFormat.FBX7500ASCII` with `FileFormat.FBX7500` when calling
      `scene.save(...)`.
    question: How do I change the output format to binary FBX?
  - answer: Yes, use `scene.getUserData().add("Key", "Value")` to embed additional
      key‑value pairs.
    question: Can I add custom user‑defined metadata beyond the built‑in asset fields?
  - answer: It does. Simply change the `FileFormat` enum to `OBJ` or `GLTF2` as needed.
    question: Does Aspose.3D support other export formats like OBJ or GLTF?
  - answer: Aspose.3D for Java supports Java 8 and later.
    question: What version of Java is required?
  - answer: Absolutely. Load the file with `new Scene("input.fbx")`, modify `scene.getAssetInfo()`,
      then save.
    question: Is it possible to load an existing FBX, modify its asset info, and resave?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- export scene to fbx
- Aspose.3D
- Java 3D
- define units
- 3D asset metadata
title: Come definire le unità ed esportare la scena in FBX con Java
url: /it/java/3d-scenes-and-models/get-scene-information/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come definire le unità ed esportare la scena in FBX con Java

## Introduzione

Se stai cercando una guida chiara e pratica su **come definire le unità** e **esportare una scena in FBX** estraendo metadati utili dalle tue scene 3D, sei nel posto giusto. In questo tutorial percorreremo ogni passaggio usando la libreria **Aspose.3D for Java**: dalla creazione di una scena, **impostare il nome dell'applicazione**, **definire le unità di misura**, fino all'**esportazione della scena in FBX**. Alla fine avrai un file FBX pronto all'uso che contiene le informazioni sugli asset necessarie per le pipeline successive.

## Risposte rapide
- **Qual è l'obiettivo principale?** Esportare una scena in FBX che contenga informazioni personalizzate sugli asset.  
- **Quale libreria viene utilizzata?** Aspose.3D for Java.  
- **È necessaria una licenza?** Una versione di prova gratuita funziona per lo sviluppo; è necessaria una licenza commerciale per la produzione.  
- **Posso cambiare le unità di misura?** Sì – usa `setUnitName` e `setUnitScaleFactor`.  
- **Dove viene salvato l'output?** Nel percorso che specifichi in `scene.save(...)`.  

## Prerequisiti

Prima di iniziare, assicurati di avere:

- Una solida conoscenza della sintassi di base di Java.  
- **Aspose.3D for Java** scaricato e aggiunto al tuo progetto (puoi ottenerlo dalla pagina ufficiale) [Aspose 3D download page](https://releases.aspose.com/3d/java/).  
- Il tuo IDE Java preferito (IntelliJ IDEA, Eclipse, NetBeans, ecc.) correttamente configurato.

## Importare i pacchetti

Nel tuo file sorgente Java, importa le classi Aspose.3D che forniscono la gestione della scena e il supporto dei formati file.

```java
import com.aspose.threed.FileFormat;
import com.aspose.threed.Scene;
```

> **Suggerimento:** Mantieni l'elenco degli import minimal per evitare dipendenze inutili e migliorare i tempi di compilazione.

## Qual è il processo per salvare un file FBX?

Per salvare una scena come file FBX, crei un `Scene`, imposti i metadati degli asset desiderati, definisci l'unità di misura e poi chiami `scene.save(path, FileFormat.FBX7500ASCII)`. Questa sequenza scrive geometria, materiali e metadati in un FBX ASCII che può essere ispezionato o importato da strumenti successivi.

### Passo 1: inizializzare una scena 3D

La classe `Scene` è il contenitore di livello superiore di Aspose.3D che rappresenta un'intera scena 3D, includendo geometria, luci, telecamere e metadati. Prima, crea un oggetto `Scene` vuoto. Questo sarà il contenitore per tutta la geometria, le luci, le telecamere e i metadati degli asset.

```java
// ExStart:AddAssetInformationToScene
Scene scene = new Scene();
```

### Come impostare il nome dell'applicazione in Java

L'oggetto `AssetInfo` memorizza metadati come il nome dell'applicazione, il fornitore e la versione per la scena. Aggiungere metadati personalizzati aiuta gli strumenti successivi a identificare la sorgente del file. Usa l'oggetto `AssetInfo` per **impostare il nome dell'applicazione** (e il fornitore) prima di salvare il file.

```java
scene.getAssetInfo().setApplicationName("Egypt");
scene.getAssetInfo().setApplicationVendor("Manualdesk");
```

> **Perché è importante:** Molte pipeline filtrano o etichettano gli asset in base all'applicazione di origine, rendendo questo passaggio essenziale per progetti di grandi dimensioni.

### Passo 3: definire le unità di misura

Il sistema di unità determina la scala reale della scena; Aspose.3D consente di specificare un nome di unità e un fattore di scala relativo ai metri. In questo esempio usiamo un'unità egizia antica chiamata “pole” con un fattore di scala personalizzato.

```java
scene.getAssetInfo().setUnitName("pole");
scene.getAssetInfo().setUnitScaleFactor(0.6);
```

> **Suggerimento:** Regola `unitScaleFactor` per corrispondere alle dimensioni reali dei tuoi modelli; 1.0 rappresenta una corrispondenza 1‑a‑1 con l'unità scelta.

### Passo 4: esportare la scena in FBX

Ora che le informazioni degli asset sono allegate, salviamo la scena come file FBX. L'opzione `FileFormat.FBX7500ASCII` produce un FBX ASCII leggibile dall'uomo, utile per il debug.

```java
String MyDir = "Your Document Directory";
MyDir = MyDir + "InformationToScene.fbx";
scene.save(MyDir, FileFormat.FBX7500ASCII);
System.out.println("\nAsset information added successfully to Scene.\nFile saved at " + MyDir);
// ExEnd:AddAssetInformationToScene
```

> **Ricorda:** Sostituisci `"Your Document Directory"` con un percorso assoluto o un percorso relativo alla directory di lavoro del tuo progetto.

## Perché esportare la scena in FBX con Aspose.3D?

Aspose.3D supporta **oltre 50 formati di input e output** e può elaborare scene di centinaia di pagine senza caricare l'intero file in memoria, offrendoti il pieno controllo sul file esportato — metadati, unità e geometria — senza necessità di un'applicazione di authoring 3D pesante. Questo rende la generazione automatica di asset, l'elaborazione batch e le conversioni lato server rapide e affidabili.

## Casi d'uso comuni

- **Pipeline di asset per giochi** – incorpora le informazioni del creatore direttamente nei file FBX per il tracciamento delle versioni.  
- **Visualizzazione architettonica** – memorizza unità specifiche del progetto per evitare errori di scala durante l'importazione nei motori di rendering.  
- **Reportistica automatizzata** – genera file FBX al volo con metadati che gli strumenti di analisi successivi possono leggere.  
- **Servizi 3D basati su cloud** – crea ed esporta scene programmaticamente senza interfaccia grafica, perfetto per piattaforme SaaS.

## Risoluzione dei problemi e consigli

| Problema | Soluzione |
|-------|----------|
| **File non trovato dopo il salvataggio** | Verifica che `MyDir` punti a una cartella esistente e che la tua applicazione abbia i permessi di scrittura. |
| **Le unità appaiono errate nel visualizzatore esterno** | Controlla nuovamente `unitScaleFactor`; alcuni visualizzatori si aspettano i metri come unità di base. |
| **Metadati dell'asset mancanti** | Assicurati di chiamare `scene.getAssetInfo()` **prima** del salvataggio; le modifiche effettuate dopo `save()` non verranno preservate. |
| **Collo di bottiglia delle prestazioni su scene grandi** | Usa `scene.optimize()` prima del salvataggio per ridurre l'uso di memoria. |
| **FBX ASCII troppo grande** | Passa al FBX binario usando `FileFormat.FBX7500` (vedi FAQ). |

## Domande frequenti

**Q: Come cambio il formato di output in FBX binario?**  
A: Sostituisci `FileFormat.FBX7500ASCII` con `FileFormat.FBX7500` quando chiami `scene.save(...)`.

**Q: Posso aggiungere metadati personalizzati definiti dall'utente oltre ai campi asset integrati?**  
A: Sì, usa `scene.getUserData().add("Key", "Value")` per incorporare coppie chiave‑valore aggiuntive.

**Q: Aspose.3D supporta altri formati di esportazione come OBJ o GLTF?**  
A: Sì. Basta cambiare l'enumerazione `FileFormat` in `OBJ` o `GLTF2` secondo necessità.

**Q: Quale versione di Java è richiesta?**  
A: Aspose.3D for Java supporta Java 8 e successive.

**Q: È possibile caricare un FBX esistente, modificare le sue informazioni asset e risalvarlo?**  
A: Assolutamente. Carica il file con `new Scene("input.fbx")`, modifica `scene.getAssetInfo()`, poi salva.

---

**Ultimo aggiornamento:** 2026-09-08  
**Testato con:** Aspose.3D for Java 24.11  
**Autore:** Aspose

## Tutorial correlati

- [Riduci la dimensione dei file 3D – Comprimi le scene con Aspose.3D per Java](/3d/java/3d-scenes-and-models/compress-3d-scenes/)
- [Come impostare il colore vector3 in Java: Cambia il colore Diffuse e gestisci le proprietà 3D nelle scene Java usando Aspose.3D](/3d/java/3d-scenes-and-models/managing-3d-properties-scenes/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}