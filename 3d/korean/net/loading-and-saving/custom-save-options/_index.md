---
title: 사용자 정의 저장 옵션
linktitle: 사용자 정의 저장 옵션
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D의 강력한 기능을 살펴보세요. Collada, USD, 3DS, FBX, OBJ, STL, U3D, glTF, DRC 및 RVM 형식에 대한 단계별 가이드를 통해 3D 장면 저장을 사용자 정의하는 방법을 알아보세요.
weight: 21
url: /ko/net/loading-and-saving/custom-save-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 사용자 정의 저장 옵션

## 소개

.NET용 Aspose.3D의 세계에 오신 것을 환영합니다! 3D 개발 역량을 강화하고 싶다면 잘 찾아오셨습니다. 이 튜토리얼에서는 특히 사용자 정의 저장 옵션에 중점을 두고 로드 및 저장 기능을 자세히 살펴보겠습니다. .NET용 Aspose.3D는 개발자가 3D 장면을 효율적으로 조작하고 저장할 수 있도록 지원하는 강력한 라이브러리입니다.

## 전제 조건

Aspose.3D의 흥미로운 기능을 탐색하기 전에 다음 전제 조건이 있는지 확인하십시오.

- C# 및 .NET 개발에 대한 기본 이해.
-  .NET 라이브러리용 Aspose.3D가 설치되었습니다. 다음에서 다운로드할 수 있습니다.[릴리스 페이지](https://releases.aspose.com/3d/net/).
- Visual Studio 또는 기타 선호하는 C# IDE를 사용하여 설정된 개발 환경입니다.

## 네임스페이스 가져오기

시작하려면 필요한 네임스페이스를 가져오세요.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using Aspose.ThreeD.Shading;
using System.Drawing;
```

이제 무대를 설정했으므로 튜토리얼을 여러 단계로 나누어 보겠습니다.

## 1단계: Collada 저장 옵션

널리 사용되는 3D 파일 형식인 Collada부터 시작해 보겠습니다. Collada 저장 옵션을 사용자 정의하려면 다음 단계를 따르십시오.

### 1. 디렉토리 설정:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. Collada 저장 옵션 초기화:
   ```csharp
   ColladaSaveOptions saveColladaOpts = new ColladaSaveOptions();
   ```

### 3. 옵션 구성:
   ```csharp
   saveColladaOpts.Indented = true;
   saveColladaOpts.TransformStyle = ColladaTransformStyle.Matrix;
   saveColladaOpts.LookupPaths = new List<string>(new string[] { dataDir });
   ```

## 2단계: Discrete 3DS 저장 옵션

이제 Discreet 3DS와 해당 사용자 정의 옵션을 살펴보겠습니다.

### 1. 디렉토리 설정:
   ```csharp
   string dataDir = "Your Document Directory";
   ```

### 2. 3DS 저장 옵션 초기화:
   ```csharp
   Discreet3dsSaveOptions saveOpts = new Discreet3dsSaveOptions();
   ```

### 3. 옵션 구성:
   ```csharp
   saveOpts.DuplicatedNameCounterBase = 2;
   // 추가 구성 옵션...
   ```

FBX, OBJ, STL, U3D, glTF 및 DRC 저장 옵션에 대해 이 단계별 접근 방식을 계속하여 요구 사항에 따라 각각을 사용자 정의하세요.

## 3단계: glTF 저장 옵션

이제 웹 및 모바일 애플리케이션에서 널리 사용되는 형식인 glTF에 중점을 두겠습니다. 다음 단계에 따라 glTF 저장 옵션을 맞춤설정하세요.

### 1. 장면 객체 초기화:
   ```csharp
   Scene scene = new Scene();
   scene.RootNode.CreateChildNode("sphere", new Sphere());
   ```

### 2. glTF 저장 옵션 설정:
   ```csharp
   GltfSaveOptions opt = new GltfSaveOptions(FileContentType.ASCII);
   opt.EmbedAssets = true;
   opt.UseCommonMaterials = true;
   opt.BufferFile = "mybuf.bin";
   ```

### 3. glTF 파일을 저장합니다:
   ```csharp
   scene.Save("Your Output Directory" + "glTFSaveOptions_out.gltf", opt);
   ```

DRC 및 RVM과 같은 다른 저장 옵션에 대해서도 유사한 구조를 따릅니다.

## 결론

축하해요! .NET용 Aspose.3D의 사용자 정의 저장 옵션을 성공적으로 탐색했습니다. 이 강력한 라이브러리는 3D 장면 저장 프로세스를 맞춤화할 수 있는 다양한 옵션을 제공합니다.

## FAQ

### Q1: 다른 .NET 프레임워크와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?

A1: 예, Aspose.3D는 다양한 .NET 프레임워크와 호환되므로 개발 환경의 유연성을 보장합니다.

### Q2: Aspose.3D에 사용할 수 있는 라이선스 옵션이 있습니까?

 A2: 예, 라이선스 옵션을 탐색할 수 있습니다.[여기](https://purchase.aspose.com/buy).

### Q3: Aspose.3D 관련 쿼리에 대한 지원은 어디서 찾을 수 있나요?

 A3: 다음에서 지원을 요청할 수 있습니다.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18).

### Q4: 무료 평가판이 제공됩니까?

 A4: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q5: Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A5: 임시 라이센스 취득[여기](https://purchase.aspose.com/temporary-license/).
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
