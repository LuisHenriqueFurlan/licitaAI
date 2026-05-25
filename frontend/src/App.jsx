import {

BrowserRouter,

Routes,

Route

}

from "react-router-dom";

import Dashboard from "./pages/Dashboard";

import Detalhes from "./pages/Detalhes";


function App(){

return(

<BrowserRouter>

<Routes>

<Route

path="/"

element={<Dashboard/>}

/>

<Route

path="/pregao/:id"

element={<Detalhes/>}

/>

</Routes>

</BrowserRouter>

)

}

export default App;