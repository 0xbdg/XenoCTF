import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import LoginPage from './Views/Login.jsx'
import ChallengesPage from "./Views/Challenges.jsx"
function App() {
  const [count, setCount] = useState(0)

  return (
    <ChallengesPage />
  )
}

export default App
