import React from 'react'

interface SourceCitationsProps {
  citations: string[]
}

const SourceCitations: React.FC<SourceCitationsProps> = ({ citations }) => {
  return (
    <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mt-4">
      <h4 className="font-semibold text-blue-900 mb-2">Source Citations</h4>
      <ul className="space-y-1">
        {citations.map((citation, idx) => (
          <li key={idx} className="text-sm text-blue-700">
            • {citation}
          </li>
        ))}
      </ul>
    </div>
  )
}

export default SourceCitations
