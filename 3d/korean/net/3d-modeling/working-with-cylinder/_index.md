---
date: 2026-03-26
description: Aspose.3D for .NET을 사용하여 실린더를 만들고 OBJ 파일을 내보내는 방법을 배워보세요. 이 초보자 친화적인
  가이드는 3D 씬 설정 및 OBJ 내보내기를 다룹니다.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: 전단 바닥이 있는 실린더 만들기 – Aspose.3D for .NET
url: /ko/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Shear Bottom이 있는 실린더 만들기 – Aspose.3D for .NET

## 소개
.NET 환경에서 전단 바닥이 있는 **실린더**가 만드는 방법이 정말 좋다고 생각합니다. 이 튜토리얼에서는 3D 장면 설정부터 최종 모델을 OBJ 파일로 처리하는 단계까지 모든 과정을 안내하므로 **Aspose.3D for .NET**을 사용하여 *초보자 3D 모델링* 기술을 잘라낼 수 있습니다.

## 빠른 답변
- **3D 모델을 시작하기 위해 기본 클래스는 무엇입니까?** `Scene`은 모든 Geo의 컨테이너를 생성합니다.
- **모델을 OBJ로 처리하는 방법은 무엇입니까?** `scene.Save(..., FileFormat.WavefrontOBJ)`.
- **테스트에 참여하는 것이 필요합니까?** 무료 체험판을 이용하실 수 있습니다—FAQ의 체험판 링크를 확인하세요.
- **shear 코너를 파트너로 할 수 있습니까?** 예, `ShearBottom`을 `Vector2` 값으로 수정하면 됩니다.
- **초보자에게 가요?** 물론입니다; API가 저수준 매쉬 처리를 추상화합니다.

## 3D 장면이란 무엇입니까?
*3D 장면*은 모든 부분을 분리하고, 조명, 카메라 및 변환을 포함하는 부분적 컨테이너입니다. Aspose.3D에서 `Scene` 클래스는 모델을 정리하고 나중에는 더 많은 방법을 제공합니다.

## OBJ를 내보내는 이유는 무엇입니까?
OBJ는 많은 3‑D 전용(Blender, Maya, Unity)에서 제외될 수 있는 지원되는 텍스트 기반 전송입니다. OBJ로 인해 .NET 외부에서 실린더 모델을 공유하거나 추가로 편집할 수 있습니다.

## 전제 조건
시작하기 전에 다음을 확인하세요:

- C# 및 .NET 개발에 대한 기본 지식.
- **Aspose.3D for .NET**이 설치되어 있어야 합니다 – **[여기](https://releases.aspose.com/3d/net/) ** 에서 다운로드할 수 있습니다.
- .NET IDE(Visual Studio, Rider, 또는 VS Code)를 코딩합니다.

## 네임스페이스 가져오기
먼저, 필요한 네임스페이스를 범위에 가져와 API 타입을 인식하도록 합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
```

## 1단계: 3D 장면 생성
`Scene` 객체는 모델 계층 구조의 루트 역할을 합니다.

```csharp
Scene scene = new Scene();
```

## 2단계: 원통 1 생성
반지름 2, 높이 10, 그리고 20개의 방사형 세그먼트를 가진 첫 번째 실린더를 생성합니다.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 3단계: 원통 1의 바닥면 경사각 설정
shear 변환을 적용하고, fan‑cylinder 생성을 활성화하며, 원하는 형태를 얻기 위해 다른 속성들을 조정합니다.

```csharp
// Shear 47.5deg in the xy plane (z-axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 4단계: 원통 1을 장면에 추가
변환 트랜슬레이션을 사용하여 첫 번째 실린더를 편리한 위치에 배치합니다.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 5단계: 원통 2 생성
두 번째 실린더는 동일한 기본 치수를 가지지만 맞춤 shear 없이 생성됩니다—나란히 비교하기에 완벽합니다.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 6단계: 원통 2를 장면에 추가
두 번째 실린더를 씬 그래프에 간단히 연결합니다.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 7단계: 장면을 OBJ 파일로 내보내기
마지막으로 전체 씬을 OBJ 파일로 저장하여 모든 표준 3‑D 뷰어에서 열 수 있도록 합니다.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 일반적인 문제 및 해결 방법
| 이슈 | 왜 이런 일이 일어나는가 | 수정 |
|-------|---|----|
| **OBJ 파일이 비어있음** | 씬에 기하학이 적용되지 않았습니다. | `scene.RootNode`에 두 실린더가 모두 추가되어 확인하세요. |
| **Shear가 기분이 나빠졌습니다** | `ShearBottom`은 코너의 탄젠트를 기대합니다. | `Math.Tan(angleInRadians)`를 사용하거나 약 47.5°에 해당하는 `0.83` 값을 사용하세요. |
| **파일이 작동하지 않습니다** | 대처가 잘못되었습니다. | `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`를 사용하세요. |

## 자주 묻는 질문
### Aspose.3D for .NET은 초보자에게 적합합니까?
물론입니다! .NET용 Aspose.3D는 3D 모델의 수학 핵심 부분을 추상화한 고수준 API를 제공하므로 모든 고급 개발자가 쉽게 접근할 수 있습니다.

### 실린더에 다양한 전단 각도를 적용할 수 있나요?
예를 들어, 각 `Cylinder`가 자체적으로 `ShearBottom` 속성을 가지고 있어 마다 고유한 권한을 부여할 수 없습니다.

### 체험판이 있나요?
예, 무료 체험판을 **[여기](https://releases.aspose.com/) ** 에서 받으실 수 있습니다.

### 추가 지원은 어디서 찾을 수 있나요?
커뮤니티 도움, 코드 샘플 및 토론을 위해 **[Aspose.3D 분량](https://forum.aspose.com/c/3d/18) ** 을 방문하세요.

### 임시 라이센스는 어떻게 얻을 수 있나요?
임시 기적을 **[여기](https://purchase.aspose.com/temporary-license/) ** 에서 뵙습니다.

**추가 Q&A**

**Q: 모델을 STL과 같은 다른 형식으로 내보내려면 어떻게 해야 합니까?**
A: `scene.Save` 호출에서 `FileFormat.WavefrontOBJ`를 `FileFormat.STL`로 교체하면 됩니다.

**질문: 원통을 만든 후 애니메이션을 적용할 수 있나요?**
A: 예, Aspose.3D에서 제공하는 `Animation` 클래스를 사용하여 별도의 변형에 키 프레임 애니메이션을 추가할 수 있습니다.

**Q: API는 .NET Core를 지원합니까?**
A: 이 라이브러리는 .NET Core, .NET 5+, .NET 6+와 완전히 호환됩니다.

---

**마지막 업데이트:** 2026-03-26
**테스트 환경:** .NET용 Aspose.3D(최신 릴리스)
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}