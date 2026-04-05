---
date: 2026-02-25
description: Java에서 Aspose.3D LoadOptions를 사용하여 좌표계를 뒤집고 3D 가져오기를 사용자 정의하는 방법을 배웁니다.
  3DS, OBJ, STL, U3D, glTF, PLY, X 및 선택적인 FBX에 대한 단계별 가이드.
linktitle: Customize 3D File Loading in Java with Aspose.3D LoadOptions
second_title: Aspose.3D Java API
title: 좌표계 뒤집기 – Aspose.3D를 사용한 Java에서 3D 파일 로드 맞춤화
url: /ko/java/load-and-save/customize-3d-file-loading/
weight: 12
---

25 -> "**마지막 업데이트:** 2026-02-25"

**Tested With:** Aspose.3D for Java 24.11 (latest) -> "**테스트 환경:** Aspose.3D for Java 24.11 (latest)"

**Author:** Aspose -> "**작성자:** Aspose"

Now produce final content with all translations.

Check for any missed items: The bullet list under "Why customize 3D import?" we need to keep dash bullet. Good.

Make sure to preserve markdown formatting.

Now produce final answer.{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# 좌표계 뒤집기 – Aspose.3D를 사용한 Java에서 3D 파일 로드 맞춤 설정

끊임없이 변화하는 3D 디자인 및 개발 환경에서 모델을 가져올 때 **좌표계 뒤집기**는 일반적인 요구 사항입니다. 오른손 좌표계에서 왼손 좌표계로 자산을 변환하거나 엔진의 축 규약에 맞게 모델을 정렬해야 할 경우, Aspose.3D for Java는 세밀한 제어를 제공합니다. 이 튜토리얼에서는 Aspose.3D의 `LoadOptions`를 사용하여 **3D 가져오기 맞춤 설정** 방법을 단계별로 안내하며, 3DS, OBJ, STL, U3D, glTF, PLY, X 및 선택적인 FBX와 같은 가장 많이 사용되는 포맷을 다룹니다.

## 빠른 답변
- **“좌표계 뒤집기”가 무엇을 하나요?** 대상 좌표 규약에 맞게 X/Y/Z 축을 교환합니다.  
- **어떤 포맷이 뒤집기를 지원하나요?** 모든 주요 포맷(3DS, OBJ, STL, U3D, glTF, PLY, X, FBX)에서 `setFlipCoordinateSystem` 옵션을 제공합니다.  
- **추가 라이브러리가 필요합니까?** Aspose.3D for Java JAR만 있으면 되며, 외부 변환기는 필요하지 않습니다.  
- **재질을 동시에 로드할 수 있나요?** 예—OBJ 파일의 경우 `setEnableMaterials(true)`를 사용합니다.  
- **프로덕션에 라이선스가 필요합니까?** 비시험 배포에는 유효한 Aspose.3D 라이선스가 필요합니다.

## “좌표계 뒤집기”란 무엇인가요?
좌표계를 뒤집으면 가져온 모델이 사용하는 축의 방향이 바뀝니다. 소스 파일이 렌더링 엔진과 다른 손잡이(오른손 vs. 왼손)를 사용할 때 필수적이며, 모델이 거울상이나 뒤집혀 보이는 것을 방지합니다.

## 왜 3D 가져오기를 맞춤 설정해야 할까요?
- 애니메이션 변환 보존 (`setApplyAnimationTransform`).  
- 색상 처리 보정 (`setGammaCorrectedColor`).  
- `getLookupPaths()`를 통해 외부 리소스 경로 해결.  
- 필요한 부분만 로드하여 메모리 사용량 최적화.

## 사전 요구 사항

- Java 프로그래밍에 대한 기본 이해.  
- 설치된 Java Development Kit (JDK).  
- Aspose.3D for Java 라이브러리를 다운로드했습니다. [여기](https://releases.aspose.com/3d/java/)에서 얻을 수 있습니다.  
- 3DS, OBJ, STL, U3D, glTF, PLY, X, FBX와 같은 3D 파일 포맷에 대한 친숙함.

## 패키지 가져오기

Java 프로젝트에서 필요한 Aspose.3D 패키지를 반드시 import하세요:

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## LoadOptions를 사용한 3D 가져오기 맞춤 설정 방법

다음은 각 지원 포맷에 대해 **좌표계 뒤집기** 옵션을 활성화하는 방법을 보여주는 단계별 코드 스니펫입니다. 스니펫은 프로젝트에 바로 복사해 사용할 수 있으며, `"Your Document Directory"`를 실제 자산 경로로 교체하면 됩니다.

### 단계 1: 3DS 파일 로드 맞춤 설정

```java
public static void discreet3DSLoadOption() {
    String MyDir = "Your Document Directory";
    Discreet3dsLoadOptions loadOpts = new Discreet3dsLoadOptions();
    loadOpts.setApplyAnimationTransform(true);
    loadOpts.setFlipCoordinateSystem(true);
    loadOpts.setGammaCorrectedColor(true);
    loadOpts.getLookupPaths().add(MyDir);
}
```

### 단계 2: OBJ 파일 로드 맞춤 설정

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 단계 3: STL 파일 로드 맞춤 설정

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 단계 4: U3D 파일 로드 맞춤 설정

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 단계 5: glTF 파일 로드 맞춤 설정

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 단계 6: PLY 파일 로드 맞춤 설정

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 단계 7: X 파일 로드 맞춤 설정

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 단계 8: FBX 파일 로드 맞춤 설정 (선택 사항)

```java
private static void FBXLoadOptions() throws IOException {
    String dataDir = "Your Document Directory";
    Scene scene = new Scene();
    FbxLoadOptions opt = new FbxLoadOptions();
    opt.setKeepBuiltinGlobalSettings(true);
    scene.open(dataDir + "test.FBX", opt);
    for(Property property:scene.getRootNode().getAssetInfo().getProperties()) {
        System.out.println(property);
    }
}
```

## 일반적인 문제와 해결책
- **로드 후 모델이 거울상으로 보임** – 올바른 포맷에 대해 `setFlipCoordinateSystem(true)`가 설정되어 있는지 확인하세요.  
- **재질이 누락됨** – OBJ 파일의 경우 `setEnableMaterials(true)`를 설정하고, 재질 파일(.mtl)이 lookup 경로 중 하나에 존재하는지 확인하세요.  
- **텍스처 좌표가 뒤집힘** – glTF의 경우 축을 뒤집는 것 외에 `setFlipTexCoordV(true)`가 필요할 수 있습니다.  
- **파일을 찾을 수 없음 오류** – 외부 리소스(텍스처, 보조 파일) 디렉터리를 `loadOpts.getLookupPaths()`에 추가하세요.

## 결론

Aspose.3D의 `LoadOptions`를 활용하면 거의 모든 주요 포맷에 대해 **좌표계 뒤집기**와 **3D 가져오기 맞춤 설정**을 할 수 있습니다. 이러한 수준의 제어는 후처리 스크립트가 필요 없게 만들고, 자산이 처음부터 올바르게 렌더링되도록 보장합니다.

## 자주 묻는 질문

### Q1: Aspose.3D for Java 문서는 어디에서 찾을 수 있나요?
A1: 문서는 [여기](https://reference.aspose.com/3d/java/)에서 확인할 수 있습니다.

### Q2: Aspose.3D for Java를 어떻게 다운로드하나요?
A2: [여기](https://releases.aspose.com/3d/java/)에서 다운로드할 수 있습니다.

### Q3: 무료 체험판이 있나요?
A3: 예, 무료 체험판은 [여기](https://releases.aspose.com/)에서 이용할 수 있습니다.

### Q4: Aspose.3D for Java 지원은 어디에서 받을 수 있나요?
A4: 지원 포럼은 [여기](https://forum.aspose.com/c/3d/18)에서 확인하세요.

### Q5: 테스트를 위한 임시 라이선스가 필요합니까?
A5: 예, 임시 라이선스는 [여기](https://purchase.aspose.com/temporary-license/)에서 얻을 수 있습니다.

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}

---

**마지막 업데이트:** 2026-02-25  
**테스트 환경:** Aspose.3D for Java 24.11 (latest)  
**작성자:** Aspose