---
title: Loading and Saving -  Using CancellationToken
linktitle: Loading and Saving -  Using CancellationToken
second_title: Aspose.3D .NET API
description: 
type: docs
weight: 10
url: /net/loading-and-saving/cancellation-token/
---

## Complete Source Code
```csharp
using Aspose.ThreeD;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace Aspose._3D.Examples.CSharp.Loading_and_Saving
{
    class CancellationToken
    {
        public static void Run()
        {
            // ExStart:CancellationTokenSource

            CancellationTokenSource cts = new CancellationTokenSource();
            Scene scene = new Scene();
            cts.CancelAfter(1000);
            try
            {
                scene.Open("Your Output Directory"+"document.fbx" , cts.Token);
                Console.WriteLine("Import is done within 1000ms");
            }
            catch (ImportException e)
            {
                if (e.InnerException is OperationCanceledException)
                {
                    Console.WriteLine("It takes too long time to import, import has been canceled.");
                }
            }
            // ExEnd:CancellationTokenSource
        }
    }
}

```
