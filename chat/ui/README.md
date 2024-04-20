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

