import { Visit_timer } from "./VisitTimer"

export function Home(){
    return(
    <div>
        <h1>Home</h1>
    {/*Timer with useEffect, setinterval and useState */}
        <Visit_timer/>
    </div>
    )
}