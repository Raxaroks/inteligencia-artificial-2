import React, { useReducer } from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import FirstPractice from '../components/screens/FirstPractice';
import MenuScreen from '../components/screens/MenuScreen';
import MyNavbar from '../components/ui/MyNavbar';

const AppRouter = () => {

    return (
        <Router>
            <div>
                <MyNavbar />
                <div className="main-box">
                    <Switch>

                            <Route
                                exact
                                path="/practica01"
                                component={FirstPractice}
                            />

                        <Route path="/" component={MenuScreen} />
                    </Switch>
                </div>
            </div>
        </Router>
    );
}

export default AppRouter;
