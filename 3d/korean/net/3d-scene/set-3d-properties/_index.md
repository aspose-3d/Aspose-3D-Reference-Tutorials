---
title: 3D 장면에서 3차원 속성 설정
linktitle: 3D 장면에서 3차원 속성 설정
second_title: Aspose.3D .NET API
description: 3D 속성 설정에 대한 .NET 튜토리얼용 Aspose.3D를 살펴보세요. 코드 예제를 통해 단계별로 알아보세요. 3D 장면 조작 기술을 향상시키세요.
weight: 14
url: /ko/net/3d-scene/set-3d-properties/
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 3D 장면에서 3차원 속성 설정

## 소개

매혹적인 3차원 장면을 만들려면 다양한 속성을 조작하고 프로젝트에 깊이와 현실감을 더하는 능력이 필요한 경우가 많습니다. .NET용 Aspose.3D는 이를 달성하기 위한 강력한 도구 세트를 제공하므로 3D 장면 내에서 3차원 속성을 쉽게 설정하고 수정할 수 있습니다. 이 튜토리얼에서는 프로세스를 단계별로 탐색하여 .NET용 Aspose.3D를 효과적으로 활용하는 방법에 대한 이해를 높일 것입니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

-  .NET용 Aspose.3D: .NET 프로젝트에 라이브러리가 설치되어 있는지 확인하세요. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/).

- 문서 디렉터리: 3D 문서를 저장할 디렉터리를 만듭니다.

이제 필수 사항이 준비되었으므로 .NET용 Aspose.3D를 사용하여 3D 장면에서 3차원 속성을 설정하는 프로세스를 살펴보겠습니다.

## 네임스페이스 가져오기

시작하려면 필요한 네임스페이스를 프로젝트로 가져옵니다. 이러한 네임스페이스는 .NET용 Aspose.3D의 3차원 속성 작업에 필요한 클래스와 메서드를 제공합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Shading;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1단계: 3D 장면 로드

3D 장면을 로드하여 시작합니다. 이 예에서는 텍스처가 포함된 FBX 파일을 사용합니다.

```csharp
//ExStart: Load3DScene
string dataDir = "Your Document Directory";
Scene scene = new Scene(dataDir + "EmbeddedTexture.fbx");
//확장: Load3DScene
```

## 2단계: 재료 속성에 액세스

로드된 3D 장면의 재질 속성에 액세스하여 해당 특성을 조작합니다.

```csharp
//ExStart: AccessMaterialProperties
Material material = scene.RootNode.ChildNodes[0].Material;
PropertyCollection props = material.Properties;
//ExEnd: AccessMaterialProperties
```

## 3단계: 모든 속성 나열

foreach 루프 또는 서수 for 루프를 사용하여 재료의 모든 속성을 나열합니다.

```csharp
//ExStart: ListAllProperties
foreach (var prop in props)
{
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}

//또는 서수 for 루프 사용
for (int i = 0; i < props.Count; i++)
{
    var prop = props[i];
    Console.WriteLine("{0} = {1}", prop.Name, prop.Value);
}
//ExEnd: ListAllProperties
```

## 4단계: 이름으로 속성 가져오기 및 수정

이름으로 특정 속성을 검색하고 수정합니다.

```csharp
//ExStart: GetModifyPropertyByName
var diffuse = props["Diffuse"];
Console.WriteLine(diffuse);

//이름으로 속성 값 수정
props["Diffuse"] = new Vector3(1, 0, 1);
//ExEnd: GetModifyPropertyByName
```

## 5단계: 이름으로 속성 인스턴스 가져오기

추가 조작을 위해 이름으로 속성 인스턴스를 검색합니다.

```csharp
//ExStart: GetPropertyInstanceByName
Property pdiffuse = props.FindProperty("Diffuse");
Console.WriteLine(pdiffuse);
//ExEnd: GetPropertyInstanceByName
```

## 6단계: Traverse 속성의 속성

 부터`Property` 에서 상속됩니다`A3DObject`를 사용하면 속성의 속성을 탐색할 수 있습니다.

```csharp
//ExStart: TraversePropertyProperties
Console.WriteLine("Property flags = {0}", pdiffuse.GetProperty("flags"));

//FBX 파일에만 정의된 일부 속성:
Console.WriteLine("Label = {0}", pdiffuse.GetProperty("label"));
Console.WriteLine("Type Name = {0}", pdiffuse.GetProperty("typeName"));

//부동산의 순회가 가능합니다
foreach (var pp in pdiffuse.Properties)
{
    Console.WriteLine("Diffuse.{0} = {1}", pp.Name, pp.Value);
}
//ExEnd: TraversePropertyProperties
```

## 결론

축하해요! 이제 .NET용 Aspose.3D를 사용하여 3D 장면에서 3차원 속성을 설정하는 기술을 마스터했습니다. 다양한 속성과 값을 실험하여 3D 프로젝트에 생기를 불어넣으세요.

## FAQ

### Q1: 다른 3D 파일 형식과 함께 .NET용 Aspose.3D를 사용할 수 있습니까?

A1: 예, Aspose.3D는 FBX, STL 등을 포함한 다양한 3D 파일 형식을 지원합니다.

### Q2: .NET용 Aspose.3D의 임시 라이선스를 어떻게 얻을 수 있나요?

 A2: 방문[여기](https://purchase.aspose.com/temporary-license/) 임시면허를 취득하기 위해

### Q3: Aspose.3D 사용자를 위한 커뮤니티 포럼이 있습니까?

 A3: 예, 다음 사이트에서 지원과 토론을 찾을 수 있습니다.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18).

### Q4: .NET용 Aspose.3D에 대한 자세한 문서는 어디에서 찾을 수 있습니까?

 A4: 다음을 참조하세요.[선적 서류 비치](https://reference.aspose.com/3d/net/) 종합적인 안내를 위해.

### Q5: 구매하기 전에 .NET용 Aspose.3D를 무료로 사용해 볼 수 있나요?

 A5: 물론이죠! 다운로드[무료 평가판](https://releases.aspose.com/) 그 특징을 탐구합니다.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}
