export function StudentCard({st_name,st_age,st_grade})
{
    
    return(
        <div className="single-card">
            <h3>Student Name: {st_name}</h3>
            <h3>Student Age: {st_age}</h3>
            <h3>Student Grade: {st_grade}</h3> 
        </div>  
       
    )
}