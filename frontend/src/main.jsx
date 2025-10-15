import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

import Templates from "./Components/Templates.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Templates>
        <App />
    </Templates>
  </StrictMode>
)
