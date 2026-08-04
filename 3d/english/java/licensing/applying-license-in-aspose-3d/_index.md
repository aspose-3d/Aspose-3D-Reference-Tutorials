---
title: "Apply an Aspose.3D License in Java"
linktitle: Apply Aspose.3D License in Java
second_title: Aspose.3D Java API
description: "Learn how to apply an Aspose.3D license in Java, using a license file, a stream, or metered licensing with public and private keys."
weight: 10
url: /java/licensing/applying-license-in-aspose-3d/
date: 2026-05-24
keywords:
  - apply aspose 3d license
  - aspose 3d java licensing
  - metered licensing java
schemas:
- type: TechArticle
  headline: Apply an Aspose.3D License in Java
  description: Learn how to apply an Aspose.3D license in Java, using a license file, a stream, or metered licensing with public and private keys.
  dateModified: '2026-05-24'
  author: Aspose
- type: HowTo
  name: Apply an Aspose.3D License in Java
  description: Learn how to apply an Aspose.3D license in Java, using a license file, a stream, or metered licensing with public and private keys.
  steps:
  - name: Create a `License` object
    text: Instantiate the `License` class; this prepares the runtime to accept a license file.
  - name: Apply the license file
    text: Provide the absolute or relative path to your `.lic` file and call `setLicense`. The method returns `void`, and the license is cached after the first successful call, so subsequent calls are inexpensive.
  - name: Create a `License` object
    text: As before, start by creating an instance of the `License` class.
  - name: Load the license via `FileInputStream`
    text: Open a `FileInputStream` pointing to your `.lic` file (or any `InputStream`) and pass it to `setLicense`. The stream is read once and then closed automatically.
  - name: Initialize a `Metered` license object
    text: The `Metered` class represents a cloud‑based license that validates usage against Aspose’s metering server.
  - name: Set public and private keys
    text: Call `setMeteredKey(publicKey, privateKey)` with the keys you received when you purchased a metered license. The library contacts the server once to verify the keys and then caches the result.
- type: FAQPage
  questions:
  - question: Is Aspose.3D compatible with all Java versions?
    answer: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15 major releases.
  - question: Where can I find additional documentation?
    answer: 'You can refer to the documentation [here](https://reference.aspose.com/3d/java/).'
  - question: Can I try Aspose.3D before purchasing?
    answer: 'Yes, you can explore a free trial [here](https://releases.aspose.com/).'
  - question: How can I get support for Aspose.3D?
    answer: 'Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.'
  - question: Do I need a temporary license for testing?
    answer: 'Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).'
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Apply an Aspose.3D License in Java

## Introduction

In this comprehensive tutorial you’ll discover **how to apply an Aspose.3D license** for Aspose.3D in a Java environment. Whether you prefer loading a license file, streaming it, or using metered licensing with public and private keys, we’ll walk through each approach step‑by‑step so you can unlock the full feature set of Aspose.3D quickly and confidently. Setting the license correctly removes evaluation watermarks, enables premium 3D formats, and ensures full compliance with Aspose’s licensing model.

## Quick Answers
- **What is the primary way to apply an Aspose.3D license?** Use the `License` class and call `setLicense` with a file path or stream.  
- **Can I load the license from a stream?** Yes – wrap the `.lic` file in a `FileInputStream` and pass it to `setLicense`.  
- **What if I need a metered license?** Initialize a `Metered` object and call `setMeteredKey` with your public and private keys.  
- **Do I need a license for development builds?** A trial or temporary license is required for any non‑evaluation scenario.  
- **Which Java versions are supported?** Aspose.3D works with Java 6 through Java 21, covering over 15 major releases.

## What is the `License` class?
The `License` class is Aspose.3D's core licensing object that loads a `.lic` file into memory, validates the license information, and once instantiated it applies the license globally for the JVM process, ensuring that all subsequent Aspose.3D operations run under the licensed mode without evaluation restrictions.

## Why apply the Aspose.3D license?
Applying a valid license enables **50+ premium 3D file formats** (including FBX, OBJ, STL, and GLTF) and removes the “Evaluation” watermark from rendered images. It also lifts limits on scene size, allowing processing of models with **up to 1 million vertices** without performance degradation.

## Prerequisites

Before we begin, make sure you have the following prerequisites in place:

