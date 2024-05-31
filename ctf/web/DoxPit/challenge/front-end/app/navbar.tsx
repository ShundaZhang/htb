export function NavBar() {
    return (
        <nav className="navbar navbar-default navbar-expand-lg navbar-custom fixed-top">
            <div className="container">
                <a className="navbar-brand text-white" href="/">Doxpit</a>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#navbarNav"
                    aria-controls="navbarNav"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <a className="nav-link" href="/">Home</a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/error">Add Paste</a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/error">Users</a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/error">Upgrades</a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/hof">Hall of <i>Fame</i></a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/error">TOS</a>
                        </li>
                        <li className="nav-item ms-3">
                            <a className="nav-link" href="/error">Telegram</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}