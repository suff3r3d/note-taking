import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

import SignUp from '../routes/signup.jsx'
import Homepage from '../routes/homepage.jsx'

import {Routes, Route, BrowserRouter} from "react-router-dom"

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <Routes>
     <Route path='/' element={<Homepage/>}/>
     <Route path='/signup' element={<SignUp/>}/>
    </Routes>
  </BrowserRouter>,
)
