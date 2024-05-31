"use client";

import { useState } from "react";

import PasteTable from "./pastetable";
import AsciiArt from "./asciiart";
import { NavBar } from "./navbar";

import "bootstrap/dist/css/bootstrap.min.css";

const pinnedPastes = [
  {
    title: "How to Ensure Your Paste Stays Up",
    comments: "-",
    views: 230221,
    createdBy: "dimitry [Admin]",
    added: "Nov 10st, 2020"
  },
  {
    title: "Transparency Report",
    comments: "-",
    views: 176774,
    createdBy: "aiden [Admin]",
    added: "Jun 12th, 2020"
  }
];

const recentPastes = [
  {
    "title": "PhantomStrike: A Vigilante's Past Revealed",
    "comments": 8,
    "views": 29,
    "createdBy": "mysteryhunterx",
    "added": "May 24th, 2024"
  },
  {
    "title": "GhostByte: The Enigma Decoded",
    "comments": 2,
    "views": 15,
    "createdBy": "mysteryhunterx",
    "added": "May 23rd, 2024"
  },
  {
    "title": "Anonymous unveiled (really)",
    "comments": 16,
    "views": 51,
    "createdBy": "truthfinder1999",
    "added": "May 22nd, 2024"
  },
  {
    "title": "Cipher ip/address/info",
    "comments": 13,
    "views": 48,
    "createdBy": "codetracker",
    "added": "May 21st, 2024"
  },
  {
    "title": "ShadowFang info",
    "comments": 7,
    "views": 35,
    "createdBy": "netsleuth2024",
    "added": "May 20th, 2024"
  },
  {
    "title": "blacklotus admins exposed",
    "comments": 6,
    "views": 22,
    "createdBy": "anonexplorer",
    "added": "May 19th, 2024"
  },
  {
    "title": "Nemesis dev - dev info and rat source",
    "comments": 10,
    "views": 33,
    "createdBy": "secretsunmasked",
    "added": "May 18th, 2024"
  },
  {
    "title": "Cyberphantoms faces leaked",
    "comments": 9,
    "views": 34,
    "createdBy": "identitycracker",
    "added": "May 17th, 2024"
  },
  {
    "title": "ShadowSlicer Uncovered: A New Perspective",
    "comments": 7,
    "views": 24,
    "createdBy": "mysteryhunterx",
    "added": "May 16th, 2024"
  },
  {
    "title": "darkprotector dev dox",
    "comments": 4,
    "views": 18,
    "createdBy": "underworldWatcher",
    "added": "May 15th, 2024"
  },
  {
    "title": "ChaosWielder house 😂",
    "comments": 12,
    "views": 32,
    "createdBy": "cyberanarchist",
    "added": "May 14th, 2024"
  },
  {
    "title": "Rapper Snoop dawg real address!",
    "comments": 10,
    "views": 30,
    "createdBy": "darkwebdecipher",
    "added": "May 13th, 2024"
  },
  {
    "title": "chef gordo ramson vacation home",
    "comments": 5,
    "views": 20,
    "createdBy": "darkwebdecipher",
    "added": "May 12th, 2024"
  },
  {
    "title": "XCQ token grabbed 🐟",
    "comments": 14,
    "views": 40,
    "createdBy": "doxersupreme",
    "added": "May 11th, 2024"
  },
  {
    "title": "Crypto scammer | Please swat him somebody",
    "comments": 9,
    "views": 28,
    "createdBy": "exposecyber",
    "added": "May 10th, 2024"
  },
  {
    "title": "BitLockSupp real info after arrest",
    "comments": 3,
    "views": 16,
    "createdBy": "netinsider101",
    "added": "May 9th, 2024"
  },
  {
    "title": "CrabsOnSecurity real info leaked",
    "comments": 13,
    "views": 35,
    "createdBy": "whistleblowx64",
    "added": "May 8th, 2024"
  },
  {
    "title": "mr beest - doxxed",
    "comments": 9,
    "views": 27,
    "createdBy": "warfare",
    "added": "May 7th, 2024"
  },
  {
    "title": "La'vron James information",
    "comments": 7,
    "views": 25,
    "createdBy": "leaksdigger1337",
    "added": "May 6th, 2024"
  },
  {
    "title": "🐺 GrayWolf Vendor Hacked 🐺",
    "comments": 11,
    "views": 38,
    "createdBy": "webundergroundx",
    "added": "May 5th, 2024"
  },
  {
    "title": "Andrew Bate's real ₿itcoin addresses",
    "comments": 6,
    "views": 21,
    "createdBy": "CryptoUnmasker",
    "added": "May 4th, 2024"
  }
];

export default function Home() {
  const [searchQuery, setSearchQuery] = useState("");

  return (
    <main className="main">
      <NavBar />
      <div className="container">
        <AsciiArt type={"oni"} />
        <div className="row text-center mt-4">
          <div className="col">
            <a className="link1" href="#">Official Doxpit Telegram</a>
          </div>
        </div>
        <div className="row text-center mt-2">
          <div className="col">
            <a className="link2" href="#">All Operations Paused - Admin Has Been Abducted</a>
          </div>
        </div>
        <div className="row mt-4 text-center">
          <div className="col">
            <input
              type="text"
              className="form-control"
              placeholder="Search for pastes..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
          </div>
        </div>
        <PasteTable pastes={pinnedPastes} title="Pinned Pastes" searchQuery={""} />
        <PasteTable pastes={recentPastes} title="Recent Pastes" searchQuery={searchQuery} />
        <div className="row text-center mb-5">
          <div className="col">
            <a className="link1" href="#">Back to top</a>
          </div>
        </div>
      </div>
    </main>
  );
}