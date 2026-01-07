---
date: 2026-01-07
description: Aspose.3D for .NET를 사용하여 선형 압출을 수행하면서 지면 평면을 추가하는 방법을 배우고 Wavefront OBJ
  파일을 내보내세요. 3‑D 모델링에서 중심 맞춤 및 바닥 설정 기술을 마스터하세요.
linktitle: Add Ground Plane and Center in Linear Extrusion
second_title: Aspose.3D .NET API
title: 선형 압출에 바닥 평면 및 중심 추가
url: /ko/net/3d-modeling/linear-extrusion/center-in-linear-extrusion/
weight: 10
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 선형 압출에서 바닥 평면 및 중심 추가

## 소개

Aspose.3D for .NET을 사용한 선형 압출 마스터 가이드에 오신 것을 환영합니다. 모델에 **바닥 평면을 추가**하고 **Wavefront OBJ** 파일을 내보내면서 압출을 중앙에 유지하고 싶다면 이곳이 바로 정답입니다. 이 튜토리얼에서는 선형 압출 기법을 살펴보며, 특히 중심 설정과 바닥 평면이 결과를 보다 명확하게 시각화하는 방법에 초점을 맞춥니다.

## 빠른 답변
- **“바닥 평면을 추가”하면 어떤 효과가 있나요?** X‑Z 평면에서 압출이 위치한 위치를 쉽게 확인할 수 있는 시각적 기준을 제공합니다.  
- **모델을 내보내는 형식은 무엇인가요?** 씬은 Wavefront OBJ 파일(`FileFormat.WavefrontOBJ`)로 저장됩니다.  
- **코드를 실행하려면 라이선스가 필요합니까?** 개발 단계에서는 무료 체험판으로 충분하지만, 프로덕션에서는 영구 라이선스가 필요합니다.  
- **압출 길이를 변경할 수 있나요?** 예 – `LinearExtrusion`의 두 번째 매개변수를 수정하면 됩니다.  
- **중심 설정은 선택 사항인가요?** `Center = true`로 설정하면 프로파일을 기준으로 압출이 중앙에 배치되고, `false`이면 한쪽에 정렬됩니다.

## 전제 조건

이 흥미진진한 여정을 시작하기 전에 다음 전제 조건을 확인하세요:

