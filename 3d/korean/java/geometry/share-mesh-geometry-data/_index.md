---
date: 2025-12-12
description: Aspose.3D를 사용하여 Java 3D에서 메쉬 기하학 데이터를 공유하고 장면을 FBX로 저장하면서 재질 색상을 설정하는
  방법을 배웁니다.
linktitle: Set Material Color and Share Mesh Geometry Data in Java 3D with Aspose.3D
second_title: Aspose.3D Java API
title: Aspose.3D를 사용한 Java 3D에서 재질 색상 설정 및 메쉬 기하학 데이터 공유
url: /ko/java/geometry/share-mesh-geometry-data/
weight: 15
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Java 3D에서 Aspose.3D를 사용하여 재질 색상 설정 및 메쉬 기하학 데이터 공유

## 소개

Aspose.3D와 함께 Java 3D의 세계로 여행을 시작하면 놀라운 시각화와 몰입형 경험을 만들 수 있는 무한한 가능성이 열립니다. 이 튜토리얼에서는 Aspose.3D를 사용하여 Java 3D에서 **메쉬를 공유하는 방법**과 각 메쉬 인스턴스에 **재질 색상을 설정하는 방법**을 자세히 안내합니다. 각 단계를 신중히 따라가면 여러 노드 간에 메쉬 데이터를 원활하게 교환하고 색상을 제어하며 FBX로 내보낼 수 있게 됩니다.

## 빠른 답변
- **주요 목표는 무엇인가요?** 각 노드에 재질 색상을 설정하고 메쉬 기하학 데이터를 공유합니다.  
- **필요한 라이브러리는?** Aspose.3D for Java.  
- **결과를 어떻게 내보내나요?** 씬을 FBX 파일(FBX7400ASCII)로 저장합니다.  
- **라이선스가 필요한가요?** 프로덕션 사용을 위해 임시 또는 정식 라이선스가 필요합니다.  
- **어떤 Java 버전을 사용하나요?** Java 8 이상 환경이면 모두 작동합니다.

## 사전 요구 사항

튜토리얼을 시작하기 전에 다음 사전 요구 사항을 확인하세요:

