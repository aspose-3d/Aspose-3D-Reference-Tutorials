---
date: 2026-09-28
description: Μάθετε πώς να δημιουργήσετε κίνηση σε 3D σκηνές σε Java χρησιμοποιώντας
  Aspose.3D, προσθέστε ιδιότητες animation, δημιουργήστε keyframes και εξάγετε animated
  FBX αρχεία με τεχνικές linear interpolation 3d.
keywords:
- how to animate 3d
- linear interpolation 3d
- export animated fbx
- create keyframe animation
- add animation properties
lastmod: 2026-09-28
linktitle: Πώς να δημιουργήσετε κίνηση σε 3D σκηνές σε Java με Aspose.3D
og_description: Μάθετε πώς να δημιουργήσετε κίνηση σε 3D σκηνές σε Java χρησιμοποιώντας
  Aspose.3D. Αυτός ο step‑by‑step οδηγός δείχνει πώς να προσθέτετε ιδιότητες animation,
  να δημιουργείτε keyframes και να εξάγετε animated FBX αρχεία.
og_image_alt: Developer guide showing how to animate 3D scenes in Java with Aspose.3D
og_title: Πώς να δημιουργήσετε κίνηση σε 3D σκηνές σε Java – οδηγός Aspose.3D
schemas:
- author: Aspose
  dateModified: '2026-09-28'
  description: Learn how to animate 3D scenes in Java using Aspose.3D, add animation
    properties, create keyframes, and export animated FBX files with linear interpolation
    3d techniques.
  headline: How to animate 3D scenes in Java with Aspose.3D
  type: TechArticle
