# Service User Account



## 설명

계정 처리는 아래와 같이 정리 할수있다.

- **계정 리스트**
- **사용자 계정 권한 업데이트**
- **사용자 계정 인적사항 업데이트**

으로 구성되어있습니다.



## 관리



## 계정 리스트

### 파라미터

본인 인증을 진행하기 위한 기본 파라미터는 아래와 같이 구성되어있습니다.

|      파라미터       | Type   | 정보             |
| :-----------------: | ------ | ---------------- |
| Account_Info_Search | String | 사용자 정보 검색 |

### CURL

```shell
curl -X 'GET' \
  'http://account.api.mireu.xyz/v1/admin/account/find?Account_Info_Search={Search}' \
  -H 'accept: application/json'
```


### 결과

```json
[
  {
    "Info": {
      "FirstName": "미르",
      "LastName": "임",
      "Nickname": "Mireu",
      "Phone": "01033107521",
      "Email": "limmireu1214@gmail.com",
      "Join Time": 1674741961.176492
    },
    "Auth": {
      "UID": "9c687c621311ee35c554504133b377908c30cada0ecc1e1c873208f83d09b8db",
      "Authority": {
        "Account": [
          "Write",
          "Read",
          "Delete"
        ],
        "CDN": [
          null
        ],
        "SQL": [
          null
        ],
        "Execpro": [
          null
        ],
        "Hosting": [
          null
        ]
      }
    }
  }
]
```





## 사용자 계정 권한 업데이트

### 파라미터

계정 생성을 위한 기본 파라미터는 아래와 같이 구성되어있다.

| 파라미터           | Type   | 정보                    | 필수여부 |
| ------------------ | ------ | ----------------------- | -------- |
| Appointment_User   | String | 사용자 계정 ID          | T        |
| Account_Update_Set | Enum   | 사용자 관리자 권한 부여 |          |
| CDN_Update_Set     | Enum   | 서비스 권한             |          |
| SQL_Update_Set     | Enum   | 서비스 권한             |          |
| Execpro_Update_Set | Enum   | 서비스 권한             |          |
| Hosting_Update_Set | Enum   | 서비스 권한             |          |



권한에 들어가는 Enum은 아래와 같이 구성되어있다.

| 변수명     | 정보                  |
| ---------- | --------------------- |
| None       | 권한 삭제             |
| Read       | 읽기 권한             |
| Write/Read | 쓰기/읽기 권한        |
| ALL        | 쓰기, 읽기, 삭제 권한 |



### CURL

```shell
curl -X 'PUT' \
  'http://account.api.mireu.xyz/v1/admin/account/auth/update?Appointment_User=[UserID]&Account_Update_Set=[AuthEnum]&CDN_Update_Set=[AuthEnum]&SQL_Update_Set=[AuthEnum]&Execpro_Update_Set=[AuthEnum]' \
  -H 'accept: application/json' \
  -H 'Authorization: [Admin UserID]'
```



### 결과

```json
{
  "msg": "Done."
}
```





## 사용자 계정 인적사항 업데이트

업데이트는 사용자 프로필 정보 수정을 할 수 있다.



### 파라미터

모든 파라미터는 제외할 수 있으므로 상황에 따라서 추가 할 수 있다.

| 파라미터         | Type   | 정보            |
| ---------------- | ------ | --------------- |
| Appointment_User | String | 사용자 계정 ID  |
| Info.LastName    | String | 사용자 이름 성  |
| Info.FirstName   | String | 사용자 이름     |
| Info.Nickname    | String | 사용자 닉네임   |
| Info.Phone       | String | 사용자 전화번호 |



보안을 위해서 SNS시스템과 비밀번호를 변경할수없습니다.



### CURL

```shell
curl -X 'PUT' \
  'http://account.api.mireu.xyz/v1/admin/account/info/update?Appointment_User=[UserID]' \
  -H 'accept: application/json' \
  -H 'Authorization: [Admin UserID]' \
  -H 'Content-Type: application/json' \
  -d '{  
      "Info": {
          "FirstName": "string",
          "LastName": "string",
          "Nickname": "string",
          "Phone": "string"
      }
  }
}'
```



### 결과

```json
{
    "msg" : "Done"
}
```
