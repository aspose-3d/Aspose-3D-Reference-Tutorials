---
title: Μετασχηματισμός κόμβου με μήτρα μετασχηματισμού σε τρισδιάστατες σκηνές
linktitle: Μετασχηματισμός κόμβου με μήτρα μετασχηματισμού σε τρισδιάστατες σκηνές
second_title: Aspose.3D .NET API
description: Μεταμορφώστε τους κόμβους χωρίς κόπο σε σκηνές 3D χρησιμοποιώντας το Aspose.3D για .NET. Μάθετε βήμα προς βήμα μετασχηματισμούς κόμβων με σεμινάριο.
type: docs
weight: 21
url: /el/net/geometry-and-hierarchy/transformation-node-matrix/
---
## Εισαγωγή

Στη δυναμική σφαίρα των τρισδιάστατων γραφικών και των απεικονίσεων, η ικανότητα χειρισμού αντικειμένων μέσα σε μια σκηνή είναι μια κρίσιμη πτυχή. Το Aspose.3D for .NET δίνει τη δυνατότητα στους προγραμματιστές να μετασχηματίζουν απρόσκοπτα κόμβους χρησιμοποιώντας πίνακες μετασχηματισμού, προσθέτοντας ένα επίπεδο δημιουργικότητας και ελέγχου σε 3D σκηνές. Αυτό το σεμινάριο θα σας καθοδηγήσει στη διαδικασία μετατροπής ενός κόμβου σε μια τρισδιάστατη σκηνή βήμα προς βήμα.

## Προαπαιτούμενα

Πριν ξεκινήσετε το σεμινάριο, βεβαιωθείτε ότι έχετε τις ακόλουθες προϋποθέσεις:

