---
title: 맞춤형 전단 바닥 실린더
linktitle: 맞춤형 전단 바닥 실린더
second_title: Aspose.3D .NET API
description: 자세한 단계별 가이드를 통해 .NET용 Aspose.3D를 사용하여 맞춤형 전단 바닥 실린더를 만드는 방법을 알아보세요. 지금 3D 모델링 기술을 향상해보세요!
type: docs
weight: 12
url: /ko/net/3d-modeling/working-with-cylinder/
---
## 소개
.NET용 Aspose.3D를 사용하여 맞춤형 실린더를 만드는 방법에 대한 포괄적인 가이드에 오신 것을 환영합니다. 3D 모델링 기술을 향상시키고 프로젝트에 고유한 기능을 추가하려는 경우, 잘 찾아오셨습니다. 이 튜토리얼에서는 명확한 설명과 코드 조각을 사용하여 프로세스를 단계별로 안내합니다.
## 전제 조건
튜토리얼을 시작하기 전에 다음 사항을 확인하세요.
- C# 및 .NET 프로그래밍에 대한 기본 이해.
-  .NET 라이브러리용 Aspose.3D가 설치되었습니다. 당신은 그것을 다운로드 할 수 있습니다[여기](https://releases.aspose.com/3d/net/).
- .NET 프로그래밍을 위해 설정된 개발 환경입니다.
## 네임스페이스 가져오기
C# 코드에서 필요한 네임스페이스를 가져오는 것부터 시작하세요.
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
## 1단계: 장면 만들기
Aspose.3D를 사용하여 3D 장면을 만드는 것으로 시작합니다.
```csharp
Scene scene = new Scene();
```
## 2단계: 원통 1 만들기
첫 번째 원통을 생성하고 해당 속성을 설정합니다.
```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 3단계: 원통 1의 전단 바닥 사용자 정의
첫 번째 원통에 사용자 정의된 전단 바닥 적용:
```csharp
//xy 평면(z축)에서 47.5deg 전단
cylinder1.ShearBottom = new Vector2(0, 0.83); 

// GenerateFanCylinder를 true로 설정하십시오.
cylinder1.GenerateFanCylinder = true;
// 세타 길이 설정
cylinder1.ThetaLength = MathUtils.ToRadian(270);

// 오프셋 상단 설정
cylinder1.OffsetTop = new Vector3(5, 3, 0);
```
## 4단계: 장면에 원통 1 추가
장면에 첫 번째 원통을 추가하고 변환을 설정합니다.
```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```
## 5단계: 원통 2 만들기
비슷한 속성을 가진 두 번째 원통을 생성합니다.
```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```
## 6단계: 장면에 원통 2 추가
사용자 정의된 매개변수 없이 장면에 두 번째 원통을 추가합니다.
```csharp
scene.RootNode.CreateChildNode(cylinder2);
```
## 7단계: 장면 저장
문서 디렉토리에 장면을 Wavefront OBJ 파일로 저장합니다.
```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```
## 결론
축하해요! .NET용 Aspose.3D를 사용하여 사용자 정의된 전단 바닥 실린더를 성공적으로 만들었습니다. 이 튜토리얼의 목적은 3D 모델링 및 프로그래밍에 대한 다양한 수준의 전문 지식을 가진 사용자에게 단계별 가이드를 제공하는 것입니다.
## 자주 묻는 질문
### Aspose.3D for .NET은 초보자에게 적합합니까?
전적으로! .NET용 Aspose.3D는 사용자 친화적인 인터페이스를 제공하므로 초보자와 숙련된 개발자 모두가 접근할 수 있습니다.
### 원통에 다양한 전단 각도를 적용할 수 있나요?
예, 각 실린더의 전단 바닥을 개별적으로 맞춤화하여 독특한 효과를 얻을 수 있습니다.
### 평가판을 사용할 수 있나요?
 예, 무료 평가판을 사용해 볼 수 있습니다[여기](https://releases.aspose.com/).
### 추가 지원은 어디서 찾을 수 있나요?
 방문하다[Aspose.3D 포럼](https://forum.aspose.com/c/3d/18) 커뮤니티 지원 및 토론을 위해.
### 임시 라이센스는 어떻게 얻을 수 있나요?
 임시 면허증을 받으세요[여기](https://purchase.aspose.com/temporary-license/).