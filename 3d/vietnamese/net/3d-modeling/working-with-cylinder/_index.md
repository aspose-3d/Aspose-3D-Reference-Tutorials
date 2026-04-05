---
date: 2026-03-26
description: Tìm hiểu cách tạo hình trụ và xuất tệp OBJ bằng Aspose.3D cho .NET. Hướng
  dẫn thân thiện với người mới này bao gồm việc thiết lập cảnh 3D và xuất OBJ.
linktitle: Customized Shear Bottom Cylinder
second_title: Aspose.3D .NET API
title: Cách tạo hình trụ với đáy cắt nghiêng – Aspose.3D cho .NET
url: /vi/net/3d-modeling/working-with-cylinder/
weight: 12
---

{{< blocks/products/pf/main-wrap-class >}}
{{< blocks/products/pf/main-container >}}
{{< blocks/products/pf/tutorial-page-section >}}

# Cách Tạo Hình Trụ với Đáy Cắt Xén – Aspose.3D cho .NET

## Giới thiệu
Nếu bạn đang thắc mắc **cách tạo hình trụ** với đáy cắt xén tùy chỉnh trong môi trường .NET, bạn đã đến đúng nơi. Trong hướng dẫn này, chúng tôi sẽ đi qua từng bước — từ thiết lập cảnh 3‑D đến xuất mô hình cuối cùng dưới dạng tệp OBJ — để bạn có thể nâng cao kỹ năng *mô hình 3D cho người mới bắt đầu* bằng **Aspose.3D cho .NET**.

## Trả lời nhanh
- **Lớp chính để bắt đầu một mô hình 3D là gì?** `Scene` tạo container gốc cho tất cả các hình học.  
- **Phương thức nào xuất mô hình sang OBJ?** `scene.Save(..., FileFormat.WavefrontOBJ)`.  
- **Có cần giấy phép để thử nghiệm không?** Có bản dùng thử miễn phí — xem liên kết dùng thử trong phần Câu hỏi thường gặp.  
- **Tôi có thể thay đổi góc cắt xén không?** Có, chỉnh sửa `ShearBottom` bằng giá trị `Vector2`.  
- **Điều này có phù hợp cho người mới bắt đầu không?** Chắc chắn; API trừu tượng hoá việc xử lý lưới cấp thấp.

## Cảnh 3D là gì?
Một *cảnh 3D* là một container phân cấp chứa tất cả các thực thể hình học, đèn, camera và các phép biến đổi. Trong Aspose.3D, lớp `Scene` cung cấp cách sạch sẽ để tổ chức và sau này xuất các mô hình của bạn.

## Tại sao xuất OBJ?
OBJ là một định dạng dựa trên văn bản, được hỗ trợ rộng rãi mà nhiều ứng dụng 3‑D (Blender, Maya, Unity) có thể nhập. Xuất sang OBJ cho phép bạn chia sẻ hoặc chỉnh sửa thêm các mô hình trụ của mình bên ngoài .NET.

## Yêu cầu trước
Trước khi bắt đầu, hãy chắc chắn rằng bạn có:

