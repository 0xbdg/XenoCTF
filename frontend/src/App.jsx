import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import LoginPage from './Views/Login.jsx'
import ChallengesPage from "./Views/Challenges.jsx"
import ScoreboardPage from "./Views/Scoreboard.jsx"

function App() {

  return (
    <Router>
        <Routes>
            <Route path='/login' element={<LoginPage/>} />
            <Route path='/' element={<ChallengesPage />} />
            <Route path='/scoreboard' element={<ScoreboardPage />} />
        </Routes> 
    </Router>
  )
}

export default App
