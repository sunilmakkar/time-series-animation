# Top 10 Country Populations Animation

This repository visualizes the top 10 most populous countries in the world over time through animated bar charts. The project uses Python, Matplotlib, and Pandas to clean the data, generate visualizations, and create time-series animations.

## Features
- **Population Animation**: Displays the change in the top 10 countries by population over time.
- **Flag Integration**: Adds country flags for a richer visual context.
- **Clean Design**: A focus on clean and professional visualization styles.

## Project Structure
- **`population_animation.py`**: 
  - Generates a simple horizontal bar chart animation for the top 10 countries by population for each year.
  - Outputs an MP4 video file named `video_pop.mp4`.

- **`barchart.py`**: 
  - Extends the animation with flags and mid-year population data (January and July).
  - Includes dynamic labels and additional styling for a polished presentation.

## Data
- **Input**: The cleaned dataset is stored in `./data/cleaned-data.csv`.
  - Columns: `Location`, `ISO3_code`, `Time`, `TPopulation1Jan`, `TPopulation1July`, etc.
  - Data source: United Nations or other population data sources.
- **Flags**: A folder of country flag images (ISO 3166-1 alpha-3 format) is required for `barchart.py`.
  - Example: `USA.png`, `IND.png`.

## Requirements
- Python 3.8+
- Required libraries:
  - `pandas`
  - `matplotlib`
  - `numpy`
  - `Pillow`

Install dependencies using:
```bash
pip install pandas matplotlib numpy Pillow
```

## Usage

1. Clone the repository:
```
git clone https://github.com/sunilmakkar/time-series-animation.git
cd animations
```

2. Ensure the cleaned-data.csv file is in the ./data directory.
3. Run the scripts:
- Basic animation:
```
python population_animation.py
```

- Outputs video_pop.mp4 in the current directory.
- Enhanced animation with flags: Update the FLAG_FOLDER variable in barchart.py with the path to your flag images folder:
```
FLAG_FOLDER = "/path/to/flags"
```

- Then run:
```
python barchart.py
```

## Outputs
- population_animation.py: Produces a horizontal bar chart animation saved as video_pop.mp4.
- barchart.py: Displays a more advanced animation with country flags, timestamps, and mid-year population updates.


## Notes 
- Flags should be named using the 3-letter ISO country code (e.g., USA.png, CHN.png).
- Adjust the fps parameter in the scripts to control the animation speed.
- Ensure ffmpeg is installed for saving animations:

## License
This project is licensed under the MIT License. Feel free to use, modify, and share.

## Acknowledgments
- Data Source: United Nations Population Division (https://www.un.org/development/desa/pd/)