- Kiến thức cơ bản về C# và phát triển .NET.  
- **Aspose.3D cho .NET** đã được cài đặt – bạn có thể tải xuống **[tại đây](https://releases.aspose.com/3d/net/)**.  
- Một IDE .NET (Visual Studio, Rider, hoặc VS Code) sẵn sàng để lập trình.

## Nhập các Namespace
Đầu tiên, đưa các namespace cần thiết vào phạm vi để các kiểu API được nhận diện.

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

## Bước 1: Tạo một Cảnh 3D
Đối tượng `Scene` hoạt động như nút gốc của cây mô hình của bạn.

```csharp
Scene scene = new Scene();
```

## Bước 2: Tạo Trụ 1
Chúng ta tạo trụ đầu tiên với bán kính 2, chiều cao 10 và 20 đoạn vòng tròn.

```csharp
var cylinder1 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Bước 3: Tùy chỉnh Đáy Cắt Xén cho Trụ 1
Áp dụng phép biến đổi cắt xén, bật chế độ tạo trụ‑quạt, và điều chỉnh các thuộc tính khác để đạt được hình dạng mong muốn.

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

## Bước 4: Thêm Trụ 1 vào Cảnh
Đặt trụ đầu tiên ở vị trí thuận tiện bằng phép biến đổi dịch chuyển.

```csharp
scene.RootNode.CreateChildNode(cylinder1).Transform.Translation = new Vector3(10, 0, 0);
```

## Bước 5: Tạo Trụ 2
Một trụ thứ hai được tạo với cùng kích thước cơ bản nhưng không có cắt xén tùy chỉnh — hoàn hảo để so sánh bên cạnh nhau.

```csharp
var cylinder2 = new Cylinder(2, 2, 10, 20, 1, false);
```

## Bước 6: Thêm Trụ 2 vào Cảnh
Chúng ta chỉ cần gắn trụ thứ hai vào đồ thị cảnh.

```csharp
scene.RootNode.CreateChildNode(cylinder2);
```

## Bước 7: Xuất Cảnh dưới dạng Tệp OBJ
Cuối cùng, chúng ta lưu toàn bộ cảnh vào tệp OBJ để có thể mở trong bất kỳ trình xem 3‑D tiêu chuẩn nào.

```csharp
scene.Save("Your Document Directory" + "CustomizedShearBottomCylinder.obj", FileFormat.WavefrontOBJ);
```

## Các vấn đề thường gặp và giải pháp
| Vấn đề | Nguyên nhân | Giải pháp |
|-------|-------------|----------|
| **File OBJ rỗng** | Cảnh không có hình học nào được gắn. | Đảm bảo cả hai hình trụ đều được thêm vào `scene.RootNode`. |
| **Cắt xén không đúng** | `ShearBottom` yêu cầu giá trị tang của góc. | Sử dụng `Math.Tan(angleInRadians)` hoặc giá trị `0.83` đã cung cấp cho khoảng ~47,5°. |
| **Lỗi đường dẫn tệp** | Thư mục không hợp lệ hoặc thiếu. | Sử dụng `Path.Combine(Environment.CurrentDirectory, "CustomizedShearBottomCylinder.obj")`. |

## Câu hỏi thường gặp
### Aspose.3D cho .NET có phù hợp cho người mới bắt đầu không?
Chắc chắn! Aspose.3D cho .NET cung cấp một API cấp cao trừu tượng hoá các phần toán học nặng của mô hình 3‑D, giúp dễ tiếp cận với các nhà phát triển ở mọi trình độ.

### Tôi có thể áp dụng các góc cắt xén khác nhau cho các hình trụ không?
Có, mỗi thể hiện `Cylinder` có thuộc tính `ShearBottom` riêng, vì vậy bạn có thể gán góc duy nhất cho từng đối tượng.

### Có phiên bản dùng thử không?
Có, bạn có thể khám phá bản dùng thử miễn phí **[tại đây](https://releases.aspose.com/)**.

### Tôi có thể tìm hỗ trợ bổ sung ở đâu?
Truy cập **[diễn đàn Aspose.3D](https://forum.aspose.com/c/3d/18)** để nhận trợ giúp từ cộng đồng, mẫu mã và thảo luận.

### Làm thế nào để tôi có được giấy phép tạm thời?
Nhận giấy phép tạm thời **[tại đây](https://purchase.aspose.com/temporary-license/)**.

**Câu hỏi & Trả lời bổ sung**

**H: Làm sao để xuất mô hình sang định dạng khác, như STL?**  
Đ: Thay `FileFormat.WavefrontOBJ` bằng `FileFormat.STL` trong lời gọi `scene.Save`.

**H: Tôi có thể tạo hoạt ảnh cho các hình trụ sau khi tạo không?**  
Đ: Có, bạn có thể thêm hoạt ảnh khung key cho các biến đổi node bằng các lớp `Animation` do Aspose.3D cung cấp.

**H: API có hỗ trợ .NET Core không?**  
Đ: Thư viện hoàn toàn tương thích với .NET Core, .NET 5+ và .NET 6+.

---

**Cập nhật lần cuối:** 2026-03-26  
**Đã kiểm tra với:** Aspose.3D cho .NET (phiên bản mới nhất)  
**Tác giả:** Aspose  

{{< /blocks/products/pf/tutorial-page-section >}}

{{< /blocks/products/pf/main-container >}}
{{< /blocks/products/pf/main-wrap-class >}}

{{< blocks/products/products-backtop-button >}}