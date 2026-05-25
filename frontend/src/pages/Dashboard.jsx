import {useEffect,useState} from "react";
import {Link} from "react-router-dom";

import api from "../services/api";

export default function Dashboard(){

const [pregoes,setPregoes]=useState([]);

useEffect(()=>{

carregarPregoes();

},[]);


async function carregarPregoes(){

try{

const resposta=await api.get(
"/pregoes-governo"
);

setPregoes(
resposta.data.pregoes
);

}
catch(erro){

console.log(
erro
);

}

}


return(

<div style={{

padding:"40px",
background:"#f8fafc",
minHeight:"100vh"

}}>

<h1>

Dashboard LicitaAI

</h1>

<div style={{

display:"grid",
gridTemplateColumns:
"repeat(auto-fill,minmax(300px,1fr))",
gap:"20px"

}}>

{

pregoes.map(

(pregao)=>(

<div

key={pregao.pregao_id}

style={{

background:"white",
padding:"20px",
borderRadius:"15px",
border:"1px solid #e5e7eb"

}}

>

<h2>

{pregao.itens[0]?.produto}

</h2>

<p>

Score: {pregao.score}

</p>

<p>

Categoria:
{pregao.categoria}

</p>

<p>

{pregao.resumo}

</p>

<Link

to={`/pregao/${pregao.pregao_id}`}

>

<button style={{

marginTop:"10px",
padding:"10px",
border:"none",
borderRadius:"8px",
background:"#2563eb",
color:"white"

}}>

Abrir detalhes

</button>

</Link>

</div>

)

)

}

</div>

</div>

)

}