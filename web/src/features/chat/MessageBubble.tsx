import { Message } from './types'

export default function MessageBubble({ message }: { message: Message }) {
  const isUser = message.sender === 'user'
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-xs rounded-xl px-3 py-2 text-sm shadow
          ${isUser ? 'bg-blue-500 text-white' : 'bg-gray-200 text-black'}
        `}
      >
        {message.content}
        {message.status === 'sending' && <span className="ml-2 text-xs text-gray-500">Sending</span>}
        {message.status === 'failed' && <span className="ml-2 text-xs text-red-500">Error</span>}
      </div>
    </div>
  )
}
