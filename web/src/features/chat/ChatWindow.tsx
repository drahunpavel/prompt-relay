import { useAppSelector } from '@/store'
import MessageBubble from './MessageBubble'
import ChatInput from './ChatInput'

export default function ChatWindow() {
  const messages = useAppSelector((s) => s.chat.messages)

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto p-4 space-y-2">
        {messages.map((m) => (
          <MessageBubble key={m.id} message={m} />
        ))}
        {/* {messages.some(m => m.sender === 'bot' && m.status === 'sending') && (
          <div className="text-gray-400 italic">Typing …</div>
        )} */}
      </div>
      <ChatInput />
    </div>
  )
}
