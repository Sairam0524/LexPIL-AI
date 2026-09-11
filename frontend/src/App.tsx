import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Chat from './pages/Chat'
import Analysis from './pages/Analysis'
import Corpus from './pages/Corpus'
import Admin from './pages/Admin'
import News from './pages/News'

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Chat />} />
          <Route path="/analyze" element={<Analysis />} />
          <Route path="/corpus" element={<Corpus />} />
          <Route path="/news" element={<News />} />
          <Route path="/admin" element={<Admin />} />
        </Routes>
      </Layout>
    </Router>
  )
}

export default App
