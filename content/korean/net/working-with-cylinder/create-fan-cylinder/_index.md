---
title: 팬 실린더 생성
linktitle: 팬 실린더 생성
second_title: Aspose.3D .NET API
description: .NET용 Aspose.3D로 3D 디자인의 세계를 열어보세요! 멋진 팬 실린더와 팬이 없는 실린더를 손쉽게 만들어 보세요. 지금 평가판을 다운로드하세요.
type: docs
weight: 10
url: /ko/net/working-with-cylinder/create-fan-cylinder/
---
## 소개
.NET용 Aspose.3D를 사용한 3D 모델링 및 시각화의 세계에 오신 것을 환영합니다! 이 단계별 가이드에서는 .NET용 Aspose.3D를 사용하여 매혹적인 팬 실린더를 만드는 방법을 살펴보겠습니다. Aspose.3D는 .NET 애플리케이션에서 3D 콘텐츠 작업을 위한 광범위한 기능을 제공하는 강력한 라이브러리입니다.
## 전제 조건
흥미로운 3D 모델링의 세계에 뛰어들기 전에 다음과 같은 전제 조건이 충족되었는지 확인하세요.
- .NET 프로그래밍에 대한 기본적인 이해.
- 컴퓨터에 Visual Studio가 설치되어 있습니다.
-  다운로드할 수 있는 .NET 라이브러리용 Aspose.3D[여기](https://releases.aspose.com/3d/net/).
- 3D 디자인을 통해 창의력을 발휘하는 데 진정한 관심이 있습니다.
## 네임스페이스 가져오기
.NET 프로젝트에서 Aspose.3D 기능을 사용할 수 있도록 필요한 네임스페이스를 가져오는 것으로 시작해 보겠습니다.
```csharp
using Aspose.ThreeD;
using Aspose.ThreeD.Entities;
using Aspose.ThreeD.Utilities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
// Aspose.3D 네임스페이스 가져오기
```
이제 모든 설정이 완료되었으므로 팬 실린더를 생성하는 프로세스를 관리 가능한 단계로 나누어 보겠습니다.
## 1단계: 장면 만들기
```csharp
// 장면 만들기
Scene scene = new Scene();
```
새로운 3D 장면을 초기화하는 것부터 시작하세요. 이는 팬 실린더에 생명을 불어넣을 캔버스 역할을 합니다.
## 2단계: 팬 실린더 생성
```csharp
// 원통 만들기
var fan = new Cylinder(2, 2, 10, 20, 1, false);
```
반경, 높이, 해상도 등의 매개변수를 지정하여 팬 실린더의 특성을 정의합니다.
## 3단계: 팬 실린더 속성 사용자 정의
```csharp
// GenerateFanCylinder를 true로 설정하십시오.
fan.GenerateFanCylinder = true;
// 세타 길이 설정
fan.ThetaLength = MathUtils.ToRadian(270);
```
팬 부품 생성을 활성화하고 ThetaLength를 사용하여 각도 스윕을 조정하여 팬 실린더를 맞춤화합니다.
## 4단계: 장면에 팬 실린더 배치
```csharp
// 하위 노드 생성
scene.RootNode.CreateChildNode(fan).Transform.Translation = new Vector3(10, 0, 0);
```
팬 원통을 장면의 루트 노드에 하위 노드로 추가하고 3D 공간 내에 배치합니다.
## 5단계: 팬이 없는 실린더 생성
```csharp
// 팬 없이 원통 만들기
var nonfan = new Cylinder(2, 2, 10, 20, 1, false);
```
팬 부분 없이 원통을 만들어 Aspose.3D의 유연성을 살펴보세요.
## 6단계: 팬이 없는 실린더 속성 사용자 정의
```csharp
// generateFanCylinder를 false로 설정하세요.
nonfan.GenerateFanCylinder = false;
// 세타 길이 설정
nonfan.ThetaLength = MathUtils.ToRadian(270);
```
팬 부분의 생성을 비활성화하여 팬이 없는 실린더를 구별합니다.
## 7단계: 장면에 팬이 없는 실린더 배치
```csharp
// 하위 노드 생성
scene.RootNode.CreateChildNode(nonfan);
```
마찬가지로 팬이 없는 원통을 장면의 루트 노드에 하위 노드로 추가합니다.
## 8단계: 장면 저장
```csharp
// 장면 저장
scene.Save("Your Document Directory" + "CreateFanCylinder.obj", FileFormat.WavefrontOBJ);
```
원하는 형식과 위치에 걸작을 저장하세요. 이제 .NET용 Aspose.3D를 사용하여 팬 및 팬이 없는 실린더를 성공적으로 만들었습니다!
## 결론
.NET용 Aspose.3D를 사용한 3D 모델링 실습 가이드를 완료한 것을 축하합니다! 디지털 영역에서 창의력을 발휘하여 팬 실린더와 팬이 아닌 실린더를 쉽게 제작할 수 있습니다.
## 자주 묻는 질문
### 다른 .NET 프레임워크와 함께 .NET용 Aspose.3D를 사용할 수 있습니까?
예, Aspose.3D는 다양한 .NET 프레임워크와 호환되어 개발 프로젝트에 다양성을 제공합니다.
### .NET용 Aspose.3D에 대한 무료 평가판이 있습니까?
 예, 무료 평가판을 사용해 볼 수 있습니다[여기](https://releases.aspose.com/).
### .NET용 Aspose.3D에 대한 자세한 문서는 어디서 찾을 수 있나요?
 문서를 사용할 수 있습니다[여기](https://reference.aspose.com/3d/net/).
### .NET용 Aspose.3D에 대한 지원을 어떻게 받을 수 있나요?
 지원 포럼 방문[여기](https://forum.aspose.com/c/3d/18)커뮤니티와 Aspose 전문가의 도움을 받으세요.
### .NET용 Aspose.3D에 임시 라이선스를 사용할 수 있습니까?
 예, 임시 라이센스를 얻을 수 있습니다[여기](https://purchase.aspose.com/temporary-license/).