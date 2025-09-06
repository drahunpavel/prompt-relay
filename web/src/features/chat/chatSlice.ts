import { createSlice, createAsyncThunk, nanoid, PayloadAction } from '@reduxjs/toolkit'
import { transcribeAudio, TranscribeResult } from '@/api/client'
import { Message } from './types'

interface ChatState {
  messages: Message[]
}

const initialState: ChatState = {
  messages: [],
}

export const sendAudioThunk = createAsyncThunk(
  'chat/sendAudio',
  async (file: File) => {
    const result: TranscribeResult = await transcribeAudio(file)
    return result
  }
)

const chatSlice = createSlice({
  name: 'chat',
  initialState,
  reducers: {
    sendMessage: {
      reducer(state, action: PayloadAction<Message>) {
        state.messages.push(action.payload)
      },
      prepare(content: string) {
        return {
          payload: {
            id: nanoid(),
            sender: 'user',
            type: 'text',
            content,
            createdAt: Date.now(),
            status: 'sent',
          } as Message,
        }
      },
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(sendAudioThunk.pending, (state) => {
        state.messages.push({
          id: nanoid(),
          sender: 'bot',
          type: 'text',
          content: '…',
          createdAt: Date.now(),
          status: 'sending',
        })
      })
      .addCase(sendAudioThunk.fulfilled, (state, action) => {
        const msg = state.messages.findLast(m => m.sender === 'bot' && m.status === 'sending')
        if (msg) {
          msg.content = action.payload.text
          msg.status = 'sent'
          msg.meta = {
            language: action.payload.language,
            wawDuration: action.payload.waw_duration,
            transcribeDuration: action.payload.transcribe_duration,
          }
        }
      })
      .addCase(sendAudioThunk.rejected, (state) => {
        const msg = state.messages.findLast(m => m.sender === 'bot' && m.status === 'sending')
        if (msg) {
          msg.content = 'Error receiving response'
          msg.status = 'failed'
        }
      })
  },
})

export const { sendMessage } = chatSlice.actions
export default chatSlice.reducer
