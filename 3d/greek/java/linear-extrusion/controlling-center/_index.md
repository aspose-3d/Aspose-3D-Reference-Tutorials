---
date: 2026-06-13
description: Μάθετε ένα java 3d graphics tutorial για τον έλεγχο του κέντρου σε γραμμική
  εξώθηση με Aspose.3D, συμπεριλαμβανομένου του πώς να ορίσετε το rounding radius
  και να αποθηκεύσετε αρχείο OBJ java.
keywords:
- create 3d mesh java
- set rounding radius
- export 3d model obj
- save obj file java
- aspose 3d export obj
linktitle: Έλεγχος Κέντρου σε Γραμμική Εξώθηση με Aspose.3D για Java
schemas:
- author: Aspose
  dateModified: '2026-06-13'
  description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  headline: Create 3D Mesh Java – Center in Linear Extrusion
  type: TechArticle
- description: Learn a java 3d graphics tutorial on controlling the center in linear
    extrusion with Aspose.3D, including how to set rounding radius and save OBJ file
    java.
  name: Create 3D Mesh Java – Center in Linear Extrusion
  steps:
  - name: Set Up the Base Profile
    text: First, create the 2‑D shape that will be extruded. Here we use a rectangle
      and **set rounding radius** to 0.3, which smooths the corners and demonstrates
      how to **round extrusion corners**.
  - name: Create a 3D Scene
    text: '**Scene** is the top‑level container that holds all 3‑D objects, lights,
      and cameras.'
  - name: Add Left and Right Nodes
    text: A **Node** represents a transformable object in the scene graph, allowing
      positioning and hierarchy.
  - name: Linear Extrusion – No Center (Left Node)
    text: '**LinearExtrusion** converts a 2‑D profile into a 3‑D mesh by sweeping
      it along a straight line. **setCenter(boolean)** toggles whether the extrusion
      is centered around the profile origin.'
  - name: Add a Ground Plane for Reference (Left Node)
    text: A thin box acts as a visual floor, helping you see the extrusion’s orientation.
  - name: Linear Extrusion – Centered (Right Node)
    text: Now repeat the extrusion, this time enabling `center`. The geometry will
      be symmetric around the profile’s origin, giving you a perfectly balanced **create
      3d mesh java** result.
  - name: Add a Ground Plane for Reference (Right Node)
    text: Same ground plane for the right side, making the comparison clear.
  - name: Save the 3D Scene
    text: Finally, export the entire scene to a Wavefront OBJ file – a format readily
      usable in most 3‑D editors. The `save` method automatically converts the mesh
      to the OBJ specification, allowing you to **save obj file java** without additional
      post‑processing.
  type: HowTo
- questions:
  - answer: It determines whether the extrusion is symmetric around the profile's
      origin.
    question: What does the center property do?
  - answer: A temporary license works for testing; a full license is required for
      production.
    question: Do I need a license to run the code?
  - answer: The scene is saved as a Wavefront OBJ file.
    question: Which file format is used for the result?
  - answer: Yes, use `setSlices(int)` on the `LinearExtrusion` object.
    question: Can I change the number of slices?
  - answer: Absolutely – it supports all modern Java versions.
    question: Is Aspose.3D compatible with Java 8+?
  type: FAQPage
second_title: Aspose.3D Java API
title: Δημιουργία 3D Mesh Java – Κέντρο σε Γραμμική Εξώθηση
url: /el/java/linear-extrusion/controlling-center/
weight: 11
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Δημιουργία 3D Mesh Java – Κέντρο σε Γραμμική Εξώθηση

## Εισαγωγή

Αν δημιουργείτε 3‑D οπτικοποιήσεις σε Java, η εξοικείωση με τις τεχνικές εξώθησης είναι απαραίτητη. Αυτό το **java 3d graphics tutorial** σας δείχνει πώς να **create 3d mesh java** αντικείμενα ελέγχοντας το κέντρο μιας γραμμικής εξώθησης με το Aspose.3D for Java. Στο τέλος αυτού του οδηγού θα καταλάβετε γιατί η ιδιότητα `center` είναι σημαντική, πώς να **set rounding radius**, και πώς να **save obj file java**‑συμβατό αποτέλεσμα. Θα δείτε επίσης πώς να **export 3d model obj** για χρήση σε οποιονδήποτε σημαντικό 3‑D επεξεργαστή.

