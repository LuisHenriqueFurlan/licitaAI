import { Link } from "react-router-dom";

export default function TabelaPregoes({ pregoes }) {

    return (

        <table
            style={{

                width: "100%",
                marginTop: "30px",
                borderCollapse: "collapse"

            }}
        >

            <thead>

                <tr
                    style={{
                        background: "#f2f2f2"
                    }}
                >

                    <th
                        style={{
                            padding: "10px",
                            border: "1px solid #ddd"
                        }}
                    >
                        ID
                    </th>

                    <th
                        style={{
                            padding: "10px",
                            border: "1px solid #ddd"
                        }}
                    >
                        Categoria
                    </th>

                    <th
                        style={{
                            padding: "10px",
                            border: "1px solid #ddd"
                        }}
                    >
                        Score
                    </th>

                    <th
                        style={{
                            padding: "10px",
                            border: "1px solid #ddd"
                        }}
                    >
                        Oportunidade
                    </th>

                </tr>

            </thead>

            <tbody>

                {pregoes.map((p) => (

                    <tr
                        key={p.pregao_id}
                    >

                        <td
                            style={{
                                padding: "10px",
                                border: "1px solid #ddd"
                            }}
                        >

                            <Link
                                to={`/pregao/${p.pregao_id}`}
                            >

                                {p.pregao_id}

                            </Link>

                        </td>

                        <td
                            style={{
                                padding: "10px",
                                border: "1px solid #ddd"
                            }}
                        >
                            {p.categoria}
                        </td>

                        <td
                            style={{
                                padding: "10px",
                                border: "1px solid #ddd"
                            }}
                        >
                            {p.score}
                        </td>

                        <td
                            style={{
                                padding: "10px",
                                border: "1px solid #ddd"
                            }}
                        >
                            {p.oportunidade}
                        </td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}