# Coffee_House

## Giới thiệu dự án:
1. Tên dự án: Coffee_House
2. Mô tả dự án: Dự án website quán cà phê cho phép người dùng đặt món có trên hệ thống, cho phép admin quản lý được loại sản phẩm, sản phẩm và người dùng trên hệ thống
## Loại dự án:
Dự án nhóm 4 thành viên:
1. 19T1021122_Hoàng Ngọc Long
2. 19T1021138_Đoàn Văn Minh
3. 19T1021119_Trần Văn Lộc
3. 19T1021157_Phan Văn Thành Nhân

### Ngôn ngữ sử dụng:
* HTML
* CSS
* Python

#### FrameWork:
* Bootstrap

##### DB: 
* Sqlite

###### Role Requirement
1. Admin là người quản lý các sản phẩm, loại , duyệt các đơn hàng, xem thông tin người dùng( trừ mật khẩu)
2. Người dùng: xem và mua sản phẩm
###### Function Requirement
<h4>Người dùng</h4>
1. Đăng nhập bằng tên đăng nhập và mật khẩu đã được tạo nếu chưa có thì sang thao tác đăng ký<br><br>
2. Để đăng ký người dùng nhập vào họ tên, tài khoản, số điện thoại( = 10 và không tồn tại trong db), địa chỉ, mật khẩu và nhấn đăng ký<br><br>
3. Chỉnh sửa thông tin người dùng: Sau khi đăng nhập thành công người dùng chọn tên tài khoản ở góc trên bên phải để mở dropdown menu, tại đây người dùng chọn thông tin để chuyển sang trang chỉnh sửa thông tin
sau khi người dùng chỉnh sửa xong ấn thay đổi để lưu<br><br>
4. Lọc sản phẩm theo loại: tại trang chủ người dùng có thể lọc sản phẩm theo cái loại được hiển thị trong navbar loại<br><br>
5. Thêm sản phẩm vào giỏ: tại sản phẩm người dùng chọn thêm vào giỏ hàng để thêm sản phẩm muốn chọn vào giỏ hàng( với sản phẩm được chọn 2 lần trở lên hệ thống sẽ cộng vào số lượng tương ứng với số lần sản phẩm được chọn)<br><br>
6. Giỏ hàng: Tại giỏ hàng người dùng có thể thực hiện các thao tác:
* Chỉnh sửa số lượng<br>
* Xoá sản phẩm khỏi giỏ hàng( xoá 1 hoặc nhiều sản phẩm)<br>
* Thêm sản phẩm khác vào giỏ hàng( khi click hệ thống sẽ chuyển sang trang hiển thị sản phẩm)<br>
* Thanh toán ( đơn hàng sẽ được chuyển sang lịch sử với trạng thái chờ duyệt với đơn hàng chưa giao và đã duyệt với các đơn hàng đã giao)<br><br>
7. Lịch sử: Người dùng có thể xem lại các lịch sử giao dịch trước đó<br><br>
8. Đăng xuất: Để kết thúc phiên làm việc người dùng có thể click vào đăng xuất bên dưới thông tin để tiến hành đăng xuất khỏi hệ thống<br><br>
<h4>Admin</h4>
1. Đăng nhập bằng tên đăng nhập và mật khẩu<br><br>
2. Thêm Loại: admin chọn lựa chọn để mở dropdown menu và chọn thêm loại hệ thống sẽ chuyển sang trang thêm loại, tại đây người dùng chọn thêm loại để xác nhận thêm<br><br>
3. Sửa loại: admin chọn sửa để chuyển sang trang sửa loại, tại đây admin có thể tiến hành sửa tên loại<br><br>
4. Xoá loại: admin có thể chọn xoá để xoá loại khỏi hệ thống<br><br>
5. Thêm sản phẩm:admin chọn thêm sản phẩm để tiến hành thao tác thêm sản phẩm <br><br>
6. Sửa sản phầm:admin chọn sửa để tiến hành sửa sản phẩm được chọn <br><br>
7. Xoá sản phẩm: admin chọn xoá để tiến hành xoá sản phẩm đang được chọn <br><br>
8. Duyệt đơn: admin sẽ duyệt các đơn đã được giao lúc đấy tại trang khách hàng trạng thái đơn sẽ chuyển từ chờ duyệt sang đã giao<br><br>
9. Khách hàng: tại đây admin có thể xem được các thông tin khách hàng trừ mật khẩu đã được hash nên admin không thể xem được

###### Cấu trúc Reposity:
1. admin : chứa các model,form,routes liên quan đến admin
2. khachhang : chứa các model,form,routes liên quan đến người dùng
3. sanpham : chứa các model,form,routes liên quan đến sản phẩm
4. static : chứa các file css,js,bootstrap
5. templates: chứa các file html hiển thị
6. saleapp.db : db của dự án chạy bằng sqlite
7. requirement: file chứa các thư viện flask được dùng trong dự án

## Demo:
![image](https://user-images.githubusercontent.com/109198894/210400126-755ef849-14a2-4728-8623-32a7282f7a4c.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/109198894/210400403-3512fb19-9fd9-401e-8f75-05ccee1c8305.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/109198894/210400501-2286b23e-d2f2-4375-afb9-cd6d0b7e79bb.png)
<br><br><br>
![image](https://user-images.githubusercontent.com/109198894/210400644-0e98d2ba-c2d5-4322-b083-c1ec538d0c50.png)