## Γρήγορες Απαντήσεις
- **Τι κάνει η ιδιότητα center;** Καθορίζει αν η εξώθηση είναι συμμετρική γύρω από το αρχικό σημείο του προφίλ.  
- **Χρειάζομαι άδεια για την εκτέλεση του κώδικα;** Μια προσωρινή άδεια λειτουργεί για δοκιμές· απαιτείται πλήρης άδεια για παραγωγή.  
- **Ποια μορφή αρχείου χρησιμοποιείται για το αποτέλεσμα;** Η σκηνή αποθηκεύεται ως αρχείο Wavefront OBJ.  
- **Μπορώ να αλλάξω τον αριθμό των φετών;** Ναι, χρησιμοποιήστε `setSlices(int)` στο αντικείμενο `LinearExtrusion`.  
- **Είναι το Aspose.3D συμβατό με Java 8+;** Απόλυτα – υποστηρίζει όλες τις σύγχρονες εκδόσεις της Java.

## Τι είναι ένα java 3d graphics tutorial;

Ένα **java 3d graphics tutorial** είναι ένας οδηγός βήμα‑βήμα που σας διδάσκει πώς να χρησιμοποιείτε βιβλιοθήκες Java για να δημιουργείτε, να επεξεργάζεστε και να αποδίδετε τρισδιάστατα αντικείμενα. Σε αυτόν τον οδηγό θα μάθετε να **create 3d mesh java** μετατρέποντας ένα 2‑D προφίλ σε πλήρες 3‑D μοντέλο, να ελέγχετε την κεντρική ευθυγράμμιση, να στρογγυλοποιείτε τις γωνίες της εξώθησης και τελικά να εξάγετε το αποτέλεσμα ως αρχείο OBJ που μπορεί να διαβάσει οποιοδήποτε πρόγραμμα 3‑D.

## Γιατί να χρησιμοποιήσετε το Aspose.3D for Java;

Το Aspose.3D for Java παρέχει ένα υψηλού επιπέδου API που εξαλείφει την ανάγκη για χειροκίνητους υπολογισμούς πλέγματος, επιτρέποντάς σας να εστιάσετε στο σχεδιασμό αντί στη χαμηλού επιπέδου γεωμετρία. Υποστηρίζει **50+ input and output formats**—συμπεριλαμβανομένων των OBJ, FBX, STL και GLTF—ώστε να μπορείτε να **export 3d model obj** ή οποιαδήποτε άλλη μορφή με μία κλήση μεθόδου. Η βιβλιοθήκη επεξεργάζεται σκηνές εκατοντάδων σελίδων χωρίς να φορτώνει ολόκληρο το αρχείο στη μνήμη, παρέχοντας **up to 3× faster performance** σε σύγκριση με τις ακατέργαστες αγωγές OpenGL σε τυπικό εξοπλισμό διακομιστή.

## Προαπαιτούμενα

