const express = require("express");
const { createServer } = require("http");
const { Server } = require("socket.io");

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, { 
        cors: { origin: '*' } 
    });

io.on("connection", (socket) => {
  // console.log("%%connection event%%")
  // console.log('socket id:', socket.id)

  socket.on('message', (text) => {
    const data = {
      "question": text.message,
      "history": [...text.chat_history]
    }
    fetch('http://localhost:8001', {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then((res) => res.json())
      .then((data) => {
        // console.log(data)
        io.emit('message', `${data.answer}}`)
      })
      .catch((error) => console.log(error.message));

    // console.log(text)
    // io.emit('message', `server: u just said ${text.message}`)
  })
});

httpServer.listen(3001);
