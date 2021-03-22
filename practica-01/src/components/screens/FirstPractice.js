import React, { useContext } from 'react';
import { PerceptronContext } from '../../data/PerceptronContext';
import { perceptronTypes } from '../../data/perceptronReducer';
import { useForm } from '../../hooks/useForm';
import MyChart from '../ui/MyChart';


const FirstPractice = () => {

    const { dispatch } = useContext(PerceptronContext);

    const [ formValues, handleInputChange, reset ] = useForm({
        w1: "",
        w2: "",
        b: "",
    });

    const { w1, w2, b } = formValues;

    const handleSubmit = ( evt ) => {
        evt.preventDefault();
        if ( w1 === '' || w2 === '' || b === '') {
            alert( "Uno o más campos se encuentran vacíos." );
        }

        else {
            // console.log(b, w1, w2);
            const data = {
                w1: parseFloat(w1),
                w2: parseFloat(w2),
                b: parseFloat(b),
            };
            dispatch({
                type: perceptronTypes.solve,
                payload: data
            });
            reset();
        }
    }

    return (
        <div className="box">
            <h1>Práctica 01</h1>  <hr />
            <div className="container-wrapper">
                {/* Div con los inputs de entradas y bias */}
                <div className="form-container">
                    <form onSubmit={handleSubmit}>
                        <label>W1:</label>
                        <input
                            type="number"
                            name="w1"
                            placeholder="Peso"
                            value={w1}
                            onChange={handleInputChange}
                        />

                        <label>W2:</label>
                        <input
                            type="number"
                            name="w2"
                            placeholder="Peso"
                            value={w2}
                            onChange={handleInputChange}
                        />

                        <label>b:</label>
                        <input
                            type="number"
                            name="b"
                            placeholder="Umbral"
                            value={b}
                            onChange={handleInputChange}
                        />

                        <button type="submit" className="btn-dark">
                            CALCULAR
                        </button>
                    </form>
                </div>

                {/* Div con el gráfico a mostrar los resultados del perceptrón */}
                <MyChart />
            </div>
        </div>
    );
}

export default FirstPractice;
