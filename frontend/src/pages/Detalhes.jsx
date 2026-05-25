import { useEffect,useState } from "react";
import { useParams } from "react-router-dom";
import api from "../services/api";

export default function Detalhes(){

const {id}=useParams();

const [dados,setDados]=useState(null);

useEffect(()=>{

carregar();

},[]);

async function carregar(){

const resposta=await api.get(

`/pregao/${id}`

);

setDados(

resposta.data

);

}

if(!dados){

return <h2>Carregando...</h2>

}

return(

<div style={{

background:"#f5f7fb",
minHeight:"100vh",
padding:"40px"

}}>

<div style={{

maxWidth:"1200px",
margin:"auto"

}}>

<h1 style={{

fontSize:"36px",
marginBottom:"20px"

}}>

Pregão {dados.pregao_id}

</h1>


<div style={{

display:"flex",
gap:"10px",
marginBottom:"25px"

}}>

<span style={badge()}>

{dados.categoria}

</span>

<span style={badge()}>

Score {dados.score}

</span>

<span style={{

...badge(),

background:"#dcfce7"

}}>

{dados.oportunidade}

</span>

</div>


<div style={card()}>

<strong>Resumo</strong>

<p>

{dados.resumo}

</p>

</div>


<h2 style={{

marginTop:"35px"

}}>

Produtos encontrados

</h2>


<div style={{

display:"grid",

gridTemplateColumns:

"repeat(auto-fill,minmax(400px,1fr))",

gap:"20px"

}}>

{

dados.itens?.map(

(item,index)=>(

<div

key={index}

style={card()}

>

<h3>

{item.produto}

</h3>

<hr/>

<p>

<strong>

Governo

</strong>

R${item.valor_governo}

</p>

<p>

<strong>

Mercado

</strong>

R${item.mercado?.menor_preco?.preco}

</p>

<p>

<strong>

Economia

</strong>

R${item.economia}

</p>

<p>

<strong>

Loja

</strong>

{item.mercado?.menor_preco?.loja}

</p>

<p>

<strong>

Produto

</strong>

{item.mercado?.menor_preco?.titulo}

</p>

<a

href={

item.mercado?.menor_preco?.link ||

`https://www.google.com/search?q=${encodeURIComponent(item.produto)}`

}

target="_blank"

rel="noreferrer"

>

<button style={{

padding:"12px",
marginTop:"15px",
border:"none",
borderRadius:"8px",
background:"#2563eb",
color:"white",
cursor:"pointer"

}}>

Ver produto

</button>

</a>

</div>

)

)

}

</div>

</div>

</div>

)

}

function card(){

return{

background:"white",

padding:"25px",

borderRadius:"14px",

boxShadow:"0 2px 8px rgba(0,0,0,.08)"

}

}

function badge(){

return{

background:"#e5e7eb",

padding:"8px 14px",

borderRadius:"20px",

fontWeight:"bold"

}

}