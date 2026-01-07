---
date: 2026-01-07
description: Pelajari cara mengekstrusi linier profil 2D dan mengekspor model 3D OBJ
  menggunakan Aspose.3D untuk .NET. Tutorial ekstrusi linier ini memandu Anda langkah
  demi langkah.
linktitle: Performing Linear Extrusion
second_title: Aspose.3D .NET API
title: Cara Melakukan Ekstrusi Linear dengan Aspose.3D untuk .NET
url: /id/net/3d-modeling/linear-extrusion/performing-linear-extrusion/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# how to linear extrude dengan Aspose.3D for .NET

## Introduction

Selamat datang di **tutorial linear extrusion** kami! Pada panduan ini Anda akan menemukan **cara melakukan linear extrusion** pada profil 2‑D dan mengubahnya menjadi objek 3‑D yang lengkap menggunakan Aspose.3D for .NET. Baik Anda sedang membangun aplikasi bergaya CAD atau hanya perlu **export 3d model obj** untuk proses selanjutnya, langkah‑demi‑langkah ini akan memberi Anda kepercayaan diri untuk menambahkan pembuatan geometri yang kuat ke dalam proyek Anda.

## Quick Answers
- **What is linear extrusion?** Extending a 2‑D shape along a straight path to create a 3‑D solid.  
- **Which library do we use?** Aspose.3D for .NET.  
- **Do I need a license?** A temporary license works for testing; a full license is required for production.  
- **Can I export to OBJ?** Yes – the final scene is saved as a Wavefront OBJ file.  
- **How many lines of code?** Under 30 lines of C# plus explanatory comments.

## What is Linear Extrusion?

Linear extrusion mengambil profil datar (seperti persegi panjang atau lingkaran) dan menyapu‑nya sepanjang garis lurus, dengan opsi menambahkan putaran, skala, atau offset. Hasilnya adalah solid yang dapat dirender, diedit, atau diekspor untuk digunakan di alat 3‑D lainnya.

## Why Use Aspose.3D for Linear Extrusion?

* **Zero‑dependency:** No need for external CAD kernels.  
* **Full .NET support:** Works with .NET Framework, .NET Core, and .NET 5/6+.  
* **Export flexibility:** Directly save to OBJ, STL, FBX, and many other formats.  
* **Rich API:** Control slices, twist, and offsets with just a few properties.

## Prerequisites

Sebelum Anda memulai, pastikan Anda memiliki:

1. **Aspose.3D installed** – download it from [here](https://releases.aspose.com/3d/net/).  
2. **Documentation access** – follow the setup guide [here](https://reference.aspose.com/3d/net/).  
3. Lingkungan pengembangan .NET (Visual Studio, VS Code, atau Rider) dengan namespace yang diperlukan sudah direferensikan.

## Import Namespaces

Sertakan namespace penting untuk membuka fungsionalitas Aspose.3D:

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

Namespace ini memberi Anda akses ke `Scene`, `LinearExtrusion`, `RectangleShape`, dan kelas utilitas seperti `Vector3`.

## Performing Linear Extrusion

Berikut adalah alur kerja lengkap. Setiap langkah dijelaskan dengan bahasa sederhana sebelum blok kode yang bersangkutan, sehingga Anda dapat mengikutinya tanpa menebak apa yang dilakukan kode.

### Step 1: Initialize the Base Profile

Pertama, buat bentuk 2‑D yang akan diekstrusi. Pada contoh ini kami menggunakan persegi panjang dengan radius pembulatan kecil.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

*Why this matters:* Profil menentukan penampang lintang objek 3‑D akhir. Sesuaikan `RoundingRadius`, lebar, atau tinggi untuk mendapatkan siluet yang berbeda.

### Step 2: Apply Linear Extrusion

Sekarang kami menyapu profil sejauh 10 unit sepanjang sumbu Z, menambahkan 100 slice untuk kelancaran, memusatkan geometri, dan menerapkan putaran penuh 360° dengan offset.

```csharp
var extrusion = new LinearExtrusion(profile, 10) { Slices = 100, Center = true, Twist = 360, TwistOffset = new Vector3(10, 0, 0) };
```

*Pro tip:* Mainkan nilai `Slices` untuk menyeimbangkan kinerja vs. kualitas visual, dan bereksperimen dengan `Twist` untuk efek spiral.

### Step 3: Create a Scene

`Scene` berfungsi sebagai wadah untuk semua entitas 3‑D—bayangkan sebagai kanvas.

```csharp
Scene scene = new Scene();
```

### Step 4: Add the Extrusion to the Scene

Lampirkan geometri yang diekstrusi ke node akar scene sehingga menjadi bagian dari hierarki yang dapat dirender.

```csharp
scene.RootNode.CreateChildNode(extrusion);
```

### Step 5: Save the 3‑D Model

Akhirnya, ekspor scene ke file OBJ yang banyak didukung. Ini menunjukkan kemampuan **export 3d model obj** dari Aspose.3D.

```csharp
scene.Save(RunExamples.GetOutputFilePath("LinearExtrusion.obj"), FileFormat.WavefrontOBJ);
```

Saat Anda membuka `LinearExtrusion.obj` yang dihasilkan di penampil 3‑D apa pun, Anda akan melihat prisma persegi panjang berputar—tepat seperti yang dijelaskan oleh kode.

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