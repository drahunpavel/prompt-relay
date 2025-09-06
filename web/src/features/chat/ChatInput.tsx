import { useState } from 'react'
import { useAppDispatch } from '@/store'
import { sendMessage, sendAudioThunk } from './chatSlice'
import AudioRecorder from './AudioRecorder'

export default function ChatInput() {
  const [text, setText] = useState('')
  const dispatch = useAppDispatch()

  const onSend = () => {
    if (!text.trim()) return
    dispatch(sendMessage(text))
    setText('')
  }

  return (
    <div className="flex items-center border-t p-2 space-x-2">
      <input
        className="flex-1 border rounded p-2"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Write message..."
      />
      <button className="px-3 py-2 bg-blue-500 text-white rounded" onClick={onSend}>
        Send
      </button>
      <AudioRecorder />
    </div>
  )
}
