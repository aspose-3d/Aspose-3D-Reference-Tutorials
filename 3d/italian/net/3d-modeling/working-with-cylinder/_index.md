---
date: 2026-01-12
description: Scopri come creare un cilindro di taglio inferiore e come esportare un
  modello 3D in formato OBJ usando Aspose.3D per .NET. Segui questa guida passo‑passo
  per padroneggiare la modellazione 3D.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Come creare un cilindro con base tagliata con Aspose.3D per .NET
url: /it/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cilindro con Base Inclinata Personalizzata

## Introduzione
Benvenuti alla nostra guida completa in cui **imparerete a creare modelli di cilindro con base inclinata** con Aspose.3D per .NET. Che stiate realizzando un asset per un gioco, un componente meccanico o una demo visiva, questo tutorial vi mostra esattamente come modellare la base di un cilindro, applicare un taglio e infine **esportare il file OBJ del modello 3D** per l'uso in qualsiasi pipeline successiva. Seguiamo passo passo, così potrete iniziare a produrre geometrie personalizzate in pochi minuti.

## Risposte Rapide
- **Che cos’è un cilindro con base inclinata?** Un cilindro la cui faccia inferiore è inclinata (tagliata) anziché piatta.  
- **Quale libreria viene usata?** Aspose.3D per .NET.  
- **Come si esporta il modello?** Utilizzate `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **È necessaria una licenza?** È disponibile una versione di prova; per la produzione è richiesta una licenza commerciale.  
- **Quali sono i prerequisiti?** Ambiente di sviluppo .NET e il pacchetto NuGet Aspose.3D.

## Che cos’è un cilindro con base inclinata?
Un cilindro con base inclinata è una mesh cilindrica standard la cui faccia inferiore è stata trasformata mediante un’operazione di shear. Questo consente di creare basi angolate, rampe o connettori personalizzati senza dover modificare manualmente i vertici.

## Perché usare Aspose.3D per questo compito?
- **Controllo totale** sui parametri della geometria (raggio, altezza, segmenti).  
- **Supporto integrato al shear** tramite la proprietà `ShearBottom`, evitando manipolazioni mesh a basso livello.  
- **Esportazione con un click** nei formati più popolari come OBJ, FBX e STL, rendendo l’integrazione con altri strumenti fluida.

## Prerequisiti
Prima di iniziare, assicuratevi di avere:

- Conoscenze di base di C# e .NET.  
- Aspose.3D per .NET installato. Potete scaricarlo **[qui](https://releases.aspose.com/3d/net/)**.  
- Un IDE compatibile con .NET (Visual Studio, Rider o VS Code).

## Importare i Namespace
Nel vostro file C#, iniziate importando i namespace necessari:

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

## Passo 1: Creare una Scena
Prima, istanziate una nuova scena 3‑D che conterrà tutti i nostri oggetti.

```csharp
Scene scene = new Scene();
```

## Passo 2: Creare Cilindro 1
Create il cilindro principale che personalizzeremo con una base inclinata.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Passo 3: Personalizzare la Base Inclinata per Cilindro 1
Applicate il shear, abilitate la generazione del fan e regolate le altre proprietà per ottenere la forma desiderata.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## Passo 4: Aggiungere Cilindro 1 alla Scena
Posizionate il cilindro personalizzato nella scena e spostatelo leggermente a destra così da poter vedere entrambi gli oggetti fianco a fianco.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Passo 5: Creare Cilindro 2
Create un secondo cilindro semplice per il confronto.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Passo 6: Aggiungere Cilindro 2 alla Scena
Aggiungete il secondo cilindro senza alcun shear personalizzato—questo aiuta a illustrare l’effetto dei passaggi precedenti.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Passo 7: Salvare la Scena
Infine, esportate l’intera scena come file OBJ così da poterla aprire in Blender, Maya o qualsiasi altro visualizzatore 3‑D.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Problemi Comuni & Consigli
- **Valori di shear**: il `Vector2` accetta i fattori di shear X e Y. Un valore di `0.83` corrisponde a circa 47,5°, ma potete regolarlo per ottenere angoli diversi.  
- **Percorso di esportazione**: assicuratevi che la cartella specificata esista e che abbiate i permessi di scrittura; altrimenti `scene.Save` genererà un’eccezione.  
- **Prestazioni**: per cilindri con un numero molto alto di segmenti, considerate di ridurre il conteggio dei segmenti (`20` nell’esempio) per mantenere gestibile la dimensione del file OBJ.

## Domande Frequenti

### Aspose.3D per .NET è adatto ai principianti?
Assolutamente sì! Aspose.3D per .NET offre un’API intuitiva, accessibile sia ai principianti sia agli sviluppatori esperti.

### Posso applicare angoli di shear diversi ai cilindri?
Sì, potete personalizzare la proprietà `ShearBottom` per ciascun cilindro in modo indipendente, ottenendo effetti unici.

### È disponibile una versione di prova?
Sì, potete provare la versione gratuita **[qui](https://releases.aspose.com/)**.

### Dove posso trovare supporto aggiuntivo?
Visitate il **[forum di Aspose.3D](https://forum.aspose.com/c/3d/18)** per supporto della community e discussioni.

### Come posso ottenere una licenza temporanea?
Ottenete la vostra licenza temporanea **[qui](https://purchase.aspose.com/temporary-license/)**.

**Domande & Risposte Aggiuntive**

**D: Come cambio il formato di esportazione in FBX?**  
R: Sostituite `FileFormat.WavefrontOBJ` con `FileFormat.FBX` nella chiamata a `scene.Save`.

**D: Posso animare il cilindro dopo l’esportazione?**  
R: OBJ non supporta animazioni; usate FBX o GLTF se avete bisogno di dati animati.

**D: E se avessi bisogno di un raggio di cilindro più grande?**  
R: Modificate i primi due parametri del costruttore `Cylinder` (es. `new Cylinder(4, 4, …)`).

## Conclusione
Ora avete imparato a **creare modelli di cilindro con base inclinata** ed esportarli come file OBJ usando Aspose.3D per .NET. Sperimentate con diversi valori di shear, conteggi di segmenti e formati di esportazione per adattarli alle esigenze del vostro progetto. Buon modellismo!

---

**Ultimo aggiornamento:** 2026-01-12  
**Testato con:** Aspose.3D per .NET 24.11 (ultima versione al momento della stesura)  
**Autore:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}