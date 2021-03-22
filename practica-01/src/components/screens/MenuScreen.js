import { Button } from 'react-bootstrap';
import React from 'react';

const MenuScreen = ( { history } ) => {
    return (
        <div className="screen-box">
            <div className="menu-box">
                <Button
                    variant="primary"
                    size="lg"
                    onClick={() => history.push("/practica01")}
                >
                    Práctica 01
                </Button>
            </div>
        </div>
    );
}

export default MenuScreen;