1.  Aspose.3D for .NET Library: Βεβαιωθείτε ότι έχετε εγκαταστήσει τη βιβλιοθήκη Aspose.3D στο έργο σας .NET. Μπορείτε να το κατεβάσετε[εδώ](https://releases.aspose.com/3d/net/).

2. Περιβάλλον ανάπτυξης: Ρυθμίστε ένα λειτουργικό περιβάλλον ανάπτυξης .NET και αν δεν το έχετε κάνει ήδη, δημιουργήστε ένα νέο έργο όπου θα εφαρμόσετε τους μετασχηματισμούς.

## Εισαγωγή χώρων ονομάτων

Ξεκινήστε εισάγοντας τους απαραίτητους χώρους ονομάτων στο έργο σας .NET. Αυτοί οι χώροι ονομάτων παρέχουν τις βασικές κλάσεις και μεθόδους για τον χειρισμό τρισδιάστατης σκηνής.

```csharp
using System;
using System.Collections.Generic;
using System.IO;
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
```

Τώρα που καλύψαμε τα βασικά, ας αναλύσουμε τη διαδικασία μετασχηματισμού σε έναν οδηγό βήμα προς βήμα.

## Βήμα 1: Αρχικοποίηση σκηνής και κόμβου

```csharp
// ExStart:AddTransformationToNodeByTransformationMatrix
// Αρχικοποίηση αντικειμένου σκηνής
Scene scene = new Scene();

// Αρχικοποίηση αντικειμένου κλάσης κόμβου
Node cubeNode = new Node("cube");
```

Σε αυτό το βήμα, δημιουργούμε μια νέα τρισδιάστατη σκηνή και έναν κόμβο με το όνομα "cube" εντός αυτής της σκηνής.

## Βήμα 2: Δημιουργήστε Mesh και ορίστε τη γεωμετρία

```csharp
// Καλέστε Common class δημιουργία πλέγματος χρησιμοποιώντας τη μέθοδο δημιουργίας πολυγώνων για να ορίσετε την παρουσία πλέγματος
Mesh mesh = Common.CreateMeshUsingPolygonBuilder(); 

// Σημειώστε τον κόμβο στη γεωμετρία του Mesh
cubeNode.Entity = mesh;
```

Εδώ, δημιουργούμε ένα πλέγμα χρησιμοποιώντας τη μέθοδο δημιουργίας πολυγώνων και το εκχωρούμε στον κόμβο, καθιερώνοντας τη γεωμετρία για τον κύβο μας.

## Βήμα 3: Ορίστε προσαρμοσμένη μήτρα μετάφρασης

```csharp
// Ορισμός προσαρμοσμένης μήτρας μετάφρασης
cubeNode.Transform.TransformMatrix = new Matrix4(
    1, -0.3, 0, 0,
    0.4, 1, 0.3, 0,
    0, 0, 1, 0,
    0, 20, 0, 1
);        
```

Ορίστε μια προσαρμοσμένη μήτρα μετάφρασης για να προσδιορίσετε τον συγκεκριμένο μετασχηματισμό που εφαρμόζεται στον κόμβο. Προσαρμόστε τις τιμές του πίνακα όπως απαιτείται για τον επιθυμητό μετασχηματισμό.

## Βήμα 4: Προσθήκη κόμβου στη σκηνή

```csharp
// Προσθέστε κύβο στη σκηνή
scene.RootNode.ChildNodes.Add(cubeNode);            
```

Συμπεριλάβετε τον κόμβο κύβου στη σκηνή, καθιστώντας τον μέρος του συνολικού τρισδιάστατου περιβάλλοντος.

## Βήμα 5: Αποθηκεύστε τη σκηνή

```csharp
// Η διαδρομή προς τον κατάλογο εγγράφων.
var output = "Your Output Directory" + "TransformationToNode.fbx";

//Αποθηκεύστε τη σκηνή 3D στις υποστηριζόμενες μορφές αρχείων
scene.Save(output, FileFormat.FBX7500ASCII);
// ExEnd:AddTransformationToNodeByTransformationMatrix
Console.WriteLine("\nTransformation added successfully to node.\nFile saved at " + output);
```

Καθορίστε τον κατάλογο εξόδου και το όνομα αρχείου και, στη συνέχεια, αποθηκεύστε τη σκηνή 3D στην επιθυμητή μορφή αρχείου. Σε αυτό το παράδειγμα, το αποθηκεύουμε στη μορφή FBX7500ASCII.

## συμπέρασμα

Συγχαρητήρια! Μεταμορφώσατε με επιτυχία έναν κόμβο χρησιμοποιώντας μια μήτρα μετασχηματισμού σε μια τρισδιάστατη σκηνή με το Aspose.3D για .NET. Αυτή η δυνατότητα ανοίγει πόρτες σε ποικίλες και οπτικά σαγηνευτικές εφαρμογές 3D.

## Συχνές ερωτήσεις

### Ε1: Τι είναι μια μήτρα μετασχηματισμού στα τρισδιάστατα γραφικά;

A1: Ένας πίνακας μετασχηματισμού είναι μια μαθηματική αναπαράσταση που χρησιμοποιείται για την εφαρμογή διαφόρων μετασχηματισμών (μετάφραση, περιστροφή, κλιμάκωση) σε αντικείμενα στον τρισδιάστατο χώρο.

### Ε2: Μπορώ να εφαρμόσω πολλαπλούς μετασχηματισμούς σε έναν μόνο κόμβο;

A2: Ναι, μπορείτε να συνδυάσετε πολλούς μετασχηματισμούς πολλαπλασιάζοντας τους αντίστοιχους πίνακές τους και εφαρμόζοντας το αποτέλεσμα στον κόμβο.

### Ε3: Υπάρχουν άλλες υποστηριζόμενες μορφές αρχείων για την αποθήκευση τρισδιάστατων σκηνών;

 A3: Το Aspose.3D για .NET υποστηρίζει διάφορες μορφές αρχείων, συμπεριλαμβανομένων των STL, GLTF, OBJ και άλλων. Αναφέρομαι στο[τεκμηρίωση](https://reference.aspose.com/3d/net/) για μια ολοκληρωμένη λίστα.

### Ε4: Πώς μπορώ να αποκτήσω μια προσωρινή άδεια χρήσης για το Aspose.3D για .NET;

 A4: Επισκεφθείτε το[σελίδα προσωρινής άδειας](https://purchase.aspose.com/temporary-license/) στον ιστότοπο Aspose για να αποκτήσετε προσωρινή άδεια για σκοπούς αξιολόγησης.

### Ε5: Πού μπορώ να αναζητήσω βοήθεια ή να συνδεθώ με την κοινότητα Aspose.3D;

A5: Επισκεφθείτε το[Aspose.3D φόρουμ](https://forum.aspose.com/c/3d/18) για να κάνετε ερωτήσεις, να μοιραστείτε εμπειρίες και να συνδεθείτε με άλλους προγραμματιστές χρησιμοποιώντας το Aspose.3D.