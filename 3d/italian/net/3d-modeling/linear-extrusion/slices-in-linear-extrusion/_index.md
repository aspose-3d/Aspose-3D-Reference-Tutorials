---
date: 2026-01-09
description: Impara a creare scene 3D e a salvare modelli 3D usando Aspose.3D per
  .NET, includendo l'esportazione Wavefront OBJ e le sezioni di estrusione lineare.
linktitle: Create 3D Scene with Linear Extrusion Slices
second_title: Aspose.3D .NET API
title: Crea scena 3D con fette di estrusione lineare
url: /it/net/3d-modeling/linear-extrusion/slices-in-linear-extrusion/
weight: 13
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Crea una scena 3D con fette di estrusione lineare

## Introduzione

Benvenuto nel mondo del design 3D con Aspose.3D per .NET! In questo tutorial **creerai oggetti scena 3d**, applicherai un'estrusione lineare con un numero personalizzato di fette e infine **salverai il modello 3d** come file Wavefront OBJ. Che tu stia realizzando un rapido prototipo o una visualizzazione pronta per la produzione, i passaggi seguenti ti mostreranno **come usare Aspose** per generare geometria di alta qualità direttamente da C#.

## Risposte rapide
- **Cosa significa “creare scena 3d”?** Indica la costruzione di un oggetto Scene che contiene tutte le entità 3D (mesh, luci, telecamere).  
- **Quale formato viene usato per l'esportazione?** L'esempio esporta in **Wavefront OBJ** (`export wavefront obj`).  
- **Quante fette posso impostare?** Puoi impostare qualsiasi intero; la demo mostra 2 e 10 fette.  
- **È necessaria una licenza?** È richiesta una licenza temporanea o completa per l'uso in produzione.  
- **Posso eseguirlo su .NET Core?** Sì, Aspose.3D supporta .NET Framework e .NET Core.

## Prerequisiti

Prima di immergerti nel mondo del design 3D con Aspose.3D, assicurati di avere i seguenti prerequisiti:

- Libreria Aspose.3D per .NET: Verifica di avere installato la libreria Aspose.3D. Puoi scaricarla da [qui](https://releases.aspose.com/3d/net/).

- Ambiente di sviluppo integrato (IDE): Usa qualsiasi IDE compatibile con lo sviluppo .NET.

- Conoscenze di base di C#: Familiarizzati con i fondamenti del linguaggio di programmazione C#.

- Desiderio di esplorare il design 3D: Una passione per la creazione di modelli 3D visivamente sbalorditivi!

## Importare i namespace

Per avviare il tuo percorso di design 3D con Aspose.3D, dovrai importare i namespace necessari. Questo garantisce che il tuo codice possa accedere alle classi e alle funzionalità richieste.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Come creare una scena 3d con estrusione lineare

Di seguito percorriamo ogni passaggio necessario per costruire la scena, applicare l'estrusione e **salvare il modello 3d** come file OBJ. Le spiegazioni sono scritte in tono colloquiale così da poterle seguire facilmente.

### Passo 1: Inizializzare il profilo di base

Innanzitutto, definiamo la forma 2‑D che verrà estrusa. In questo caso un rettangolo con angoli arrotondati.

```csharp
// ExStart:InitializeBaseProfile
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
// ExEnd:InitializeBaseProfile
```

### Passo 2: Creare una scena 3D

Un oggetto `Scene` è il contenitore per tutta la geometria, le luci e le telecamere – il cuore della **creazione di una scena 3d**.

```csharp
// ExStart:Create3DScene
Scene scene = new Scene();
// ExEnd:Create3DScene
```

### Passo 3: Creare i nodi sinistro e destro

Aggiungiamo due nodi figlio alla radice della scena. Uno utilizzerà un numero basso di fette, l'altro un numero più alto, così potrai vedere la differenza visiva.

```csharp
// ExStart:CreateLeftRightNodes
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(15, 0, 0);
// ExEnd:CreateLeftRightNodes
```

### Passo 4: Eseguire l'estrusione lineare sul nodo sinistro

Qui estrudiamo il rettangolo con **2 fette**. Un numero minore di fette produce un aspetto più grezzo.

```csharp
// ExStart:LinearExtrusionLeftNode
left.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 2 });
// ExEnd:LinearExtrusionLeftNode
```

### Passo 5: Eseguire l'estrusione lineare sul nodo destro

Ora estrudiamo lo stesso profilo ma con **10 fette**, ottenendo una superficie più liscia.

```csharp
// ExStart:LinearExtrusionRightNode
right.CreateChildNode(new LinearExtrusion(profile, 2) { Slices = 10 });
// ExEnd:LinearExtrusionRightNode
```

### Passo 6: Salvare la scena 3D

Infine, esportiamo la scena in un file Wavefront OBJ. Questo dimostra **come salvare obj** e **esportare wavefront obj** usando Aspose.3D.

```csharp
// ExStart:Save3DScene
scene.Save("Your Output Directory" + "SlicesInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
// ExEnd:Save3DScene
```

## Problemi comuni e soluzioni

| Problema | Perché accade | Soluzione |
|----------|---------------|-----------|
| Il file OBJ appare vuoto | Il percorso di output è errato o mancano i permessi di scrittura. | Verifica che la directory esista e che l'applicazione abbia i permessi di scrittura. |
| Le fette non influenzano la levigatezza | Il valore `Slices` è troppo basso rispetto alle dimensioni della geometria. | Aumenta il numero di fette o regola le dimensioni del profilo. |
| Eccezione di licenza | Esecuzione senza licenza valida in una build non‑trial. | Applica una licenza temporanea o permanente usando `License license = new License(); license.SetLicense("Aspose.3D.lic");` |

## Domande frequenti

**D: Posso usare Aspose.3D per .NET con altri linguaggi di programmazione?**  
R: Aspose.3D è progettato principalmente per .NET, ma puoi esplorare opzioni di interoperabilità con linguaggi come Python usando binding .NET.

**D: Dove posso trovare la documentazione dettagliata per Aspose.3D per .NET?**  
R: Consulta la documentazione [qui](https://reference.aspose.com/3d/net/) per informazioni approfondite sulle capacità e sull'uso di Aspose.3D.

**D: È disponibile una versione di prova gratuita per Aspose.3D per .NET?**  
R: Sì, puoi ottenere la tua prova gratuita [qui](https://releases.aspose.com/) per esplorare le funzionalità della libreria prima di acquistare.

**D: Come posso ottenere supporto tecnico per Aspose.3D per .NET?**  
R: Visita il forum Aspose.3D [qui](https://forum.aspose.com/c/3d/18) per chiedere assistenza e interagire con la community.

**D: Posso usare una licenza temporanea per Aspose.3D per .NET?**  
R: Sì, ottieni una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/) per scopi di valutazione.

## Conclusione

Congratulazioni! Hai appreso con successo come **creare una scena 3d**, applicare un'estrusione lineare con un numero personalizzato di fette e **salvare il modello 3d** come file Wavefront OBJ usando Aspose.3D per .NET. Questo è solo l'inizio del tuo percorso di design 3D—sperimenta con diversi profili, valori di fette e formati di esportazione per sbloccare tutto il potenziale del **3d modeling c#**.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Ultimo aggiornamento:** 2026-01-09  
**Testato con:** Aspose.3D 24.11 per .NET  
**Autore:** Aspose