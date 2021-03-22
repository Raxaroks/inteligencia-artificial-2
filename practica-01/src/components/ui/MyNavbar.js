import React from 'react';
import 'react-bootstrap/'
import { Navbar } from 'react-bootstrap/';
import AILogo from '../../assets/icons/artificial-intelligence.png';

const MyNavbar = () => {
    return (
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand href="/home">
                <img
                    alt=""
                    src={AILogo}
                    width="35"
                    height="35"
                    className="d-inline-block align-top"
                /> &nbsp;
                Seminario de Solución de Problemas de Inteligencia Artificial II
            </Navbar.Brand>
        </Navbar>
    );
}

export default MyNavbar;
