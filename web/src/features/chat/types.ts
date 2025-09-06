export type Sender = 'user' | 'bot'
export type MessageType = 'text' | 'audio'

export interface Message {
  id: string
  sender: Sender
  type: MessageType
  content: string
  createdAt: number
  status?: 'sending' | 'sent' | 'failed'
  meta?: {
    language?: string
    wawDuration?: number
    transcribeDuration?: number
  }
}