---
date: 2026-03-28
description: Scopri come elencare le proprietà dei materiali, modificare il colore
  diffuso e alterare gli attributi dei materiali 3D usando Aspose.3D per .NET. Sono
  inclusi esempi di codice passo‑passo.
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

Se hai bisogno di **elencare le proprietà dei materiali** di un modello 3D e poi regolare cose come il colore diffuso, sei nel posto giusto. Aspose.3D for .NET ti offre un'API pulita, orientata agli oggetti, che ti consente di ispezionare, recuperare e modificare gli attributi dei materiali senza uscire dal tuo codice C#. In questo tutorial vedremo come caricare una scena, enumerare le sue proprietà dei materiali e cambiare valori come il componente diffuso—così potrai dare ai tuoi modelli l'aspetto esatto che desideri.

## Risposte rapide
- **Qual è l'obiettivo principale?** Elencare le proprietà dei materiali e modificarle (ad es., colore diffuso).  
- **Quale libreria è necessaria?** Aspose.3D for .NET.  
- **Ho bisogno di una licenza?** È necessaria una licenza temporanea o completa per l'uso in produzione.  
- **Formati di file supportati?** FBX, OBJ, STL, STL‑ASCII, 3MF e altri.  
- **Tempo tipico di implementazione?** Circa 10‑15 minuti per uno script di base di elencazione delle proprietà.

## Cos'è **elencare le proprietà dei materiali**?
Elencare le proprietà dei materiali significa iterare su `PropertyCollection` di un materiale per leggere ogni nome di proprietà e il suo valore corrente. Questo è utile per il debug, l'ispezione visiva o la creazione di controlli UI che consentono agli utenti di modificare le impostazioni del materiale in tempo reale.

## Perché usare Aspose.3D per **accedere alle proprietà dei materiali**?
- **Nessun convertitore esterno** – lavora direttamente con oggetti .NET nativi.  
- **Modello di proprietà ricco** – supporta attributi specifici FBX personalizzati oltre ai valori PBR standard.  
- **Cross‑platform** – funziona su .NET Framework, .NET Core e .NET 5/6+.  

## Prerequisiti

- Aspose.3D for .NET installato nel tuo progetto. Scaricalo [qui](https://releases.aspose.com/3d/net/).
- Una cartella su disco per contenere i tuoi file sorgente 3‑D (ad esempio, un file FBX con texture incorporate).

Ora che hai sistemato le basi, immergiamoci nel codice.

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

## Passo 2: **Accedi alle proprietà dei materiali** del primo nodo

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## Passo 3: **Elenca le proprietà dei materiali** – vedi ogni coppia nome/valore

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

## Passo 4: **Come cambiare il diffuso** – modifica la proprietà Diffuse

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//modify property value by name
props["Diffuse"] = new Vector3(1, 0, 1); // sets a magenta diffuse color
//ExEnd: GetModifyPropertyByName
```

## Passo 5: **Recupera la proprietà per nome** – ottieni un'istanza tipizzata

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## Passo 6: Attraversa le proprietà proprie di una proprietà (avanzato)

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

## Come **cambiare il colore del materiale 3D** oltre il diffuso
Se devi influenzare i colori specular, ambient o emissive, basta sostituire `"Diffuse"` con `"Specular"` o `"Ambient"` nell'assegnazione `props["..."]` sopra. Si applicano le stesse strutture `Vector3` o `Vector4`.

## Come **aggiornare il colore del materiale in C#**
Modificare l'aspetto visivo di un materiale si riduce ad aggiornare la proprietà appropriata nella `PropertyCollection`. Che tu voglia modificare il diffuso, lo specular o qualsiasi attributo di colore personalizzato, il modello rimane lo stesso:

1. Recupera la proprietà con il suo nome esatto (case‑sensitive).  
2. Assegna un nuovo valore `Vector3` (RGB) o `Vector4` (RGBA).  

Poiché l'API lavora direttamente con oggetti C#, puoi **aggiornare il colore del materiale C#** senza file o convertitori intermedi. Questo lo rende perfetto per editor in tempo reale o pipeline di elaborazione batch.

## Problemi comuni e consigli
- **Sensibilità al maiuscolo/minuscolo del nome della proprietà** – le chiavi delle proprietà di Aspose.3D sono case‑sensitive; usa il nome esatto mostrato nell'output dell'elenco.  
- **Proprietà mancante** – non tutti i materiali espongono ogni attributo PBR. Controlla `props.ContainsKey("Specular")` prima di accedere.  
- **Salvataggio delle modifiche** – dopo aver modificato le proprietà, chiama `scene.Save("output.fbx");` per persistere le modifiche.

## Conclusione
Ora hai imparato come **elencare le proprietà dei materiali**, **recuperare una proprietà per nome** e **cambiare il colore diffuso** (o qualsiasi altro attributo del materiale) usando Aspose.3D per .NET. Sperimenta con diversi tipi di proprietà per perfezionare l'aspetto dei tuoi asset 3‑D, e ricorda che puoi **aggiornare il colore del materiale C#** con una sola riga di codice.

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

**D: Cosa rappresenta `Vector3(1, 0, 1)`?**  
R: Imposta il colore diffuso a magenta (rosso = 1, verde = 0, blu = 1) nello spazio colore lineare.

**D: Devo chiamare `scene.Save` dopo aver modificato le proprietà?**  
R: Sì, persistere la scena scrive le modifiche su disco; altrimenti le modifiche rimangono solo in memoria.

**D: Posso enumerare attributi FBX personalizzati?**  
R: Assolutamente. `PropertyCollection` includerà tutti gli attributi personalizzati, che puoi accedere tramite `GetProperty("customName")`.

**D: Esiste un modo per aggiornare in batch più materiali?**  
R: Scorri `scene.RootNode.ChildNodes` e ripeti i passaggi di modifica delle proprietà per ogni materiale.

**D: Aspose.3D supporta .NET 6?**  
R: Sì, la libreria è pienamente compatibile con .NET 6 e versioni successive.

---

**Ultimo aggiornamento:** 2026-03-28  
**Testato con:** Aspose.3D 24.11 per .NET  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}