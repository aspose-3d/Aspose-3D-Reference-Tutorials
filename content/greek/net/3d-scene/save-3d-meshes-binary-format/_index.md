---
title: Αποθήκευση τρισδιάστατων ματιών σε προσαρμοσμένη δυαδική μορφή
linktitle: Αποθήκευση τρισδιάστατων ματιών σε προσαρμοσμένη δυαδική μορφή
second_title: Aspose.3D .NET API
description: Εξερευνήστε τον κόσμο του 3D με το Aspose.3D για .NET. Μάθετε να αποθηκεύετε πλέγματα σε προσαρμοσμένη δυαδική μορφή.
type: docs
weight: 13
url: /el/net/3d-scene/save-3d-meshes-binary-format/
---
## Εισαγωγή

Καλώς ήρθατε στον κόσμο του Aspose.3D for .NET, μιας ισχυρής βιβλιοθήκης που δίνει τη δυνατότητα στους προγραμματιστές να εργάζονται με αρχεία 3D χωρίς κόπο. Σε αυτό το σεμινάριο, θα εμβαθύνουμε στη διαδικασία αποθήκευσης δικτύων 3D σε προσαρμοσμένη δυαδική μορφή χρησιμοποιώντας το Aspose.3D για .NET. Αυτός ο οδηγός προϋποθέτει ότι έχετε βασική κατανόηση της C# και είστε εξοικειωμένοι με τη βιβλιοθήκη Aspose.3D.

## Προαπαιτούμενα

Πριν προχωρήσουμε στο σεμινάριο, βεβαιωθείτε ότι έχετε τα εξής:

-  Aspose.3D για .NET: Βεβαιωθείτε ότι έχετε εγκαταστήσει τη βιβλιοθήκη Aspose.3D. Μπορείτε να το κατεβάσετε από[εδώ](https://releases.aspose.com/3d/net/).

- Περιβάλλον ανάπτυξης: Ρυθμίστε το προτιμώμενο περιβάλλον ανάπτυξης C#, όπως το Visual Studio.

- Εισαγωγή αρχείου 3D: Έχετε ένα αρχείο 3D (π.χ. test.fbx) που θέλετε να μετατρέψετε σε προσαρμοσμένη δυαδική μορφή.

## Εισαγωγή χώρων ονομάτων

Στον κώδικα C#, συμπεριλάβετε τους απαραίτητους χώρους ονομάτων για πρόσβαση στις λειτουργίες Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
```

## Βήμα 1: Φορτώστε ένα αρχείο 3D

Φορτώστε το αρχείο 3D χρησιμοποιώντας το Aspose.3D. Σε αυτό το παράδειγμα, φορτώνουμε ένα αρχείο με το όνομα "test.fbx":

```csharp
Scene scene = Scene.FromFile("test.fbx");
```

## Βήμα 2: Ορισμός προσαρμοσμένης δυαδικής μορφής

Καθορίστε τη δομή της προσαρμοσμένης δυαδικής μορφής στην οποία θέλετε να αποθηκεύσετε τα τρισδιάστατα πλέγματα. Το παράδειγμα χρησιμοποιεί μια δομή με στοιχεία MeshBlock, Vertex και Triangle.

```csharp
// Η διάταξη μνήμης μιας κορυφής είναι
// float[3] θέση?
// float[3] normal?
// float[3] uv;
var vertexDeclaration = new VertexDeclaration();
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Position);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.Normal);
vertexDeclaration.AddField(VertexFieldDataType.FVector3, VertexFieldSemantic.UV);

