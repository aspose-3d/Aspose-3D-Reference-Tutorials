---
date: 2026-02-25
description: Μάθετε πώς να αντιστρέψετε το σύστημα συντεταγμένων και να προσαρμόσετε
  την εισαγωγή 3D χρησιμοποιώντας το Aspose.3D LoadOptions στη Java. Οδηγός βήμα‑προς‑βήμα
  για 3DS, OBJ, STL, U3D, glTF, PLY, X και προαιρετικά FBX.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: Αναστροφή Συστήματος Συντεταγμένων – Προσαρμογή Φόρτωσης 3D Αρχείων σε Java
  με το Aspose.3D
url: /el/java/load-and-save/customize-3d-file-loading/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Flip Coordinate System – Customize 3D File Loading in Java with Aspose.3D

Στο συνεχώς εξελισσόμενο τοπίο του 3D σχεδιασμού και ανάπτυξης, η **αναστροφή του συστήματος συντεταγμένων** κατά την εισαγωγή μοντέλων είναι συχνή απαίτηση. Είτε μετατρέπετε πόρους από δεξιόχειρο σε αριστερόχειρο σύστημα, είτε χρειάζεται να ευθυγραμμίσετε τα μοντέλα με τις αξονικές συμβάσεις της μηχανής σας, το Aspose.3D for Java σας προσφέρει ακριβή έλεγχο. Αυτό το tutorial σας καθοδηγεί πώς να **προσαρμόσετε την εισαγωγή 3D** χρησιμοποιώντας το `LoadOptions` του Aspose.3D, καλύπτοντας τις πιο δημοφιλείς μορφές όπως 3DS, OBJ, STL, U3D, glTF, PLY, X και προαιρετικά FBX.

## Quick Answers
- **Τι κάνει η “αναστροφή του συστήματος συντεταγμένων”;** Αντιστρέφει τους άξονες X/Y/Z ώστε να ταιριάζουν με τη στοχευμένη σύμβαση συντεταγμένων.  
- **Ποιες μορφές υποστηρίζουν την αναστροφή;** Όλες οι κύριες μορφές (3DS, OBJ, STL, U3D, glTF, PLY, X, FBX) εκθέτουν την επιλογή `setFlipCoordinateSystem`.  
- **Χρειάζομαι επιπλέον βιβλιοθήκες;** Μόνο το JAR του Aspose.3D for Java· δεν απαιτούνται εξωτερικοί μετατροπείς.  
- **Μπορώ να φορτώσω υλικά ταυτόχρονα;** Ναι—χρησιμοποιήστε `setEnableMaterials(true)` για αρχεία OBJ.  
- **Απαιτείται άδεια για παραγωγή;** Απαιτείται έγκυρη άδεια Aspose.3D για μη‑δοκιμαστικές εγκαταστάσεις.

## What is “flip coordinate system”?
Η αναστροφή του συστήματος συντεταγμένων αλλάζει τον προσανατολισμό των αξόνων που χρησιμοποιεί το εισαγόμενο μοντέλο. Αυτό είναι απαραίτητο όταν το αρχείο προέλευσης χρησιμοποιεί διαφορετική χειρονομία (δεξιόχειρο vs. αριστερόχειρο) από τη μηχανή απόδοσής σας, αποτρέποντας την εμφάνιση των μοντέλων ως κατοπτρισμένα ή ανεστραμμένα.

## Why customize 3D import?
Η προσαρμογή της εισαγωγής σας επιτρέπει:
- Διατήρηση των μετασχηματισμών κίνησης (`setApplyAnimationTransform`).  
- Διόρθωση της διαχείρισης χρωμάτων (`setGammaCorrectedColor`).  
- Επίλυση διαδρομών εξωτερικών πόρων μέσω `getLookupPaths()`.  
- Βελτιστοποίηση χρήσης μνήμης φορτώνοντας μόνο ό,τι χρειάζεστε.

## Prerequisites

