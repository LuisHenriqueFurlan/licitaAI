export default function Card({titulo,valor}){

    return(

        <div style={{

            border:"1px solid #ddd",
            borderRadius:"10px",
            padding:"20px",
            width:"220px",
            boxShadow:"0px 2px 8px rgba(0,0,0,.1)"

        }}>

            <h3>{titulo}</h3>

            <h1>{valor}</h1>

        </div>

    )

}