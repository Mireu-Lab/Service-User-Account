# Service User Account



## 설명

계정 처리는 아래와 같이 정리 할수있다.

- **본인 인증**
- **생성**
- **업데이트**
- **삭제**
- **인적정보**
- **계정 찾기**

으로 구성되어있습니다.



## 관리



## 본인 인증

### 파라미터

본인 인증을 진행하기 위한 기본 파라미터는 아래와 같이 구성되어있습니다.

| 파라미터 | Type   | 정보   | 필수여부 |
| :------: | ------ | ------ | -------- |
|  Email   | String | 이메일 | T        |

### CURL

```shell
curl -X 'POST' \
  'http://account.api.mireu.xyz/v1/account/auth?Email=[Email]' \
  -H 'accept: application/json' \
  -d ''
```


### 결과

이메일 전송 처리에 성공시 아래와 같이 출력이 됩니다.

```json
{
  "msg": "Done!"
}
```


이메일 본인인증은 첫 시도후 10분뒤 재시도가 가능하며 재시도 가능한 시간은 아래와 같이 결과가 출력됩니다.

```json
{
  "msg": "Not processed.",
  "Retry Time": "09:56"
}
```



## 계정 생성



**해당 시스템은 인증 토큰이 필요한 프로그램입니다.**



### 파라미터

계정 생성을 위한 기본 파라미터는 아래와 같이 구성되어있다.

| 파라미터       | Type   | 정보            | 필수여부 |
| -------------- | ------ | --------------- | -------- |
| Token          | String | 이메일 인증번호 | T        |
| Password       | String | 비밀번호        | T        |
| Info.LastName  | String | 사용자 이름 성  | T        |
| Info.FirstName | String | 사용자 이름     | T        |
| Info.Nickname  | String | 사용자 닉네임   | T        |
| Info.Phone     | String | 사용자 전화번호 | T        |



### CURL

```shell
curl -X 'POST' \
  'http://account.api.mireu.xyz/v1/account/add?Token=a7e4cf' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Password": "string",
  "Info": {
    "FirstName": "string",
    "LastName": "string",
    "Nickname": "string",
    "Phone": "string"
  }
}'
```



### 결과

```json
{
  "msg": "Done.",
  "UserID": "6f8ef70a36f013f3332ef65240fd86363751119c28661738e63b649a149a1c29"
}
```



결과로는 UserID와 메세지가 출력 된다. 또한 중복되는 계정 인 경우 아래와 같이 출력이 된다.



```json
{
  "msg": "Not processed."
}
```



만약 인증 시간이 지나거나 알맞지 않는 인증번호인 경우 아래와 같이 출력됩니다.



```json
{
  "msg": "Account not found",
  "Auth": "Incorrect authentication information and timed out information"
}
```





## 인적정보 업데이트

업데이트는 사용자 프로필 정보 수정을 할 수 있다.



### 파라미터

모든 파라미터는 제외할 수 있으므로 상황에 따라서 추가 할 수 있다.

| 파라미터       | Type   | 정보            |
| -------------- | ------ | --------------- |
| Info.LastName  | String | 사용자 이름 성  |
| Info.FirstName | String | 사용자 이름     |
| Info.Nickname  | String | 사용자 닉네임   |
| Info.Phone     | String | 사용자 전화번호 |



### CURL

```shell
curl -X 'PUT' \
  'http://account.api.mireu.xyz/v1/account/update' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer asfd' \
  -H 'Content-Type: application/json' \
  -d '{
  "Password": "string",
  "Info": {
    "FirstName": "string",
    "LastName": "string",
    "Nickname": "string",
    "Phone": "string"
  }
}'
```



### 결과

```json
{
    "msg" : "Done"
}
```





## 보안 업데이트

**해당 시스템은 인증 토큰이 필요한 프로그램입니다.**



### 파라미터

모든 파라미터는 제외할 수 있으므로 상황에 따라서 추가 할 수 있다.

