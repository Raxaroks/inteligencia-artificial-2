import React, { useContext, useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { AXIS_MAX_RANGE } from '../../data/data';
import { getPixelsCoordinates, PixelToPoints } from '../../data/helpers';
import { setDataLinetoChart, setDataPointstoChart, solvePerceptrons } from '../../data/perceptron';
import { PerceptronContext } from '../../data/PerceptronContext';


const MyChart = (  ) => {

    const { inputData } = useContext(PerceptronContext);

    // arreglo donde almacenaremos todos los patrones, es decir, cada par de coordenadas a graficar
    const [patterns, setPatterns] = useState([]);

    // función que se dispara al hacer click en algún lugar del chart
    const handleChartClick = (event) => {
        // asignando las coordinadas basadas en los pixeles
        const layerX = event.layerX;
        const layerY = 400 - event.layerY;

        // ajustando las medidas reales del chart
        const realPos = getPixelsCoordinates(layerX, layerY);
        // console.log(realPos);

        // transformando los pixeles a los puntos que queremos mostrar
        const points = PixelToPoints(realPos.realX, realPos.realY);

        const array = patterns;
        array.push(points);
        setPatterns(array);

        const newChart = {
            data: {
                datasets: [
                    {
                        label: "Patrones",
                        backgroundColor: "rgba( 0,0,0,1 )",
                        data: patterns,
                        pointRadius: 5
                    },
                ],
            },
            options: chartProps.options,
        };

        // console.log( newChart );
        setChartProps( newChart );
    };

    // estado que maneja la información mostrada en el gráfico, por defecto siempre dibuja un gráfico vacío
    const [chartProps, setChartProps] = useState({
        data: {
            datasets: [
                {
                    label: "Vacío",
                    fillColor: "rgba(220,220,220,0.2)",
                    strokeColor: "rgba(220,220,220,1)",
                    pointColor: "rgba(220,220,220,1)",
                    pointStrokeColor: "#fff",
                    pointHighlightFill: "#fff",
                    pointHighlightStroke: "rgba(220,220,220,1)",
                    data: [],
                },
            ],
        },
        options: {
            onClick: handleChartClick,
            animation: false,
            scaleShowGridLines: true,
            scaleShowVerticalLines: true,
            showTooltips: false,
            tooltips: { enabled: false },
            showLines: false,
            responsive: true,
            scales: {
                xAxes: [
                    {
                        type: "linear",
                        ticks: { min: 0, max: AXIS_MAX_RANGE },
                    },
                ],
                yAxes: [
                    { ticks: { min: 0, max: AXIS_MAX_RANGE } },
                ],
            },
        },
    }); // dibujamos un chart vacío - estado por defecto

    useEffect(() => {
        if (inputData.solve) {
            console.log("hay que resolver los perceptrones");

            // hacemos toda la machaca de cálculos
            const { actives, inactives, line } = solvePerceptrons(
                patterns,
                inputData.w1,
                inputData.w2,
                inputData.b
            );

            console.log( actives, inactives, line );

            setChartProps({
                data: {
                    datasets: [
                        {
                            label: "Inactivos",
                            backgroundColor: "rgba(240, 52, 52, 1)",
                            pointRadius: 5,
                            data: setDataPointstoChart(inactives),
                        }, // inactivos
                        {
                            label: "Activos",
                            backgroundColor: "rgba(123, 239, 178, 1)",
                            pointRadius: 5,
                            data: setDataPointstoChart(actives),
                        }, // activos
                        {
                            label: "Línea",
                            fill: false,
                            showLine: true,
                            backgroundColor: "rgb(130, 60, 200)",
                            borderColor: "rgba(130, 60, 200, 0.8)",
                            pointRadius: 1,
                            data: setDataLinetoChart(line),
                        }, // linea separadora
                    ],
                },
                options: {
                    animation: false,
                    scaleShowGridLines: true,
                    scaleShowVerticalLines: true,
                    showTooltips: false,
                    tooltips: { enabled: false },
                    showLines: false,
                    responsive: true,
                    scales: {
                        xAxes: [
                            {
                                type: "linear",
                                ticks: { min: 0, max: AXIS_MAX_RANGE },
                            },
                        ],
                        yAxes: [{ ticks: { min: 0, max: AXIS_MAX_RANGE } }],
                    },
                },
            });

            // preparamos la línea separadora - verde!!!
            // const datasetLine = {};
        }


    }, [inputData.solve]);

    return (
        <div id="chart">
            <Line data={chartProps.data} options={chartProps.options} redraw />
        </div>
    );
};

export default MyChart;
