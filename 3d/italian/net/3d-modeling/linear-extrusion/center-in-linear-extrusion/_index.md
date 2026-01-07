---
date: 2026-01-07
description: Scopri come aggiungere un piano di appoggio durante l'estrusione lineare
  con Aspose.3D per .NET ed esportare file Wavefront OBJ. Padroneggia le tecniche
  di centratura e di ancoraggio nel modellismo 3‑D.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: Aggiungi piano di riferimento e centro nell'estrusione lineare
url: /it/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Aggiungere Piano di Base e Centrare nell'Estrusione Lineare

## Introduzione

Benvenuti a questa guida completa per padroneggiare l'estrusione lineare usando Aspose.3D per .NET. Se desideri **aggiungere un piano di base** ai tuoi modelli e **esportare file Wavefront OBJ** mantenendo l'estrusione centrata, sei nel posto giusto. In questo tutorial approfondiremo la tecnica dell'estrusione lineare, concentrandoci in particolare sull'aspetto del centramento e su come un piano di base ti aiuti a visualizzare il risultato più chiaramente.

## Risposte Rapide
- **Cosa ottieni aggiungendo “piano di base”?** Fornisce un riferimento visivo che rende facile vedere dove l'estrusione si trova sul piano X‑Z.  
- **Quale formato viene usato per esportare il modello?** La scena viene salvata come file Wavefront OBJ (`FileFormat.WavefrontOBJ`).  
- **È necessaria una licenza per eseguire il codice?** Una versione di prova gratuita è sufficiente per lo sviluppo; è richiesta una licenza permanente per la produzione.  
- **Posso modificare la lunghezza dell'estrusione?** Sì – modifica il secondo parametro di `LinearExtrusion`.  
- **Il centramento è opzionale?** Impostando `Center = true` l'estrusione viene centrata attorno al profilo; `false` la allinea a un lato.

## Prerequisiti

Prima di intraprendere questo entusiasmante percorso, assicurati di avere i seguenti prerequisiti:

- Conoscenza di base del linguaggio di programmazione C#.  
- Visual Studio installato sulla tua macchina.  
- Libreria Aspose.3D per .NET, che puoi scaricare dalla [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/).  
- Assicurati di avere accesso alla [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/) per riferimento durante tutto il tutorial.

## Importare Namespace

Per iniziare, importiamo i namespace necessari. Questi costituiranno la base del nostro capolavoro di modellazione 3D.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## Passo 1: Inizializzare il Profilo Base

Iniziamo definendo un profilo rettangolare che verrà estruso. Il `RoundingRadius` aggiunge un leggero raccordo agli angoli.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## Passo 2: Creare una Scena 3D

Un oggetto `Scene` funge da contenitore per tutta la geometria, le luci e le telecamere.

```csharp
Scene scene = new Scene();
```

## Passo 3: Creare Nodi Sinistro e Destro

Due nodi fratelli vengono creati sotto la radice. Uno dimostrerà l'estrusione **senza** centramento, l'altro **con** centramento. Trasliamo inoltre il nodo sinistro affinché i due esempi non si sovrappongano.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## Passo 4: Eseguire l'Estrusione Lineare sul Nodo Sinistro (Nessun Centro)

Qui estrudiamo il profilo senza centramento. Nota la proprietà `Center = false`.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## Passo 5: Aggiungere Piano di Base per Riferimento (Nodo Sinistro)

L'aggiunta di una scatola sottile funge da **piano di base** così da vedere chiaramente come l'estrusione si posizioni sulla base.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## Passo 6: Eseguire l'Estrusione Lineare sul Nodo Destro (Con Centro)

Ora estrudiamo lo stesso profilo ma abilitiamo il centramento. La geometria sarà posizionata in modo simmetrico attorno all'origine del profilo.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## Passo 7: Aggiungere Piano di Base per Riferimento (Nodo Destro)

Un secondo piano di base viene aggiunto al nodo destro per mantenere coerente il confronto visivo.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## Passo 8: Esportare File Wavefront OBJ

Infine, **esportiamo Wavefront OBJ** così il risultato può essere aperto in qualsiasi visualizzatore 3‑D standard.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## Perché Aggiungere un Piano di Base?

Aggiungere un piano di base ti fornisce un'indicazione visiva immediata sull'altezza e l'allineamento dell'estrusione. È particolarmente utile quando devi confrontare risultati centrati vs. non centrati, come dimostrato in questo tutorial.

## Problemi Comuni & Suggerimenti

- **Piano di base non visibile:** Assicurati che lo spessore del piano (`0.01` nel costruttore `Box`) sia sufficientemente piccolo da non oscurare l'estrusione ma abbastanza grande da essere renderizzato.  
- **Esportazione fallita:** Verifica che la cartella di destinazione esista e che tu abbia i permessi di scrittura.  
- **L'estrusione centrata appare spostata:** Ricontrolla la proprietà `Center`; `true` centra il profilo, `false` lo allinea a un lato.

## Domande Frequenti

### Q1: Posso usare Aspose.3D per .NET con altri linguaggi di programmazione?

A1: Aspose.3D supporta principalmente linguaggi .NET come C# e VB.NET.

### Q2: Dove posso trovare supporto per domande relative ad Aspose.3D?

A2: Visita il [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) per supporto dedicato e discussioni.

### Q3: È disponibile una versione di prova gratuita per Aspose.3D per .NET?

A3: Sì, puoi accedere alla prova gratuita [qui](https://releases.aspose.com/).

### Q4: Come posso ottenere una licenza temporanea per Aspose.3D per .NET?

A4: Puoi acquisire una licenza temporanea [qui](https://purchase.aspose.com/temporary-license/).

### Q5: Dove posso acquistare la licenza di Aspose.3D per .NET?

A5: Acquista la tua licenza [qui](https://purchase.aspose.com/buy).

### Q6: Posso esportare la scena in altri formati oltre a OBJ?

A6: Sì, Aspose.3D supporta molti formati come STL, FBX e GLTF. Basta cambiare il valore dell'enumerazione `FileFormat` nel metodo `Save`.

### Q7: Come modifico il numero di slice dell'estrusione?

A7: Regola la proprietà `Slices` nel costruttore `LinearExtrusion` per controllare la densità della mesh.

---

**Ultimo aggiornamento:** 2026-01-07  
**Testato con:** Aspose.3D per .NET ultima versione  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}