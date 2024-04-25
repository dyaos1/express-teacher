### note

- enter 치면 input에 입력한 내용 자동으로 submit 되게 하기
```javascript
onKeyDown={(e: { key: string; }) => {if(e.key == "Enter") {sendMessage()}}}
```

- 자동 스크롤 다운 구현
```javascript
useEffect(() => {
  let mySpace = document.getElementById("event-box");
  if(mySpace) {mySpace.scrollTop = mySpace.scrollHeight;}
}, [Event])
```

- TypeError: isValidUTF8 is not a function 에러가 발생
보고된 오류 위치에 webpack-internal:///(ssr)/./node_modules/ws/lib/validation.js:120:53
```
if (!process.env.WS_NO_UTF_8_VALIDATE)
```
가 있어서 환경변수에 WS_NO_UTF_8_VALIDATE를 추가함


- react에서 docker compose 에 세팅된 hostname을 알지 못하는 문제
react는 클라이언트의 브라우저 에서 돌아가므로 도커 내부에 설정된 hostname을 알지 못함
localhost도 마찬가지
따라서 document.location.hostname을 사용해서 backend에 접속해야 하고
backend port도 열어줘야 한다.
ㅋ