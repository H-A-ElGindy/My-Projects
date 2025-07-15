import { useState } from "react";

export function Counter(){
    
    const[count,setCount]=useState(0)
    
    function increment(){
        setCount(count + 1)
    }

    function decrement(){
        count>0?setCount(count-1):alert('count can not be less than 0')
    }

    return(
        <div className="counter">
            <p>{count}</p>
            <div className="control">
                <button onClick={increment}>+</button>
                <button onClick={decrement}>-</button> 
            </div>
        </div>
    )
}