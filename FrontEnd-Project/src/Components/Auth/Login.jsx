import React, { useState } from 'react'
import "../Auth/Login.css"
import { useRef } from 'react'
import { useNavigate } from 'react-router-dom'

const Login = () => {
    
    const users=[{'email':'hazem@gmail.com','password':'12345'}]
    localStorage.setItem('users',JSON.stringify(users))

    const [email,setEmail]=useState('')
    const [password,setPass]=useState('')
    
    const nav=useNavigate()
    function handlelogin(ev){
        ev.preventDefault() 
    }

    const stored=JSON.parse(localStorage.getItem('users'))
    
    function checkUsers(){
        try {
            const email_exists=stored.find((user)=>user.email===email).email
            const pass_exists=stored.find((user)=>user.password===password).password
            if(email_exists && pass_exists){
                nav('/')
            }
            
        } catch (error) {
            alert('login failed')
        }
        
    }

    return (
    
        <div className="login-container">
            <form onSubmit={handlelogin}>
                <div className="email-container">
                    <label htmlFor="email">User Email</label>
                    <input type="email" name="email" id="email" placeholder='Enter your email' value={email} onChange={(ev)=>{setEmail(ev.target.value)}} />   
                </div>
                <div className="password-container">
                    <label htmlFor="password">User Password</label>
                    <input type="password" name="password" id="password" placeholder='Enter your password' value={password} onChange={(ev)=>{setPass(ev.target.value)}} />
                </div>
                <div className="remember-forget">
                    <div className="remember">
                        <input type="checkbox" name="remember" id="remember" /> Remember me
                    </div>
                    <div className="forget">
                        <link rel="stylesheet" href="" />Forget Password?
                    </div>
                </div>
                <button id='login' onClick={checkUsers}>Login</button>
            </form>
            <div className="create-account">
                <h4>Don't have account</h4>
                <span>
                    <link rel="stylesheet" href="" />Sign up
                </span>
            </div>
        </div>
   
  )
}

export default Login