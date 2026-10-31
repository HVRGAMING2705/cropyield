from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation(); prs.slide_width = Inches(13.33); prs.slide_height = Inches(7.5)
def add(i, title, lines):
    s = prs.slides.add_slide(prs.slide_layouts[1])
    s.shapes.title.text = title
    tf = s.placeholders[1].text_frame; tf.word_wrap = True
    for j, ln in enumerate(lines):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.text = ln; p.font.size = Pt(20); p.space_after = Pt(10)
add(0, "CropYield — Crop Yield Predictor", ["An AI/ML project by Vikranth Reddy", "B.Tech CSE (AI & ML), 2nd Year — Woxsen University", "Ridge regression that estimates crop yield right in your browser"])
add(1, "The Problem", ["Farmers plan seeds, fertilizer and loans around an uncertain harvest", "Yield depends on rainfall, temperature, fertilizer, soil and irrigation together", "Guessing from last year's harvest ignores how this season actually differs", "A simple, explainable estimate helps farmers plan before harvest time"])
add(2, "The Solution — CropYield", ["Enter rainfall, average temperature, fertilizer, soil pH and irrigation", "A trained ridge regression model predicts yield in quintals per hectare", "Runs fully in the browser — no backend, no waiting", "The same model weights power both the Python training and the web demo"])
add(3, "Tech Stack", ["Python + scikit-learn: data generation and model training", "Ridge regression (alpha = 1.0) on standardised features", "HTML, CSS and vanilla JavaScript for the interactive demo", "GitHub for source control, Vercel for free hosting"])
add(4, "Architecture", ["Synthetic dataset: 600 farm seasons, 5 features, seed 42", "Standardisation (mean / std) -> Ridge regression -> model.json", "model.json ships with the site; JavaScript applies the same formula", "Prediction is clipped to a realistic 5–60 quintals per hectare range"])
add(5, "Live Demo", ["Try it: enter your season details and press Estimate", "Example: 1000 mm rain, 24 C, 250 kg/ha fertilizer, pH 6.8, irrigated -> about 48.3 q/ha", "Change any input and the estimate updates instantly", "Demo: https://cropyield.vercel.app"])
add(6, "Results", ["5-fold cross-validation R-squared: 0.844", "Mean absolute error: 2.50 q/ha (RMSE 3.13 q/ha)", "Baseline (always guessing the average): MAE 6.45 q/ha", "The model is about 2.6x better than the baseline guess", "Browser demo matches Python predictions to within 0.01 q/ha"])
add(7, "Future Scope", ["Train on real district-level crop data from government open datasets", "Add crop type, soil type and sowing date as features", "Compare gradient boosting and small neural networks", "Add a per-field total yield calculator and a season planner"])
add(8, "Thank You", ["CropYield — Crop Yield Predictor", "Vikranth Reddy, B.Tech CSE (AI & ML), Woxsen University", "Source: github.com/HVRGAMING2705/cropyield", "Questions welcome!"])
prs.save("/home/hatch/workspace/goals/daily-ai-ml-project-factory/files/AIML_CropYield_2026-10-31.pptx")
print("slides:", len(prs.slides.__iter__.__self__._sldIdLst))
