# Cài đặt và xử lý lỗi thường gặp

## Yêu cầu

- Python 3.10–3.12
- Git
- 2 GB RAM trống là đủ cho các bài hiện tại

## Cài đặt

```bash
git clone https://github.com/HongQuang26/data-science-from-zero.git
cd data-science-from-zero
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Trong Jupyter, chọn kernel `.venv` nếu được hỏi. Nếu thư viện import không được, kiểm tra thanh kernel trong notebook rồi chạy `python -m pip install -r requirements.txt` khi môi trường `.venv` đã được kích hoạt.

## Làm việc trong fork

```bash
git checkout -b learn/module-01
git add 01-python-foundations
git commit -m "complete module 01 exercises"
git push origin learn/module-01
```

Không đưa token, file `.env`, dữ liệu khách hàng hoặc dataset có thông tin cá nhân vào fork công khai.
