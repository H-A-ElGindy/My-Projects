import { useState } from "react"
import { StudentCard } from "./StudentCard"


export function StudentList(){
    
    const studentsList=[
        {
            name:"Hazem",
            age:40,
            grade:100
        },
        {
            name:"Ahmed",
            age:35,
            grade:90
        },
        {
            name:"Dina",
            age:28,
            grade:95
        }

    ]
    
    return(
        <div className="students-cards">
        {studentsList?.map((student,index)=>(
           <StudentCard key={index} st_name={student.name} st_age={student.age} st_grade={student.grade}/>
        ))}
        </div>
    )   


}