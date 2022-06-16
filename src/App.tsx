import "./App.css";
import { RepositionButton } from "./buttons/RepositionButton";

function App() {
  return (
    <div className="App flex m-0 h-screen w-screen justify-center bg-slate-900">
      {RepositionButton.HoverButton()}
    </div>
  );
}

export default App;
