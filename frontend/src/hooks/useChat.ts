import axios from 'axios'

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api'

export const useChat = () => {
  const chat = async (message: string) => {
    const response = await axios.post(`${API_BASE_URL}/chat`, {
      message,
      user_id: 1, // TODO: Get from auth
    })
    return response.data
  }

  return { chat }
}
