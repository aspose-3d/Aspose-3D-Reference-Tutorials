---
date: 2026-01-22
description: Μάθετε πώς να δημιουργήσετε κόμβο‑παιδί και να προσθέσετε κόμβο μετασχηματισμού
  χρησιμοποιώντας γωνίες Euler με το Aspose.3D για .NET. Ακολουθήστε τον βήμα‑βήμα
  οδηγό μας για εντυπωσιακά αποτελέσματα.
linktitle: Create Child Node and Transform by Euler Angles
second_title: Aspose.3D .NET API
title: Δημιουργία παιδικού κόμβου και μετασχηματισμός με γωνίες Euler
url: /el/net/geometry-and-hierarchy/transformation-node-euler-angles/
weight: 19
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Μετασχηματισμός Node με Γωνίες Euler

## Εισαγωγή

Καλώς ήρθατε σε αυτό το ολοκληρωμένο tutorial σχετικά με **πώς να δημιουργήσετε child node** και να μετασχηματίζετε nodes με γωνίες Euler σε 3D σκηνές χρησιμοποιώντας το Aspose.3D for .NET. Σε αυτόν τον οδηγό, θα εξετάσουμε γιατί η προσθήκη ενός transformation node είναι σημαντική, θα περάσουμε βήμα‑βήμα από κάθε διαδικασία και θα σας δείξουμε πώς να **αποθηκεύσετε τη σκηνή ως FBX** για χρήση σε άλλα εργαλεία.

## Γρήγορες Απαντήσεις
- **Τι σημαίνει “create child node”;** Δημιουργεί ένα νέο node κάτω από έναν υπάρχοντα γονέα στο γράφημα σκηνής.  
- **Σε ποια μορφή μπορώ να εξάγω;** Χρησιμοποιήστε `scene.Save` για **να αποθηκεύσετε τη σκηνή ως FBX** (ή άλλες υποστηριζόμενες μορφές).  
- **Χρειάζομαι άδεια;** Ναι, απαιτείται έγκυρη άδεια Aspose.3D για παραγωγ 3 childου αντικειμένου `Node` στην ιεραρχία μιας υπάρχουσας σκηνής. Αυτό το child κληρονομεί τους μετασχηματισμούς από τον γονέα του, επιτρέποντάς σας να χτίσετε σύνθετες δομές όπως ρομποτικούς βραχίονες, συναρμολογήσεις οχημάτων ή UI overlay.

## Γιατί να προσθέσετε ένα transformation node;
Η εφαρμογή γωνιών Euler ή άλλων μετασχηματισμών απευθείας σε ένα node σας δίνει ακριβή έλεγχο πάνω στην προσανατολισμό, θέση και κλίμακα. Είναι ο πιο απλός τρόπος για να αναπαράγετε ή να μετακινήσετε αντικείμενα χωρίς να τροποποιήσετε τα υποκείμενα δεδομένα του mesh.

## Προαπαιτούμενα

