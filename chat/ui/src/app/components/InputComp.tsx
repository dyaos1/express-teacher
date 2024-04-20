import { useState } from "react"


interface InputCompProps {
  inputMessage: string
  onChange: any
  onClick: any
  onKeyDown: any
}

export default function InputComp({
  inputMessage, onChange, onClick, onKeyDown
}: InputCompProps) {

  return (
    <div className="flex">
      <input 
        className="w-4/5 p-1 text-black"
        value={inputMessage}
        onChange={onChange}
        onKeyDown={onKeyDown}
      /> 
      <input 
        className="w-1/5 bg-neutral-700 rounded mx-1 cursor-pointer" 
        type="submit" 
        value="send"
        onClick={onClick}
      />
    </div>
  )
}