import streamlit as st
import streamlit.components.v1 as components

st.title("Visualizador HTML desde portapapeles")

# Área donde el usuario pega el contenido HTML copiado
html_content = st.text_area('Pega aqui el contenido hml', '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anuario A&RR 2025 – Accounting & Regulatory Reporting</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;900&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8;
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            height: 350px;
            max-height: 40vh;
        }
        .kpi-card {
            background: linear-gradient(145deg, #0A9396, #005F73);
            color: white;
            border-radius: 1rem;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 10px 20px rgba(0, 95, 115, 0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .kpi-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0, 95, 115, 0.3);
        }
        .kpi-number {
            font-size: 4rem;
            font-weight: 900;
            line-height: 1;
            color: #E9D8A6;
        }
        .kpi-label {
            font-size: 1.125rem;
            font-weight: 500;
            margin-top: 0.5rem;
        }
        .section-title {
            color: #005F73;
            font-weight: 900;
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        .section-subtitle {
            text-align: center;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            color: #0A9396;
            margin-bottom: 3rem;
        }
        .card {
            background-color: white;
            border-radius: 1rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .timeline {
            position: relative;
            max-width: 1000px;
            margin: 0 auto;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #94D2BD;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        .timeline-container {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }
        .timeline-container.left {
            left: 0;
        }
        .timeline-container.right {
            left: 50%;
        }
        .timeline-container::after {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            right: -17px;
            background-color: white;
            border: 4px solid #EE9B00;
            top: 15px;
            border-radius: 50%;
            z-index: 1;
        }
        .timeline-container.right::after {
            left: -16px;
        }
        .timeline-content {
            padding: 20px 30px;
            background-color: white;
            position: relative;
            border-radius: 6px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body class="text-gray-800">

    <header class="bg-[#005F73] text-white text-center py-20 px-4">
        <h1 class="text-4xl md:text-6xl font-black uppercase tracking-wider">Anuario A&RR 2025</h1>
        <p class="text-xl md:text-2xl mt-4 font-light text-[#E9D8A6]">Transformación, talento y comunidad global</p>
    </header>

    <main class="container mx-auto px-4 py-12 md:py-16">
        
        <section id="mensaje" class="mb-16 md:mb-24">
            <div class="max-w-3xl mx-auto text-center p-8 bg-white rounded-2xl shadow-lg">
                <h2 class="text-2xl md:text-3xl font-bold text-[#005F73] mb-4">Mensaje del Equipo Global A&RR</h2>
                <p class="text-lg text-gray-600 leading-relaxed">
                    2025 ha sido un año de transformación profunda, marcado por la innovación y el fortalecimiento de nuestra comunidad. Hemos superado desafíos complejos gracias al talento colectivo y a una colaboración sin fronteras. Este anuario celebra nuestros logros compartidos y renueva nuestra visión para un futuro donde la excelencia en Accounting & Regulatory Reporting sea nuestro estándar global. Miramos hacia 2026 con el compromiso de seguir creciendo, aprendiendo y liderando juntos.
                </p>
            </div>
        </section>

        <section id="cifras" class="mb-16 md:mb-24">
            <h2 class="section-title">2025 en Cifras</h2>
            <p class="section-subtitle">Los números que definen un año de crecimiento e impacto excepcional en nuestra comunidad.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                <div class="kpi-card">
                    <div class="kpi-number">850+</div>
                    <div class="kpi-label">Practitioners Activos</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-number">12k+</div>
                    <div class="kpi-label">Horas de Formación</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-number">75+</div>
                    <div class="kpi-label">Casos de Uso IA/Data</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-number">200+</div>
                    <div class="kpi-label">Eventos Realizados</div>
                </div>
            </div>
        </section>

        <section id="hitos" class="mb-16 md:mb-24">
            <h2 class="section-title">Hitos Globales</h2>
            <p class="section-subtitle">Los proyectos y eventos que han marcado nuestra evolución y fortalecido nuestra práctica a nivel mundial.</p>
            <div class="timeline">
                <div class="timeline-container left">
                    <div class="timeline-content">
                        <h3 class="font-bold text-xl text-[#CA6702]">Lanzamiento Pilar III ESG</h3>
                        <p class="text-gray-600 mt-2">Implementación exitosa del marco de reporting de sostenibilidad, unificando criterios y mejorando la transparencia en todos los mercados.</p>
                    </div>
                </div>
                <div class="timeline-container right">
                    <div class="timeline-content">
                        <h3 class="font-bold text-xl text-[#CA6702]">Kick-off Global 2025</h3>
                        <p class="text-gray-600 mt-2">Evento de inicio de año que reunió a más de 500 practitioners para alinear objetivos estratégicos y fomentar la cohesión de la comunidad.</p>
                    </div>
                </div>
                 <div class="timeline-container left">
                    <div class="timeline-content">
                        <h3 class="font-bold text-xl text-[#CA6702]">Consolidación del Control</h3>
                        <p class="text-gray-600 mt-2">Evolución del modelo de gobierno con nuevos frameworks de control automatizado, reduciendo el riesgo operacional en un 15%.</p>
                    </div>
                </div>
                <div class="timeline-container right">
                    <div class="timeline-content">
                        <h3 class="font-bold text-xl text-[#CA6702]">Itinerarios Formativos</h3>
                        <p class="text-gray-600 mt-2">Despliegue de 5 nuevos itinerarios formativos en Data, IA y Sostenibilidad, capacitando a más de 300 personas.</p>
                    </div>
                </div>
            </div>
        </section>

        <section id="innovacion" class="mb-16 md:mb-24">
            <h2 class="section-title">Innovación y Tecnología</h2>
            <p class="section-subtitle">Impulsando la eficiencia y la calidad a través de la automatización y el uso inteligente de los datos.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                <div class="card">
                    <h3 class="text-xl font-bold text-[#005F73] mb-4">Distribución de Casos de Uso</h3>
                    <p class="text-gray-600 mb-4">La automatización de procesos y la analítica avanzada lideran nuestras iniciativas de innovación, demostrando un claro enfoque en la eficiencia y la generación de valor a partir de los datos.</p>
                    <div class="chart-container">
                        <canvas id="iaUseCasesChart"></canvas>
                    </div>
                </div>
                <div class="card">
                     <h3 class="text-xl font-bold text-[#005F73] mb-4">Herramientas y Colaboraciones</h3>
                    <ul class="space-y-4 text-gray-700">
                        <li class="flex items-start">
                            <span class="text-[#EE9B00] font-bold text-2xl mr-3">⚡</span>
                            <div>
                                <h4 class="font-bold">Módulos de Alertas Proactivas</h4>
                                <p>Desarrollo de un sistema de alertas que anticipa desviaciones en el reporting regulatorio, mejorando la precisión.</p>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <span class="text-[#EE9B00] font-bold text-2xl mr-3">📊</span>
                            <div>
                                <h4 class="font-bold">Colaboración "Data en A&RR"</h4>
                                <p>Iniciativa conjunta con el área de Data que ha permitido crear 3 nuevos dashboards de control para la alta dirección.</p>
                            </div>
                        </li>
                        <li class="flex items-start">
                            <span class="text-[#EE9B00] font-bold text-2xl mr-3">🤖</span>
                             <div>
                                <h4 class="font-bold">RPA para Conciliaciones</h4>
                                <p>Automatización del 80% de las conciliaciones manuales, liberando más de 5,000 horas anuales para tareas de análisis.</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="comunidad" class="mb-16 md:mb-24">
            <h2 class="section-title">Voces de la Comunidad</h2>
            <p class="section-subtitle">Nuestros practitioners son el corazón de A&RR. Sus experiencias y testimonios reflejan el poder de nuestra comunidad.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="card text-center">
                    <p class="text-gray-600 italic">"La colaboración con equipos de otros países en el proyecto ESG fue una experiencia increíble. Aprendí muchísimo y sentí que realmente éramos un equipo global."</p>
                    <p class="mt-4 font-bold text-[#005F73]">- Ana García, Practitioner (España)</p>
                </div>
                 <div class="card text-center">
                    <p class="text-gray-600 italic">"Los 'Coffee&Talks' son mi evento favorito. Es un espacio informal para conectar con líderes y compañeros, y entender mejor la estrategia global."</p>
                    <p class="mt-4 font-bold text-[#005F73]">- Mehmet Yilmaz, Data Analyst (Turquía)</p>
                </div>
                <div class="card text-center">
                    <p class="text-gray-600 italic">"Gracias al nuevo itinerario de Data, he podido aplicar nuevas técnicas de visualización en nuestros informes locales, aportando mucho más valor."</p>
                    <p class="mt-4 font-bold text-[#005F73]">- Sofía Rojas, Reporting Specialist (Colombia)</p>
                </div>
            </div>
        </section>

        <section id="mundo" class="mb-16 md:mb-24">
            <h2 class="section-title">A&RR en el Mundo</h2>
            <p class="section-subtitle">Nuestra comunidad tiene una fuerte presencia global. Aquí se compara la distribución de practitioners por geografía, destacando el alcance de nuestra red.</p>
            <div class="card md:col-span-2">
                 <h3 class="text-xl font-bold text-center text-[#005F73] mb-4">Distribución de Practitioners por Geografía</h3>
                 <div class="chart-container h-[400px] max-h-[50vh]">
                    <canvas id="practitionersByCountryChart"></canvas>
                </div>
            </div>
        </section>
        
        <section id="whoiswho" class="mb-16 md:mb-24">
            <h2 class="section-title">Who is Who – Equipos Protagonistas</h2>
            <p class="section-subtitle">Conoce a los equipos que lideran nuestras iniciativas estratégicas y marcan el rumbo de A&RR.</p>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                <div class="card text-center p-8">
                    <div class="text-5xl mb-4">🛡️</div>
                    <h3 class="text-xl font-bold text-[#005F73]">Gobierno y Control</h3>
                    <p class="text-gray-600 mt-2">Aseguran la integridad y el cumplimiento normativo, implementando los frameworks que protegen nuestra operativa.</p>
                </div>
                <div class="card text-center p-8">
                    <div class="text-5xl mb-4">📊</div>
                    <h3 class="text-xl font-bold text-[#005F73]">Data y Reporting</h3>
                    <p class="text-gray-600 mt-2">Transforman los datos en información de valor, desarrollando los informes y dashboards que guían la toma de decisiones.</p>
                </div>
                <div class="card text-center p-8">
                    <div class="text-5xl mb-4">🌱</div>
                    <h3 class="text-xl font-bold text-[#005F73]">Sostenibilidad</h3>
                    <p class="text-gray-600 mt-2">Lideran la integración de los criterios ESG en nuestro reporting, respondiendo a las nuevas demandas de un mundo más consciente.</p>
                </div>
            </div>
        </section>

        <section id="proyeccion" class="mb-16 md:mb-24">
            <h2 class="section-title">Proyección 2026</h2>
            <p class="section-subtitle">Nuestra hoja de ruta para el próximo año: objetivos ambiciosos, desafíos estimulantes y el compromiso de seguir innovando.</p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div class="card">
                    <h3 class="font-bold text-xl text-[#AE2012] mb-3">Objetivos Estratégicos</h3>
                    <ul class="space-y-2 text-gray-700 list-disc list-inside">
                        <li>IA Generativa en Reporting</li>
                        <li>Expansión del marco de Sostenibilidad</li>
                        <li>Certificación global en Data Literacy</li>
                        <li>Reducción del 50% en procesos manuales</li>
                    </ul>
                </div>
                <div class="card">
                    <h3 class="font-bold text-xl text-[#AE2012] mb-3">Desafíos Clave</h3>
                     <ul class="space-y-2 text-gray-700 list-disc list-inside">
                        <li>Adaptación a la nueva regulación IFRS 18</li>
                        <li>Integración de datos no estructurados</li>
                        <li>Gestión del cambio y adopción de IA</li>
                        <li>Escalabilidad de soluciones globales</li>
                    </ul>
                </div>
                <div class="card">
                    <h3 class="font-bold text-xl text-[#AE2012] mb-3">Eventos Programados</h3>
                     <ul class="space-y-2 text-gray-700 list-disc list-inside">
                        <li>Global A&RR Summit 2026 (Q2)</li>
                        <li>Datathon Anual de Reporting (Q3)</li>
                        <li>Ciclo de Webinars sobre IA Generativa</li>
                        <li>Programa de Mentoring Internacional</li>
                    </ul>
                </div>
            </div>
        </section>

    </main>
    
    <footer class="bg-[#005F73] text-white text-center p-12">
        <h3 class="text-3xl font-black text-[#E9D8A6] mb-4">"When you share, everybody wins"</h3>
        <p class="text-xl">"Si compartes, ganamos todos"</p>
        <p class="mt-6 text-sm text-[#94D2BD]">&copy; 2025 A&RR Community of Practice. Todos los derechos reservados.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            
            const wrapLabel = (label, maxLength) => {
                if (label.length <= maxLength) {
                    return label;
                }
                const words = label.split(' ');
                const lines = [];
                let currentLine = '';
                words.forEach(word => {
                    if ((currentLine + ' ' + word).trim().length > maxLength) {
                        lines.push(currentLine.trim());
                        currentLine = word;
                    } else {
                        currentLine = (currentLine + ' ' + word).trim();
                    }
                });
                if (currentLine) {
                    lines.push(currentLine.trim());
                }
                return lines;
            };
            
            const tooltipTitleCallback = (tooltipItems) => {
                const item = tooltipItems[0];
                let label = item.chart.data.labels[item.dataIndex];
                if (Array.isArray(label)) {
                  return label.join(' ');
                } else {
                  return label;
                }
            };

            const sharedChartOptions = {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        labels: {
                            color: '#374151'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            title: tooltipTitleCallback
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { color: '#4b5563' },
                        grid: { color: '#e5e7eb' }
                    },
                    x: {
                        ticks: { color: '#4b5563' },
                        grid: { display: false }
                    }
                }
            };

            const iaUseCasesCtx = document.getElementById('iaUseCasesChart');
            if(iaUseCasesCtx) {
                new Chart(iaUseCasesCtx, {
                    type: 'doughnut',
                    data: {
                        labels: ['Automatización de Procesos', 'Analítica Avanzada y Predictiva', 'Reporting Inteligente', 'Control y Detección de Anomalías'],
                        datasets: [{
                            label: 'Casos de Uso',
                            data: [45, 25, 20, 10],
                            backgroundColor: ['#0A9396', '#94D2BD', '#EE9B00', '#CA6702'],
                            borderColor: '#ffffff',
                            borderWidth: 2
                        }]
                    },
                    options: {
                       responsive: true,
                       maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: { color: '#374151' }
                            },
                            tooltip: {
                                callbacks: {
                                    title: tooltipTitleCallback
                                }
                            }
                        }
                    }
                });
            }

            const practitionersByCountryCtx = document.getElementById('practitionersByCountryChart');
            if (practitionersByCountryCtx) {
                const rawLabels = ['España', 'México', 'Colombia', 'Argentina', 'Chile', 'Turquía', 'Uruguay', 'Venezuela'];
                const wrappedLabels = rawLabels.map(label => wrapLabel(label, 16));
                
                new Chart(practitionersByCountryCtx, {
                    type: 'bar',
                    data: {
                        labels: wrappedLabels,
                        datasets: [{
                            label: 'Nº de Practitioners',
                            data: [210, 180, 155, 120, 95, 55, 25, 10],
                            backgroundColor: '#0A9396',
                            borderColor: '#005F73',
                            borderWidth: 1,
                            borderRadius: 5
                        }]
                    },
                    options: {
                        ...sharedChartOptions,
                        indexAxis: 'y',
                        scales: {
                            x: {
                                beginAtZero: true,
                                ticks: { color: '#4b5563' },
                                grid: { color: '#e5e7eb' }
                            },
                            y: {
                                ticks: { color: '#4b5563' },
                                grid: { display: false }
                            }
                        },
                        plugins: {
                            legend: {
                                display: false
                            },
                            tooltip: {
                                callbacks: {
                                    title: tooltipTitleCallback
                                }
                            }
                        }
                    }
                });
            }
        });
    </script>
</body>
</html>
''')

# Mostrar el HTML si hay contenido
if html_content:
    components.html(html_content, height=800, scrolling=True)
else:
    st.info("Pega el contenido HTML en el área de texto para visualizarlo")