| 파라미터        | Type   | 정보        |
| --------------- | ------ | ----------- |
| Token           | String | 사용자 ID   |
| Password        | String | 비밀번호    |
| Sns.SNS_Service | String | 서비스 이름 |
| Sns.UID         | String | OAuth UID   |



### CURL

```shell
curl -X 'PUT' \
  'http://account.api.mireu.xyz/v1/account/auth/update?Token=[Token]' \
  -H 'accept: application/json' \
  -H 'Authorization: [UserID]' \
  -H 'Content-Type: application/json' \
  -d '{
  "Password": "string",
  "Sns": {
    "SNS_Service": "string",
    "UID": "string"
  }
}'
```





### 결과

```json
{
    "msg" : "Done"
}
```

결과로는 처리 메세지가 출력 된다.

또한 이미 처리 된 계정 인 경우 아래와 같이 출력이 된다.



```json
{
  "msg": "Account not found"
}
```



만약 인증 시간이 지나거나 알맞지 않는 인증번호인 경우 아래와 같이 출력됩니다.

```json
{
  "msg": "Account not found",
  "Auth": "Incorrect authentication information and timed out information"
}
```





## 삭제

**해당 시스템은 인증 토큰이 필요한 프로그램입니다.**


계정 삭제는 계정에 대한 접속 권한이 사라질 뿐 이전 데이터에 대한 정보는 보존되어있는 형식으로 구현되어있다.

또한 계정 삭제 후 백업을 할 수 없는 형식으로 구현되어있다.



### 파라미터

| 파라미터 | Type   | 정보            |
| -------- | ------ | --------------- |
| Token    | String | 이메일 인증번호 |


### CURL

```shell
curl -X 'DELETE' \
  'http://account.api.mireu.xyz/v1/account/delete?Token=[Token]' \
  -H 'accept: application/json' \
  -H 'Authorization: [UserID]'
```



### 결과

```json
{
    "msg" : "Done"
}
```

결과로는 처리 메세지가 출력 된다.

또한 이미 처리 된 계정 인 경우 아래와 같이 출력이 된다.



```json
{
  "msg": "Account not found"
}
```



만약 인증 시간이 지나거나 알맞지 않는 인증번호인 경우 아래와 같이 출력됩니다.

```json
{
  "msg": "Account not found",
  "Auth": "Incorrect authentication information and timed out information"
}
```




## 인적 정보

계정에 있는 인적 정보를 출력 해 준다.



### CURL

```shell
curl -X 'GET' \
  'http://account.api.mireu.xyz/v1/account/info' \
  -H 'accept: application/json' \
  -H 'Authorization: [UserID]'
```



### 결과

```json
{
  "Info": {
    "FirstName": "string",
    "LastName": "string",
    "Nickname": "string",
    "Phone": "string",
    "Email": "limmireu1214@gmail.com",
    "Join Time": 1673283405.56986
  }
}
```





## 계정 찾기

**해당 시스템은 인증 토큰이 필요한 프로그램입니다.**

### 파라미터

계정 찾기는 아래와 같은 파라미터로 찾게 된다.

| 파라미터 | Type   | 정보            |
| -------- | ------ | --------------- |
| Token    | String | 이메일 인증번호 |
| Password | String | 비밀번호        |



### CURL

```shell
curl -X 'POST' \
  'http://account.api.mireu.xyz/v1/account/find?Token=[Token]' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Password": "string"
}'
```



### 결과

```json
{
  "UID": "3a599f60a72427450bb5bd6e7d11e084f5a9d09e80959d712c53612046631240"
}
```

결과로는 처리 메세지가 출력 된다.

또한 이미 처리 된 계정 인 경우 아래와 같이 출력이 된다.



```json
{
  "msg": "Account not found"
}
```



만약 인증 시간이 지나거나 알맞지 않는 인증번호인 경우 아래와 같이 출력됩니다.

```json
{
  "msg": "Account not found",
  "Auth": "Incorrect authentication information and timed out information"
}
```

