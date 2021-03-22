
export const perceptronTypes = {
    solve: '[perceptron] solve',
    done:  '[perceptron] done'
};

export const perceptronReducer = (state={}, action) => {

    switch ( action.type ) {
        case perceptronTypes.solve:
            return {
                ...action.payload,
                solve: true
            }

        case perceptronTypes:
            {
                return {
                    solve: false
                }
            }

        default:
            return state;
    }

}