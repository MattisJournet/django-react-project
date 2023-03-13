import React from 'react';
import {useRouter} from "next/router";

function Navbar(props) {
    const router = useRouter();

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="#">Navbar</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse"
                    data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                    aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active">
                        <a style={{cursor: "pointer"}} onClick={() => router.push('/')} className="nav-link">Home</a>
                    </li>
                    <li className="nav-item active">
                        <a style={{cursor: "pointer"}} onClick={() => router.push('list/')} className="nav-link">List</a>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default Navbar;
