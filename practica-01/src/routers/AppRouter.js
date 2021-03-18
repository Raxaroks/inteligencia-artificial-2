import React from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import MenuScreen from '../components/screens/MenuScreen';

const AppRouter = () => {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/" component={ MenuScreen } />
                </Switch>
            </div>
        </Router>
    );
}

export default AppRouter;
