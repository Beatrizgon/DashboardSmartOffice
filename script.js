// script.js - versão animada com dark mode e eixo temporal (datas no rodapé)

// Variáveis globais
let temps = [];
let lux = [];
let occ = [];
let currentIndex = 0;

// Referências para os gráficos
let tempChart, luxChart, occChart;

Papa.parse("smart_office_data.csv", {
    download: true,
    header: true,
    complete: function (results) {
        const data = results.data;

        // Filtrar dados por tipo de sensor
        temps = data.filter(r => r.sensor_type === "temperature");
        lux = data.filter(r => r.sensor_type === "luminosity");
        occ = data.filter(r => r.sensor_type === "occupancy");

        // Criar gráficos vazios
        criarGraficos();

        // Iniciar simulação (1 segundo = 15 minutos simulados)
        setInterval(() => {
            if (currentIndex < temps.length) {
                currentIndex++;
                atualizarGraficos();
            }
        }, 2000);
    }
});

// Criar gráficos vazios com Chart.js
function criarGraficos() {
    // --- Temperatura ---
    const ctxTemp = document.getElementById("tempChart").getContext("2d");
    tempChart = new Chart(ctxTemp, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Temperatura (°C)",
                data: [],
                borderColor: "#ff4c4c", // vermelho neon
                backgroundColor: "rgba(255,76,76,0.2)",
                fill: true
            }]
        },
        options: chartOptions("°C")
    });

    // --- Luminosidade ---
    const ctxLux = document.getElementById("luxChart").getContext("2d");
    luxChart = new Chart(ctxLux, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Luminosidade (lux)",
                data: [],
                borderColor: "#4c9dff", // azul neon
                backgroundColor: "rgba(76,157,255,0.2)",
                fill: true
            }]
        },
        options: chartOptions("lux")
    });

    // --- Ocupação ---
    const ctxOcc = document.getElementById("occChart").getContext("2d");
    occChart = new Chart(ctxOcc, {
        type: "line",
        data: {
            labels: [],
            datasets: [{
                label: "Ocupação (0=livre, 1=ocupado)",
                data: [],
                borderColor: "#4cff4c", // verde neon
                backgroundColor: "rgba(76,255,76,0.2)",
                fill: true,
                stepped: true
            }]
        },
        options: chartOptions("ocupado")
    });
}

// Configurações padrão de gráfico (dark mode + eixo temporal)
function chartOptions(yLabel) {
    return {
        responsive: true,
        scales: {
            x: {
                type: "time",
                time: {
                    parser: "YYYY-MM-DD HH:mm:ss",
                    tooltipFormat: "DD/MM HH:mm",
                    displayFormats: {
                        minute: "DD/MM HH:mm",
                        hour: "DD/MM HH:mm"
                    }
                },
                ticks: {
                    color: "#cccccc",     // cor da fonte das datas
                    maxTicksLimit: 8      // limita quantas datas aparecem para não poluir
                },
                grid: {
                    color: "rgba(255,255,255,0.1)"
                }
            },
            y: {
                ticks: { color: "#cccccc" },
                grid: { color: "rgba(255,255,255,0.1)" }
            }
        },
        plugins: {
            legend: {
                labels: { color: "#ffffff" }
            }
        }
    };
}


// Atualizar gráficos conforme o currentIndex
function atualizarGraficos() {
    // Temperatura
    const tempData = temps.slice(0, currentIndex);
    tempChart.data.labels = tempData.map(r => r.timestamp);
    tempChart.data.datasets[0].data = tempData.map(r => parseFloat(r.value));
    tempChart.update();

    // Luminosidade
    const luxData = lux.slice(0, currentIndex);
    luxChart.data.labels = luxData.map(r => r.timestamp);
    luxChart.data.datasets[0].data = luxData.map(r => parseFloat(r.value));
    luxChart.update();

    // Ocupação
    const occData = occ.slice(0, currentIndex);
    occChart.data.labels = occData.map(r => r.timestamp);
    occChart.data.datasets[0].data = occData.map(r => parseInt(r.value));
    occChart.update();
}