- **Java 개발 환경:** 시스템에 Java 개발 환경이 설정되어 있는지 확인합니다.  
- **Aspose.3D 라이브러리:** Aspose.3D 라이브러리를 다운로드하고 설치합니다. 라이브러리는 [여기](https://releases.aspose.com/3d/java/)에서 찾을 수 있습니다.

## 패키지 가져오기

Java 프로젝트에 필요한 패키지를 가져옵니다. 이 단계는 Aspose.3D 라이브러리가 제공하는 기능에 접근하기 위해 필수입니다.

```java
import com.aspose.threed.*;
```

## 단계 1: 씬 객체 초기화 (initialize scene java)

프로세스를 시작하기 위해 씬 객체를 초기화합니다. 이 객체는 3D 마법이 펼쳐질 캔버스 역할을 합니다.

```java
// Initialize scene object
Scene scene = new Scene();
```

## 단계 2: 색상 벡터 정의

이 단계에서는 3D 씬의 다양한 요소에 적용할 색상 벡터 배열을 정의합니다.

```java
// Define color vectors
Vector3[] colors = new Vector3[] {
    new Vector3(1, 0, 0),
    new Vector3(0, 1, 0),
    new Vector3(0, 0, 1)
};
```

## 단계 3: 폴리곤 빌더를 사용하여 3D 메쉬 Java 생성 (create 3d mesh java)

Common 클래스를 활용해 폴리곤 빌더 메서드로 메쉬를 생성합니다. 이 메쉬가 3D 요소들의 기반이 됩니다.

```java
// Call Common class create mesh using polygon builder method to set mesh instance
Mesh mesh = Common.createMeshUsingPolygonBuilder();
```

## 각 노드에 재질 색상을 설정하는 방법은?

색상 벡터를 순회하면서 큐브 노드를 생성하고 재질, **재질 색상 설정**, 변환 등의 속성을 지정합니다. 이것이 각 메쉬 인스턴스의 시각적 모습을 제어하는 핵심 단계입니다.

```java
int idx = 0;
for(Vector3 color : colors) {
    // Initialize cube node object
    Node cube = new Node("cube");
    cube.setEntity(mesh);
    LambertMaterial mat = new LambertMaterial();
    // Set color
    mat.setDiffuseColor(color);
    // Set material
    cube.setMaterial(mat);
    // Set translation
    cube.getTransform().setTranslation(new Vector3(idx++ * 20, 0, 0));
    // Add cube node
    scene.getRootNode().addChildNode(cube);
}
```

## 단계 5: 3D 씬 저장 (save scene fbx, convert mesh to fbx)

지원되는 파일 형식(FBX7400ASCII)으로 3D 씬을 저장할 디렉터리와 파일명을 지정합니다. 이 단계에서는 **메쉬를 FBX로 변환**하는 방법도 보여줍니다.

```java
// The path to the documents directory.
String MyDir = "Your Document Directory";
MyDir = MyDir + "MeshGeometryData.fbx";

// Save 3D scene in the supported file formats
scene.save(MyDir, FileFormat.FBX7400ASCII);
```

## 결론

축하합니다! 이제 Aspose.3D for Java를 사용해 **재질 색상을 설정**하고, 여러 노드 간에 메쉬 기하학 데이터를 공유했으며, 결과를 FBX 파일로 내보냈습니다. 이를 통해 시각적으로 뛰어나고 인터랙티브한 3D 애플리케이션을 만들 수 있는 무한한 가능성이 열렸습니다.

## FAQ

### Q1: Aspose.3D를 다른 Java 프레임워크와 함께 사용할 수 있나요?

A1: 네, Aspose.3D는 다양한 Java 프레임워크와 원활하게 작동하도록 설계되었습니다.

### Q2: Aspose.3D에 대한 라이선스 옵션이 있나요?

A2: 네, 라이선스 옵션은 [여기](https://purchase.aspose.com/buy)에서 확인할 수 있습니다.

### Q3: Aspose.3D에 대한 지원을 어떻게 받을 수 있나요?

A3: 지원 및 토론을 위해 Aspose.3D [포럼](https://forum.aspose.com/c/3d/18)을 방문하세요.

### Q4: 무료 체험판이 있나요?

A4: 네, 무료 체험판은 [여기](https://releases.aspose.com/)에서 받을 수 있습니다.

### Q5: Aspose.3D의 임시 라이선스를 어떻게 얻나요?

A5: 임시 라이선스는 [여기](https://purchase.aspose.com/temporary-license/)에서 얻을 수 있습니다.

## 추가 자주 묻는 질문

**Q: FBX 외에 다른 형식으로 씬을 내보낼 수 있나요?**  
A: 네, Aspose.3D는 OBJ, STL, 3MF 등 다양한 형식을 지원합니다. `save` 호출 시 `FileFormat` 열거형만 변경하면 됩니다.

**Q: 씬을 만든 후에 재질을 변경하려면 어떻게 하나요?**  
A: 해당 노드를 조회한 뒤 `LambertMaterial`(예: `setDiffuseColor`)을 수정하고 씬을 다시 저장하면 됩니다.

**Q: 라이브러리가 대용량 메쉬를 효율적으로 처리하나요?**  
A: Aspose.3D는 최적화된 데이터 구조를 사용하지만, 매우 큰 메쉬의 경우 스트리밍이나 씬 분할을 고려하는 것이 좋습니다.

**Q: 색상 변화를 애니메이션으로 만들 수 있나요?**  
A: 네, `AnimationController` API를 사용해 재질 속성을 애니메이션화할 수 있습니다.

---

**마지막 업데이트:** 2025-12-12  
**테스트 환경:** Aspose.3D 24.11 for Java  
**작성자:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}