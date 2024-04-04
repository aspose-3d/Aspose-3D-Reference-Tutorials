---
title: Aspose.3D를 사용하여 Java의 현실감 향상을 위해 3D 재료를 PBR로 업그레이드
linktitle: Aspose.3D를 사용하여 Java의 현실감 향상을 위해 3D 재료를 PBR로 업그레이드
second_title: Aspose.3D 자바 API
description: Aspose.3D를 사용하여 Java에서 3D 자료를 PBR로 손쉽게 업그레이드하세요. 시선을 사로잡는 시각적 효과를 위해 향상된 사실성을 달성하세요.
type: docs
weight: 13
url: /ko/java/load-and-save/upgrade-materials-to-pbr/
---
## 소개

3D 자료를 PBR로 업그레이드하는 것은 Java 애플리케이션에서 실제와 같은 시각적 효과를 얻기 위한 혁신적인 단계입니다. Aspose.3D는 이 프로세스를 단순화하여 기존 재료에서 PBR 재료로 원활하게 전환할 수 있도록 합니다. 이 튜토리얼에서는 필수 전제 조건을 살펴보고, 패키지를 가져오고, 각 예제를 세부 단계로 분류합니다.

## 전제 조건

튜토리얼을 시작하기 전에 다음 전제조건이 충족되었는지 확인하십시오.

1.  Java용 Aspose.3D: 다음에서 Aspose.3D 라이브러리를 다운로드하고 설치하세요.[릴리스 페이지](https://releases.aspose.com/3d/java/).

2. Java 개발 환경: 컴퓨터에 Java 개발 환경이 설정되어 있는지 확인하십시오.

3. 문서 디렉터리: 3D 문서 전용 디렉터리를 만듭니다.

## 패키지 가져오기

업그레이드 프로세스를 시작하려면 필요한 패키지를 Java 프로젝트로 가져옵니다. 다음 코드 조각을 가이드로 사용하세요.

```java
import com.aspose.threed.*;
```

해당 기능을 원활하게 활용하려면 필요한 Aspose.3D 패키지를 모두 포함해야 합니다.

## 1단계: 새 3D 장면 초기화

다음 코드를 사용하여 새로운 3D 장면을 초기화하는 것부터 시작하세요.

```java
// ExStart:초기화장면
String MyDir = "Your Document Directory";
Scene s = new Scene();
// 확장:초기화장면
```

## 2단계: PhongMaterial을 사용하여 상자 만들기

3D 상자를 만들고 여기에 PhongMaterial을 할당합니다.

```java
// ExStart:CreateBoxWithMaterial
Box box = new Box();
PhongMaterial mat = new PhongMaterial();
mat.setDiffuseColor(new Vector3(1, 0, 1));
s.getRootNode().createChildNode("box1", box).setMaterial(mat);
// ExEnd:CreateBoxWithMaterial
```

## 3단계: GLTF 2.0 형식으로 저장

장면을 GLTF 2.0 형식으로 저장하고 프로세스 중에 PhongMaterial을 PBRMaterial로 변환합니다.

```java
// ExStart:SaveInGLTF
GltfSaveOptions opt = new GltfSaveOptions(FileFormat.GLTF2);
opt.setMaterialConverter(new MaterialConverter() {
    @Override
    public Material call(Material material) {
        PhongMaterial m = (PhongMaterial) material;
        PbrMaterial ret = new PbrMaterial();
        ret.setAlbedo(m.getDiffuseColor());
        return ret;
    }
});
s.save(MyDir + "Non_PBRtoPBRMaterial_Out.gltf", opt);
// 확장:SaveInGLTF
```

3D 자료를 PBR로 원활하게 업그레이드하여 Java 애플리케이션의 현실감을 높이려면 다음 단계를 꼼꼼하게 따르십시오.

## 결론

결론적으로, Java용 Aspose.3D는 자료를 PBR로 업그레이드하여 3D 그래픽의 시각적 매력을 높일 수 있도록 해줍니다. 이 기술을 활용하여 현실감을 높이고 시각적으로 뛰어난 Java 애플리케이션으로 청중의 마음을 사로잡으세요.

## FAQ

### Q1: Aspose.3D는 Eclipse 이외의 Java 개발 환경과 호환됩니까?

A1: 예, Aspose.3D는 다양한 Java 개발 환경과 호환됩니다.

### Q2: Aspose.3D를 상업용 프로젝트에 사용할 수 있나요?

 A2: 예, 개인 및 상업 프로젝트 모두에 Aspose.3D를 사용할 수 있습니다. 방문하다[구매 페이지](https://purchase.aspose.com/buy) 라이선스 세부정보를 확인하세요.

### Q3: 무료 평가판이 제공됩니까?

A3: 예, 무료 평가판에 액세스할 수 있습니다.[여기](https://releases.aspose.com/).

### Q4: Aspose.3D에 대한 지원은 어디서 찾을 수 있나요?

 A4: 탐색해 보세요.[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 지역 사회 지원을 위해.

### Q5: Aspose.3D에 대한 임시 라이선스를 어떻게 얻나요?

 A5: 방문[이 링크](https://purchase.aspose.com/temporary-license/) 임시 라이센스 정보를 확인하세요.