- Βασική κατανόηση του προγραμματισμού Java.  
- Εγκατεστημένο Java Development Kit (JDK).  
- Βιβλιοθήκη Aspose.3D for Java που έχετε κατεβάσει. Μπορείτε να την αποκτήσετε [εδώ](https://releases.aspose.com/3d/java/).  
- Εξοικείωση με μορφές αρχείων 3D όπως 3DS, OBJ, STL, U3D, glTF, PLY, X και FBX.

## Import Packages

Στο έργο Java, βεβαιωθείτε ότι έχετε εισάγει τα απαραίτητα πακέτα Aspose.3D:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## How to customize 3D import with LoadOptions

Παρακάτω θα βρείτε βήμα‑βήμα αποσπάσματα κώδικα που δείχνουν πώς να ενεργοποιήσετε την επιλογή **αναστροφή του συστήματος συντεταγμένων** για κάθε υποστηριζόμενη μορφή. Τα αποσπάσματα είναι έτοιμα για αντιγραφή στο έργο σας· απλώς αντικαταστήστε το `"Your Document Directory"` με την πραγματική διαδρομή των πόρων σας.

### Step 1: Customize 3DS File Loading

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### Step 2: Customize OBJ File Loading

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### Step 3: Customize STL File Loading

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### Step 4: Customize U3D File Loading

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### Step 5: Customize glTF File Loading

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### Step 6: Customize PLY File Loading

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### Step 7: Customize X File Loading

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### Step 8: Customize FBX File Loading (Optional)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## Common Issues and Solutions
- **Το μοντέλο εμφανίζεται κατοπτρισμένο μετά τη φόρτωση** – Ελέγξτε ότι το `setFlipCoordinateSystem(true)` είναι ορισμένο για τη σωστή μορφή.  
- **Τα υλικά λείπουν** – Για αρχεία OBJ, βεβαιωθείτε ότι το `setEnableMaterials(true)` είναι ενεργό και ότι τα αρχεία υλικών (.mtl) βρίσκονται σε μία από τις διαδρομές αναζήτησης.  
- **Οι συντεταγμένες υφής είναι ανάποδες** – Για glTF, ίσως χρειαστεί `setFlipTexCoordV(true)` εκτός από την αναστροφή των αξόνων.  
- **Σφάλματα “αρχείο δεν βρέθηκε”** – Προσθέστε τον φάκελο που περιέχει εξωτερικούς πόρους (υφές, βοηθητικά αρχεία) στο `loadOpts.getLookupPaths()`.

## Conclusion

Αξιοποιώντας το `LoadOptions` του Aspose.3D, μπορείτε να **αναστρέψετε το σύστημα συντεταγμένων** και να **προσαρμόσετε την εισαγωγή 3D** για σχεδόν κάθε κύρια μορφή. Αυτό το επίπεδο ελέγχου εξαλείφει την ανάγκη για μεταγενέστερα scripts επεξεργασίας και εξασφαλίζει ότι οι πόροι σας αποδίδονται σωστά από την πρώτη φορά.

## Frequently Asked Questions

### Q1: Πού μπορώ να βρω την τεκμηρίωση του Aspose.3D for Java;
A1: Η τεκμηρίωση είναι διαθέσιμη [εδώ](https://reference.aspose.com/3d/java/).

### Q2: Πώς μπορώ να κατεβάσω το Aspose.3D for Java;
A2: Μπορείτε να το κατεβάσετε [εδώ](https://releases.aspose.com/3d/java/).

### Q3: Υπάρχει δωρεάν δοκιμαστική έκδοση;
A3: Ναι, μπορείτε να αποκτήσετε τη δωρεάν δοκιμή [εδώ](https://releases.aspose.com/).

### Q4: Πού μπορώ να λάβω υποστήριξη για το Aspose.3D for Java;
A4: Επισκεφθείτε το φόρουμ υποστήριξης [εδώ](https://forum.aspose.com/c/3d/18).

### Q5: Χρειάζομαι προσωρινή άδεια για δοκιμές;
A5: Ναι, αποκτήστε προσωρινή άδεια [εδώ](https://purchase.aspose.com/temporary-license/).

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**Last Updated:** 2026-02-25  
**Tested With:** Aspose.3D for Java 24.11 (latest)  
**Author:** Aspose