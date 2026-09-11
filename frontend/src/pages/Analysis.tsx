import React, { useState } from 'react'
import { useAnalyze } from '../hooks/useAnalyze'

const Analysis: React.FC = () => {
  const [formData, setFormData] = useState({
    party1: '',
    party2: '',
    party1_jurisdiction: '',
    party2_jurisdiction: '',
    dispute_subject: '',
    facts: '',
  })
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const { analyze } = useAnalyze()

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    try {
      const response = await analyze(formData)
      setResult(response)
    } catch (error) {
      console.error('Error analyzing case:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">Case Analysis</h1>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Case Details</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Party 1</label>
                <input
                  type="text"
                  name="party1"
                  value={formData.party1}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Party 1 Jurisdiction</label>
                <input
                  type="text"
                  name="party1_jurisdiction"
                  value={formData.party1_jurisdiction}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                  required
                />
              </div>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Party 2</label>
                <input
                  type="text"
                  name="party2"
                  value={formData.party2}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                  required
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Party 2 Jurisdiction</label>
                <input
                  type="text"
                  name="party2_jurisdiction"
                  value={formData.party2_jurisdiction}
                  onChange={handleChange}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                  required
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Dispute Subject</label>
              <input
                type="text"
                name="dispute_subject"
                value={formData.dispute_subject}
                onChange={handleChange}
                placeholder="e.g., Contract, Tort, Property"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                required
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">Facts</label>
              <textarea
                name="facts"
                value={formData.facts}
                onChange={handleChange}
                rows={6}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
                required
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 transition font-semibold"
            >
              {loading ? 'Analyzing...' : 'Analyze Case'}
            </button>
          </form>
        </div>

        {result && (
          <div className="bg-white rounded-lg shadow p-6 overflow-y-auto max-h-96">
            <h2 className="text-xl font-semibold text-gray-900 mb-4">Analysis Results</h2>
            <pre className="bg-gray-50 p-4 rounded text-sm overflow-x-auto">
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        )}
      </div>
    </div>
  )
}

export default Analysis
