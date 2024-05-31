"use client";

import { NavBar } from "../navbar";
import AsciiArt from "../asciiart";

const actors = [
    {
        "title": "diogt",
        "description": "Loves hardware a bit too much.",
    },
    {
        "title": "xclow3n",
        "description": "Well known in the community for his totally \"ironic\" jokes."
    },
    {
        "title": "WizardAlfredo",
        "description": "Has spent life savings on custom keyboards and accesories."
    },
    {
        "title": "canopus",
        "description": "Master PHD in stego challenges."
    },
    {
        "title": "w3th4nds",
        "description": "Willing to do questionable things for challenge submissions."
    },{
        "title": "wildspirit",
        "description": "Certified clown expert 🤡"
    },
    {
        "title": "ir0nstone",
        "description": "u w0t m8"
    },
    {
        "title": "lean",
        "description": "Script kid wordpress site developer"
    },
    {
        "title": "r4sti",
        "description": "Claims to be hacker but is actually just a mathematician."
    },
    {
        "title": "makelaris",
        "description": "Professional acting instructor, highschool dropout."
    },
]

const generateRandomString = (length: number) => {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let result = "";
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

export default function Home() {
    return (
        <main className="main">
            <NavBar />
            <div className="container text-center">
                <AsciiArt type={"hof"} />
                <h4 className="rainbow mt-2"><b>HALL OF FAME</b></h4>
                {actors.map((actor, index) => (
                    <div className="hof-container" key={index}>
                        <div className="hof-image">
                            {/* Using random chars to bypass caching */}
                            <img src={`https://i.pravatar.cc/?v=${generateRandomString(12)}`} />
                        </div>
                        <div className="hof-name rainbow">
                            { actor.title }
                        </div>
                        <div className="hoa-description text-white">
                            { actor.description }
                        </div>
                    </div>
                ))}
            </div>
        </main>
    );
}