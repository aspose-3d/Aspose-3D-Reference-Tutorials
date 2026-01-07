---
date: 2026-01-07
description: Μάθετε πώς να κάνετε γραμμική εξώθηση ενός 2D προφίλ και να εξάγετε 3D
  μοντέλο OBJ χρησιμοποιώντας το Aspose.3D για .NET. Αυτό το σεμινάριο γραμμικής εξώθησης
  σας καθοδηγεί βήμα‑βήμα.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Πώς να κάνετε γραμμική εξώθηση με το Aspose.3D για .NET
url: /el/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# how to linear extrude με Aspose.3D for .NET

## Introduction

Καλώς ήρθατε στο **linear extrusion tutorial** μας! Σε αυτόν τον οδηγό θα ανακαλύψετε **how to linear extrude** ένα 2‑D προφίλ και να το μετατρέψετε σε ένα πλήρες 3‑D αντικείμενο χρησιμοποιώντας το Aspose.3D for .NET. Είτε δημιουργείτε μια εφαρμογή τύπου CAD είτε χρειάζεστε απλώς να **export 3d model obj** αρχεία για επεξεργασία, αυτή η βήμα‑βήμα περιήγηση θα σας δώσει την αυτοπεποίθηση να προσθέσετε ισχυρή δημιουργία γεωμετρίας στα έργα σας. Ακολουθήστε αυτόν τον οδηγό για να μάθετε how to linear extrude με πρακτικά παραδείγματα.

## Quick Answers
- **Τι είναι η linear extrusion;** Η επέκταση ενός 2‑D σχήματος κατά μήκος μιας ευθείας διαδρομής για δημιουργία 3‑D στερεού.  
- **Ποια βιβλιοθήκη χρησιμοποιούμε;** Aspose.3D for .NET.  
- **Χρειάζομαι άδεια;** Μια προσωρινή άδεια λειτουργεί για δοκιμές· απαιτείται πλήρης άδεια για παραγωγή.  
- **Μπορώ να εξάγω σε OBJ;** Ναι – η τελική σκηνή αποθηκεύεται ως αρχείο Wavefront OBJ.  
- **Πόσες γραμμές κώδικα;** Λιγότερες από 30 γραμμές C# συν επεξηγηματικά σχόλια.

## What is Linear Extrusion?

Η linear extrusion παίρνει ένα επίπεδο προφίλ (όπως ορθογώνιο ή κύκλο) και το «σουρώ» κατά μήκος μιας ευθείας γραμμής, με δυνατότητα προσθήκης περιστροφών, κλιμάκωσης ή μετατοπίσεων. Το αποτέλεσμα είναι ένα στερεό που μπορεί να αποδοθεί, να επεξεργαστεί ή να εξαχθεί για χρήση σε άλλα 3‑D εργαλεία.

## Why Use Aspose.3D for Linear Extrusion?

* **Zero‑dependency:** Δεν απαιτούνται εξωτερικοί CAD πυρήνες.  
* **Full .NET support:** Λειτουργεί με .NET Framework, .NET Core και .NET 5/6+.  
* **Export flexibility:** Αποθήκευση απευθείας σε OBJ, STL, FBX και πολλές άλλες μορφές.  
* **Rich API:** Έλεγχος slices, twist και offsets με λίγες μόνο ιδιότητες.

## Prerequisites

Πριν ξεκινήσετε, βεβαιωθείτε ότι έχετε:

1. **Aspose.3D installed** – κατεβάστε το από [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – ακολουθήστε τον οδηγό εγκατάστασης [here](https://reference.aspose.com/3d/net/).  
3. Ένα .NET περιβάλλον ανάπτυξης (Visual Studio, VS Code ή Rider) με τις απαιτούμενες namespaces.

## Import Namespaces

Συμπεριλάβετε τις απαραίτητες namespaces για να ενεργοποιήσετε τη λειτουργικότητα του Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Αυτές οι namespaces σας δίνουν πρόσβαση σε `Scene`, `LinearExtrusion`, `RectangleShape` και βοηθητικές κλάσεις όπως `Vector3`.

## Performing Linear Extrusion

Ακολουθεί η πλήρης ροή εργασίας. Κάθε βήμα εξηγείται με απλή γλώσσα πριν από το αντίστοιχο μπλοκ κώδικα, ώστε να μπορείτε να ακολουθήσετε χωρίς εικασίες.

### Step 1: Initialize the Base Profile

Αρχικά, δημιουργήστε το 2‑D σχήμα που θα εξαχθεί. Στο παράδειγμά μας χρησιμοποιούμε ένα ορθογώνιο με μικρή ακτίνα στρογγυλοποίησης.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Γιατί είναι σημαντικό:* Το προφίλ ορίζει τη διατομή του τελικού 3‑D αντικειμένου. Ρυθμίστε το `RoundingRadius`, το πλάτος ή το ύψος για διαφορετικές σιλουέτες.

### Step 2: Apply Linear Extrusion

Τώρα «σουρούμε» το προφίλ 10 μονάδες κατά τον άξονα Z, προσθέτοντας 100 slices για ομαλότητα, κεντράροντας τη γεωμετρία και εφαρμόζοντας πλήρη περιστροφή 360° με offset.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Συμβουλή:* Πειραματιστείτε με το `Slices` για ισορροπία απόδοσης‑ποιότητας, και δοκιμάστε το `Twist` για σπειροειδείς επιδράσεις.

### Step 3: Create a Scene

Ένα `Scene` λειτουργεί ως δοχείο για όλα τα 3‑D στοιχεία—σκεφτείτε το ως καμβά.

```csharp
Scene scene = new Scene();
```

### Step 4: Add the Extrusion to the Scene

Συνδέστε τη γεωμετρία extrusion στον ριζικό κόμβο της σκηνής ώστε να γίνει μέρος της ιεραρχίας απόδοσης.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Step 5: Save the 3‑D Model

Τέλος, εξάγετε τη σκηνή σε ένα ευρέως υποστηριζόμενο αρχείο OBJ. Αυτό δείχνει τη δυνατότητα **export 3d model obj** του Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Όταν ανοίξετε το παραγόμενο `LinearExtrusion.obj` σε οποιονδήποτε 3‑D προβολέα, θα δείτε ένα στρόβιλο ορθογώνιο πρίσμα—ακριβώς όπως περιγράφεται από τον κώδικα.

## Common Pitfalls & Tips

| Issue | Why it Happens | How to Fix |
|-------|----------------|------------|
| **Profile not visible** | Forgetting to add the extrusion to the scene. | Ensure `CreateChildNode` is called. |
| **Twist looks flat** | `Slices` too low, causing coarse geometry. | Increase `Slices` (e.g., 200) for smoother twist. |
| **Export fails** | Output folder does not exist or missing write permission. | Use `RunExamples.GetOutputFilePath` or create the directory manually. |
| **Unexpected scaling** | `Center` set to `false` shifts geometry. | Set `Center = true` unless you need an offset. |

## Frequently Asked Questions

### Q1: Is Aspose.3D suitable for beginners?

A1: Absolutely! Aspose.3D offers a user‑friendly API, and this tutorial walks you through the basics of linear extrusion.

### Q2: Can I use Aspose.3D for commercial projects?

A2: Yes, Aspose.3D comes with licensing options for both personal and commercial use. Check [here](https://purchase.aspose.com/buy) for details.

### Q3: How can I get temporary licenses for testing?

A3: Visit [this link](https://purchase.aspose.com/temporary-license/) for obtaining temporary licenses for testing purposes.

### Q4: Where can I find community support?

A4: Join the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) to connect with a vibrant community and seek assistance.

### Q5: Is there a free trial available?

A5: Certainly! Download the free trial version [here](https://releases.aspose.com/) to experience Aspose.3D's capabilities firsthand.

---

**Last Updated:** 2026-01-07  
**Tested With:** Aspose.3D 24.11 for .NET  
**Author:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}