# Service User Account



## 설명

계정 처리는 아래와 같이 정리 할수있다.

- **계정 서비스 권한**

으로 구성되어있습니다.



## 관리



## 계정 서비스 권한

### 파라미터

본인 인증을 진행하기 위한 기본 파라미터는 아래와 같이 구성되어있습니다.

|      파라미터       | Type   | 정보             |
| :-----------------: | ------ | ---------------- |
| UserID | String | 사용자 ID |

### CURL

```shell
curl -X 'GET' \
  'http://account.api.mireu.xyz/v1/app/account/auth/view' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer [UserID]'
```


### 결과

```json
{
  "Auth": {
    "Authority": {
      "CDN": [
        "Read",
        "Write",
        "Delete"
      ],
      "SQL": [
        "Read",
        "Write",
        "Delete"
      ],
      "Execpro": [
        "Read",
        "Write",
        "Delete"
      ],
      "Hosting": [
        "Read",
        "Write",
        "Delete"
      ],
      "Scientific_Treatise": [
        "On"
      ]
    }
  }
}
```