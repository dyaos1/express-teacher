"use client";

import { SetStateAction, useEffect, useRef, useState } from "react";
import { socket } from "./socket"
import ChatBox from "./components/ChatBox";
import InputComp from "./components/InputComp";
import Spacer from "./components/Spacer";
import ConSensor from "./components/ConSensor";

export default function Home() {
  const [isConnected, setIsConnected] = useState(false);
  const [transport, setTransport] = useState("N/A");

  useEffect(() => {
    if (socket.connected) {
      onConnect();
    }

    function onConnect() {
      setIsConnected(true);
      setTransport(socket.io.engine.transport.name);

      socket.io.engine.on("upgrade", (transport) => {
        setTransport(transport.name);
      });
    }

    function onDisconnect() {
      setIsConnected(false);
      setTransport("N/A");
    }

    socket.on("connect", onConnect);
    socket.on("disconnect", onDisconnect);

    return () => {
      socket.off("connect", onConnect);
      socket.off("disconnect", onDisconnect);
    };
  }, []);


// 메시지 받기
const [messageText, setMessage] = useState("")

interface Chat {
  text: string
  type: 'client' | 'server'
}

const [transactionMessages, setTransactionMessages] = useState<Chat[]>([])

const sendMessage = () => {
  let chat: Chat = {text: messageText, type: 'client'}
  setTransactionMessages([...transactionMessages, chat])

  // chat history 숫자 제한하기
  let chat_history = []
  const transactionMessagesLen = transactionMessages.length
  if(transactionMessagesLen > 4) {
    chat_history.push(transactionMessages[transactionMessagesLen-4])
    chat_history.push(transactionMessages[transactionMessagesLen-3])
    chat_history.push(transactionMessages[transactionMessagesLen-2])
    chat_history.push(transactionMessages[transactionMessagesLen-1])
  } else {
    chat_history = transactionMessages
  }

  socket.emit('message', {
    'message': messageText,
    'chat_history': chat_history
  })

  setMessage("")
  console.log(transactionMessages)

}

socket.on('message', (return_message) => {
  let chat: Chat = {text: return_message, type: 'server'}
  setTransactionMessages([...transactionMessages, chat])
})

const [Event, setEvent] = useState<any>()


useEffect(() => {
  let Events:any
  let num = 0;
  Events = transactionMessages.map((e:Chat) => {
    num++;
    return <ChatBox chat_text={e.text} chat_type={e.type} key={num.toString()}/>
  })
  
  setEvent(
    Events
  )  
}, [transactionMessages])

// 자동 스크롤 다운 Event를 effect array 에 추가 
useEffect(() => {
  let mySpace = document.getElementById("event-box");
  if(mySpace) {mySpace.scrollTop = mySpace.scrollHeight;}
}, [Event])

return (
  <>
    <p>input question about Express</p>
    <ConSensor status={isConnected}/>
    <div id="event-box" className="h-96 overflow-scroll">
      {Event}
    </div>
    <Spacer />
    <InputComp 
      inputMessage={messageText}
      onChange={(e: { target: { value: SetStateAction<string>; }; }) => {setMessage(e.target.value)}}
      onClick={sendMessage}
      onKeyDown={(e: { key: string; }) => {if(e.key == "Enter") {sendMessage()}}}
    />
  </>
);
}
