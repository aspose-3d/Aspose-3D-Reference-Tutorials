---
title: 사용자 정의 로드 옵션
linktitle: 사용자 정의 로드 옵션
second_title: Aspose.3D .NET API
description: 원활한 3D 모델 로드 및 저장을 위한 최고의 솔루션인 .NET용 Aspose.3D를 살펴보세요.
weight: 15
url: /ko/net/loading-and-saving/custom-load-options/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 사용자 정의 로드 옵션

## 소개

개발자가 3D 파일을 원활하게 사용할 수 있도록 지원하는 강력한 라이브러리인 .NET용 Aspose.3D의 세계에 오신 것을 환영합니다. 이 튜토리얼에서는 사용자 정의 로드 옵션에 중점을 두고 3D 모델 로드 및 저장의 복잡성을 자세히 살펴보겠습니다. 숙련된 개발자이든 초보자이든 이 가이드는 프로세스를 단계별로 안내하여 .NET용 Aspose.3D의 잠재력을 최대한 활용하도록 보장합니다.

## 전제 조건

이 여정을 시작하기 전에 다음과 같은 전제 조건이 갖추어져 있는지 확인하세요.

-  .NET용 Aspose.3D: 라이브러리가 설치되어 있는지 확인하세요. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/).

- 문서 디렉터리: 3D 모델 파일을 저장할 디렉터리를 만듭니다.

이제 필수 사항을 익혔으므로 3D 모델 조작의 흥미로운 세계로 뛰어들어 봅시다!

## 네임스페이스 가져오기

먼저 필요한 네임스페이스를 가져오겠습니다. 이는 Aspose.3D 영역으로의 여정을 위한 무대를 마련할 것입니다.

```csharp
using System;
using System.IO;
using System.Collections.Generic;
using System.Collections;
using Aspose.ThreeD;
using Aspose.ThreeD.Formats;
```

## 로드 및 저장 - 사용자 정의 로드 옵션

### 1단계: Discreet3DS 파일 로드

```csharp
private static void Discreet3DSLoadOption()
{
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();

    //맞춤 옵션 설정
    loadOpts.ApplyAnimationTransform = true;
    loadOpts.FlipCoordinateSystem = true;
    loadOpts.GammaCorrectedColor = true;
    loadOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //로드 옵션을 사용하여 파일 로드
    var scene = Scene.FromFile("test.3ds", loadOpts);
}
```

### 2단계: OBJ 파일 로드

```csharp
private static void ObjLoadOption()
{
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();

    //맞춤 옵션 설정
    loadObjOpts.EnableMaterials = true;
    loadObjOpts.FlipCoordinateSystem = true;
    loadObjOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //로드 옵션을 사용하여 파일 로드
    var scene = Scene.FromFile("test.obj", loadObjOpts);

}
```

### 3단계: STL 파일 로드

```csharp
private static void STLLoadOption()
{
    // 문서 디렉터리의 경로입니다.
    StlLoadOptions loadSTLOpts = new StlLoadOptions();

    //맞춤 옵션 설정
    loadSTLOpts.FlipCoordinateSystem = true;
    loadSTLOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //로드 옵션을 사용하여 파일 로드
    var scene = Scene.FromFile("test.stl", loadSTLOpts);
}
```

### 4단계: U3D 파일 로드

```csharp
private static void U3DLoadOption()
{
    // 문서 디렉터리의 경로입니다.
    string dataDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();

    //맞춤 옵션 설정
    loadU3DOpts.FlipCoordinateSystem = true;
    loadU3DOpts.LookupPaths = new List<string>(new string[] { dataDir });

    //로드 옵션을 사용하여 파일 로드
    var scene = Scene.FromFile("test.u3d", loadU3DOpts);
}
```

### 5단계: glTF 파일 로드

```csharp
private static void glTFLoadOptions()
{
    // 문서 디렉터리의 경로입니다.
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();

    //맞춤 옵션 설정
    loadOpt.FlipTexCoordV = true;
    scene.Open("Duck.gltf", loadOpt);
}
```

### 6단계: PLY 파일 로드

```csharp
private static void PlyLoadOptions()
{
    // 문서 디렉터리의 경로입니다.
    string dataDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();

    //맞춤 옵션 설정
    loadPLYOpts.FlipCoordinateSystem = true;
    scene.Open("vase-v2.ply", loadPLYOpts);
}
```

### 7단계: FBX 파일 로드

```csharp
private static void FBXLoadOptions()
{
    // 문서 디렉터리의 경로입니다.
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions() { KeepBuiltinGlobalSettings = true };

    //맞춤 옵션 설정
    scene.Open("test.FBX", opt);

    // FBX 파일의 GlobalSettings에 정의된 출력 속성
    foreach (Property property in scene.RootNode.AssetInfo.Properties)
    {
        Console.WriteLine(property);
    }
}
```

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 3D 모델을 로드하고 저장하는 복잡한 세계를 성공적으로 탐색했습니다. 이 튜토리얼에서는 다양한 파일 형식과 해당 사용자 정의 로드 옵션을 다루므로 3D 자산을 쉽게 조작할 수 있습니다.

## FAQ

### Q1: Aspose.3D for .NET은 초보자에게 적합합니까?

A1: 물론이죠! .NET용 Aspose.3D는 사용자 친화적인 인터페이스를 제공하므로 모든 수준의 개발자가 액세스할 수 있습니다.

### Q2: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?

A2: 예, .NET용 Aspose.3D는 상업용 라이선스와 함께 제공되므로 프로젝트에서 사용할 수 있습니다.

### Q3: 지원되는 파일 형식에 제한이 있나요?

 A3: .NET용 Aspose.3D는 OBJ, STL, FBX 등을 포함하여 널리 사용되는 다양한 3D 파일 형식을 지원합니다. 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 포괄적인 목록을 보려면

### Q4: 평가판을 사용할 수 있나요?

A4: 예, 다음을 다운로드하여 .NET용 Aspose.3D의 기능을 탐색할 수 있습니다.[무료 시험판](https://releases.aspose.com/).

### Q5: .NET용 Aspose.3D에 대한 지원은 어디서 찾을 수 있습니까?

 A5: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지역 사회 지원 및 지원을 위해.
{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
