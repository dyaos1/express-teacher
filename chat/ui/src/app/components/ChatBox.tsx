import React from 'react'

interface ChatBoxProps {
    chat_text: string
    chat_type: 'client' | 'server'
}

export default function ChatBox({ chat_text, chat_type }: ChatBoxProps) {

    let wrapperStyle = "flex p-2"    
    let messageStyle = "flex relative float-none p-1.5 rounded"
    if(chat_type === 'client') {
        wrapperStyle += " justify-end"
        messageStyle += " text-black bg-orange-300"
    } else {
        wrapperStyle += " justify-start"
        messageStyle += " text-white bg-neutral-700"
    }
    
    return(
        <div className="block">
            <div className={wrapperStyle}>
                <div className={messageStyle}>
                    <p>{chat_text}</p>
                </div>
            </div>
        </div>
    )
}