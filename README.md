# JobTracker

A powerful AI-driven job scraper and analyzer designed to streamline the job search process by extracting and processing postings from platforms like Computrabajo.

## Description
JobTracker is a Python-based utility that automates the collection and analysis of job offers. It goes beyond simple scraping by integrating with AI models (like Groq or Gemini) to summarize requirements, extract key skills, and provide strategic insights into the current job market, all while maintaining a structured local database.

## Detailed Overview
Searching for jobs manually is time-consuming. JobTracker automates this by systematically scraping job portals, extracting detailed descriptions, and using Large Language Models (LLMs) to analyze each posting. The tool identifies essential technical requirements, salary ranges (when available), and company expectations, presenting the data in a clean CSV format for easy review and comparison.

## Features
- Deep scraping of job postings from Computrabajo
- AI-powered analysis for skill extraction and summaries
- Automated data persistence in CSV format
- Smart filtering of redundant or irrelevant offers
- Detailed logging of scraping and analysis progress
- Secure management of API credentials via environment variables

## Technologies Used
- Python 3.x
- Selenium / BeautifulSoup4 (Scraping)
- AI Integration (Groq API / Google Gemini)
- Pandas (Data processing)
- Dotenv (Environment management)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Santiprz27/JobTracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JobTracker
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with the following variables:
   ```env
   GROQ_API_KEY=your_api_key_here
   GEMINI_API_KEY=your_api_key_here
   ```
5. Run the scraper:
   ```bash
   python scraper_computrabajo.py
   ```

## Usage Examples
Run the analysis script to process existing offers:
```bash
python analista_ia.py
```
This will process the `ofertas_detalladas.csv` file and generate an AI-enhanced report.

## Project Structure
- `scraper_computrabajo.py`: Core logic for web scraping and data extraction.
- `analista_ia.py`: AI-driven analysis module for job descriptions.
- `run.bat`: Batch file for easy execution in Windows environments.
- `ofertas_detalladas.csv`: Primary data storage for scraped job postings.
- `requirements.txt`: List of Python dependencies.

## Configuration
Adjust search criteria (keywords, location) within the `scraper_computrabajo.py` script or through a configuration file if available.

## API Documentation
Internal functions are documented for ease of extension. For AI interactions, refer to the respective AI provider's documentation.

## Screenshots or Examples
![Scraping in Progress](img/1.gif) *(Example of visual progress indicators)*

## Roadmap / Future Improvements
- Support for additional platforms (LinkedIn, Indeed)
- Web-based dashboard for viewing analyzed offers
- Automated application features via browser automation
- Real-time notification system for new matches

## Contributing Guidelines
Contributions are welcome! Please open an issue or submit a PR for any improvements or new features.

## License
MIT License

---

# JobTracker (Español)

Un potente extractor y analizador de empleos impulsado por IA, diseñado para optimizar el proceso de búsqueda laboral mediante la extracción y procesamiento de ofertas de plataformas como Computrabajo.

## Descripción
JobTracker es una utilidad basada en Python que automatiza la recopilación y el análisis de ofertas de trabajo. Va más allá de la simple extracción al integrarse con modelos de IA (como Groq o Gemini) para resumir requisitos, extraer habilidades clave y proporcionar información estratégica del mercado laboral.

## Resumen Detallado
Buscar trabajo manualmente requiere mucho tiempo. JobTracker automatiza esto mediante el scraping sistemático de portales de empleo, la extracción de descripciones detalladas y el uso de modelos de lenguaje (LLM) para analizar cada oferta. La herramienta identifica requisitos técnicos esenciales, rangos salariales y expectativas de la empresa.

## Características
- Extracción profunda de ofertas de trabajo desde Computrabajo
- Análisis potenciado por IA para la extracción de habilidades y resúmenes
- Persistencia de datos automatizada en formato CSV
- Filtrado inteligente de ofertas redundantes o irrelevantes
- Registro detallado del progreso de extracción y análisis
- Gestión segura de credenciales mediante variables de entorno

## Tecnologías Utilizadas
- Python 3.x
- Selenium / BeautifulSoup4 (Scraping)
- Integración con IA (Groq API / Google Gemini)
- Pandas (Procesamiento de datos)

## Instrucciones de Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Santiprz27/JobTracker.git
   ```
2. Navegar al directorio del proyecto:
   ```bash
   cd JobTracker
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Configurar el archivo `.env` con tus API keys.
5. Ejecutar el extractor:
   ```bash
   python scraper_computrabajo.py
   ```

## Ejemplos de Uso
Ejecuta el script de análisis para procesar las ofertas:
```bash
python analista_ia.py
```

## Estructura del Proyecto
- `scraper_computrabajo.py`: Lógica principal de scraping y extracción de datos.
- `analista_ia.py`: Módulo de análisis con IA para descripciones de puestos.
- `run.bat`: Archivo por lotes para ejecución sencilla en Windows.
- `ofertas_detalladas.csv`: Almacenamiento principal de las ofertas extraídas.

## Configuración
Ajusta los criterios de búsqueda (palabras clave, ubicación) directamente en el script.

## Documentación de la API
Funciones internas documentadas.

## Capturas de Pantalla o Ejemplos
![Progreso del Scraping](img/1.gif)

## Hoja de Ruta / Mejoras Futuras
- Soporte para plataformas adicionales (LinkedIn, Indeed)
- Dashboard web para visualización de ofertas analizadas
- Características de postulación automatizada
- Sistema de notificaciones en tiempo real para nuevos puestos

## Guía para Contribuir
¡Las contribuciones son bienvenidas!

## Licencia
Licencia MIT