- Basic understanding of Java programming.  
- Aspose.3D library installed. You can download it from the [release page](https://releases.aspose.com/3d/java/).  

## Import Packages

To get started, import the necessary packages into your Java project. Ensure that Aspose.3D is added to your classpath. Here's an example:

```java
import com.aspose.threed.License;
import com.aspose.threed.Metered;

import java.io.FileInputStream;
import java.io.IOException;
```

## Applying a License Using a File

### Step 1: Create a `License` object
Instantiate the `License` class; this prepares the runtime to accept a license file.

### Step 2: Apply the license file
Provide the absolute or relative path to your `.lic` file and call `setLicense`. The method returns `void`, and the license is cached after the first successful call, so subsequent calls are inexpensive.

```java
license.setLicense("Aspose._3D.lic");
```
 
## How to apply a license from a stream?

Streaming a license is useful when the file is embedded as a resource, stored in a secure location, or retrieved from a remote service at runtime. By using an `InputStream`, you avoid exposing the physical file path and can keep the license data encrypted or packaged inside your JAR, enhancing security while still allowing the library to read the license bytes.

### Step 1: Create a `License` object
As before, start by creating an instance of the `License` class.

```java
License license2 = new License();
```

### Step 2: Set License from Stream Object

Utilize a `FileInputStream` to create a stream and set the license:

```java
 try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
     license2.setLicense(myStream);
 }
 
 ```

## How to use public and private keys for metered licensing?

Initialize a `Metered` license object:

 ````java
 Metered metered = new Metered();
 ````

### Step 1: Initialize a `Metered` license object
The `Metered` class represents a cloud‑based license that validates usage against Aspose’s metering server.

### Step 2: Set public and private keys
Call `setMeteredKey(publicKey, privateKey)` with the keys you received when you purchased a metered license. The library contacts the server once to verify the keys and then caches the result.

 ````java
 metered.setMeteredKey("your-public-key", "your-private-key");
 ````
## Why Setting the License Matters

Applying the correct license removes evaluation watermarks, unlocks premium file formats, and ensures compliance with Aspose’s licensing model. Using the appropriate method (file, stream, or metered) lets you integrate licensing seamlessly into CI/CD pipelines, cloud deployments, or desktop applications.

## Common Issues & Tips

- **File not found** – Verify that the `.lic` file path is correct relative to the working directory or use an absolute path.  
- **Stream closed prematurely** – When using a stream, keep the `License` object alive for the duration of the application; the license is cached after the first successful call.  
- **Metered key mismatch** – Double‑check that the public and private keys correspond to the same metered license; a typo will cause a runtime exception.  
- **Pro tip:** Store the license file in a secure location outside the source tree and load it via an environment variable to avoid committing it to version control.

## Conclusion

Congratulations! You've successfully learned **how to apply an Aspose.3D license** in Java using three reliable methods: applying a license from a file, streaming it, and configuring metered licensing with public and private keys. With the license in place, you can now integrate Aspose.3D seamlessly into your Java applications, unlock all premium 3D processing features, and comply with Aspose’s licensing requirements.

## Frequently Asked Questions

**Q: Is Aspose.3D compatible with all Java versions?**  
A: Yes, Aspose.3D supports Java 6 through Java 21, covering more than 15 major releases.

**Q: Where can I find additional documentation?**  
A: You can refer to the documentation [here](https://reference.aspose.com/3d/java/).

**Q: Can I try Aspose.3D before purchasing?**  
A: Yes, you can explore a free trial [here](https://releases.aspose.com/).

**Q: How can I get support for Aspose.3D?**  
A: Visit the [Aspose.3D Forum](https://forum.aspose.com/c/3d/18) for support.

**Q: Do I need a temporary license for testing?**  
A: Yes, obtain a temporary license [here](https://purchase.aspose.com/temporary-license/).

**Q: What is the difference between a file license and a metered license?**  
A: A file license is a static `.lic` file tied to a specific product version, while a metered license validates usage against Aspose’s cloud‑based metering service using public/private keys.

**Q: Can I embed the license loading code in a static initializer?**  
A: Absolutely – placing the `License` initialization in a static block ensures the license is applied once when the class is first loaded.

```java
static {
    try {
        License license = new License();
        license.setLicense("Aspose.3D.lic");
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

```java
try (FileInputStream myStream = new FileInputStream("Aspose._3D.lic")) {
    License license = new License();
    license.setLicense(myStream);
}
```

```java
Metered metered = new Metered();
metered.setMeteredKey("your-public-key", "your-private-key");
```

{{< /blocks/products/pf/tutorial-page-section >}}
{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
