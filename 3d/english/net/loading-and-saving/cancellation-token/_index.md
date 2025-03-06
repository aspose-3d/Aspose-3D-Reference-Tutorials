---
title: Using CancellationToken
linktitle:  Using CancellationToken
second_title: Aspose.3D .NET API
description: Explore the seamless world of 3D modeling with Aspose.3D for .NET. Learn to load and save 3D documents efficiently using CancellationToken.
weight: 10
url: /net/loading-and-saving/cancellation-token/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Using CancellationToken

## Introduction

Welcome to our comprehensive guide on utilizing Aspose.3D for .NET to enhance your 3D modeling and rendering projects. Aspose.3D is a powerful library that empowers .NET developers to seamlessly work with 3D files. In this tutorial, we will delve into the loading and saving aspects, specifically focusing on the usage of CancellationToken for efficient management of asynchronous tasks.

## Prerequisites

Before we embark on this journey, ensure you have the following prerequisites in place:

- Aspose.3D for .NET: Download and install the library from [here](https://releases.aspose.com/3d/net/).
- .NET Environment: Ensure you have a compatible .NET development environment set up.
- Basic Understanding of C#: Familiarity with C# programming language is recommended.

## Import Namespaces

To get started, make sure you include the necessary namespaces in your project. These namespaces will provide access to the functionalities needed for 3D file manipulation.

```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
```

## Loading and Saving - Using CancellationToken

### Step 1: Create CancellationTokenSource

```csharp
// ExStart:CancellationTokenSource

CancellationTokenSource cts = new CancellationTokenSource();
```

Here, we instantiate a CancellationTokenSource, a crucial component for managing cancellation in asynchronous operations.

### Step 2: Initialize 3D Scene

```csharp
Scene scene = new Scene();
```

Create an instance of the Scene class. This will be the canvas for your 3D modeling activities.

### Step 3: Set CancellationToken Timeout

```csharp
cts.CancelAfter(1000);
```

Set the cancellation timeout using the `CancelAfter` method. In this example, the timeout is set to 1000 milliseconds (1 second).

### Step 4: Open 3D Document

```csharp
try
{
    scene.Open("Your Output Directory" + "document.fbx", cts.Token);
    Console.WriteLine("Import is done within 1000ms");
}
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
```

Attempt to open the 3D document within the specified time frame. The `cts.Token` parameter ensures that the operation can be canceled if it exceeds the set timeout.

### Step 5: Handle Import Exception

In case of an ImportException, handle it gracefully by checking if it was caused by an OperationCanceledException.

```csharp
catch (ImportException e)
{
    if (e.InnerException is OperationCanceledException)
    {
        Console.WriteLine("It takes too long time to import, import has been canceled.");
    }
}
// ExEnd:CancellationTokenSource
```

## Conclusion

Congratulations! You've successfully navigated through the process of using Aspose.3D for .NET with CancellationToken to manage the loading of 3D documents. This technique ensures efficient and timely import operations, enhancing the overall performance of your 3D applications.

## FAQ's

### Q1: Is Aspose.3D compatible with all 3D file formats?

A1: Aspose.3D supports a wide range of 3D file formats, including FBX, STL, OBJ, and more. Refer to the [documentation](https://reference.aspose.com/3d/net/) for the complete list.

### Q2: How can I get a temporary license for Aspose.3D?

A2: Obtain a temporary license by visiting [this link](https://purchase.aspose.com/temporary-license/).

### Q3: Where can I find support for Aspose.3D?

A3: Join the community discussion at the [Aspose.3D forum](https://forum.aspose.com/c/3d/18).

### Q4: Can I try Aspose.3D for free before purchasing?

A4: Yes, explore the features with a free trial available [here](https://releases.aspose.com/).

### Q5: What is the latest version of Aspose.3D for .NET?

A5: Stay up-to-date by checking the [download page](https://releases.aspose.com/3d/net/) for the latest release.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
