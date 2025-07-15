import { useState } from 'react'
import {Routes,Route,Link,Outlet} from"react-router-dom"
import './App.css'
import {Header} from "./Components/Header.jsx"
import { StudentCard } from './Components/StudentCard.jsx'
import { StudentList } from './Components/StudentList.jsx'
import { Counter } from './Components/Counter.jsx'
import { Visit_timer } from './Components/VisitTimer.jsx'
import { Home } from './Components/Home.jsx'
import { Posts } from './Components/Posts.jsx'


function App() {
  
  return (
    <>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/dashboard">Students</Link>
        <Link to="/posts">Posts</Link>
      </nav>
      
     {/* Header component */}
     <Header  title="Student Dashboard"/>
     <Routes>
      {/*Home Route with Visit timer */}
      <Route path="/" Component={Home}/>
      {/*Student card embedded in student list */}
      <Route path="/dashboard" element={<StudentList/>}/>
       {/*Posts Route with counter  */}
      <Route path="/posts" element={<Posts/>}/>
    </Routes>
    </>
  )
}

export default App
