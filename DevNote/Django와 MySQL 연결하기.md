### Django와 MySQL 연결하기

- `setting.py`의 `DATABASE `부분 수정 필요

- password가 있으므로 다른 파일로 빼서 관리 필요

  ```python
  DATABASES = {
      'default' : {
          'ENGINE': 'django.db.backends.mysql',   
          'NAME': 'db_name',  
          'USER': 'user', 
          'PASSWORD': 'password',
          'HOST': '127.0.0.1',
          'PORT': '3306', 
      }
  }
  ```



- DB 마이그레이션

  ```
  $ python manager.py makemigration
  
  $ python manager,py migrate
  ```



- 발생한 오류
  - `django.db.utils.OperationalError: (1049, "Unknown database 'db name'")`
  - db가 생성되어 있지 않아서 생기는 문제
  - mysql 서버에서 DB 생성 후 연결하면 해결 가능



