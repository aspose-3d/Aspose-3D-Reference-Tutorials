---
title: Esportazione nel formato PLY come nuvola di punti
linktitle: Esportazione nel formato PLY come nuvola di punti
second_title: API Aspose.3D .NET
description: Esplora il mondo della modellazione 3D con Aspose.3D per .NET. Impara a esportare modelli nel formato PLY senza sforzo. Migliora i tuoi progetti con immagini straordinarie.
weight: 16
url: /it/net/loading-and-saving/ply/export-to-ply-point-cloud/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Esportazione nel formato PLY come nuvola di punti

## introduzione
Nel dinamico mondo della modellazione e dello sviluppo 3D, Aspose.3D per .NET si distingue come un potente toolkit. Questo tutorial ti guiderà attraverso il processo di esportazione di modelli 3D in formato PLY come nuvola di punti utilizzando Aspose.3D per .NET. Se sei pronto a migliorare i tuoi progetti con immagini straordinarie, segui e sblocca tutto il potenziale di questa versatile libreria.
## Prerequisiti
Prima di immergerti nel tutorial, assicurati di disporre dei seguenti prerequisiti:
-  Aspose.3D per .NET: scarica e installa la libreria da[pagina di download](https://releases.aspose.com/3d/net/).
- Ambiente di sviluppo: configura il tuo ambiente di sviluppo .NET preferito, come Visual Studio.
## Importa spazi dei nomi
Per iniziare con Aspose.3D per .NET, importa gli spazi dei nomi necessari nel tuo progetto:
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```
## Passaggio 1: crea un modello 3D
Inizia creando un modello 3D che desideri esportare come nuvola di punti. Ad esempio, creiamo una sfera:
```csharp
Sphere sphere = new Sphere();
```
## Passaggio 2: definire le impostazioni di esportazione
Specifica le impostazioni di esportazione, incluso il formato file (PLY) e abilita l'esportazione della nuvola di punti:
```csharp
PlySaveOptions saveOptions = new PlySaveOptions() { PointCloud = true };
```
## Passaggio 3: imposta il percorso di esportazione
Determina la directory in cui desideri salvare il file PLY esportato:
```csharp
string exportPath = "Your Document Directory" + "sphere.ply";
```
## Passaggio 4: codifica ed esportazione
 Utilizza il`Encode` metodo per esportare il modello 3D in formato PLY:
```csharp
FileFormat.PLY.Encode(sphere, exportPath, saveOptions);
```
## Conclusione
Congratulazioni! Hai esportato con successo un modello 3D in formato PLY come nuvola di punti utilizzando Aspose.3D per .NET. Ciò apre infinite possibilità per integrare immagini coinvolgenti nelle tue applicazioni.

## Domande frequenti
### 1. Aspose.3D è compatibile con tutti i framework .NET?
Aspose.3D supporta vari framework .NET, garantendo la compatibilità con un'ampia gamma di ambienti di sviluppo.
### 2. Posso utilizzare Aspose.3D per progetti commerciali?
 Assolutamente! Aspose.3D offre opzioni di licenza flessibili, incluso l'uso commerciale. Dai un'occhiata a[pagina di acquisto](https://purchase.aspose.com/buy) per dettagli.
### 3. Come posso ottenere supporto per Aspose.3D?
 Visitare il[Forum Aspose.3D](https://forum.aspose.com/c/3d/18) per connettersi con la comunità e ottenere assistenza da esperti.
### 4. È disponibile una prova gratuita?
 Sì, esplora le funzionalità con a[prova gratuita](https://releases.aspose.com/) prima di prendere un impegno.
### 5. Come posso ottenere una licenza temporanea?
 Per le opzioni di licenza temporanea, visitare[questo link](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
