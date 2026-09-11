import React from 'react'
import { Link } from 'react-router-dom'

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-100">
      <nav className="w-64 bg-gray-900 text-white p-6">
        <h1 className="text-2xl font-bold mb-8">LexPIL AI</h1>
        <ul className="space-y-4">
          <li>
            <Link to="/" className="hover:text-blue-400 transition">
              Chat
            </Link>
          </li>
          <li>
            <Link to="/analyze" className="hover:text-blue-400 transition">
              Analysis
            </Link>
          </li>
          <li>
            <Link to="/corpus" className="hover:text-blue-400 transition">
              Corpus
            </Link>
          </li>
          <li>
            <Link to="/news" className="hover:text-blue-400 transition">
              News
            </Link>
          </li>
          <li>
            <Link to="/admin" className="hover:text-blue-400 transition">
              Admin
            </Link>
          </li>
        </ul>
      </nav>
      <main className="flex-1 overflow-auto">{children}</main>
    </div>
  )
}

export default Layout
