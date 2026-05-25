import { useState } from "react";
import axios from "axios";
import { Upload, Trophy } from "lucide-react";
import "./App.css";

function App() {

  const [arquivo, setArquivo] = useState(null);

  const [resultado, setResultado] = useState(null);

  async function enviarPDF() {

    if (!arquivo) {

      alert(
        "Escolha um PDF"
      );

      return;
    }

    const formData = new FormData();

    formData.append(
      "arquivo",
      arquivo
    );

    try {

      const resposta = await axios.post(

        "http://localhost:8000/edital",

        formData

      );

      setResultado(
        resposta.data
      );

    }

    catch (erro) {

      console.log(
        erro
      );

      alert(
        "Erro ao enviar PDF"
      );
    }
  }

  return (

    <div className="container">

      <div className="card">

        <h1>
          LicitaAI
        </h1>

        <p>
          Análise inteligente de editais
        </p>

        <div className="upload">

          <Upload size={25}/>

          <input

            type="file"

            onChange={(e)=>{

              setArquivo(
                e.target.files[0]
              )

            }}

          />

        </div>

        <button
          onClick={enviarPDF}
        >

          Enviar edital

        </button>

      </div>

      {

      resultado && (

      <div className="resultado">

        <div className="card">

          <h2>

            Produto identificado

          </h2>

          <p>

            {

            resultado.analise?.produto

            }

          </p>

        </div>

        <div className="card">

          <h2
          style={{
            display:"flex",
            alignItems:"center",
            gap:"10px"
          }}
          >

          <Trophy/>

          Ranking

          </h2>

          {

          resultado.ranking?.map(

          (
            produto,
            index
          )=>(

          <div

            key={
              produto.produto_id
            }

            className="produto"

          >

          <div
          className="linha"
          >

          <span>

          {

          index===0
          ? "🥇 "

          :

          index===1
          ? "🥈 "

          :

          index===2
          ? "🥉 "

          :

          "• "

          }

          {

          produto.nome

          }

          </span>

          <strong>

          R$

          {

          produto.preco

          }

          </strong>

          </div>

          <div
          className="barra"
          >

          <div

          className="progresso"

          style={{

          width:

          `${produto.compatibilidade}%`

          }}

          >

          </div>

          </div>

          <p>

          {

          produto.compatibilidade

          }%

          compatível

          </p>

          </div>

          ))}

        </div>

      </div>

      )}

    </div>

  );

}

export default App;