- Aspose.3D for .NET Library: Βεβαιωθείτε ότι έχετε εγκαταστήσει τη βιβλιοθήκη Aspose.3D. Μπορείτε να τη κατεβάσετε [εδώ](https://releases.aspose.com/3d/net/).
- Περιβάλλον Ανάπτυξης: Ρυθμίστε το προτιμώμενο .NET περιβάλλον ανάπτυξης, όπως το Visual Studio.

## Εισαγ να έχετε πρόσβαση στη λειτουργικότητα που παρέχει το Aspose.3D for .NET:

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Τώρα, ας αναλύσουμε το παράδειγμα σε πολλαπλά βήματα για καλύτερη κατανόηση.

## Πώς να δημιουργήσετε child node

### Βήμα 1: Αρχικοποίηση Αντικειμένου Scene

```csharp
// ExStart:AddTransformationToNodeByEulerAngles
// Initialize scene object
Scene scene = new Scene();
```

Ξεκινήστε δημιουργώντας μια νέα 3D σκηνή χρησιμοποιώντας την κλάση `Scene`.

### Βήμα 2: Δημιουργία Mesh με primitive Box

```csharp
// Call Common class create mesh using polygon builder method to set mesh instance 
Mesh mesh = (new Box()).ToMesh();
```

Κληθείτε μια μέθοδο (σε αυτήν την περίπτωση, `CreateMeshUsingPolygonBuilder` από μια προσαρμοσμένη κλάση `Common`) για να δημιουργήσετε ένα mesh για το 3D αντικείμενο.

### Βήμα 3: Δημιουργία container node για το mesh

```csharp
// Point node to the Mesh geometry
Node cubeNode = scene.RootNode.CreateChildNode(mesh);
```

Δημιουργήστε ένα node μέσα στη σκηνή χρησιμοποιώντας την κλάση `Node`. Αυτό το node θα λειτουργήσει ως container για το 3D αντικείμενό μας.

### Βήμα 4: Ορισμός Euler Angles και Translation (προσθήκη transformation node)

```csharp
// Euler angles
cubeNode.Transform.EulerAngles = new Vector3(0.3, 0.1, -0.5);            
// Set translation
cubeNode.Transform.Translation = new Vector3(0, 0, 20);
```

Ορίστε τις γωνίες Euler και τηδώ είναι που **προσθέτουμε δεδομένα transformation node**.

### Βήμα 5: Αποθήκευση της 3D Σκηνής (αποθήκευση σκηνής ως FBX)

```csharp
// The path to the documents directory.
var output = "TransformationToNode.fbx";

// Save 3D scene in the supported file formats
scene.Save(output);
// ExEnd:AddTransformationToNodeByEulerAngles
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Καθορίστε τον φάκελο εξόδου και **αποθηκεύστε τη σκηνή ως FBX** (ή οποιαδήποτε άλλη υποστηριζόμενη μορφή) χρησιμοποιώντας `scene.Save`.

## Συνηθισμένα Προβλήματα και Λύσεις
- ** με σειρά Z‑Y‑X. Αν το αντικείμενο φαίνεται στριμωγμένο, προσαρμόστε τη σειρά ή χρησιμοποιήστε quaternions.
- **Node δεν είναι ορατό:** Βεβαιωθείτε ότι η κάμερα είναι τοποθετημένη ώστε να βλέπει το μετατοπισμένο node (π.χ., `Translation = new Vector3(0,0,20)` το μετακινεί προς τα εμπρός).
- **Αποτυχία αποθήκευσης αρχείου:** Ελέγξτε τα δικαιώματα εγγραφής για το φάκελο προορισμού και ότι η κατάληξη αρχείου ταιριάζει με μια υποστηριζόμενη μορφή.

## Συχνές Ερωτήσεις

**Ε: Είναι το Aspose.3D συμβατό με άλλα εργαλεία 3D μοντελοποίησης;**  
Α: Το Aspose.3D υποστηρίζει διάφορες μορφές 3D αρχείων, ενισχύοντας τη συμβατότητα με δημοφιλή εργαλεία μοντελοποίησης.

**Ε: Μπορώ να εφαρμόσω πολλαπλούς μετασχηματισμούς σε ένα μόνο node;**  
Α: Ναι, μπορείτε να συνδυάσετε και να εφαρμόσετε πολλαπλούς μετασχηματισμούς για να πετύχετε σύνθετα εφέ.

**Ε: Πού μπορώ να βρω επιπλέον τεκμηρίωση για το Aspose.3D;**  
Α: Ανατρέξτε στην [τεκμηρίωση](https://reference.aspose.com/3d/net/) για λεπτομερείς πληροφορίες και παραδείγματα.

**Ε: Χρειάζομαι άδεια για χρήση του Aspose.3D for .NET;**  
Α: Ναι, μπορείτε να αποκτήσετε άδεια [εδώ](https://purchase.aspose.com/buy) ή να δοκιμάσετε μια [δωρεάν δοκιμή](https://releases.aspose.com/).

**Ε: Χρειάζεστε βοήθεια ή έχετε συγκεκριμένες ερωτήσεις;**  
Α: Επισκεφθείτε το [φόρουμ Aspose.3D](https://forum.aspose.com/c/3d/18) για υποστήριξη από την κοινότητα.

## Συμπέρασμα

Συγχαρητήρια! Έχετε μάθει με επιτυχία πώς να **δημιουργήσετε child node** και **προσθέσετε transformation node** χρησιμοποιώντας γωνίες Euler, και στη συνέχεια **να αποθηκεύσετε τη σκηνή ως FBX** με το Aspose.3D for .NET. Αυτή η ισχυρή βιβλιοθήκη ανοίγει το δρόμο για ατελείωτες δυνατότητες στην ανάπτυξη 3D γραφικών.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Τελευταία ενημέρωση:** 2026-01-22  
**Δοκιμή με:** Aspose.3D 24.12 for .NET  
**Συγγραφέας:** Aspose  

---