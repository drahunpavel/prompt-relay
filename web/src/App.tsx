import { Routes, Route, Navigate } from 'react-router-dom'
import ChatPage from '@/pages/ChatPage'


function App() {
  return (
    <div className="h-screen w-screen flex flex-col bg-gray-100">
      <Routes>
        <Route path="/" element={<Navigate to="/chat" replace />} />
        <Route path="/chat" element={<ChatPage />} />
        {/* <Route path="/login" element={<LoginPage />} /> */}
        {/* <Route path="/settings" element={<SettingsPage />} /> */}
      </Routes>
    </div>
  )
}

export default App
