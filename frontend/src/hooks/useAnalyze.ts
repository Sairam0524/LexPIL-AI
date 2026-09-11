import axios from 'axios'

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api'

export const useAnalyze = () => {
  const analyze = async (caseData: any) => {
    const response = await axios.post(`${API_BASE_URL}/analyze`, caseData)
    return response.data
  }

  return { analyze }
}
