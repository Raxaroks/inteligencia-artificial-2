import { AXIS_MAX_RANGE, CHARTHEIGHT, CHARTWIDTH, OFFSET_X, OFFSET_Y } from "./data";

export const round = (value, precision) => {
    const multi = Math.pow(10, precision || 0);
    return Math.round(value * multi) / multi;
};

export const getPixelsCoordinates = ( layerX, layerY ) => {
    return {
        realX: round(layerX - OFFSET_X, 2), 
        realY: layerY - OFFSET_Y
    }
}

export const PixelToPoints = ( realX, realY ) => {

    const x = (realX*AXIS_MAX_RANGE) / CHARTWIDTH;
    const y = (realY*AXIS_MAX_RANGE) / CHARTHEIGHT

    return {
        x: round(x,2),
        y: round(y,2)
    }
}