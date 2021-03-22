import React, { useReducer } from 'react';
import { PerceptronContext } from './data/PerceptronContext';
import { perceptronReducer } from './data/perceptronReducer';
import AppRouter from './routers/AppRouter';

// context para la práctica 01
const initPerceptronContext = () => {
    return { solve: false }
}

const App = () => {
    // context para la práctica 01
    const [inputData, dispatch] = useReducer(
        perceptronReducer,
        {},
        initPerceptronContext
    );

    return (
        <PerceptronContext.Provider value={{ inputData, dispatch }}>
            <AppRouter />
        </PerceptronContext.Provider>
    );
}

export default App;
