import { useEffect } from "react"
import { useState } from 'react';

export function Visit_timer(){
    
    const [timer, setTimer] = useState(0)
    
    useEffect(()=>
        {
        const timerid= setInterval(()=>{setTimer(prev => prev + 1)},1000)
        
        return ()=> clearInterval(timerid)
    },[])

    return(
        <p className="visit">{timer}</p>
    )
}