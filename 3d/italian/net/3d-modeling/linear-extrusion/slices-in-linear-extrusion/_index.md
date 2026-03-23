---
date: 2026-03-23
description: Scopri come eseguire l'estrusione lineare con sezioni usando Aspose.3D
  per .NET. Crea modelli 3D dettagliati con esempi di codice passo‑passo.
linktitle: How to Linear Extrusion with Slices
second_title: Aspose.3D .NET API
title: Come eseguire l'estrusione lineare con sezioni usando Aspose.3D per .NET
url: /it/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Come eseguire l'estrusione lineare con fette usando Aspose.3D per .NET

## Introduzione

Benvenuti nel mondo del design 3D con Aspose.3D per .NET! In questo tutorial scoprirete **come eseguire l'estrusione lineare** con fette, una tecnica che vi permette di controllare il livello di dettaglio nei vostri modelli. Che siate sviluppatori esperti o alle prime armi, vi guideremo passo passo, spiegheremo il perché di ogni azione e vi forniremo consigli pratici da applicare subito.

## Risposte rapide
- **Che cos'è l'estrusione lineare con fette?** È un metodo per estendere un profilo 2D in 3D specificando quante sezioni trasversali intermedie (fette) vengono generate.  
- **Perché usare le fette?** Più fette garantiscono curvature più fluide; meno fette mantengono la mesh leggera.  
- **Prerequisiti?** Aspose.3D per .NET, un IDE compatibile con .NET e conoscenze di base di C#.  
- **Tempo di esecuzione tipico?** L'esempio viene eseguito in meno di un secondo su un PC moderno.  
- **Formato di output?** L'esempio salva in Wavefront OBJ, ma Aspose.3D supporta molti formati.

## Che cos'è l'estrusione lineare con fette?

L'estrusione lineare prende una forma 2‑D (un profilo) e la allunga lungo una linea retta per creare un solido 3‑D. La proprietà **Slices** determina quante sezioni trasversali intermedie vengono inserite tra l'inizio e la fine dell'estrusione, influenzando la levigatezza e il numero di poligoni.

## Perché usare le fette nell'estrusione lineare?

- **Controllo della densità della mesh:** Affinate il bilanciamento tra qualità visiva e dimensione del file.  
- **Ottimizzazione delle prestazioni:** Usate meno fette per applicazioni in tempo reale, più fette per rendering ad alta risoluzione.  
- **Flessibilità creativa:** Combinate diversi conteggi di fette su oggetti separati per evidenziare l'intento di design.

## Prerequisiti

Prima di iniziare, assicuratevi di avere:

- Libreria Aspose.3D per .NET – scaricatela da [here](https://releases.aspose.com/3d/net/).  
- Un IDE che supporti C# (Visual Studio, Rider, VS Code, ecc.).  
- Familiarità di base con la sintassi C# e i concetti di programmazione orientata agli oggetti.  
- Curiosità nello sperimentare con la geometria 3‑D!

## Importare i namespace

Per prima cosa, importate i namespace che vi danno accesso alle classi core di Aspose.3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Guida passo‑passo

### Passo 1: Inizializzare il profilo di base

Iniziamo con una semplice forma rettangolare e le diamo un piccolo raggio di arrotondamento così i bordi non sono perfettamente affilati.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Passo 2: Creare una scena 3D

Una `Scene` funge da contenitore per tutti i nodi, le mesh, le luci e le telecamere.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Passo 3: Aggiungere i nodi sinistro e destro

Creeremo due nodi fratelli sotto la radice della scena. Il nodo sinistro riceverà un conteggio di fette basso, il nodo destro un conteggio alto, così potrete confrontare la differenza visiva.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Passo 4: Eseguire l'estrusione lineare sul nodo sinistro (basso dettaglio)

Qui estrudiamo il rettangolo con sole **2 fette**. Questo produce una mesh grezza—ideale per anteprime rapide.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Passo 5: Eseguire l'estrusione lineare sul nodo destro (alto dettaglio)

Ora usiamo **10 fette** per un risultato molto più liscio. Notate come la geometria diventi più fine.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Passo 6: Salvare la scena 3D

Infine, scrivete la scena in un file OBJ. Sostituite `"Your Output Directory"` con un percorso valido sulla vostra macchina.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|----------------|-----------|
| **Nessun file creato** | Il percorso di output è non valido o manca il permesso di scrittura. | Usate un percorso assoluto e assicuratevi che la cartella esista. |
| **L'oggetto appare piatto** | `Slices` impostato a 1 o 0. | Impostate `Slices` ad almeno 2 per un'estrusione visibile. |
| **Geometria inattesa** | Raggio di arrotondamento troppo grande rispetto alle dimensioni del rettangolo. | Regolate `RoundingRadius` a un valore inferiore a metà del lato più piccolo del rettangolo. |

## Domande frequenti

**D: Posso cambiare la direzione dell'estrusione?**  
R: Sì. Usate la proprietà `Transform` sul nodo per ruotare o traslare la geometria estrusa prima di salvarla.

**D: Aspose.3D supporta altri tipi di estrusione?**  
R: Assolutamente. Oltre a `LinearExtrusion`, potete usare `RevolveExtrusion`, `SweepExtrusion` e altri.

**D: In quali formati posso esportare?**  
R: Aspose.3D supporta OBJ, STL, FBX, 3MF, Collada e molti altri. Basta cambiare l'enumerazione `FileFormat`.

**D: È possibile impostare un materiale in modo programmatico?**  
R: Sì. Dopo aver creato il nodo, assegnate un `Material` alla sua collezione `Entity`.

**D: Come influisce il numero di fette sull'uso della memoria?**  
R: Più fette aumentano il conteggio di vertici e facce, il che eleva il consumo di memoria proporzionalmente. Utilizzate il profiling per trovare il punto ottimale per la vostra piattaforma target.

## FAQ originali

### Q1: Posso usare Aspose.3D per .NET con altri linguaggi di programmazione?

A1: Aspose.3D è progettato principalmente per .NET, ma potete esplorare opzioni di interoperabilità con linguaggi come Python usando binding .NET.

### Q2: Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?

A2: Consultate la documentazione [here](https://reference.aspose.com/3d/net/) per informazioni approfondite sulle capacità e sull'uso di Aspose.3D.

### Q3: È disponibile una versione di prova gratuita per Aspose.3D per .NET?

A3: Sì, potete scaricare la vostra prova gratuita [here](https://releases.aspose.com/) per esplorare le funzionalità della libreria prima di acquistare.

### Q4: Come posso ottenere supporto tecnico per Aspose.3D per .NET?

A4: Visitate il forum Aspose.3D [here](https://forum.aspose.com/c/3d/18) per chiedere assistenza e interagire con la community.

### Q5: Posso usare una licenza temporanea per Aspose.3D per .NET?

A5: Sì, ottenete una licenza temporanea [here](https://purchase.aspose.com/temporary-license/) per scopi di valutazione.

## Conclusione

Avete ora visto **come eseguire l'estrusione lineare** con fette usando Aspose.3D per .NET, esplorato l'impatto di diversi conteggi di fette e imparato a esportare il vostro lavoro. Sperimentate con altri profili, giocate con il valore `Slices` e integrate materiali o luci per creare asset 3‑D pronti per la produzione.

---

**Ultimo aggiornamento:** 2026-03-23  
**Testato con:** Aspose.3D 24.11 per .NET (ultima versione al momento della stesura)  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}