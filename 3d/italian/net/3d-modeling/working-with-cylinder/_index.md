---
date: 2026-03-26
description: Scopri come creare un cilindro ed esportare un file OBJ usando Aspose.3D
  per .NET. Questa guida per principianti copre la configurazione della scena 3D e
  l'esportazione OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Come creare un cilindro con base di taglio – Aspose.3D per .NET
url: /it/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come creare un cilindro con base inclinata – Aspose.3D per .NET

## Introduzione
Se ti chiedi **come creare cilindri** con una base inclinata personalizzata in un ambiente .NET, sei nel posto giusto. In questo tutorial percorreremo ogni passaggio—dalla configurazione di una scena 3‑D all'esportazione del modello finale come file OBJ—così potrai migliorare le tue competenze di *modellazione 3D per principianti* usando **Aspose.3D per .NET**.

## Risposte rapide
- **Qual è la classe principale per avviare un modello 3D?** `Scene` crea il contenitore radice per tutta la geometria.  
- **Quale metodo esporta il modello in OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Ho bisogno di una licenza per i test?** È disponibile una versione di prova gratuita — vedi il link della prova nella FAQ.  
- **Posso modificare l'angolo di inclinazione?** Sì, modifica `ShearBottom` con un valore `Vector2`.  
- **È adatto ai principianti?** Assolutamente; l'API astrae la gestione a basso livello della mesh.

## Cos'è una scena 3D?
Una *scena 3D* è un contenitore gerarchico che contiene tutte le entità geometriche, luci, telecamere e trasformazioni. In Aspose.3D la classe `Scene` fornisce un modo pulito per organizzare e successivamente esportare i tuoi modelli.

## Perché esportare OBJ?
OBJ è un formato basato su testo ampiamente supportato che molte applicazioni 3‑D (Blender, Maya, Unity) possono importare. Esportare in OBJ ti consente di condividere o modificare ulteriormente i tuoi modelli di cilindro al di fuori di .NET.

## Prerequisiti
Prima di iniziare, assicurati di avere:

- Conoscenza di base di C# e sviluppo .NET.  
- **Aspose.3D for .NET** installato – puoi scaricarlo **[qui](https://releases.aspose.com/3d/net/)**.  
- Un IDE .NET (Visual Studio, Rider o VS Code) pronto per la programmazione.

## Importare gli spazi dei nomi
Prima, importa gli spazi dei nomi richiesti in modo che i tipi dell'API siano riconosciuti.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## Passo 1: Creare una scena 3D
L'oggetto `Scene` funge da radice della gerarchia del tuo modello.

```csharp
Scene scene = new Scene();
```

## Passo 2: Creare Cylinder 1
Generiamo il primo cilindro con un raggio di 2, altezza 10 e 20 segmenti radiali.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Passo 3: Personalizzare Shear Bottom per Cylinder 1
Applica una trasformazione di shear, abilita la generazione di cilindro a ventaglio e regola altre proprietà per ottenere la forma desiderata.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Passo 4: Aggiungere Cylinder 1 alla scena
Posiziona il primo cilindro in una posizione conveniente usando una trasformazione di traslazione.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Passo 5: Creare Cylinder 2
Viene creato un secondo cilindro con le stesse dimensioni di base ma senza shear personalizzato—perfetto per un confronto fianco a fianco.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Passo 6: Aggiungere Cylinder 2 alla scena
Allegiamo semplicemente il secondo cilindro al grafo della scena.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Passo 7: Esportare la scena come file OBJ
Infine, salviamo l'intera scena in un file OBJ così può essere aperto in qualsiasi visualizzatore 3‑D standard.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemi comuni e soluzioni
| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| **Il file OBJ è vuoto** | La scena non ha geometria allegata. | Assicurati che entrambi i cilindri siano aggiunti a `scene.RootNode`. |
| **Shear appare errato** | `ShearBottom` si aspetta la tangente dell'angolo. | Usa `Math.Tan(angleInRadians)` o il valore fornito `0.83` per ~47,5°. |
| **Errori di percorso file** | Directory non valida o mancante. | Usa `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Domande frequenti
### Aspose.3D for .NET è adatto ai principianti?
Assolutamente! Aspose.3D per .NET offre un'API di alto livello che astrae le parti matematiche della modellazione 3‑D, rendendola accessibile a sviluppatori di qualsiasi livello di competenza.

### Posso applicare angoli di shear diversi ai cilindri?
Sì, ogni istanza di `Cylinder` ha la propria proprietà `ShearBottom`, così puoi assegnare un angolo unico a ciascun oggetto.

### È disponibile una versione di prova?
Sì, puoi esplorare la versione di prova gratuita **[qui](https://releases.aspose.com/)**.

### Dove posso trovare supporto aggiuntivo?
Visita il **[forum Aspose.3D](https://forum.aspose.com/c/3d/18)** per aiuto della community, esempi di codice e discussioni.

### Come posso ottenere una licenza temporanea?
Ottieni la tua licenza temporanea **[qui](https://purchase.aspose.com/temporary-license/)**.

**Domande aggiuntive**

**Q: Come esportare il modello in un formato diverso, come STL?**  
A: Sostituisci `FileFormat.WavefrontOBJ` con `FileFormat.STL` nella chiamata `scene.Save`.

**Q: Posso animare i cilindri dopo la creazione?**  
A: Sì, puoi aggiungere animazioni a fotogrammi chiave alle trasformazioni dei nodi usando le classi `Animation` fornite da Aspose.3D.

**Q: L'API supporta .NET Core?**  
A: La libreria è pienamente compatibile con .NET Core, .NET 5+ e .NET 6+.

---

**Ultimo aggiornamento:** 2026-03-26  
**Testato con:** Aspose.3D per .NET (ultima release)  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}