```

## Βήμα 3: Ανοίξτε το Αρχείο για εγγραφή

Ανοίξτε ένα δυαδικό αρχείο για εγγραφή, όπου θα αποθηκευτούν τα 3D meshes που έχουν μετατραπεί:

```csharp
using (var writer = new BinaryWriter(new FileStream("Your Output Directory" + "Save3DMeshesInCustomBinaryFormat_out", FileMode.Create, FileAccess.Write)))
```

## Βήμα 4: Επανάληψη μέσω κόμβων και οντοτήτων

Επισκεφτείτε κάθε κόμβο στην τρισδιάστατη σκηνή και μετατρέψτε οντότητες πλέγματος στην προσαρμοσμένη δυαδική μορφή. Αγνοήστε τα φώτα, τις κάμερες και άλλες οντότητες χωρίς πλέγμα:

```csharp
scene.RootNode.Accept(delegate(Node node)
{
    foreach (Entity entity in node.Entities)
    {
        if (!(entity is IMeshConvertible))
            continue;
        // ... (συνέχεια επεξεργασίας)
    }
    return true;
});
```

## Βήμα 5: Μετατροπή και εγγραφή σημείων ελέγχου και τριγώνων

Για κάθε οντότητα πλέγματος, μετατρέψτε τα σημεία ελέγχου σε παγκόσμιο χώρο και γράψτε τα στο δυαδικό αρχείο μαζί με δείκτες τριγώνου:

```csharp
Mesh m = ((IMeshConvertible)entity).ToMesh();

var triMesh = TriMesh.FromMesh(vertexDeclaration, m);


//Η διάταξη μνήμης του πλέγματος είναι:
// float[16] transform_matrix;
// int vertices_count;
// int indices_count;
// vertex[vertices_count] κορυφές;
// ushort[index_count] δείκτες.


//γράφω μετασχηματισμός
var transform = node.GlobalTransform.TransformMatrix.ToArray();
for(int i = 0; i < transform.Length; i++)
    writer.Write((float)transform[i]);
//γράψτε τον αριθμό των κορυφών/δεικτών
writer.Write(triMesh.VerticesCount);
writer.Write(triMesh.IndicesCount);
//γράψτε κορυφές και δείκτες
writer.Flush();
triMesh.WriteVerticesTo(writer.BaseStream);
triMesh.Write16bIndicesTo(writer.BaseStream);

```

## συμπέρασμα

Σε αυτό το σεμινάριο, καλύψαμε τη διαδικασία αποθήκευσης τρισδιάστατων ματιών σε προσαρμοσμένη δυαδική μορφή χρησιμοποιώντας το Aspose.3D για .NET. Αυτή η ισχυρή βιβλιοθήκη παρέχει στους προγραμματιστές τα εργαλεία που χρειάζονται για τον απρόσκοπτο χειρισμό των τρισδιάστατων αρχείων. Πειραματιστείτε με διαφορετικές μορφές και ρυθμίσεις για να ξεκλειδώσετε πλήρως τις δυνατότητες του Aspose.3D στα έργα σας.

## Συχνές ερωτήσεις

### Ε1: Μπορώ να χρησιμοποιήσω το Aspose.3D για .NET με άλλες γλώσσες προγραμματισμού;

A1: Το Aspose.3D υποστηρίζει κυρίως γλώσσες .NET, αλλά μπορείτε να εξερευνήσετε επιλογές συμβατότητας για άλλες γλώσσες.

### Ε2: Πού μπορώ να βρω επιπλέον παραδείγματα και πόρους;

 Α2: Το[Aspose.3D φόρουμ](https://forum.aspose.com/c/3d/18)είναι ένα εξαιρετικό μέρος για να βρείτε υποστήριξη, παραδείγματα και να ασχοληθείτε με την κοινότητα.

### Ε3: Υπάρχει διαθέσιμη δοκιμαστική έκδοση για το Aspose.3D;

 A3: Ναι, μπορείτε να λάβετε δωρεάν δοκιμή από[εδώ](https://releases.aspose.com/).

### Ε4: Πώς μπορώ να αποκτήσω μια προσωρινή άδεια για το Aspose.3D;

 Α4: Επίσκεψη[αυτός ο σύνδεσμος](https://purchase.aspose.com/temporary-license/) για να λάβετε προσωρινή άδεια για σκοπούς δοκιμών.

### Ε5: Μπορώ να αγοράσω το Aspose.3D για .NET;

 A5: Ναι, μπορείτε να αγοράσετε το Aspose.3D από το[σελίδα αγοράς](https://purchase.aspose.com/buy).