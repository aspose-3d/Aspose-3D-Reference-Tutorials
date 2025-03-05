---
title: 3D 장면을 압축된 AMF 형식으로 내보내기
linktitle: 압축된 AMF로 장면 내보내기
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D를 사용하여 3D 장면을 압축된 AMF 형식으로 내보내는 방법을 알아보세요. 이 단계별 가이드를 통해 개발 기술을 향상하세요.
type: docs
weight: 11
url: /ko/net/loading-and-saving/amf/export-scene-compressed-amf/
---
## 소개

3D 모델링 및 렌더링의 역동적인 세계에서는 효율성과 유연성이 가장 중요합니다. .NET용 Aspose.3D를 사용하면 개발자는 3D 장면을 압축된 AMF(적층 가공 파일) 형식으로 원활하게 내보내어 품질 저하 없이 최적의 파일 크기를 보장할 수 있습니다. 이 튜토리얼은 프로세스를 단계별로 안내하므로 초보자와 숙련된 개발자 모두 .NET용 Aspose.3D의 기능을 쉽게 활용할 수 있습니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제 조건이 충족되었는지 확인하세요.

- 3D 모델링 개념에 대한 기본 이해
- 컴퓨터에 설치된 Visual Studio
-  .NET 라이브러리용 Aspose.3D. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/)
- 3D 개발 능력을 향상시키고 싶은 욕구!

## 네임스페이스 가져오기

프로젝트에서 .NET용 Aspose.3D의 기능을 활용하는 데 필요한 네임스페이스를 가져와야 합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Formats;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1단계: 3D 장면 로드

.NET용 Aspose.3D를 사용하여 3D 장면을 로드하는 것부터 시작하세요. 장면 개체를 만들고 여기에 상자와 같은 개체를 추가합니다.

```csharp
Scene scene = new Scene();
var box = new Box();
var tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scale = new Vector3(12, 12, 12);
tr.Translation = new Vector3(10, 0, 0);
```

## 2단계: 규모 변환

다음으로 장면의 다른 상자에 크기 조정 변환을 적용합니다.

```csharp
tr = scene.RootNode.CreateChildNode(box).Transform;
tr.Scaling = new Vector3(5, 5, 5);
```

## 3단계: 오일러 각도 설정

변환을 위한 오일러 각도를 설정합니다.

```csharp
tr.EulerAngles = new Vector3(50, 10, 0);
```

## 4단계: 압축된 AMF 파일 저장

마지막으로 3D 장면을 원하는 출력 디렉터리에 압축된 AMF 파일로 저장합니다.

```csharp
scene.Save("Your Output Directory/" + "Aspose.amf", new AmfSaveOptions() { EnableCompression = false });
```

## 결론

축하해요! .NET용 Aspose.3D를 사용하여 3D 장면을 압축된 AMF 형식으로 성공적으로 내보냈습니다. 이 강력한 라이브러리는 3D 개발자에게 가능성의 세계를 열어 효율적이고 시각적으로 놀라운 모델을 만들 수 있도록 해줍니다.

## FAQ

### Q1: Aspose.3D는 널리 사용되는 3D 모델링 소프트웨어와 호환됩니까?

A1: Aspose.3D는 다양한 파일 형식을 지원하므로 널리 사용되는 3D 모델링 도구와 호환됩니다.

### Q2: AMF 외에 다른 파일 형식에 대한 압축을 활성화할 수 있습니까?

A2: 예, Aspose.3D는 다양한 파일 형식에 대한 압축을 활성화하는 옵션을 제공합니다.

### Q3: Aspose.3D는 초보자와 고급 개발자 모두에게 적합합니까?

A3: 물론이죠! Aspose.3D는 초보자를 위한 단순성과 노련한 개발자를 위한 고급 기능을 제공합니다.

### Q4: 내보낼 수 있는 3D 장면의 크기에 제한이 있습니까?

A4: Aspose.3D는 다양한 복잡성의 장면을 처리하도록 설계되었으며 엄격한 크기 제한이 없습니다.

### Q5: 추가 지원 및 커뮤니티 토론은 어디에서 찾을 수 있습니까?

 A5: 다음을 방문하세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지원과 토론을 위해.