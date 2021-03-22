import { round } from "./helpers";

export const activateFunc = ( inputs, weights ) => {
    console.log( inputs, weights );

    const res = inputs.x1 * weights.w1 + inputs.x2 * weights.w2 - weights.b;

    // console.log( "res", res  );
    return res;
}

export const neuronIsActive = ( result ) => {
    return ( result > 0 );
}

export const setDataPointstoChart = ( array ) => {
    if ( array !== undefined ) {
        return array.map( element => ({
            x: element.x1,
            y: element.x2
        }) );
    }

    return [];
}

export const setDataLinetoChart = ( array ) => {
    if (array !== undefined) {
        return array.map((element) => ({
            x: element.x,
            y: element.y,
        }));
    }

    return [];
}

export const getActivesAndInactives = ( neurons, weights ) => {
    const actives = [], inactives = [];

    neurons.forEach( n => {
        if ( n.active ) { actives.push(n); }
        else { inactives.push(n) }
    } );

    const line = solvePoints( neurons.map( n => n.x1 ), weights )

    return { 
        actives, 
        inactives,
        line
     }
}

export const solvePoints = ( x1, weights ) => {
    const m = - (weights.w1 / weights.w2);
    const a = weights.b / weights.w2;

    return x1.map( x => {
        return {
            x: x,
            y: round(m*x+a, 2)
        }
    } );
}

export const solvePerceptrons = ( neurons, w1, w2, b ) => {
    // console.log(neurons, w1, w2, b);

    const perceptrons = neurons.map( neuron => {
        const inp = { 
            x1: neuron.x,
            x2: neuron.y
         };

        const wei = {
            w1, w2, b
        };

        const res = activateFunc( inp, wei );

        return { 
            x1: neuron.x,
            x2: neuron.y,
            result: res,
            active: neuronIsActive( res )
         }
    } );

    // console.log( perceptrons );

    // debe de retornar 3 arreglos:
    // - uno con los puntos activos
    // - uno con los inactivos
    // - uno con la línea a separar
    const solved = getActivesAndInactives(perceptrons, { w1, w2, b });
    return solved;
}