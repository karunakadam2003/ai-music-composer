// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

import React, { useState } from "react";
import axios from "axios";

function App() {
    const [response, setResponse] = useState(null);

    const generateMusic = () => {
        axios.post("http://127.0.0.1:5000/generate-music", {
            genre: "jazz",
            mood: "happy",
            tempo: 120
        }).then(res => setResponse(res.data));
    };

    return (
        <div>
            <h1>AI Music Composer</h1>
            <button onClick={generateMusic}>Generate Music</button>
            {response && <p>{response.message}</p>}
        </div>
    );
}

export default App;
