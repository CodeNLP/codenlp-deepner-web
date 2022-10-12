![](gfx/codenlp-deepner-gui.png)

# Setup

```bash
pip install -r requirements.txt
```

# Run

## API

```bash
docker run -p 8000:8000  --gpus all mczuk/poldeepner2:nkjp_base_sq
```

## Web GUI

```bash
streamlit run app.py
```