---
date: 2026-01-17
description: Scopri come elencare le proprietà dei materiali, modificare il colore
  diffuso e alterare gli attributi dei materiali 3D utilizzando Aspose.3D per .NET.
  Sono inclusi esempi di codice passo‑passo.
linktitle: List Material Properties in 3D Scenes with Aspose.3D
second_title: Aspose.3D .NET API
title: Elenca le proprietà dei materiali nelle scene 3D con Aspose.3D
url: /it/net/3d-scene/set-3d-properties/
weight: 14
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Elenca le proprietà dei materiali nelle scene 3D con Aspose.3D

## Introduzione

Se hai bisogno di **list material properties** di un modello 3D e poi regolare elementi come il colore diffuso, sei nel posto giusto. Aspose.3D per .NET ti offre un'API pulita, orientata agli oggetti, che ti permette di ispezionare, recuperare e modificare gli attributi dei materiali senza uscire dal tuo codice C#. In questo tutorial vedremo come caricare una scena, enumerare le sue proprietà dei materiali e cambiare valori come il componente diffuso—così potrai dare ai tuoi modelli l'aspetto esatto che desideri.

## Risposte rapide
- **Qual è l'obiettivo principale?** Elencare le proprietà dei materiali e modificarle (ad es., colore diffuso).  
- **Quale libreria è necessaria?** Aspose.3D per .NET.  
- **È necessaria una licenza?** È necessaria una licenza temporanea o completa per l'uso in produzione.  
- **Formati di file supportati?** FBX, OBJ, STL, STL‑ASCII, 3MF e altri.  
- **Tempo tipico di implementazione?** Circa 10‑15 minuti per uno script base di elencazione delle proprietà.

## Cos'è **list material properties**?
Elencare le proprietà dei materiali significa iterare sulla `PropertyCollection` di un materiale per leggere ogni nome di proprietà e il suo valore corrente. Questo è utile per il debug, l'ispezione visiva o per costruire controlli UI che consentono agli utenti di regolare le impostazioni dei materiali in tempo reale.

## Perché usare Aspose.3D per **access material properties**?
- **Nessun convertitore esterno** – lavora direttamente con oggetti .NET nativi.  
- **Modello di proprietà ricco** – supporta attributi specifici FBX personalizzati oltre ai valori PBR standard.  
- **Cross‑platform** – funziona su .NET Framework, .NET Core e .NET 5/6+.  

## Prerequisiti

- Aspose.3D per .NET installato nel tuo progetto. Scaricalo [qui](https://releases.aspose.com/3d/net/).
- Una cartella su disco per contenere i tuoi file sorgente 3‑D (ad es., un file FBX con texture incorporate).

Ora che hai le basi pronte, immergiamoci nel codice.

## Importa gli spazi dei nomi

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Passo 1: Carica la scena 3D

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//ExEnd: Load3DScene
```

## Passo 2: **Access material properties** del primo nodo

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Passo 3: **List material properties** – visualizza ogni coppia nome/valore

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//or using ordinal for loop
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## Passo 4: **How to change diffuse** – modifica la proprietà Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Passo 5: **Retrieve property by name** – ottieni un'istanza tipizzata

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Passo 6: Attraversa le proprietà di una proprietà (avanzato)

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//and some properties that only defined in FBX file:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//traversal on property's property is possible
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## Come **change 3d material color** oltre il diffuso
Se devi influenzare i colori specular, ambient o emissive, sostituisci semplicemente `"Diffuse"` con `"Specular"` o `"Ambient"` nell'assegnazione `props["..."]` sopra. Si applicano le stesse strutture `Vector3` o `Vector4`.

## Problemi comuni e suggerimenti
- **Sensibilità al maiuscolo/minuscolo del nome della proprietà** – le chiavi delle proprietà di Aspose.3D sono case‑sensitive; usa il nome esatto mostrato nell'output dell'elenco.  
- **Proprietà mancante** – non tutti i materiali espongono ogni attributo PBR. Controlla `props.ContainsKey("Specular")` prima di accedere.  
- **Salvataggio delle modifiche** – dopo aver modificato le proprietà, chiama `scene.Save("output.fbx");` per persistere le modifiche.

## Conclusione

Hai ora imparato come **list material properties**, **retrieve a property by name** e **change the diffuse color** (o qualsiasi altro attributo del materiale) usando Aspose.3D per .NET. Sperimenta con diversi tipi di proprietà per perfezionare l'aspetto dei tuoi asset 3‑D.

## FAQ

### Q1: Posso usare Aspose.3D per .NET con altri formati di file 3D?
A1: Sì, Aspose.3D supporta vari formati di file 3D, inclusi FBX, STL e molti altri.

### Q2: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?
A2: Visita [qui](https://purchase.aspose.com/temporary-license/) per ottenere una licenza temporanea.

### Q3: Esiste un forum della community per gli utenti di Aspose.3D?
A3: Sì, puoi trovare supporto e discussioni al [forum Aspose.3D](https://forum.aspose.com/c/3d/18).

### Q4: Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?
A4: Consulta la [documentazione](https://reference.aspose.com/3d/net/) per una guida completa.

### Q5: Posso provare Aspose.3D per .NET gratuitamente prima di acquistare?
A5: Certamente! Scarica la [versione di prova gratuita](https://releases.aspose.com/) per esplorare le sue funzionalità.

## Domande frequenti

**Q: Cosa rappresenta `Vector3(1, 0, 1)`?**  
A: Imposta il colore diffuso a magenta (rosso = 1, verde = 0, blu = 1) nello spazio colore lineare.

**Q: Devo chiamare `scene.Save` dopo aver modificato le proprietà?**  
A: Sì, persistere la scena scrive le modifiche su disco; altrimenti le modifiche rimangono solo in memoria.

**Q: Posso enumerare attributi FBX personalizzati?**  
A: Assolutamente. La `PropertyCollection` includerà tutti gli attributi personalizzati, accessibili tramite `GetProperty("customName")`.

**Q: Esiste un modo per aggiornare in batch più materiali?**  
A: Scorri `scene.RootNode.ChildNodes` e ripeti i passaggi di modifica delle proprietà per ogni materiale.

**Q: Aspose.3D supporta .NET 6?**  
A: Sì, la libreria è pienamente compatibile con .NET 6 e versioni successive.

**Ultimo aggiornamento:** 2026-01-17  
**Testato con:** Aspose.3D 24.11 per .NET  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}