1. **Java Development Environment** – Εγκατεστημένο JDK 8 ή νεότερο.  
2. **Aspose.3D for Java** – Κατεβάστε τη βιβλιοθήκη και την τεκμηρίωση [here](https://reference.aspose.com/3d/java/).  
3. **Document Directory** – Δημιουργήστε ένα φάκελο στον υπολογιστή σας για να αποθηκεύετε τα παραγόμενα αρχεία· θα τον αναφέρουμε ως **“Your Document Directory.”**

## Εισαγωγή Πακέτων

Στο Java IDE σας, εισάγετε τις κλάσεις Aspose.3D που θα χρειαστείτε. Αυτό δίνει στον μεταγλωττιστή πρόσβαση στις δυνατότητες εξώθησης και δημιουργίας σκηνών.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## Οδηγός Βήμα‑Βήμα

### Βήμα 1: Ρύθμιση του Βασικού Προφίλ

Πρώτα, δημιουργήστε το 2‑D σχήμα που θα εξωθηθεί. Εδώ χρησιμοποιούμε ένα ορθογώνιο και **set rounding radius** στο 0.3, το οποίο λειαίνει τις γωνίες και δείχνει πώς να **round extrusion corners**.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
RectangleShape profile = new RectangleShape();
profile.setRoundingRadius(0.3);
```

### Βήμα 2: Δημιουργία 3D Σκηνής

**Scene** είναι το κορυφαίο κοντέινερ που περιέχει όλα τα 3‑D αντικείμενα, τα φώτα και τις κάμερες.

```java
Scene scene = new Scene();
```

### Βήμα 3: Προσθήκη Αριστερών και Δεξιών Κόμβων

Ένας **Node** αντιπροσωπεύει ένα μετασχηματιζόμενο αντικείμενο στο γράφημα σκηνής, επιτρέποντας την τοποθέτηση και την ιεραρχία.

```java
Node left = scene.getRootNode().createChildNode();
Node right = scene.getRootNode().createChildNode();
left.getTransform().setTranslation(new Vector3(5, 0, 0));
```

### Βήμα 4: Γραμμική Εξώθηση – Χωρίς Κέντρο (Αριστερός Κόμβος)

**LinearExtrusion** μετατρέπει ένα 2‑D προφίλ σε 3‑D πλέγμα σκάνοντας το κατά μήκος μιας ευθείας γραμμής.  
**setCenter(boolean)** εναλλάσσει αν η εξώθηση είναι κεντραρισμένη γύρω από το αρχικό σημείο του προφίλ.

```java
left.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(false); setSlices(3); }});
```

### Βήμα 5: Προσθήκη Επιπέδου Εδάφους για Αναφορά (Αριστερός Κόμβος)

Ένα λεπτό κουτί λειτουργεί ως οπτικό πάτωμα, βοηθώντας σας να δείτε τον προσανατολισμό της εξώθησης.

```java
left.createChildNode(new Box(0.01, 3, 3));
```

### Βήμα 6: Γραμμική Εξώθηση – Κεντραρισμένη (Δεξιός Κόμβος)

Τώρα επαναλάβετε την εξώθηση, αυτή τη φορά ενεργοποιώντας το `center`. Η γεωμετρία θα είναι συμμετρική γύρω από το αρχικό σημείο του προφίλ, παρέχοντάς σας ένα τέλεια ισορροπημένο αποτέλεσμα **create 3d mesh java**.

```java
right.createChildNode(new LinearExtrusion(profile, 2) {{ setCenter(true); setSlices(3); }});
```

### Βήμα 7: Προσθήκη Επιπέδου Εδάφους για Αναφορά (Δεξιός Κόμβος)

Ίδιο επίπεδο εδάφους για τη δεξιά πλευρά, κάνοντας τη σύγκριση σαφή.

```java
right.createChildNode(new Box(0.01, 3, 3));
```

### Βήμα 8: Αποθήκευση της 3D Σκηνής

Τέλος, εξάγετε ολόκληρη τη σκηνή σε αρχείο Wavefront OBJ – μια μορφή που μπορεί εύκολα να χρησιμοποιηθεί στα περισσότερα 3‑D προγράμματα. Η μέθοδος `save` μετατρέπει αυτόματα το πλέγμα στην προδιαγραφή OBJ, επιτρέποντάς σας να **save obj file java** χωρίς πρόσθετη επεξεργασία.

```java
scene.save(MyDir + "CenterInLinearExtrusion.obj", FileFormat.WAVEFRONTOBJ);
```

## Συχνά Προβλήματα και Λύσεις

| Πρόβλημα | Γιατί συμβαίνει | Διόρθωση |
|-------|----------------|-----|
| **Extrusion appears offset** | `setCenter(false)` αφήνει το προφίλ δεσμευμένο στην γωνία του. | Χρησιμοποιήστε `setCenter(true)` για συμμετρικά αποτελέσματα. |
| **OBJ file is empty** | Η διαδρομή του φακέλου εξόδου είναι λανθασμένη ή λείπουν δικαιώματα εγγραφής. | Επαληθεύστε ότι το `MyDir` δείχνει σε υπάρχον φάκελο και η εφαρμογή έχει δικαιώματα εγγραφής. |
| **Rounded corners look sharp** | Η ακτίνα στρογγυλοποίησης είναι πολύ μικρή σε σχέση με το μέγεθος του ορθογωνίου. | Αυξήστε την τιμή της ακτίνας (π.χ., `setRoundingRadius(0.5)`). |

## Συχνές Ερωτήσεις

### Q1: Μπορώ να χρησιμοποιήσω το Aspose.3D for Java σε εμπορικά έργα;

A1: Ναι, το Aspose.3D for Java είναι διαθέσιμο για εμπορική χρήση. Για λεπτομέρειες άδειας, επισκεφθείτε [here](https://purchase.aspose.com/buy).

### Q2: Υπάρχει διαθέσιμη δωρεάν δοκιμή;

A2: Ναι, μπορείτε να εξερευνήσετε μια δωρεάν δοκιμή του Aspose.3D for Java [here](https://releases.aspose.com/).

### Q3: Πού μπορώ να βρω υποστήριξη για το Aspose.3D for Java;

A3: Το φόρουμ κοινότητας Aspose.3D είναι ένας εξαιρετικός τόπος για να ζητήσετε υποστήριξη και να μοιραστείτε τις εμπειρίες σας. Επισκεφθείτε το φόρουμ [here](https://forum.aspose.com/c/3d/18).

### Q4: Χρειάζομαι προσωρινή άδεια για δοκιμές;

A4: Ναι, εάν χρειάζεστε προσωρινή άδεια για δοκιμαστικούς σκοπούς, μπορείτε να την αποκτήσετε [here](https://purchase.aspose.com/temporary-license/).

### Q5: Πού μπορώ να βρω την τεκμηρίωση;

A5: Η τεκμηρίωση για το Aspose.3D for Java είναι διαθέσιμη [here](https://reference.aspose.com/3d/java/).

## Συμπέρασμα

Με την ολοκλήρωση αυτού του **java 3d graphics tutorial**, τώρα ξέρετε πώς να δημιουργήσετε αντικείμενα **create 3d mesh java**, να ελέγξετε το κέντρο μιας γραμμικής εξώθησης, να προσαρμόσετε την ακτίνα στρογγυλοποίησης και να **save obj file java** χρησιμοποιώντας το Aspose.3D. Αυτές οι τεχνικές σας δίνουν λεπτομερή έλεγχο της συμμετρίας του πλέγματος, κάτι που είναι ζωτικής σημασίας για στοιχεία παιχνιδιών, πρωτότυπα CAD και επιστημονικές οπτικοποιήσεις. Μη διστάσετε να πειραματιστείτε με διαφορετικά προφίλ, αριθμούς φετών και μορφές εξαγωγής για να επεκτείνετε το 3‑D εργαλείο σας.

---

**Τελευταία Ενημέρωση:** 2026-06-13  
**Δοκιμή Με:** Aspose.3D for Java 24.11  
**Συγγραφέας:** Aspose

## Σχετικά Μαθήματα

- [Δημιουργία 3D Εξώθησης Java με Aspose.3D](/3d/java/linear-extrusion/performing-linear-extrusion/)
- [Πώς να Ορίσετε Κατεύθυνση στη Γραμμική Εξώθηση με Aspose.3D for Java](/3d/java/linear-extrusion/setting-direction/)
- [Δημιουργία 3D Σκηνής με Περιστροφή στη Γραμμική Εξώθηση – Aspose.3D for Java](/3d/java/linear-extrusion/applying-twist/)


{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}