- C# 프로그래밍 언어에 대한 기본 이해.  
- 머신에 Visual Studio가 설치되어 있음.  
- [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/)에서 다운로드할 수 있는 Aspose.3D for .NET 라이브러리.  
- 튜토리얼 전반에 걸쳐 참고할 수 있도록 [Aspose.3D .NET Documentation](https://reference.aspose.com/3d/net/)에 접근 가능해야 합니다.

## 네임스페이스 가져오기

먼저 필요한 네임스페이스를 가져옵니다. 이는 3D 모델링 걸작의 기반을 마련합니다.

```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Profiles;
using Aspose.ThreeD.Utilities;
```

## 단계 1: 기본 프로파일 초기화

압출할 직사각형 프로파일을 정의합니다. `RoundingRadius`는 모서리에 미세한 라운드를 추가합니다.

```csharp
var profile = new RectangleShape()
{
    RoundingRadius = 0.3
};
```

## 단계 2: 3D 씬 생성

`Scene` 객체는 모든 기하, 조명 및 카메라를 담는 컨테이너 역할을 합니다.

```csharp
Scene scene = new Scene();
```

## 단계 3: 좌·우 노드 생성

루트 아래에 두 개의 형제 노드를 생성합니다. 하나는 **중심 없이** 압출을 시연하고, 다른 하나는 **중심을 두고** 압출을 시연합니다. 또한 좌측 노드를 이동시켜 두 예제가 겹치지 않게 합니다.

```csharp
var left = scene.RootNode.CreateChildNode();
var right = scene.RootNode.CreateChildNode();
left.Transform.Translation = new Vector3(5, 0, 0);
```

## 단계 4: 좌측 노드에서 선형 압출 수행 (중심 없음)

프로파일을 중심 없이 압출합니다. `Center = false` 플래그에 주목하세요.

```csharp
left.CreateChildNode(new LinearExtrusion(profile, 2) { Center = false, Slices = 3 });
```

## 단계 5: 좌측 노드에 바닥 평면 추가 (참조용)

얇은 박스를 추가하여 **바닥 평면** 역할을 하게 하면 압출이 기반 위에 어떻게 놓이는지 명확히 볼 수 있습니다.

```csharp
left.CreateChildNode(new Box(0.01, 3, 3));
```

## 단계 6: 우측 노드에서 선형 압출 수행 (중심 있음)

같은 프로파일을 압출하지만 이번에는 중심을 활성화합니다. 기하학은 프로파일 원점을 기준으로 대칭적으로 배치됩니다.

```csharp
right.CreateChildNode(new LinearExtrusion(profile, 2) { Center = true, Slices = 3 });
```

## 단계 7: 우측 노드에 바닥 평면 추가 (참조용)

시각적 비교를 일관되게 유지하기 위해 우측 노드에도 두 번째 바닥 평면을 추가합니다.

```csharp
right.CreateChildNode(new Box(0.01, 3, 3));
```

## 단계 8: Wavefront OBJ 파일 내보내기

마지막으로 **Wavefront OBJ**를 **내보내**어 결과를 표준 3‑D 뷰어에서 열 수 있게 합니다.

```csharp
scene.Save("Your Output Directory" + "CenterInLinearExtrusion.obj", FileFormat.WavefrontOBJ);
```

## 왜 바닥 평면을 추가하나요?

바닥 평면을 추가하면 압출의 높이와 정렬에 대한 즉각적인 시각적 단서를 제공하므로, 중심 여부에 따른 결과를 비교할 때 특히 유용합니다.

## 일반적인 문제 및 팁

- **바닥 평면이 보이지 않음:** `Box` 생성자에서 지정한 두께(`0.01`)가 압출을 가리지 않을 만큼 작지만, 렌더링될 정도로 충분히 큰지 확인하세요.  
- **내보내기 실패:** 출력 디렉터리가 존재하고 쓰기 권한이 있는지 확인하세요.  
- **중심 압출이 오프셋됨:** `Center` 속성을 다시 확인하세요; `true`는 프로파일을 중앙에, `false`는 한쪽에 정렬합니다.

## 자주 묻는 질문

### Q1: Aspose.3D for .NET을 다른 프로그래밍 언어와 함께 사용할 수 있나요?

A1: Aspose.3D는 주로 C# 및 VB.NET과 같은 .NET 언어를 지원합니다.

### Q2: Aspose.3D 관련 문의에 대한 지원은 어디서 받을 수 있나요?

A2: 전용 지원 및 토론을 위해 [Aspose.3D Forum](https://forum.aspose.com/c/3d/18)을 방문하세요.

### Q3: Aspose.3D for .NET의 무료 체험판을 이용할 수 있나요?

A3: 예, 무료 체험판은 [여기](https://releases.aspose.com/)에서 이용할 수 있습니다.

### Q4: Aspose.3D for .NET의 임시 라이선스를 어떻게 얻나요?

A4: 임시 라이선스는 [여기](https://purchase.aspose.com/temporary-license/)에서 획득할 수 있습니다.

### Q5: Aspose.3D for .NET 라이선스는 어디서 구매하나요?

A5: 라이선스는 [여기](https://purchase.aspose.com/buy)에서 구매하세요.

### Q6: OBJ 외에 다른 형식으로 씬을 내보낼 수 있나요?

A6: 예, Aspose.3D는 STL, FBX, GLTF 등 다양한 형식을 지원합니다. `Save` 메서드에서 `FileFormat` 열거형 값을 변경하면 됩니다.

### Q7: 압출의 슬라이스 수를 어떻게 변경하나요?

A7: `LinearExtrusion` 생성자에서 `Slices` 속성을 조정하여 메시 밀도를 제어할 수 있습니다.

---

**마지막 업데이트:** 2026-01-07  
**테스트 환경:** Aspose.3D for .NET 최신 버전  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}