- questions:
  - answer: Yes. Purchase a commercial license on the [Aspose purchase page](https://purchase.aspose.com/buy).
    question: Can I use Aspose.3D for commercial projects?
  - answer: Absolutely. Download a trial from the [Aspose releases page](https://releases.aspose.com/).
    question: Is a free trial available?
  - answer: Join the community at the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)
      for help from staff and other developers.
    question: Where can I get support?
  - answer: Request a [temporary license](https://purchase.aspose.com/temporary-license/)
      to remove runtime restrictions during testing.
    question: How do I obtain a temporary evaluation license?
  - answer: Yes—explore the full [Aspose.3D documentation](https://reference.aspose.com/3d/java/)
      for advanced scenarios such as skeletal animation, morph targets, and custom
      shaders.
    question: Are there more tutorials?
  type: FAQPage
second_title: Aspose.3D Java API
tags:
- animate 3d java
- Aspose.3D
- linear interpolation
- FBX export
- Java animation tutorial
title: Πώς να δημιουργήσετε κίνηση σε 3D σκηνές σε Java με Aspose.3D
url: /el/java/animations/add-animation-properties-to-scenes/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Πώς να δημιουργήσετε κίνηση σε 3Δ σκηνές σε Java με Aspose.3D

## Εισαγωγή

Σε αυτό το tutorial θα μάθετε **πώς να δημιουργείτε κίνηση 3Δ** αντικειμένων σε μια εφαρμογή Java χρησιμοποιώντας το Aspose.3D. Θα ξεκινήσουμε δημιουργώντας μια σκηνή, θα κατασκευάσουμε ένα απλό πλέγμα, θα συνδέσουμε ιδιότητες κίνησης, θα ορίσουμε keyframes με γραμμική παρεμβολή και τέλος θα εξάγουμε το αποτέλεσμα ως αρχείο FBX με κίνηση. Στο τέλος θα έχετε ένα έτοιμο FBX που λειτουργεί σε Unity, Blender ή οποιονδήποτε σύγχρονο 3‑D viewer.

## Γρήγορες απαντήσεις
- **Ποια βιβλιοθήκη τροφοδοτεί την κίνηση;** Aspose.3D for Java, μια καθαρά‑Java 3‑D μηχανή.  
- **Μπορώ να εξάγω το αποτέλεσμα ως FBX;** Ναι – το δείγμα αποθηκεύει ένα αρχείο `FBX7500ASCII` που διατηρεί όλα τα keyframes.  
- **Χρειάζεται πληρωμένη άδεια για να δοκιμάσω αυτό;** Μια δωρεάν δοκιμή λειτουργεί για ανάπτυξη· απαιτείται εμπορική άδεια για παραγωγική χρήση.  
- **Ποια έκδοση της Java απαιτείται;** Java 8 ή νεότερη.  
- **Η παρεμβολή είναι γραμμική ή spline;** Και οι δύο υποστηρίζονται· μπορείτε να επιλέξετε `Interpolation.LINEAR` για κίνηση ευθείας γραμμής ή `Interpolation.BEZIER` για ομαλές καμπύλες.

## Τι είναι η γραμμική παρεμβολή 3Δ;

Η γραμμική παρεμβολή 3Δ είναι ο υπολογισμός ενδιάμεσων τιμών μετασχηματισμού μεταξύ δύο keyframes χρησιμοποιώντας έναν τύπο ευθείας γραμμής. Στο Aspose.3D επιλέγετε `Interpolation.LINEAR` όταν προσθέτετε ένα keyframe, και η μηχανή δημιουργεί αυτόματα κίνηση σταθερής ταχύτητας μεταξύ των πλαισίων.

## Γιατί να προσθέσετε ιδιότητες κίνησης σε μια σκηνή;

Η προσθήκη ιδιοτήτων κίνησης μετατρέπει τη στατική γεωμετρία σε δυναμικό περιεχόμενο που μπορεί να επαναχρησιμοποιηθεί σε παιχνίδια, προσομοιώσεις ή οπτικοποιήσεις προϊόντων. Με το Aspose.3D μπορείτε να κινείτε πολλούς κόμβους ανεξάρτητα, να εξάγετε πλήρως κινούμενα αρχεία FBX και να διατηρήσετε όλη τη ροή εργασίας σε καθαρή Java χωρίς εγγενείς DLL.

## Γιατί να χρησιμοποιήσετε το Aspose.3D για κίνηση;

Το Aspose.3D υποστηρίζει **12+** μορφές εξαγωγής—συμπεριλαμβανομένων των FBX, OBJ, 3MF, STL και GLTF—ώστε να στοχεύετε σε οποιοδήποτε pipeline. Η βιβλιοθήκη τρέχει μόνο στο JVM, εξαλείφοντας τις εγγενείς εξαρτήσεις. Προσφέρει επίσης τρεις τρόπους παρεμβολής (BEZIER, LINEAR, STEP) και ένα πλήρες API σκηνικού γραφήματος που σας επιτρέπει να χειρίζεστε κόμβους, πλέγματα, υλικά και κινήσεις μέσω ενός ενιαίου, συνεπούς μοντέλου αντικειμένων.

## Προαπαιτούμενα

- Βασικές γνώσεις προγραμματισμού Java.  
- Aspose.3D for Java εγκατεστημένο – κατεβάστε το από τη [σελίδα κυκλοφορίας](https://releases.aspose.com/3d/java/).  
- Maven ή Gradle ρυθμισμένα για τη μεταγλώττιση του δείγματος έργου.  

## Εισαγωγή πακέτων

Στο αρχείο πηγαίου κώδικα Java, εισάγετε τους βασικούς χώρους ονομάτων του Aspose.3D και την βοηθητική κλάση `Common` που δημιουργεί ένα απλό πλέγμα κύβου. Η κλάση `Common` παρέχει στατικές μεθόδους για τη δημιουργία βασικής γεωμετρίας όπως ένας μονάδα κύβος.

```java
import com.aspose.threed.*;
```

Τώρα που οι χώροι ονομάτων είναι έτοιμοι, ας αρχίσουμε να χτίζουμε τη σκηνή.

## Βήμα 1: αρχικοποίηση της σκηνής

Η κλάση `Scene` είναι το κορυφαίο κοντέινερ του Aspose.3D που κρατά όλους τους κόμβους, πλέγματα, φωτισμούς και δεδομένα κίνησης.

```java
// Initialize scene object
Scene scene = new Scene();
```

## Βήμα 2: δημιουργία πλέγματος με χρήση κατασκευαστή πολυγώνων

Η κλάση `Mesh` αντιπροσωπεύει μια συλλογή κορυφών, προσώπων και κανονικών που ορίζουν ένα 3‑D αντικείμενο. Σε αυτό το βήμα η βοηθητική κλάση δημιουργεί ένα βασικό πλέγμα κύβου που θα κινήσουμε αργότερα.

```java
Mesh mesh = new Mesh();
```

## Βήμα 3: δημιουργία κόμβου κύβου με μετάφραση

Ένας `Node` είναι ένα στοιχείο στο γράφημα σκηνής που μπορεί να κρατήσει ένα πλέγμα και τις ιδιότητες μετασχηματισμού του (μετάφραση, περιστροφή, κλίμακα). Εδώ συνδέουμε το πλέγμα του κύβου σε έναν νέο κόμβο και το τοποθετούμε στην αρχή.

```java
// Each cube node has its own translation
Node cube1 = scene.getRootNode().createChildNode("cube1", mesh);
```

## Βήμα 4: εύρεση ιδιότητας μετάφρασης

Ένα **bind point** συνδέει μια συγκεκριμένη ιδιότητα—όπως η μετάφραση—με μια καμπύλη κίνησης. Εντοπίζοντας το bind point της μετάφρασης, επιτρέπουμε στη μηχανή να τροποποιεί τη θέση του κόμβου με την πάροδο του χρόνου.

```java
// Find translation property on node's transform object
Property translation = cube1.getTransform().findProperty("Translation");
```

## Βήμα 5: δημιουργία καμπύλης κίνησης για τον άξονα x

Μια καμπύλη κίνησης αποθηκεύει μια σειρά από keyframes για ένα μόνο στοιχείο (X, Y ή Z). Η παρακάτω καμπύλη ορίζει τρία keyframes στα 0 s, 3 s και 5 s. Τα πρώτα δύο χρησιμοποιούν BEZIER για ομαλή επιτάχυνση, ενώ το τελευταίο keyframe χρησιμοποιεί LINEAR για να δείξει τη γραμμική παρεμβολή 3d.

```java
// Create an animation node for the scene
AnimationNode animNode = new AnimationNode("TranslationAnimation");

// Create a bind point for the translation property on the cube's transform
BindPoint bp = animNode.createBindPoint(cube1.getTransform(), "Translation");

// Create the animation curve on the X component of the translation
KeyframeSequence kfsX = new KeyframeSequence();

// Add keyframes for X component
kfsX.add(0, 10.0f, Interpolation.BEZIER);
kfsX.add(3, 20.0f, Interpolation.BEZIER);
kfsX.add(5, 30.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the X channel of the bind point
bp.bindKeyframeSequence("X", kfsX);
```

## Βήμα 6: επανάληψη για το στοιχείο z

Η κίνηση του άξονα Z προσθέτει βάθος στην κίνηση του κύβου, δημιουργώντας μια πιο δυναμική 3‑D διαδρομή. Η ίδια λογική bind‑point και καμπύλης εφαρμόζεται, αλλά με τιμές που μετακινούν τον κύβο μπροστά και πίσω.

```java
// Repeat the process for the Z component
KeyframeSequence kfsZ = new KeyframeSequence();
kfsZ.add(0, 10.0f, Interpolation.BEZIER);
kfsZ.add(3, -10.0f, Interpolation.BEZIER);
kfsZ.add(5, 0.0f, Interpolation.LINEAR);

// Bind the keyframe sequence to the Z channel of the same bind point
bp.bindKeyframeSequence("Z", kfsZ);
```

## Πώς να εξάγετε το κινούμενο FBX

Καλώντας `scene.save(...)` με `FileFormat.FBX7500ASCII` γράφει όλες τις καμπύλες κίνησης, τα bind points και τα keyframes σε ένα ενιαίο κοντέινερ FBX. Το `FileFormat` είναι μια απαρίθμηση που ορίζει τις υποστηριζόμενες μορφές εξόδου, συμπεριλαμβανομένου του `FBX7500ASCII`. Βεβαιωθείτε ότι ο φάκελος προορισμού υπάρχει και έχετε δικαιώματα εγγραφής· διαφορετικά η λειτουργία αποθήκευσης θα πετάξει εξαίρεση.

```java
// Specify the directory for saving the 3D scene
String MyDir = "Your Document Directory";
MyDir = MyDir + "PropertyToDocument.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7500ASCII);
```

Το παραγόμενο αρχείο μπορεί να ανοιχτεί στο Blender, Unity, Autodesk Maya ή οποιονδήποτε viewer που υποστηρίζει τη μορφή FBX, επιτρέποντάς σας να προβάλετε την κίνηση άμεσα.

## Κοινά προβλήματα και λύσεις

| Συμπτωμα | Πιθανή αιτία | Διόρθωση |
|---------|--------------|----------|
| Δεν φαίνεται κίνηση | Τα keyframes προστέθηκαν στο λάθος στοιχείο (π.χ., “Y” αντί για “X”) | Επαληθεύστε το όνομα του στοιχείου στο `bindKeyframeSequence`. |
| Η κίνηση «πηδά» | Μίξη BEZIER και LINEAR λανθασμένα | Διατηρήστε την παρεμβολή συνεπή για ομαλότερη κίνηση ή ρυθμίστε τα εφαπτόμενα χειροκίνητα. |
| Το αρχείο δεν αποθηκεύεται | Μη έγκυρη διαδρομή φακέλου | Βεβαιωθείτε ότι το `MyDir` δείχνει σε υπάρχον φάκελο με δικαιώματα εγγραφής και ότι λήγει σε `.fbx`. |

## Συχνές ερωτήσεις

**Ε: Μπορώ να χρησιμοποιήσω το Aspose.3D για εμπορικά έργα;**  
Α: Ναι. Αγοράστε εμπορική άδεια στη [σελίδα αγοράς του Aspose](https://purchase.aspose.com/buy).

**Ε: Υπάρχει δωρεάν δοκιμή;**  
Α: Απόλυτα. Κατεβάστε μια δοκιμή από τη [σελίδα κυκλοφορίας του Aspose](https://releases.aspose.com/).

**Ε: Πού μπορώ να λάβω υποστήριξη;**  
Α: Ενταχθείτε στην κοινότητα στο [Φόρουμ Aspose.3D](https://forum.aspose.com/c/3d/18) για βοήθεια από το προσωπικό και άλλους προγραμματιστές.

**Ε: Πώς να αποκτήσω προσωρινή άδεια αξιολόγησης;**  
Α: Ζητήστε μια [προσωρινή άδεια](https://purchase.aspose.com/temporary-license/) για να αφαιρέσετε περιορισμούς χρόνου εκτέλεσης κατά τη δοκιμή.

**Ε: Υπάρχουν περισσότερα tutorials;**  
Α: Ναι—εξερευνήστε την πλήρη [τεκμηρίωση Aspose.3D](https://reference.aspose.com/3d/java/) για προχωρημένα σενάρια όπως σκελετική κίνηση, morph targets και προσαρμοσμένα shaders.

## Συμπέρασμα

Τώρα γνωρίζετε **πώς να δημιουργείτε κίνηση 3Δ** αντικειμένων σε Java με Aspose.3D: δημιουργήστε μια σκηνή, συνδέστε ιδιότητες μετάφρασης, ορίστε ακολουθίες keyframe με γραμμική παρεμβολή και εξάγετε ένα κινούμενο αρχείο FBX. Πειραματιστείτε με περιστροφή, κλίμακα ή πολλαπλούς κόμβους για να δημιουργήσετε πιο πλούσιες κινήσεις για παιχνίδια, προσομοιώσεις ή οπτικοποιήσεις προϊόντων.

---

**Τελευταία ενημέρωση:** 2026-09-28  
**Δοκιμή με:** Aspose.3D for Java 24.12 (τελευταία)  
**Συγγραφέας:** Aspose

## Σχετικά Μαθήματα

- [Create an FBX File with Aspose.3D for Java – 3D Graphics Tutorial](/3d/java/load-and-save/create-empty-3d-document/)
- [Save 3D Scenes in Java with Aspose.3D – Convert 3D Files Efficiently](/3d/java/load-and-save/save-3d-scenes/)
- [Export Model to FBX with Quaternions in Java using Aspose.3D](/3d/java/geometry/transform-3d-nodes-with-quaternions/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}