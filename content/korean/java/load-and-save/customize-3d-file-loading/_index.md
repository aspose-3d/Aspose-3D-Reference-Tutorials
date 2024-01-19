---
title: Aspose.3D LoadOptions를 사용하여 Java에서 3D 파일 로딩 사용자 정의
linktitle: Aspose.3D LoadOptions를 사용하여 Java에서 3D 파일 로딩 사용자 정의
second_title: Aspose.3D 자바 API
description: Aspose.3D 사용자 정의 가능한 LoadOptions를 사용하여 Java에서 3D 파일 로딩을 향상하세요. 3DS, OBJ, STL, U3D, glTF, PLY, X 및 선택적 FBX에 대한 단계별 사용자 정의를 알아보세요.
type: docs
weight: 12
url: /ko/java/load-and-save/customize-3d-file-loading/
---
## 소개

끊임없이 진화하는 3D 디자인 및 개발 환경에서는 3D 파일 형식을 효율적으로 처리하는 것이 중요합니다. Aspose.3D for Java는 다양한 3D 파일 형식의 로딩을 사용자 정의할 수 있는 강력한 솔루션을 제공합니다. 이 튜토리얼은 Aspose.3D의 LoadOptions를 사용하여 Java에서 3D 파일 로딩을 사용자 정의하는 과정을 안내합니다.

## 전제 조건

사용자 정의 프로세스를 시작하기 전에 다음 사항을 확인하세요.

- Java 프로그래밍에 대한 기본 이해.
- JDK(Java 개발 키트)가 설치되었습니다.
-  Java 라이브러리용 Aspose.3D가 다운로드되었습니다. 획득하실 수 있습니다[여기](https://releases.aspose.com/3d/java/).
- 3DS, OBJ, STL, U3D, glTF, PLY, X 및 FBX와 같은 3D 파일 형식에 익숙합니다.

## 패키지 가져오기

Java 프로젝트에서 필요한 Aspose.3D 패키지를 가져와야 합니다.

```java
import com.aspose.threed.*;


import java.io.IOException;
```

## 3D 파일 로딩 사용자 정의

### 1단계: 3DS 파일 로딩 사용자 정의

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

### 2단계: OBJ 파일 로딩 사용자 정의

```java
public static void objLoadOption() {
    String MyDir = "Your Document Directory";
    ObjLoadOptions loadObjOpts = new ObjLoadOptions();
    loadObjOpts.setEnableMaterials(true);
    loadObjOpts.setFlipCoordinateSystem(true);
    loadObjOpts.getLookupPaths().add(MyDir);
}
```

### 3단계: STL 파일 로딩 사용자 정의

```java
public static void stlLoadOption() {
    String MyDir = "Your Document Directory";
    StlLoadOptions loadSTLOpts = new StlLoadOptions();
    loadSTLOpts.setFlipCoordinateSystem(true);
    loadSTLOpts.getLookupPaths().add(MyDir);
}
```

### 4단계: U3D 파일 로딩 사용자 정의

```java
public static void u3dLoadOption() {
    String MyDir = "Your Document Directory";
    U3dLoadOptions loadU3DOpts = new U3dLoadOptions();
    loadU3DOpts.setFlipCoordinateSystem(true);
    loadU3DOpts.getLookupPaths().add(MyDir);
}
```

### 5단계: glTF 파일 로딩 사용자 정의

```java
public static void gltfLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    GltfLoadOptions loadOpt = new GltfLoadOptions();
    loadOpt.setFlipTexCoordV(true);
    scene.open(MyDir + "Duck.gltf", loadOpt);
}
```

### 6단계: PLY 파일 로딩 사용자 정의

```java
public static void plyLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    PlyLoadOptions loadPLYOpts = new PlyLoadOptions();
    loadPLYOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "vase-v2.ply", loadPLYOpts);
}
```

### 7단계: X 파일 로딩 사용자 정의

```java
public static void xLoadOptions() throws IOException {
    String MyDir = "Your Document Directory";
    Scene scene = new Scene();
    XLoadOptions loadXOpts = new XLoadOptions(FileContentType.ASCII);
    loadXOpts.setFlipCoordinateSystem(true);
    scene.open(MyDir + "warrior.x", loadXOpts);
}
```

### 8단계: FBX 파일 로딩 사용자 정의(선택 사항)

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

## 결론

Aspose.3D의 LoadOptions를 사용하여 Java에서 3D 파일 로딩을 사용자 정의하면 개발자가 특정 요구 사항에 맞게 가져오기 프로세스를 맞춤화할 수 있습니다. 애니메이션 변환 조정, 좌표계 뒤집기, 외부 종속성 처리 등 Aspose.3D는 원활한 통합에 필요한 유연성을 제공합니다.

## 자주 묻는 질문

### Q1: Java 설명서용 Aspose.3D는 어디에서 찾을 수 있습니까?

 A1: 문서를 사용할 수 있습니다.[여기](https://reference.aspose.com/3d/java/).

### Q2: Java용 Aspose.3D를 어떻게 다운로드할 수 있나요?

 A2: 다운로드할 수 있습니다[여기](https://releases.aspose.com/3d/java/).

### Q3: 무료 평가판이 제공됩니까?

 A3: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: Java용 Aspose.3D에 대한 지원은 어디서 받을 수 있나요?

 A4: 지원 포럼을 방문하세요.[여기](https://forum.aspose.com/c/3d/18).

### Q5: 테스트하려면 임시 라이센스가 필요합니까?

 A5: 네, 임시 라이센스를 취득하세요[여기](https://purchase.aspose.com/temporary-license/).