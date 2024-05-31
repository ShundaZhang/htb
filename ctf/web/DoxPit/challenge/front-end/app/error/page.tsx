import AsciiArt from "../asciiart";
import { NavBar } from "../navbar";

import "bootstrap/dist/css/bootstrap.min.css";

export default function Home() {
    return (
        <main className="main">
            <NavBar />
            <div className="container">
                <AsciiArt type={"oni"} />
                <div className="row text-center mt-4">
                    <div className="col">
                        <AsciiArt type={"text"} />
                    </div>
                </div>
            </div>
        </main>
    );
}