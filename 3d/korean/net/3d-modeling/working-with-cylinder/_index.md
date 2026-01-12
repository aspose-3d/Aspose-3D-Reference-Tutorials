---
date: 2026-01-12
description: Aspose.3D for .NET를 사용하여 전단 바닥 실린더를 만드는 방법과 3D 모델 OBJ를 내보내는 방법을 배웁니다.
  이 단계별 가이드를 따라 3D 모델링을 마스터하세요.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Aspose.3D for .NET를 사용하여 전단 바닥 원통 만들기
url: /ko/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 맞춤형 전단 바닥 실린더

## 소개
Aspose.3D for .NET을 사용하여 **전단 바닥 실린더** 모델을 만드는 방법을 배우는 포괄적인 가이드에 오신 것을 환영합니다. 게임 에셋, 기계 부품, 시각적 데모 등 무엇을 만들든, 이 튜토리얼에서는 실린더의 바닥을 형태화하고 전단을 적용한 뒤 **3D 모델 OBJ** 파일을 내보내는 과정을 정확히 보여줍니다. 각 단계를 함께 따라가며 몇 분 안에 맞춤형 기하학을 만들 수 있습니다.

## 빠른 답변
- **전단 바닥 실린더란?** 바닥 면이 평평하지 않고 기울어져(전단되어) 있는 실린더입니다.  
- **사용 라이브러리:** Aspose.3D for .NET.  
- **모델을 내보내는 방법:** `scene.Save(..., FileFormat.WavefrontOBJ)` 사용.  
- **라이선스가 필요한가요?** 체험판을 사용할 수 있으며, 상용 제품에는 상업용 라이선스가 필요합니다.  
- **필수 사전 조건:** .NET 개발 환경 및 Aspose.3D NuGet 패키지.

## 전단 바닥 실린더란?
전단 바닥 실린더는 표준 원통형 메쉬의 바닥 면이 전단 연산을 통해 변형된 형태입니다. 이를 통해 정점을 수동으로 편집하지 않고도 각진 베이스, 경사면 또는 맞춤형 연결부를 만들 수 있습니다.

## 이 작업에 Aspose.3D를 사용하는 이유
- **전체 제어**: 반경, 높이, 세그먼트 등 기하학 매개변수를 완벽히 제어합니다.  
- **내장 전단 지원**: `ShearBottom` 속성을 통해 저수준 메쉬 조작 없이 전단을 적용할 수 있습니다.  
- **원클릭 내보내기**: OBJ, FBX, STL 등 인기 포맷으로 한 번에 내보내어 다른 도구와의 연동을 원활하게 합니다.

## 사전 준비
시작하기 전에 다음을 준비하세요:

- C# 및 .NET에 대한 기본 지식.  
- Aspose.3D for .NET이 설치되어 있어야 합니다. **[여기](https://releases.aspose.com/3d/net/)**에서 다운로드할 수 있습니다.  
- .NET 호환 IDE(Visual Studio, Rider, VS Code 등).

## 네임스페이스 가져오기
C# 파일 상단에 필요한 네임스페이스를 가져옵니다:

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

## 단계 1: 씬 생성
먼저 모든 객체를 담을 새로운 3‑D 씬을 인스턴스화합니다.

```csharp
Scene scene = new Scene();
```

## 단계 2: Cylinder 1 생성
전단된 바닥을 적용할 기본 실린더를 생성합니다.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 단계 3: Cylinder 1 전단 바닥 맞춤 설정
전단을 적용하고, 팬 생성 옵션을 활성화하며, 원하는 형태가 나오도록 다른 속성을 조정합니다.

```csharp
// Shear 47.5deg in the xy plane (z‑axis)
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// Set GenerateFanCylinder to true
cylinder1.GenerateFanCylinder = true;
// Set ThetaLength
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// Set OffsetTop
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```

## 단계 4: Cylinder 1을 씬에 추가
맞춤형 실린더를 씬에 배치하고 오른쪽으로 약간 이동시켜 두 객체를 나란히 볼 수 있게 합니다.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## 단계 5: Cylinder 2 생성
비교용으로 두 번째, 일반 실린더를 생성합니다.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## 단계 6: Cylinder 2를 씬에 추가
전단을 적용하지 않은 두 번째 실린더를 추가하여 앞 단계의 효과를 명확히 보여줍니다.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## 단계 7: 씬 저장
마지막으로 전체 씬을 OBJ 파일로 내보내어 Blender, Maya 등 3‑D 뷰어에서 열 수 있게 합니다.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## 일반적인 문제 및 팁
- **전단 값**: `Vector2`는 X와 Y 전단 계수를 받습니다. `0.83` 값은 대략 47.5°에 해당하지만, 원하는 각도에 맞게 조정할 수 있습니다.  
- **내보내기 경로**: 지정한 폴더가 존재하고 쓰기 권한이 있는지 확인하세요. 그렇지 않으면 `scene.Save`가 예외를 발생시킵니다.  
- **성능**: 세그먼트 수가 매우 높은 실린더는 세그먼트 수(`예시에서는 20`)를 줄여 OBJ 파일 크기를 관리 가능한 수준으로 유지하세요.

## 자주 묻는 질문

### Aspose.3D for .NET은 초보자에게 적합한가요?
물론입니다! Aspose.3D for .NET은 사용자 친화적인 API를 제공하여 **초보자**와 숙련된 개발자 모두 쉽게 사용할 수 있습니다.

### 실린더마다 다른 전단 각도를 적용할 수 있나요?
네, 각 실린더의 `ShearBottom`을 개별적으로 설정하여 **고유한 효과**를 만들 수 있습니다.

### 체험판 버전이 있나요?
네, 무료 체험판을 **[여기](https://releases.aspose.com/)**에서 확인할 수 있습니다.

### 추가 지원은 어디서 받을 수 있나요?
커뮤니티 지원 및 토론을 위해 **[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18)**을 방문하세요.

### 임시 라이선스는 어떻게 얻나요?
임시 라이선스를 **[여기](https://purchase.aspose.com/temporary-license/)**에서 받을 수 있습니다.

**추가 Q&A**

**Q: 내보내기 포맷을 FBX로 바꾸려면?**  
A: `scene.Save` 호출에서 `FileFormat.WavefrontOBJ`를 `FileFormat.FBX`로 교체하면 됩니다.

**Q: 내보낸 후 실린더를 애니메이션할 수 있나요?**  
A: OBJ는 애니메이션을 지원하지 않으므로, 애니메이션이 필요하면 FBX 또는 GLTF를 사용하세요.

**Q: 실린더 반경을 더 크게 하고 싶다면?**  
A: `Cylinder` 생성자의 첫 두 매개변수를 조정합니다(예: `new Cylinder(4, 4, …)`).

## 결론
이제 Aspose.3D for .NET을 사용해 **전단 바닥 실린더** 모델을 만들고 OBJ 파일로 내보내는 방법을 마스터했습니다. 다양한 전단 값, 세그먼트 수, 내보내기 포맷을 실험하여 프로젝트에 맞게 활용해 보세요. 즐거운 모델링 되시길 바랍니다!

---

**마지막 업데이트:** 2026-01-12  
**테스트 환경:** Aspose.3D for .NET 24.11 (작성 시 최신 버전)  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}